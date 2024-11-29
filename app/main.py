from fastapi import FastAPI
import psycopg2

DB_HOST = "172.17.0.2"
DB_NAME = "KPI_database"
DB_USER = "postgres"
DB_PASSWORD = "password"

app = FastAPI()

@app.get("/machines", summary="Fetch machine records", 
         description="This endpoint retrieves all records from the machines table in the database, displaying details about each machine.")
async def fetch_machines():
    try:
        with psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        ) as conn:
            with conn.cursor() as cursor:
                print("Connessione al database riuscita.")

                # Query the machines table to fetch all rows
                cursor.execute("SELECT * FROM machines;")
                machines = cursor.fetchall()

                # Print the results of the query
                print("\nRisultati della query:")
                for row in machines:
                    print(row)
        
        return {"message": "Machines fetched successfully", "data": machines}

    except Exception as e:
        print(f"Si è verificato un errore: {e}")
        return {"message": "An error occurred", "error": str(e)}
    
@app.get("/maintenance_records", summary="Fetch maintenance records", 
         description="This endpoint retrieves all maintenance records from the database and displays them.")
async def fetch_maintenance_records():
    try:
        with psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        ) as conn:
            with conn.cursor() as cursor:
                print("Connessione al database riuscita.")
                cursor.execute("SELECT * FROM maintenance_records;")
                records = cursor.fetchall()
                print("\nRisultati della query:")
                for row in records:
                    print(row)
        return {"message": "Maintenance records fetched successfully", "data": records}
    except Exception as e:
        print(f"Si è verificato un errore: {e}")
        return {"message": "An error occurred", "error": str(e)}


@app.get("/real_time_data", summary="Fetch real-time data", 
         description="This endpoint retrieves all real-time data related to KPIs from the database, enabling live performance tracking.")
async def fetch_personal_data():
    try:
        with psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        ) as conn:
            with conn.cursor() as cursor:
                print("Connessione al database riuscita.")
                cursor.execute("SELECT * FROM personal_data;")
                data = cursor.fetchall()
                print("\nRisultati della query:")
                for row in data:
                    print(row)
        return {"message": "Personal data fetched successfully", "data": data}
    except Exception as e:
        print(f"Si è verificato un errore: {e}")
        return {"message": "An error occurred", "error": str(e)}

@app.get("/production_logs", summary="Fetch production logs", 
         description="This endpoint retrieves all production logs from the database, useful for monitoring and analytics purposes.")
async def fetch_production_logs():
    try:
        with psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        ) as conn:
            with conn.cursor() as cursor:
                print("Connessione al database riuscita.")
                cursor.execute("SELECT * FROM production_logs;")
                logs = cursor.fetchall()
                print("\nRisultati della query:")
                for row in logs:
                    print(row)
        return {"message": "Production logs fetched successfully", "data": logs}
    except Exception as e:
        print(f"Si è verificato un errore: {e}")
        return {"message": "An error occurred", "error": str(e)}

