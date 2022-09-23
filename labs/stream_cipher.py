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
    
key = KeyStream(11)
message = "HEY YOU".encode()
cipher = encrypt(key, message)
print(cipher)

key.next = 11
# decrypt
print(encrypt(key, cipher))