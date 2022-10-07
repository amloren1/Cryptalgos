import random


def xor(x, s):
    print(f"{bin(x)} xor {bin(s)} = {bin(x ^ s)}")


def generate_key_stream(n):
    return bytes([random.randrange(0, 255) for _ in range(n)])


def xor_bytes(key_stream, message):
    print(len(key_stream))
    print(len(message))
    length = min(len(key_stream), len(message))
    return bytes([key_stream[i] ^ message[i] for i in range(length)])


message = "HEY YOU"
message = message.encode()
key_stream = generate_key_stream(len(message))
cipher = xor_bytes(key_stream, message)
print(cipher)
print(xor_bytes(key_stream, cipher))
