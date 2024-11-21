from cryptography.fernet import Fernet

def generate_key():
    """Generate and save a key for encryption."""
    key = Fernet.generate_key()
    with open("enc_key.key", "wb") as key_file:
        key_file.write(key)
    return key

generate_key()