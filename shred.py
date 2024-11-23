# shred.py
import os
import random
import string

def shred_file(file_path):
    """
    Shred the file by overwriting its contents and then deleting it.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")

    # Overwrite the file with random data to ensure its contents are gone
    with open(file_path, "r+b") as f:
        length = os.path.getsize(file_path)
        for _ in range(3):  # Overwrite 3 times
            f.seek(0)
            f.write(bytearray(random.getrandbits(8) for _ in range(length)))
    
    # Delete the file after overwriting
    os.remove(file_path)

    return f"File {file_path} shredded successfully."

