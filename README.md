**Table of Contents**

- [Industry 5.0 Data Architecture for Smart Applications](#industry-50-data-architecture-for-smart-applications)
  - [📁 Repository Contents](#-repository-contents)
  - [📜 Introduction](#-introduction)
    - [Industry 5.0 Data Architecture for Smart Applications](#industry-50-data-architecture-for-smart-applications-1)
  - [🚀 Getting Started](#-getting-started)
    - [Prerequisites](#prerequisites)
    - [Setting Up the Database](#setting-up-the-database)
    - [Using pgAdmin (optional)](#using-pgadmin-optional)
  - [🧪 Testing the Database](#-testing-the-database)
  - [Try our API](#try-our-api)
  - [Understanding the Architecture and E-R Schema of the Database](#understanding-the-architecture-and-e-r-schema-of-the-database)
  - [🔐 DevSecOps](#-devsecops)

# Industry 5.0 Data Architecture for Smart Applications

This repository contains resources and tools to explore and implement a data architecture framework designed for Industry 5.0. It supports real-time data ingestion and processing for smart applications and can be used for educational purposes in a university course.

## 📁 Repository Contents

The repository contains the following files and directories:

```bash
📂 Project Root
├── 🗄️ backup.py
├── 🔐 backups_decryption
│   ├── 🔓 decrypt_backup.py
│   ├── 🔑 enc_key.key
│   └── 🛠️ generate_key.py
├── 🔒 backups_encrypted
├── 🛠️ build_db.sh
├── 🐳 dockerfile
├── 🗂️ exports.sql
├── 🖼️ images
│   ├── 🏗️ architecture_diagram.png
│   └── 📊 er_schema.png
├── 📜 LICENSE
├── 📝 query_template.py
├── 📖 README.md
├── 📦 requirements.txt
├── 📊 smart_app_data.csv
└── 🧪 test_database.py
```

In order the contents are:

- **`backup.py`**
  A Python script that backs up the database and saves the encrypted backup file to the `backups_encrypted` directory.
- **`backups_decryption`**
  - **`decrypt_backup.py`**
    A Python script that decrypts the encrypted backup files from the `backups_encrypted` directory.
  - **`enc_key.key`** A file containing the encryption key used to encrypt the database backups.
  - **`generate_key.py`**
    A Python script that generates a new encryption key and saves it to the `enc_key.key` file.
- **`backups_encrypted`**
  A directory containing encrypted database backups.
- **`build_db.sh`**
  A shell script that creates a new database in the smart-database instance and imports the schema and initial data from the provided SQL file.
- **`dockerfile`**
  A Dockerfile that can be used to build a custom Docker image for the project.
- **`exports.sql`**
  A PostgreSQL database dump. This contains the schema and initial data required for the project. It can be imported into the smart-database instance using the `build_db.sh` script.
- **`smart_app_data.csv`**
  A CSV file containing real-time data used to fill the database for testing and demonstration purposes.
- **`query_template`**
  A Python file to show how to query the database.
- **`requirements.txt`**
  A file containing the required Python packages for the project.
- **`test_database.py`**
  A Python script that contains unit tests for the database functions (see the Testing section for more details).

## 📜 Introduction

### Industry 5.0 Data Architecture for Smart Applications

This project aims to provide a data architecture framework for Industry 5.0 applications. This repo is part of a larger project for the Smart Applications course at the University of Pisa. This architecture is made by using a customised version of `PostgreSQL`. This `PostgreSQL` instance includes two extensions:

- **`TimescaleDB`** which is an open-source time-series extension that allows PostgreSQL to be optimized for fast ingest and complex queries; and
- **`pgvector`** which is a PostgreSQL extension that provides support for vector similarity search and indexing. The architecture supports real-time data ingestion and processing for smart applications and can be used for educational purposes in a university course; and
- **`pgcrypto`** which is a PostgreSQL extension that provides cryptographic functions for encrypting and decrypting data.

## 🚀 Getting Started

### Prerequisites

- [`Docker`](https://www.docker.com/) should be installed on your machine.
- [`Git`](https://git-scm.com/) should be installed on your machine.
- [`Python`](https://www.python.org/) should be installed on your machine.
- [`pytest`](https://docs.pytest.org/en/stable/) is used for testing the database functions.

### Setting Up the Database

Clone this repository to your local machine using the following command:

```bash
git clone https://github.com/Kreative-Performative-Individuals/smart-industrial-database
```

This will create a new directory named `smart-industrial-database` in your current working directory.
Navigate to the cloned repository and install the required Python packages in your enviroment by using the following command:

```bash
pip install -r requirements.txt
```

Build the Docker image using the following command:

```bash
docker build -t smart-database .
```

This will build a new Docker image named `smart-database` based on the provided Dockerfile.
You can check the list of Docker images on your machine using the following command:

```bash
docker images
```

1. Open your terminal or command prompt inside the cloned repository.
2. Run the following command to start the smart-database Docker container:

```bash
docker volume create pg_data
docker run -d --name kpi-database -p 5432:5432 -p 8002:8002 -v pg_data:/var/lib/postgresql/data  smart-database
```

This command will start a new Docker container named `kpi-database` with the required environment variables and port mappings. From now on, you can use this container to interact with the smart-database instance.
You can check the list of running Docker containers using the following command:
The volume `pg_data` contains data for the persistency of the database.

```bash
docker ps
```

If you remove the container, all the data will be stored in the `data` directory in the project root, so you can easily recreate the container with the same data by running the same command.
1. Run the following commands to prepare the database:

```bash
   chmod +x build_db.sh
```

```bash
   ./build_db.sh kpi-database exports.sql KPI_database
```

This will create a new database named `KPI_database` in the `kpi-database` instance and import the schema and initial data from the `exports.sql` file.

### Using pgAdmin (optional)

`pgAdmin` is a popular open-source administration and development platform for PostgreSQL. You can use pgAdmin to interact with the smart-database instance running in the Docker container. Follow the steps below to set up pgAdmin and connect it to the smart-database instance:

Run the following command to install pgAdmin on Docker:

```bash
docker pull dpage/pgadmin4:latest
```

Run the following command to start the pgAdmin Docker container:

```bash
docker run --name pgadmin-postgres -p 5051:80 -e "PGADMIN_DEFAULT_EMAIL=admin@admin.com" -e "PGADMIN_DEFAULT_PASSWORD=password" -d dpage/pgadmin4
```

Open your web browser and navigate to `http://localhost:5051`. You will be prompted to log in with the default credentials. Use the following credentials to log in:

- Email: `admin@admin.com`
- Password: `password`

After logging in, you can add a new server connection to the smart-database instance running in the Docker container. Use the following connection details:

- Hostname/address: `172.17.0.2`
- Port: `5432`
- Username: `postgres`
- Password: `password`

If the localhost does not work, you can use the IP address of the Docker container. To find the IP address, run the following command:

```bash
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' <container_id_or_name>
```

Replace `<container_id_or_name>` with the ID or name of the Docker container running the smart-database instance.

## 🧪 Testing the Database

If you want to test the database, all you need to do is run the following command:

```bash
pytest test_database.py
```

If you want more details about the tests, you can run the following command:

```bash
pytest test_database.py -v
```

More details about `pytest` can be found by running the following command:

```bash
pytest --help
```

---

## Try our API

We implemented our endpoints using FastAPI.

After you have started the container and filled the database by using `build_db.sh`, you can try our endpoints by visiting **http://localhost:8002/docs**.

There you can find the instructions and the description of the endpoints and try them using the GUI.

## Understanding the Architecture and E-R Schema of the Database

The following architecture Diagram shows the overall design of the Industry 5.0 data architecture, including real-time data flows and processing pipelines.

![architecture_diagram](images/architecture_diagram.png)

The following E-R Diagram Illustrates the relationships between entities in the database schema.

![er_schema](images/er_schema.png)

---

## 🔐 DevSecOps

DevSecOps is a set of practices that combines software development (Dev) with IT operations (Ops) and security (Sec). It aims to integrate security into the software development process from the beginning, rather than treating it as an afterthought. The following security measures have been implemented in this project:

- **password hashing + salt for the postgres users passwords**: The passwords of the users of postgres by default are hashed and salted to ensure that they are not stored in plain text inside the database.
- **encryption of specific columns for the personal data**: The personal data of the users is encrypted before being stored in the database. This ensures that the data is secure and cannot be accessed by unauthorized users.
- **encryption of the database backups**: The database backups are encrypted before being saved to the `backups_encrypted` directory. This ensures that the backup files are secure and cannot be accessed by unauthorized users.
