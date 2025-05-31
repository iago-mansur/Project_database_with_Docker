import os
import shutil
import pandas as pd
import kagglehub
from pathlib import Path

# Constants
DEST_FOLDER = Path("../data")
FEB_FILE = DEST_FOLDER / "ifood-restaurants-february-2021.csv"
NOV_FILE = DEST_FOLDER / "ifood-restaurants-november-2020.csv"
MERGED_FILE = DEST_FOLDER / "ifood_combined.csv"

def download_dataset():
    print("📥 Checking Kaggle dataset...")
    dataset_path = kagglehub.dataset_download("ricardotachinardi/ifood-restaurants-data")
    DEST_FOLDER.mkdir(exist_ok=True)

    for file_name in os.listdir(dataset_path):
        src = Path(dataset_path) / file_name
        dst = DEST_FOLDER / file_name
        if not dst.exists():
            shutil.copy(src, dst)
            print(f"✅ Downloaded and saved: {file_name}")
        else:
            print(f"🔁 Already exists, skipping: {file_name}")

def compare_csvs(feb_path, nov_path):
    feb_df = pd.read_csv(feb_path)
    nov_df = pd.read_csv(nov_path)

    print("\n🔍 Comparing CSV files...")

    if list(feb_df.columns) == list(nov_df.columns):
        print("✅ Column names and order match")
    else:
        print("❌ Columns differ")
        print("Feb columns:", feb_df.columns.tolist())
        print("Nov columns:", nov_df.columns.tolist())

    if feb_df.dtypes.equals(nov_df.dtypes):
        print("✅ Data types match")
    else:
        print("❌ Data types differ")
        print("Feb dtypes:\n", feb_df.dtypes)
        print("Nov dtypes:\n", nov_df.dtypes)

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

    print("\n📌 Sample data from February 2021:")
    print(feb_df.head(2))
    print("\n📌 Sample data from November 2020:")
    print(nov_df.head(2))

def normalize_and_merge(feb_file, nov_file):
    feb_df = pd.read_csv(feb_file)
    nov_df = pd.read_csv(nov_file)

    feb_only = set(feb_df.columns) - set(nov_df.columns)
    nov_only = set(nov_df.columns) - set(feb_df.columns)

    for col in nov_only:
        feb_df[col] = pd.NA
    for col in feb_only:
        nov_df[col] = pd.NA

    all_columns = sorted(feb_df.columns.union(nov_df.columns))
    feb_df = feb_df[all_columns]
    nov_df = nov_df[all_columns]

    feb_df["source"] = "feb2021"
    nov_df["source"] = "nov2020"

    merged_df = pd.concat([feb_df, nov_df], ignore_index=True)
    print("\n✅ Normalized and merged DataFrame:")
    print(merged_df.head(3))
    print(f"\n🔢 Total records: {len(merged_df)}")

    return merged_df

if __name__ == "__main__":
    download_dataset()

    if FEB_FILE.exists() and NOV_FILE.exists():
        compare_csvs(FEB_FILE, NOV_FILE)
        merged = normalize_and_merge(FEB_FILE, NOV_FILE)
        merged.to_csv(MERGED_FILE, index=False)
        print(f"\n💾 Saved normalized data to {MERGED_FILE}")
    else:
        print("❌ Required CSV files not found.")