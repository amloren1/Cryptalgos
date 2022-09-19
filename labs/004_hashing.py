"""
Hashing can be used to validate the integrity of a file. The hash of the file is
calculated and stored with the file. When the file is opened, the hash is
calculated again and compared to the stored hash. If they match, the file is
assumed to be uncorrupted.

"""

import rsa


def example_1():
    message = b"text to be hashed"

    hashed_text = rsa.compute_hash(message, "SHA-1")  # normally do not use SHA-1

    print(hashed_text.hex())

    # change the message text slightly and compare hashes

    message = b"text to behashed."

    hashed_text_2 = rsa.compute_hash(message, "SHA-1")

    print(hashed_text_2.hex())


def example_2():
    """
    do the same with SHA-512. More secure and less chance of collisions
    """
    message = b"longer message to be hashed. SHA-512 will always produce a hash of the same length"

    hashed_text = rsa.compute_hash(message, "SHA-512")

    print(hashed_text.hex())


if __name__ == "__main__":
    example_2()
