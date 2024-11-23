import tkinter as tk
from tkinter import filedialog, messagebox
import main
from Crypto.Random import get_random_bytes
from tkinter.simpledialog import askstring

# Generate a random AES key for encryption and decryption
def generate_key():
    return get_random_bytes(16)  # 128-bit key for AES

# Encrypt File
# Encrypt File
def encrypt_file_gui():
    file_path = filedialog.askopenfilename(title="Select a file to encrypt")
    if file_path:
        key = generate_key()  # Generate a random AES key
        try:
            # Call encrypt_and_shred instead of encrypt_file
            encrypted_file = main.encrypt_and_shred(file_path, key)
            # Show the generated key to the user
            key_hex = key.hex()
            messagebox.showinfo(
                "Success",
                f"File encrypted and shredded successfully!\nEncrypted file: {encrypted_file}\n\n"
                f"Save this key to decrypt later: {key_hex}",
            )
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
    else:
        messagebox.showerror("Error", "No file selected.")
        
    print(f"AES Key (hex): {key.hex()}")  # Add this line to display the key




def decrypt_file_gui():
    encrypted_file_path = filedialog.askopenfilename(title="Select an encrypted file to decrypt")
    if encrypted_file_path:
        # Ask the user to provide the original key
        key_hex = askstring("Input Key", "Enter the AES key (in hex format):")
        if key_hex:
            try:
                key = bytes.fromhex(key_hex)  # Convert hex key back to bytes
                decrypted_file = main.decrypt_file(encrypted_file_path, key)
                messagebox.showinfo("Success", f"File decrypted successfully!\nDecrypted file: {decrypted_file}")
            except ValueError as e:
                messagebox.showerror("Error", f"An error occurred: {e}")
        else:
            messagebox.showerror("Error", "Key not provided.")
    else:
        messagebox.showerror("Error", "No file selected.")


# Shred File
def shred_file_gui():
    file_path = filedialog.askopenfilename(title="Select a file to shred")
    if file_path:
        try:
            result = main.shred_file(file_path)
            messagebox.showinfo("Success", result)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
    else:
        messagebox.showerror("Error", "No file selected.")

# Create GUI
def create_gui():
    window = tk.Tk()
    window.title("File Encryptor, Decryptor & Shredder")
    window.geometry("400x300")
    window.configure(bg="#f0f8ff")  # Light blue background

    # Title Label
    title_label = tk.Label(
        window, text="File Encryptor, Decryptor & Shredder", font=("Helvetica", 16, "bold"), bg="#f0f8ff"
    )
    title_label.pack(pady=20)

    # Buttons with styling
    button_style = {"font": ("Helvetica", 12), "bg": "#4caf50", "fg": "white", "width": 20, "height": 2}

    encrypt_button = tk.Button(window, text="Encrypt File", command=encrypt_file_gui, **button_style)
    encrypt_button.pack(pady=10)

    decrypt_button = tk.Button(window, text="Decrypt File", command=decrypt_file_gui, **button_style)
    decrypt_button.pack(pady=10)

    shred_button = tk.Button(window, text="Shred File", command=shred_file_gui, **button_style)
    shred_button.pack(pady=10)

    # Run the main loop
    window.mainloop()

if __name__ == "__main__":
    create_gui()

