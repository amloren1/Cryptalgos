"""
Encrypting asymmetrically with RSA introduces a limitation that RSA can only encrypt messages
shorter than the length of the keys. Symmetric encryption does not have this limitation. 
A common technique then is to encrypt files with symmetric encryption methods and pass the 
keys using asymmetric encryption. This module will demonstrate this in practice:

1. Generate public and private key pair. Same them to .pem files
2. Generate a symmetric key and cipher
3. Encrypt the symmetric key with the public key
4. Encrypt the file and encrypted key into the same file with symmetric encryption


"""

from cryptography.fernet import Fernet
import rsa


def generate_key_pair():
    public_key, private_key = rsa.newkeys(1024)

    with open("data/003_public_key_file.pem", "wb") as file:
        file.write(public_key.save_pkcs1("PEM"))

    with open("data/003_private_key_file.pem", "wb") as file:
        file.write(private_key.save_pkcs1("PEM"))


def encrypt_file_and_key():
    """
    Asymmetrical encryption of the symmetric key

    Symmetric encryption is used to encrypt the encrypted key and the encrypted file
    into the same file.
    """

    # symmetric key
    key = Fernet.generate_key()

    cipher = Fernet(key)

    # open the public key file, encrypt the symmetric key with it
    with open("data/003_public_key_file.pem", "rb") as file:
        public_key = rsa.PublicKey.load_pkcs1(file.read())
        encrypted_symmetric_key = rsa.encrypt(key, public_key)

    # encrypt the file with the symmetric key
    with open("data/001_plaintext.txt", "rb") as file:
        data = file.read()
        encrypted_data = cipher.encrypt(data)

    # save the encrypted symmetric key and encrypted data to a file
    with open("results/003_encrypted_data.txt", "wb") as file:
        file.write(encrypted_symmetric_key)
        file.write(encrypted_data)


def decrypt_file_and_key():
    """
    Decrypt the encrypted file and key

    Use the provided symmetric key to decrypt the file. Then decrypt the encrypted
    symmetric key with the private key.


    """

    # open the private key file, decrypt the symmetric key with it
    with open("data/003_private_key_file.pem", "rb") as file:
        private_key = rsa.PrivateKey.load_pkcs1(file.read())

    # open the encrypted file. The first 128 bytes are the encrypted symmetric key
    with open("results/003_encrypted_data.txt", "rb") as file:
        encrypted_symmetric_key = file.read(
            128
        )  # symmetric key encrypted with public key
        encrypted_data = file.read()

    symmetric_key = rsa.decrypt(encrypted_symmetric_key, private_key)

    cipher = Fernet(symmetric_key)

    decrypted_data = cipher.decrypt(encrypted_data)
    with open("results/003_decrypted_data.txt", "wb") as file:
        file.write(decrypted_data)


if __name__ == "__main__":
    generate_key_pair()
    encrypt_file_and_key()
    decrypt_file_and_key()
