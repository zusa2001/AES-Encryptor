from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from aesEncryptor import encryptorAES
from aesDecryptor import decryptorAES
import os

# AES Key and IV Generation
key = os.urandom(32)  # 256-bit AES key
iv = os.urandom(16)   # 16-byte IV for AES
flag = False

if os.path.exists("encrypted_data.bin"):
    with open("encrypted_data.bin", "rb") as file:
        content = file.read()
        flag = True
else:
    print("You need to create a new Entry")
   
def add_entry(): 
    new_entry = input("Write the message you want to encrypt:\n")
    ciphertext=encryptorAES(new_entry, key, iv)
    # Write the IV and ciphertext to a binary file
    with open("encrypted_data.bin", "wb") as binary_file:
        binary_file.write(iv + ciphertext)
    with open("key.bin", "wb") as text_file:
        text_file.write(key)

def search_entry():
    print("in progress")
    
def list_all_entries():
    if os.path.exists("encrypted_data.bin"):
        with open("encrypted_data.bin", "rb") as file:
            content = file.read()
        with open("key.bin", "rb") as file:
            key = file.read()
        decryptorAES(content,key)
    else:
        print("You need to create a new Entry")

def menu():
    while True:
        print("\nMenu:")
        print("1. Add an Entry")
        print("2. Search for a Specific Entry")
        print("3. List All Entries")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            add_entry()
        elif choice == "2":
            search_entry()
        elif choice == "3":
            list_all_entries()
        elif choice == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please try again.")
menu()