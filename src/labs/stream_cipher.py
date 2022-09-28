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
        # by first taking the integer division of the LSB, 
        # we can take the modulus of the 8 most significant bits, increasing
        # the key space over the previous version

        return (self.rand() // 2**23) % 256
    def get_key_byte_old(self):
        # modulus with 256 in order to get one byte
        # will shift the original key down to 8 bit
        # that reduces the key size significantly. not good
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
    
def get_key(message, cipher):
    """
    Recover key from message and cipher
    """
    return bytes([message[i] ^ cipher[i] for i in range(len(message))])

def crack(key_stream, cipher):
    """
    Recover key from message and cipher
    """
    length = min(len(key_stream), len(cipher))
    return bytes([key_stream[i] ^ cipher[i] for i in range(length)])

def brute_force(plain, cipher):
    """
    Brute force attack on a stream cipher

    Parameters
    ----------
    plain : bytes
        known plaintext
    cipher : bytes
        ciphertext
    """
    # brute force all possible keys

    # loop through all possible keys
    for i in range(2**31):
        bf_key = KeyStream(i)
        # using test key and known plaintext, 
        # xor plaintext with cipher byte-by-byte and compare results with 
        # key
        # if one byte does not match, get next key
        for k in range(len(plain)):
            xor_value = plain[k] ^ cipher[k]
            if xor_value != bf_key.get_key_byte():
                break
        else:
            print("Found key: ", i)
            return i
    return False

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


def example_2_authenticity_weakness():
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


def example_3_reuse_keys_weakness():
    """
    This example runs though an attack on a stream cipher to 
    recover the key used. 

    Keys can be poached if message is known by attacker. 
    
    """
    # message known by attacker. 
    attacker_message = "This is the most valued secret of all time".encode()
    
    # Alice sends message to Bob
    key = KeyStream(10)
    message = attacker_message
    print(message)
    cipher = encrypt(key, message)
    print(cipher)

    # attacker intercepts message and can now recover the key
    attacker_key_stream = get_key(attacker_message, cipher)

    # Alice sends another message to Bob
    key = KeyStream(10)
    message = "Plan to take over the world. Using robots and social engineering in that order".encode()
    cipher = encrypt(key, message)
    print(cipher)

    # Bob decrypts the message
    key = KeyStream(10)
    print(encrypt(key, cipher))

    # Attacker eve intercepts the new message
    print(crack(attacker_key_stream, cipher))



    return 

def example_4_low_entropy_weakness():
    """
    The key generator can have low-entropy, exposing a weakness to
    brute-force cracking.


    """
    # Alice send a message to Bob
    secret_key = random.randrange(0, 2**20)
    key = KeyStream(secret_key)
    message = "MESSAGE: This is the most valued secret of all time".encode()
    print(f"Secret Key: {secret_key}")
    print(message)
    cipher = encrypt(key, message)
    print(cipher)

    # Bob decrypts the message
    key = KeyStream(secret_key)
    print(encrypt(key, cipher))

    # This is the attacker
    # In this case, the message has a header. Therefore we know  the first few bytes of the message
    print("\n** Attack **\n")
    header = "MESSAGE: ".encode()
    bf_key = brute_force(header, cipher)
    key = KeyStream(bf_key)
    message = encrypt(key, cipher)
    
    print(message)

    # Key takeaway:
    # Only a few bytes of known text are necessary to brute force a cipher to recover the key. 




example_4_low_entropy_weakness()