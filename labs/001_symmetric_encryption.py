from cryptography.fernet import Fernet


def new_key_simple_text():

    # key generation
    # key will be in byte format
    key = Fernet.generate_key()

    print(f"new key: {key}")

    # create a cipher, engine to encrypt data
    cipher = Fernet(key)

    # encrypt text using the cipher
    # plaintext must be byte encoded first
    encrypted_text = cipher.encrypt(b'this is the secret')

    print(encrypted_text)

    decrypted_text = cipher.decrypt(encrypted_text)

    print(decrypted_text.decode())


def key_from_file_encrypt_file():
    # grab key from file
    with open('data/001_key.key', 'rb') as file:
        key = file.read()

    print(f"key from file: {key}")

    # grab plaintext from file
    with open('data/001_plaintext.txt', 'rb') as file:
        data = file.read()

    print(data)

    cipher = Fernet(key)
    encrypted_data = cipher.encrypt(data)

    with open('results/001_encrypted_data.txt', 'wb') as e_file:
        e_file.write(encrypted_data)

    decrypted_data = cipher.decrypt(encrypted_data)
    with open('results/001_decrypted_data.txt', 'wb') as d_file:
        d_file.write(decrypted_data)

if __name__ == "__main__":
    key_from_file_encrypt_file()
