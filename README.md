# iFood Restaurants Dataset Exploration with kagglehub and Docker

This project demonstrates how to use [`kagglehub`](https://github.com/Kaggle/kagglehub) inside a Docker container to load and explore the [iFood Restaurants Dataset](https://www.kaggle.com/datasets/ricardotachinardi/ifood-restaurants-data).

It is an upgraded version of the original project:
[projeto_vemsertech_banco_de_dados_i](https://github.com/iago-mansur/projeto_vemsertech_banco_de_dados_i).

---

## 📦 What's Inside

- **Python 3.10-slim** Docker container
- Installs `kagglehub[pandas-datasets]`
- Downloads a real Kaggle dataset
- Saves data to a shared /data volume
- Uses Docker Compose for orchestration

---

## 🚀 Quickstart

### 1. Clone the Repo

```bash
git clone https://github.com/iago-mansur/Project_database_with_Docker.git
cd Project_database_with_Docker
```

### 2. Build & Run with Docker Compose

```bash
docker compose up --build
```

Dataset files will be saved to your local `./data` folder.

--- 

## 🧠 About the Dataset

- Dataset: [iFood Restaurants Data](https://www.kaggle.com/datasets/ricardotachinardi/ifood-restaurants-data)

- Provided by Kaggle user: [ricardotachinardi](https://www.kaggle.com/ricardotachinardi)

---

## 📂 Folder Structure

```bash
Project_database_with_Docker/
├── app/
│   └── data_loader.py      # Python script to download dataset
├── data/                   # ⬅️ Dataset files will be saved here
├── Dockerfile              # Docker build config
├── docker-compose.yml      # Docker Compose config
├── requirements.txt        # Python dependencies
└── README.md               # Project info
```

---

## 🐳 Docker Notes

**Volume**: The `./data` folder is mounted inside the container as `/app/data`.

**Kagglehub** automatically downloads and caches datasets.

**Data output** is handled by the script at `app/data_loader.py`.

---



## 📄 License

This project is open-source and for educational/demo purposes only.

> **Note:** To use `kagglehub`, you may need to have your Kaggle API credentials configured.
