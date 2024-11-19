import os
import subprocess
from datetime import datetime

def backup_postgres_database(db_name, user, password, host='localhost', port=5432, backup_dir='backups'):
    """
    Backs up a PostgreSQL database using pg_dump
    
    Parameters:
        db_name (str): The name of the database to back up
        user (str): The PostgreSQL username
        password (str): The PostgreSQL password
        host (str): The PostgreSQL host
        port (int): The PostgreSQL port 
        backup_dir (str): The directory to store the backup file
    """
    try:
        # Create the backup directory if it doesn't exist
        if not os.path.exists(backup_dir):
            os.makedirs(backup_dir)
        
        # Generate a timestamped filename
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        backup_file = os.path.join(backup_dir, f"{db_name}_backup_{timestamp}.sql")
        
        # Set the PGPASSWORD environment variable for authentication
        env = os.environ.copy()
        env["PGPASSWORD"] = password
        
        # Construct the pg_dump command
        dump_command = [
            "pg_dump",
            "-h", host,
            "-p", str(port),
            "-U", user,
            "-F", "c",  # Custom format; for plain SQL, use '-F p'
            "-f", backup_file,
            db_name
        ]
        
        # Execute the command
        subprocess.run(dump_command, env=env, check=True)
        
        print(f"Backup successful! File saved to: {backup_file}")
    
    except Exception as e:
        print(f"An error occurred during the backup: {e}")

# Configuration
DB_NAME = "Db_name"
DB_USER = "UserName"
DB_PASSWORD = "Password"
DB_HOST = "localhost"
DB_PORT = 5432
BACKUP_DIR = "backups"

# Perform the backup
backup_postgres_database(DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, BACKUP_DIR)
