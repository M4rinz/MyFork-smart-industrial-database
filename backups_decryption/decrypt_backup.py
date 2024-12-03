from cryptography.fernet import Fernet
from dotenv import load_dotenv
import os

def load_key():
    return os.getenv("KEY")

def decrypt(filepath, key):
    data = None
    with open(filepath, "rb") as f_backup:
        data = f_backup.read()
    if (data is None) or (len(data) <= 0):
        return False 
    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(data)
    filename = filepath.split("/")[-1]
    print(filename)
    with open("decrypted_" + filename, "wb") as f_backup:
        f_backup.write(decrypted_data)

load_dotenv()
decrypt("../backups/SmartApps_backup_20241121105637.sql",load_key())