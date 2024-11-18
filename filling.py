import psycopg2
import pandas as pd
from os import path

DB_HOST = "localhost"
DB_NAME = "KPI_database"
DB_USER = "postgres"
DB_PASSWORD = "password"

# Obtain the asset_id and name from the dataset
pathname = path.join("smart_app_data.csv")
dataset = pd.read_csv(pathname)
assets = dataset[['asset_id', 'name']]
asset_dict = dict(zip(assets['asset_id'], assets['name']))

try:
    with psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    ) as conn:
        with conn.cursor() as cursor:
            print("Connessione al database riuscita.")

            # populate the machines table
            for asset_id, name in asset_dict.items():
                cursor.execute(
                    """
                    INSERT INTO machines (asset_id, name)
                    VALUES (%s, %s)
                    ON CONFLICT (asset_id) DO NOTHING;
                    """,
                    (asset_id, name)
                )
            # populate the real_time_data table
            for index, row in dataset.iterrows():
                cursor.execute(
                    """
                    INSERT INTO real_time_data (time, asset_id, name, kpi, sum,
                     avg, min, max)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                    ON CONFLICT (time, asset_id, kpi) DO NOTHING;
                    """,
                    (row['time'], row['asset_id'], row['name'], row['kpi'],
                     row['sum'], row['avg'], row['min'], row['max'])
                )

            conn.commit()

except Exception as e:
    print(f"Errore: {e}")
