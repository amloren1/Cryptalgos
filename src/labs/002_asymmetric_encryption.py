import rsa


def exercise_1():
    """
    Generating and saving key pairs
    """
    # generate a keypair 1024 bits
    public_key, private_key = rsa.newkeys(1024)

    print(public_key)
    # save key to a file
    print(public_key.save_pkcs1())  # Public Key Cryptography Standard 1

    print(public_key.save_pkcs1("PEM").decode())  # decode to text


def exercise_2():
    """
    Encrypting text.

    Asymmetric encryption uses a public and private key pair.
    In this example, we will encrypt with a public key and decrypt with a private key.
    This method of passing information will allow users to encrypt messages
    with my own public key so that I (the private key owner) am the only one who
    can view the decrypted message.

    RSA can only encrypt messages that are smaller than the keys. Therefore this is not a method
    for encrypting large files.
    """

    # generate the key pair
    public_key, private_key = rsa.newkeys(1024)

    e_data = rsa.encrypt(b"this is a secret message", public_key)

    print(e_data)

    d_data = rsa.decrypt(e_data, private_key)

    print(d_data.decode())


if __name__ == "__main__":

    exercise_2()
