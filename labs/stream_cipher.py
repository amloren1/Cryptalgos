import random

class KeyStream:
    """
    liner congruential generator
    """
    def __init__(self, key = 1):
        self.next = key

    def rand(self):
        self.next = (1103515245 * self.next + 12345) % 2**31

        return self.next

    def get_key_byte(self):
        return self.rand() % 256

def encrypt(key, message):
    return bytes( [message[i] ^ key.get_key_byte() for i in range(len(message)) ])

def transmit(cipher, likely):
    """simulates transmission errors when passing cipher"""
    b =[]
    for c in cipher:
        if random.randrange(0,likely) == 0:
            c = c ^ 2**random.randrange(0, 8)

        b.append(c)
    return bytes(b)
    
def example_1():
    key = KeyStream(11)
    message = "HEY YOU".encode()
    cipher = encrypt(key, message)
    print(cipher)

    key.next = 11
    # decrypt
    print(encrypt(key, cipher))

def modification(cipher):
    """ modify cipher
    Proof:

    key ^ message = cipher
    mod = message ^ new_message
    cipher' = cipher ^ mod
    message' = cipher' ^ key = cipher ^ mod ^ key 
        = cipher ^ message ^ new_message ^ key 
        = message ^ key ^ message ^ new_message ^ key 
        = new_message
    """
    mod = [0] * len(cipher)

    mod[10] = ord(" ") ^ ord("1")
    mod[11] = ord(" ") ^ ord("0")
    mod[12] = ord("1") ^ ord("0")
    return bytes(mod[i] ^ cipher[i] for i in range(len(cipher)))


def example_2():
    """
    Message authenticity issues with stream ciphers

    Bob wants to intercept a message from Alice to Bank
    and modify amount of money sent to Bob
    """
    key = KeyStream(10)

    message = "Send Bob:   10$".encode()
    cipher = encrypt(key, message)
    print(cipher)
    print(message)

    # modify
    mod = modification(cipher)
    key = KeyStream(10)
    # decrypt
    print(encrypt(key, mod))

example_2()