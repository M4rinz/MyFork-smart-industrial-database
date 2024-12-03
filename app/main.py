from fastapi import FastAPI
import psycopg2
from datetime import datetime
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
from datetime import datetime
import psycopg2
import os
import json
from fastapi.encoders import jsonable_encoder
from fastapi import Query
from typing import Optional
from math import isnan, isinf
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

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


@app.get("/query", summary="Fetch query records", )
async def fetch_query(statement: str):
    print("Statement", statement)
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
                cursor.execute(statement)
                result = cursor.fetchall()

        return {"message": "Query fetched successfully", "data": result}

    except Exception as e:
        print(f"An error occurred: {e}")
        return {"message": "An error occurred", "error": str(e)}


@app.post("/insert", summary="Insert records", )
async def insert_query(statement: str, data: dict):
    try:
        with psycopg2.connect(
                host=DB_HOST,
                database=DB_NAME,
                user=DB_USER,
                password=DB_PASSWORD
        ) as conn:
            with conn.cursor() as cursor:
                # Query the machines table to fetch all rows
                cursor.execute(statement, data)
                conn.commit()

        return {"message": "Query inserted successfully"}

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


# TODO, implement a query to return requested data to allow group 3 to do their calculations.
# Please check the data format of the return. 
# The query should filter based on the parameters: 
#     machine_name, asset_id, kpi, operation, timestamp_start, timestamp_end
# and should return the records with the same information, 
# so a list of records like:
#     machine_name, asset_id, kpi, operation, timestamp_start, timestamp_end
# Test the endpoint before pushing so that we are sure that group 3 can use it.


def safe_float(val):
    if isinstance(val, float):
        if val == float('inf') or val == float('-inf'):
            return str(val)  # Convert infinite values to a string representation
        if isnan(val):
            return None  # Convert NaN values to None
    return val


def row_to_dict(columns, row):
    return {col: safe_float(value) for col, value in zip(columns, row)}


from math import isnan


@app.get("/historical_data")
async def get_historical_data():
    try:
        with psycopg2.connect(
                host=DB_HOST,
                database=DB_NAME,
                user=DB_USER,
                password=DB_PASSWORD
        ) as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM real_time_data")
                rows = cursor.fetchall()
                columns = [desc[0] for desc in cursor.description]  # This retrieves column names from cursor

                data = [row_to_dict(columns, row) for row in rows]

                if not data:
                    print("No data found.")
                return {"data": data}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {"message": "An error occurred", "error": str(e)}
    



# TODO, implement the query for the endpoint.
# This endpoint should allow group 3 to post data inside the database. 
# The data that should be stored is like this 
# datapoint = {
#     'timestamp': 'timepoint',
#     'isset_id': 'ast-yhccl1zjue2t',
#     'name': 'metal_cutting',
#     'kpi': 'time',
#     'operation': 'working',
#     'sum': float, 
#     'avg': float,
#     'min': float,
#     'max': float,
#     'var': float
# }

# And should go in the real-time data table. The AnomlayDataRequest object stores the informations that are needed to perform the query
# there is an extra field called anomaly, that can be ignored if we don't want to use that, but they can identify anomalies so it's 
# included. Test the endponits before pushing so that we are sure group 3 can use them.
@app.post("/store_datapoint")
async def post_data_point(data: AnomalyDataRequest):
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
                    INSERT INTO real_time_data (
                        timestamp, asset_id, name, kpi, operation, sum, avg, min, max, var, anomaly
                    )
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    RETURNING id;
                """

                cursor.execute(query, (data.timestamp, data.isset_id, data.name, data.kpi,
                                       data.operation, data.sum, data.avg, data.min,
                                       data.max, data.var, data.anomaly))

                logs = cursor.fetchall()
        return {"data": logs}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {"message": "An error occurred", "error": str(e)}


# FILTERED GET HISTORICAL DATA
@app.get("/filtered_historical_data")
def filtered_get_historical_data(machine_name:str, asset_id:str, kpi:str, operation:str, timestamp_start:datetime, timestamp_end:datetime):
    try:
        with psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
            
        ) as conn:
            with conn.cursor() as cursor:
                print("Connessione al database riuscita.")
                # AL POSTO DI real_time_data METTERE IL NOME DELLA TABELLA
                query = """
                    SELECT * FROM real_time_data
                """
                conditions = []
                params = []

                if machine_name:
                    conditions.append("name = %s")
                    params.append(machine_name)

                if asset_id:
                    conditions.append("asset_id = %s")
                    params.append(asset_id)

                if kpi:
                    conditions.append("kpi = %s")
                    params.append(kpi)

                if timestamp_start:
                    conditions.append("time >= %s")
                    params.append(timestamp_start)

                if timestamp_end:
                    conditions.append("time <= %s")
                    params.append(timestamp_end)

                # Aggiungi la clausola WHERE se ci sono condizioni
                if conditions:
                    query += " WHERE " + " AND ".join(conditions)

                # Aggiungi l'ordinamento
                query += " ORDER BY time ASC;"

                # Esegui la query
                cursor.execute(query, params)
                data = cursor.fetchall()

                # Print the results of the query
                print("\nPrint the results of the query':")
                for row in data:
                    print(row)

    except Exception as e:
        print(f"Errore: {e}")
        return {"message": "An error occurred", "error": str(e)}