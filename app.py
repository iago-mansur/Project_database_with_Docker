import kagglehub
import os
import shutil

# Download dataset
dataset_path = kagglehub.dataset_download("ricardotachinardi/ifood-restaurants-data")

# Target folder to save files
output_dir = "data"
os.makedirs(output_dir, exist_ok=True)

print("Files in dataset:")
for filename in os.listdir(dataset_path):
    src = os.path.join(dataset_path, filename)
    dst = os.path.join(output_dir, filename)
    shutil.copy2(src, dst)
    print("-", filename)
