import re
import json
import csv
import os
from typing import Dict, List, Any

def clean_text(text: Any, default: str = "") -> str:
    """Clean text by stripping whitespace and replacing multiple spaces with a single space."""
    if text is None:
        return default
    return re.sub(r"\s+", " ", str(text).strip())

def process_hadith(hadith: Dict[str, Any]) -> Dict[str, str]:
    """Process a single hadith entry to extract and clean fields."""
    return {
        "hadithNumber": clean_text(hadith.get("hadithNumber")),
        "englishNarrator": clean_text(hadith.get("englishNarrator")),
        "hadithEnglish": clean_text(hadith.get("hadithEnglish")),
        "chapterEnglish": clean_text(hadith.get("chapter", {}).get("chapterEnglish")),
        "bookName": clean_text(hadith.get("book", {}).get("bookName")),
        "volume": clean_text(hadith.get("volume")),
        "status": clean_text(hadith.get("status"))
    }

# Directory setup
input_dir = "Sahih Muslim Ahadith"
output_dir = "Sahih Muslim CSV"
os.makedirs(output_dir, exist_ok=True)

for i in range(292, 595):  # Adjusted range for Sahih Muslim (292-594)
    input_path = f"{input_dir}/sahi_muslim_hadith_page{i}.json"  

    try:
        with open(input_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        hadiths = data.get("hadiths", {}).get("data", [])
        rag_rows = [process_hadith(h) for h in hadiths]

        if not rag_rows:
            print(f"⚠️ No data found in page {i}")
            continue

        # Write to CSV
        output_path = f"{output_dir}/sahih_muslim_page{i}.csv"
        with open(output_path, mode="w", encoding="utf-8-sig", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=rag_rows[0].keys())
            writer.writeheader()
            writer.writerows(rag_rows)

        print(f"✔️ Converted page {i} to CSV")

    except FileNotFoundError:
        print(f"⚠️ File not found: {input_path}")
    except json.JSONDecodeError as e:
        print(f"❌ Invalid JSON in page {i}: {e}")
    except Exception as e:
        print(f"❌ Error processing page {i}: {e}")