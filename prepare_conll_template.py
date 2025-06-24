import pandas as pd

# Load your preprocessed data
df = pd.read_csv("preprocessed_telegram_data.csv")

# Drop empty messages
df = df[df["Cleaned_Message"].notnull()]

# Select a random subset (30–50 messages)
sampled_df = df.sample(n=40, random_state=42)

# Write to CoNLL format
with open("ner_labeling_template.conll", "w", encoding="utf-8") as f:
    for message in sampled_df["Cleaned_Message"]:
        tokens = message.split()
        for token in tokens:
            f.write(f"{token}\tO\n")  # Default label is O
        f.write("\n")  # Blank line separates messages

print("✅ Template created: ner_labeling_template.conll — You can now label it manually.")
