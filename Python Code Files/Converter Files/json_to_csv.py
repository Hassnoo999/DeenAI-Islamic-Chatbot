import os
import json
import pandas as pd
import re

# ✅ Clean up whitespace and formatting issues
def clean_hadith_text(text):
    if not isinstance(text, str):
        return ""
    
    # Trim leading/trailing whitespace
    text = text.strip()
    
    # Remove blank lines and trim each line
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    text = "\n".join(lines)

    # Remove extra spaces before punctuation
    text = re.sub(r'\s+([.,;:!?])', r'\1', text)

    # Collapse multiple spaces into one
    text = re.sub(r' {2,}', ' ', text)

    return text

# 📂 Paths
json_folder = r'F:\Studiees\4th Semester\Information Retrieval\Deen AI (Semester Project)\Sahih Muslim Ahadith'
csv_output_folder = r'F:\Studiees\4th Semester\Information Retrieval\Deen AI (Semester Project)\Muslim CSV'

os.makedirs(csv_output_folder, exist_ok=True)

# ✅ Only the needed fields (Arabic removed)
required_columns = [
    "hadithNumber",
    "englishNarrator",
    "hadithEnglish",
    "hadithUrdu",
    "chapter.chapterEnglish",
    "book.bookName",
    "book.writerName",
    "volume",
    "status"
]

for filename in os.listdir(json_folder):
    if filename.endswith('.json'):
        json_path = os.path.join(json_folder, filename)

        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        hadith_list = data.get("hadiths", {}).get("data", [])

        clean_hadiths = []
        for hadith in hadith_list:
            if not isinstance(hadith, dict):
                continue

            numbers = str(hadith.get("hadithNumber", "")).split(",")
            numbers = [num.strip() for num in numbers]

            for number in numbers:
                h = hadith.copy()
                h["hadithNumber"] = number

                # 🧼 Clean hadith texts
                h["hadithEnglish"] = clean_hadith_text(h.get("hadithEnglish", ""))
                h["hadithUrdu"] = clean_hadith_text(h.get("hadithUrdu", ""))

                clean_hadiths.append(h)

        # Flatten nested structure
        df = pd.json_normalize(clean_hadiths)

        # Add any missing columns as empty
        for col in required_columns:
            if col not in df.columns:
                df[col] = ""

        # Keep only the required columns
        df = df[required_columns]

        # Rename nested column names
        df.columns = [col.split(".")[-1] for col in df.columns]

        # 💾 Save to CSV
        csv_filename = filename.replace('.json', '.csv')
        csv_path = os.path.join(csv_output_folder, csv_filename)
        df.to_csv(csv_path, index=False, encoding='utf-8-sig')

        print(f"✅ Converted (cleaned): {filename} → {csv_filename}")
