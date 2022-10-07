import random


def generate_key():

    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cletters = list(letters)
    key = {}

    for c in letters:
        key[c] = cletters.pop(random.randint(0, len(cletters) - 1))

    return key


def encrypt(key, message):
    cipher = ""
    for c in message:
        if c in key:
            cipher += key[c]
        else:
            cipher += c

    return cipher


def get_decryption_key(key: dict):
    dkey = {}

    for char in key:
        dkey[key[char]] = char

    return dkey


key = generate_key()

cipher = encrypt(key, "HEY YOU")
print(cipher)
