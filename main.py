import os
from encrypt import encrypt_and_shred as encrypt_function
from decrypt import decrypt_file as decrypt_function
import shred

# Encrypt a file
def encrypt_file(file_path, key):
    """
    Encrypt the file and save it as a new file.
    """
    encrypted_file = encrypt_function(file_path, key)  # Corrected to call the encrypt_file function from encrypt.py
    return encrypted_file

# Decrypt a file
def decrypt_file(encrypted_file_path, key):
    """
    Decrypt the file using the provided key.
    """
    decrypted_file = decrypt_function(encrypted_file_path, key)  # Corrected to call the decrypt_file function from decrypt.py
    return decrypted_file

# Shred a file
def shred_file(file_path):
    """
    Shred the file (delete it securely).
    """
    result = shred.shred_file(file_path)
    return result

# Encrypt and Shred a file
def encrypt_and_shred(file_path, key):
    """
    Encrypt the file and then shred the original file.
    """
    encrypted_file = encrypt_file(file_path, key)
    shred_file(file_path)
    return encrypted_file

