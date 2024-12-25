from cryptography.fernet import Fernet 

def generate_key():
    key = Fernet.generate_key()
    with open("key.key",'wb') as key_file:
        key_file.write(key)
        key_file.close()

def load_key():
    with open("key.key", 'rb') as key_file:
        key = key_file.read()
    return key 

def encrypt_file(file_path, key):
    chiper = Fernet(key)
    with open(file_path, 'rb') as file:
        file_data = file.read()
    encrypt_data = chiper.encrypt(file_data)    
    with open(file_path, "wb") as file:
        file.write(encrypt_data)

def decrypt_file(file_path, key):
    cipher = Fernet(key)
    with open(file_path, 'rb') as file:
        encrypt_data = file.read()
    decrypt_data = cipher.decrypt(encrypt_data)
    with open(file_path,'wb') as file:
        file.write(decrypt_data)

# Generate a new key (run this only once)
# generate_key()

key = load_key()

#Encrypt file 
# try:
#     file_to_encrypt = "playing.txt"
#     encrypt_file(file_to_encrypt, key)
#     print("File encrypted successfully")
# except FileNotFoundError:
#     print("File not found")
# except ValueError:
#     print("Authentication Error")
#Decrypt the file
try: 
    file_to_decrypt= "playing.txt"
    decrypt_file(file_to_decrypt,key)
    print("File Decrypted successfully")
except FileNotFoundError:
    print("File not found")
except ValueError:
    print("Authentication Error")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
