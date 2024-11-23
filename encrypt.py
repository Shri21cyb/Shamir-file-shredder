from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
import os

def encrypt_and_shred(file_path, key):
    """
    Encrypt a file using AES in CBC mode and shred the original file.
    """
    if not key:
        raise ValueError("AES key is required for encryption.")

    with open(file_path, 'rb') as file:
        data = file.read()  # Read plaintext data

    # Generate a random IV for encryption
    cipher = AES.new(key, AES.MODE_CBC)
    iv = cipher.iv
    encrypted_data = cipher.encrypt(pad(data, AES.block_size))  # Encrypt and pad the data

    # Save the IV and encrypted data to a new file
    encrypted_file_path = file_path + '.enc'
    with open(encrypted_file_path, 'wb') as encrypted_file:
        encrypted_file.write(iv)  # Write IV (first 16 bytes)
        encrypted_file.write(encrypted_data)  # Write encrypted content

    # Shred the original file by overwriting it with random data
    shred_file(file_path)

    print(f"File encrypted successfully. Saved as: {encrypted_file_path}")  # Debugging: Print file path
    return encrypted_file_path

def shred_file(file_path):
    """
    Overwrite the file with random data to prevent recovery, then delete it.
    """
    try:
        file_size = os.path.getsize(file_path)
        with open(file_path, 'wb') as file:
            file.write(get_random_bytes(file_size))  # Overwrite with random bytes
        os.remove(file_path)  # Delete the file
        print(f"File shredded successfully: {file_path}")
        return "File shredded successfully."
    except Exception as e:
        print(f"Error during shredding: {e}")
        raise

