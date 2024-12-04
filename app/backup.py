import argparse
import os
import subprocess
from datetime import datetime
from cryptography.fernet import Fernet
from dotenv import load_dotenv
import os



def load_key():
    return os.getenv("KEY")


def encrypt_backup_file(filename, file_data):
    """Encrypt the content of a file."""
    key = load_key()
    fernet = Fernet(key)

    # Encrypt the file data
    encrypted_data = fernet.encrypt(file_data)
    # Write the encrypted data back to the file
    with open(filename, "wb") as file:
        file.write(encrypted_data)
    print(f"File '{filename}' has been encrypted.")


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
        dump_command = [
            "pg_dump",
            "-h", host,
            "-p", str(port),
            "-U", user,
            "-F", "c",  # Custom format; for plain SQL, use '-F p'
            db_name
        ]
        # Execute the command and capture the output
        result = subprocess.run(dump_command, env=env, check=True, stdout=subprocess.PIPE)
        # Return the output as a byte stream
        encrypt_backup_file(backup_file,result.stdout)
        print(f"Backup successful! File saved to: {backup_file}")
    except Exception as e:
        print(f"An error occurred during the backup: {e}")


def main():
    load_dotenv()

    # Create the parser
    '''parser = argparse.ArgumentParser(description="Process model_name from the terminal.")
    parser.add_argument("db_name", type=str, help="database name")
    parser.add_argument("db_username", type=str, help="database user name")
    parser.add_argument("db_password", type=str, help="Database user password")
    parser.add_argument("db_host", type=str, help="Database address")
    parser.add_argument("db_port", type=str, help="Database port")
    parser.add_argument("backup_dir", type=str, help="Directory where to store backups")
    args = parser.parse_args()'''
    # Configuration
    DB_NAME = os.getenv('DB_NAME')
    DB_USER = os.getenv('DB_USER')
    DB_PASSWORD = os.getenv('DB_PASSWORD')
    DB_HOST = os.getenv('DB_HOST')
    DB_PORT =  os.getenv('DB_PORT')
    BACKUP_DIR =  os.getenv('BACKUP_DIR')

    # Perform the backup
    backup_postgres_database(DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, BACKUP_DIR)

if __name__ == "__main__":
    main()