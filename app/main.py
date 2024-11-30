from fastapi import FastAPI
import psycopg2
import pandas as pd
from datetime import datetime
from pydantic import BaseModel

DB_HOST = "172.17.0.2"
DB_NAME = "KPI_database"
DB_USER = "postgres"
DB_PASSWORD = "password"

app = FastAPI()

class AnomalyDataRequest(BaseModel):
    timestamp: datetime
    isset_id: str
    name: str
    kpi: str
    operation: str
    sum: float
    avg: float
    min: float
    max: float
    var: float
    anomaly: str

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
        print(f"An error occurred: {e}")
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
        print(f"An error occurred: {e}")
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
        print(f"An error occurred: {e}")
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
        print(f"An error occurred: {e}")
        return {"message": "An error occurred", "error": str(e)}

# Endpoint requested from group 3, to get informations based on the parameters passed.
@app.get("/historical_data")
async def get_historical_data(
    machine_name: str,
    asset_id: str,
    kpi: str,
    operation: str,
    timestamp_start: datetime,
    timestamp_end: datetime
):
    try:
        with psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        ) as conn:
            with conn.cursor() as cursor:
                print(machine_name, asset_id, kpi, operation, timestamp_start, timestamp_end) 
                #TODO implement the real query.
                query = """
                    SELECT 1 WHERE 1 = 1; 
                """
                
                cursor.execute(query, (machine_name, asset_id, kpi, operation, timestamp_start, timestamp_end))
                print(machine_name, asset_id, kpi, operation, timestamp_start, timestamp_end)
                logs = cursor.fetchall()
                
        return logs 
    except Exception as e:
        print(f"An error occurred: {e}")
        return {"message": "An error occurred", "error": str(e)}

@app.post("/anomaly_data")
async def get_anomaly_data(data: AnomalyDataRequest):
    try:
        with psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        ) as conn:
            with conn.cursor() as cursor:
                print("parameters")
                # Print to check if parameters are passed correctly.
                print(data.timestamp, data.isset_id, data.name, data.kpi, data.operation,
                      data.sum, data.avg, data.min, data.max, data.var, data.anomaly)
                
                # TODO implement the real query.
                query = """
                    SELECT 1 WHERE 1 = 1;
                """
                
                cursor.execute(query, (data.timestamp, data.isset_id, data.name, data.kpi, 
                                       data.operation, data.sum, data.avg, data.min, 
                                       data.max, data.var, data.anomaly))
                
                logs = cursor.fetchall()
        return {"data": logs}  
    except Exception as e:
        print(f"An error occurred: {e}")
        return {"message": "An error occurred", "error": str(e)}

"""
curl -X POST "http://127.0.0.1:8000/anomaly_data" \
-H "Content-Type: application/json" \
-d '{
  "timestamp": "2024-11-30T12:00:00",
  "isset_id": "ABC123",
  "name": "Machine A",
  "kpi": "Production Rate",
  "operation": "Normal",
  "sum": 1000.5,
  "avg": 50.2,
  "min": 10.1,
  "max": 100.0,
  "var": 15.5,
  "anomaly": "None"
}'
"""
