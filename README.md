# iFood Restaurants Dataset Exploration with kagglehub and Docker

This project demonstrates how to use [`kagglehub`](https://github.com/Kaggle/kagglehub) inside a Docker container to load and explore the [iFood Restaurants Dataset](https://www.kaggle.com/datasets/ricardotachinardi/ifood-restaurants-data).

It is an upgraded version of the original project:
[projeto_vemsertech_banco_de_dados_i](https://github.com/iago-mansur/projeto_vemsertech_banco_de_dados_i).

---

## 📦 What's Inside

- **Python 3.10-slim** Docker container
- Installs `kagglehub[pandas-datasets]`
- Loads a Kaggle dataset

---

## 🚀 Quickstart

### 1. Clone the Repo

```bash
git clone https://github.com/iago-mansur/Project_database_with_Docker.git
cd Project_database_with_Docker
```

### 2. Build the Docker Image

```bash
docker build -t kagglehub-demo .
```

### 3. Run the Container

```bash
docker run --rm kagglehub-demo
```

You should see the the files downloaded.

--- 

## 🧠 About the Dataset

- Dataset: [iFood Restaurants Data](https://www.kaggle.com/datasets/ricardotachinardi/ifood-restaurants-data)

- Provided by Kaggle user: [ricardotachinardi](https://www.kaggle.com/ricardotachinardi)

---

## 🛠 Modify Dataset File Path

You can list available files in the dataset by modifying `app.py`:

```python
import kagglehub
import os

dataset_path = kagglehub.dataset_download("ricardotachinardi/ifood-restaurants-data")
print("Files in dataset:")
for filename in os.listdir(dataset_path):
    print("-", filename)
```

Then set `file_path` accordingly:

```python
file_path = "ifood-restaurants-february-2021.csv"
```

## 🐳 Docker Notes

- **Base image**: python:3.10-slim

- **Dependencies** installed via: `pip install kagglehub[pandas-datasets]`

- **Run-time data** is downloaded inside the container at /root/.cache/kagglehub

---

## 📄 License

This project is open-source and for educational/demo purposes only.

> **Note:** To use `kagglehub`, ensure you have your Kaggle API credentials properly configured inside the Docker container or on your host machine.
