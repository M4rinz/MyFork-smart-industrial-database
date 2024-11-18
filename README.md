# Industry 5.0 Data Architecture for Smart Applications

This repository contains resources and tools to explore and implement a data architecture framework designed for Industry 5.0. It supports real-time data ingestion and processing for smart applications and can be used for educational purposes in a university course.

---

## 📁 Repository Contents

1. **`export.sql`**  
   A PostgreSQL database dump (compatible with PostgreSQL version 17). This contains the schema and initial data required for the project. Instructions for importing this file are provided below.

2. **`filling.py`**  
   A Python script that populates the database using data from the provided CSV file.

3. **`smart_app_data.csv`**  
   A CSV file containing real-time data used to fill the database for testing and demonstration purposes.

---

## 🚀 Getting Started

### Prerequisites
- **PostgreSQL version 17**: Ensure that PostgreSQL is installed on your system.
- **Python 3.8+**: Required to run the filling script (`filling.py`).
- **pgAdmin (Optional)**: GUI for database management.

---

### Importing the Database

#### Using the Command Line
1. Open your terminal or command prompt.
2. Navigate to the directory containing `export.sql`.
3. Run the following command to import the database dump:
   ```bash
   psql -U <username> -d <database_name> -f export.sql
    ```
Replace <username> with your PostgreSQL username and <database_name> with your database name.
In alternative, you can use pgAdmin to import the database.
### Using pgAdmin
1. Open pgAdmin and connect to your PostgreSQL server.
2. Create a new database (if not already created).
3. Right-click on the database and choose Restore.
4. Browse and select the export.sql file, then click Restore.

### Understanding the Architecture and E-R Schema

    ![The following architecture Diagram shows the overall design of the Industry 5.0 data architecture, including real-time data flows and processing pipelines.](images/architecture_diagram.png)

    ![The following E-R Diagram Illustrates the relationships between entities in the database.] (images/er_schema.png)

### 🛠️ Tools & Technologies

- PostgreSQL 17
- Python
- CSV
- pgAdmin (optional)

