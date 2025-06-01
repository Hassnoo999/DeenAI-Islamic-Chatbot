import pandas as pd
import os
import glob

# Folder containing your CSV files
folder_path = r'Bukhari CSV'

# Output merged CSV file name
output_file = r'Combined Sahih Bukhari CSV.csv'

# Get all CSV files in the folder
csv_files = glob.glob(os.path.join(folder_path, '*.csv'))

combined_list = []  # This will store the dataframes that are successfully read

for file in csv_files:
    try:
        # First try reading with UTF-8 encoding
        df = pd.read_csv(file, encoding='utf-8')
    except UnicodeDecodeError:
        try:
            # If UTF-8 fails, try ISO-8859-1 encoding
            df = pd.read_csv(file, encoding='ISO-8859-1')
        except Exception as e:
            print(f"❌ Skipping file {file} due to error: {e}")
            continue  # Skip this file and go to the next one
    combined_list.append(df)

# Combine all dataframes into one
combined_df = pd.concat(combined_list, ignore_index=True)

# Save the final combined CSV
combined_df.to_csv(output_file, index=False, encoding='utf-8-sig')

print(f"✅ Successfully merged {len(combined_list)} CSV files into:\n{output_file}!")
