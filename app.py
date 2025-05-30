import kagglehub
import os

# Download dataset
dataset_path = kagglehub.dataset_download("ricardotachinardi/ifood-restaurants-data")

# List files
print("Listing files in:", dataset_path)
for filename in os.listdir(dataset_path):
    print("-", filename)
