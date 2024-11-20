# Industry 5.0 Data Architecture for Smart Applications

This repository contains resources and tools to explore and implement a data architecture framework designed for Industry 5.0. It supports real-time data ingestion and processing for smart applications and can be used for educational purposes in a university course.

---

## 📁 Repository Contents

1. **`export.sql`**A PostgreSQL database dump (compatible with TimescaleDB extension). This contains the schema and initial data required for the project. Instructions for importing this file are provided below.
2. **`filling.py`**A Python script that populates the database using data from the provided CSV file.
3. **`smart_app_data.csv`**
   A CSV file containing real-time data used to fill the database for testing and demonstration purposes.

---

## 🚀 Getting Started

### Prerequisites

- Docker should be installed on your machine.
- Git should be installed on your machine.

---

### 1. Clone the Repository

Clone this repository to your local machine using the following command:

```bash
git clone https://github.com/Kreative-Performative-Individuals/smart-industrial-database
```

This will create a new directory named `smart-industrial-database` in your current working directory.

### 2. Pull the Docker Image

Pull the official TimeScaleDB Docker image from Docker Hub by running the following command:

```bash
docker pull timescale/timescaledb-ha:pg16
```

This will download the required Docker image to your machine.

#### 3. Run the TimescaleDB Docker Container

1. Open your terminal or command prompt inside the cloned repository.
2. Run the following command to start the TimescaleDB Docker container:
   ```bash
   $ docker run -itd -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=password -p 5432:5432 -v ./data:/var/lib/postgresql/data --name timescale-container timescale/timescaledb-ha:pg16
   ```

This command will start a new Docker container named `timescale-container` with the required environment variables and port mappings. From now on, you can use this container to interact with the TimescaleDB instance.
3. Run the following commands to prepare the database:

```bash
   chmod +x build_db.sh
```

```bash
   ./build_db.sh timescale-container export.sql KPI_Database
```

This will create a new database named `KPI_Database` in the TimescaleDB instance and import the schema and initial data from the `export.sql` file.

### Using pgAdmin

pgAdmin is a popular open-source administration and development platform for PostgreSQL. You can use pgAdmin to interact with the TimescaleDB instance running in the Docker container. Follow the steps below to set up pgAdmin and connect it to the TimescaleDB instance:

### 1. Install pgAdmin on Docker

Run the following command to install pgAdmin on Docker:

```bash
docker pull dpage/pgadmin4:latest
```

### 2. Run the pgAdmin Docker Container

Run the following command to start the pgAdmin Docker container:

```bash
$ docker run --name pgadmin-postgres -p 5051:80 -e "PGADMIN_DEFAULT_EMAIL=admin@admin.com" -e "PGADMIN_DEFAULT_PASSWORD=password" -d dpage/pgadmin4
```

### 3. Access pgAdmin

Open your web browser and navigate to `http://localhost:5051`. You will be prompted to log in with the default credentials. Use the following credentials to log in:

- Email: `admin@admin.com`
- Password: `password`

After logging in, you can add a new server connection to the TimescaleDB instance running in the Docker container. Use the following connection details:

- Hostname/address: 172.17.0.2
- Port: `5432`
- Username: `postgres`
- Password: `password`

If the localhost does not work, you can use the IP address of the Docker container. To find the IP address, run the following command:

```bash
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' <container_id_or_name>
```

Replace `<container_id_or_name>` with the ID or name of the Docker container running the TimescaleDB instance.

---
### Testing the Database
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

### Understanding the Architecture and E-R Schema

![The following architecture Diagram shows the overall design of the Industry 5.0 data architecture, including real-time data flows and processing pipelines.](images/architecture_diagram.png)

![The following E-R Diagram Illustrates the relationships between entities in the database.](images/er_schema.png)

### 🛠️ Tools & Technologies

- PostgreSQL 17
- Python
- CSV
- pgAdmin (optional)
