import pandas as pd
import re

# Step 1: Load scraped data
df = pd.read_csv("telegram_data.csv")

# Step 2: Define text cleaning function
def clean_text(text):
    if pd.isnull(text):
        return ""
    text = str(text)
    text = re.sub(r'[^\w\s፡፣።]', '', text)  # Remove emojis/symbols, keep basic Amharic punctuations
    text = re.sub(r'\s+', ' ', text)  # Normalize whitespace
    text = text.strip()
    return text

# Step 3: Apply cleaning
df["Cleaned_Message"] = df["Message"].apply(clean_text)

# Step 4: Tokenization (simple whitespace for now)
df["Tokens"] = df["Cleaned_Message"].apply(lambda x: x.split())

# Step 5: Drop empty rows
df = df[df["Cleaned_Message"].str.strip().astype(bool)]

# Step 6: Save preprocessed dataset
df.to_csv("preprocessed_telegram_data.csv", index=False, encoding='utf-8')

print("✅ Preprocessing complete! Saved to preprocessed_telegram_data.csv")
