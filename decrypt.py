from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def decrypt_file(encrypted_file_path, key):
    """
    Decrypt a file using AES in CBC mode.
    - Expects the first 16 bytes of the file to be the IV.
    """
    if not key:
        raise ValueError("AES key is required for decryption.")

    try:
        # Open the encrypted file
        with open(encrypted_file_path, 'rb') as encrypted_file:
            iv_from_file = encrypted_file.read(16)  # Read IV (first 16 bytes)
            encrypted_data = encrypted_file.read()  # Read the rest (ciphertext)
        
        # Create AES cipher for decryption
        cipher = AES.new(key, AES.MODE_CBC, iv_from_file)
        decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)  # Decrypt and unpad

        # Save the decrypted data to a new file
        decrypted_file_path = encrypted_file_path.replace('.enc', '.dec')
        with open(decrypted_file_path, 'wb') as decrypted_file:
            decrypted_file.write(decrypted_data)

        print(f"File decrypted successfully. Saved as: {decrypted_file_path}")  # Debugging: Print file path
        return decrypted_file_path
    
    except Exception as e:
        print(f"Error during decryption: {e}")
        raise

