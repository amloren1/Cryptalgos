def key_generator(n: int):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    key = {}
    for idx, char in enumerate(letters):
        key[char] = letters[(idx + n) % len(letters)]

    return key


def get_decryption_key(key: dict):
    dkey = {}

    for char in key:
        dkey[key[char]] = char

    return dkey


def encrypt(key: dict, message: str):
    cipher = ""
    for char in message.upper():
        if char in key:
            cipher += key[char]

        else:
            cipher += char  # keep the spaces

    return cipher


key = key_generator(2)
decryption_key = key_generator(26 - 2)
cipher = encrypt(key=key, message="hey you")
dcipher = encrypt(key=get_decryption_key(key), message=cipher)
print(cipher)
print(dcipher)
