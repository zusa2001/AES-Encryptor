from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os

def decryptorAES(encrypted_data,key):
    # Extract the IV and the actual ciphertext from the binary data
    iv_from_file, ciphertext_from_file = encrypted_data[:16], encrypted_data[16:]

    # Decrypt the data
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv_from_file), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_padded_text = decryptor.update(ciphertext_from_file) + decryptor.finalize()

    # Unpad the decrypted text
    unpadder = padding.PKCS7(128).unpadder()
    decrypted_text = unpadder.update(decrypted_padded_text) + unpadder.finalize()

    # Print the decrypted text
    print("Decrypted Text:", decrypted_text.decode())