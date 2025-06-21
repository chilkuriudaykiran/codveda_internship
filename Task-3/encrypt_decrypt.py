from cryptography.fernet import Fernet

# Generate and save a key (do this only once)
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

# Load the key from file
def load_key():
    return open("secret.key", "rb").read()

# Encrypt the file content
def encrypt_file(filename):
    key = load_key()
    f = Fernet(key)
    with open(filename, "rb") as file:
        original = file.read()
    encrypted = f.encrypt(original)
    with open("encrypted_" + filename, "wb") as enc_file:
        enc_file.write(encrypted)
    print(f"✅ Encrypted: encrypted_{filename}")

# Decrypt the file content
def decrypt_file(filename):
    key = load_key()
    f = Fernet(key)
    with open(filename, "rb") as enc_file:
        encrypted = enc_file.read()
    decrypted = f.decrypt(encrypted)
    with open("decrypted_" + filename, "wb") as dec_file:
        dec_file.write(decrypted)
    print(f"✅ Decrypted: decrypted_{filename}")

# MAIN PROGRAM
if __name__ == "__main__":
    import os

    if not os.path.exists("secret.key"):
        generate_key()

    action = input("Enter 'e' to encrypt or 'd' to decrypt: ").lower()
    file = input("Enter the file name (e.g. myfile.txt): ")

    if action == 'e':
        encrypt_file(file)
    elif action == 'd':
        decrypt_file(file)
    else:
        print("❌ Invalid choice. Use 'e' or 'd'.")