import os
import shutil
import pandas as pd
import kagglehub

# Download dataset only if not already downloaded
dataset_path = kagglehub.dataset_download("ricardotachinardi/ifood-restaurants-data")

# Define destination folder
destination_folder = "data"
os.makedirs(destination_folder, exist_ok=True)

# List files in the Kaggle dataset
for file_name in os.listdir(dataset_path):
    src_file = os.path.join(dataset_path, file_name)
    dst_file = os.path.join(destination_folder, file_name)
    if not os.path.exists(dst_file):
        shutil.copy(src_file, dst_file)
        print(f"✅ Downloaded and saved: {file_name}")
    else:
        print(f"🔁 Already exists, skipping: {file_name}")

# Paths to both CSVs
feb_path = os.path.join(destination_folder, "ifood-restaurants-february-2021.csv")
nov_path = os.path.join(destination_folder, "ifood-restaurants-november-2020.csv")

# Load both files
feb_df = pd.read_csv(feb_path)
nov_df = pd.read_csv(nov_path)

print("\n🔍 Comparing CSV files...")

# Check column names and order
if list(feb_df.columns) == list(nov_df.columns):
    print("✅ Column names and order match")
else:
    print("❌ Columns differ")
    print("Feb columns:", feb_df.columns.tolist())
    print("Nov columns:", nov_df.columns.tolist())

# Check column data types
if feb_df.dtypes.equals(nov_df.dtypes):
    print("✅ Data types match")
else:
    print("❌ Data types differ")
    print("Feb dtypes:\n", feb_df.dtypes)
    print("Nov dtypes:\n", nov_df.dtypes)

# Check for missing/extra columns
diff1 = set(feb_df.columns) - set(nov_df.columns)
diff2 = set(nov_df.columns) - set(feb_df.columns)
if not diff1 and not diff2:
    print("✅ No missing or extra columns")
else:
    print("❌ Difference in columns")
    if diff1:
        print("Only in Feb:", diff1)
    if diff2:
        print("Only in Nov:", diff2)

# (Optional) Show preview of data
print("\n📌 Sample data from February 2021:")
print(feb_df.head(2))
print("\n📌 Sample data from November 2020:")
print(nov_df.head(2))
