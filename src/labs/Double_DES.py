"""
This script implements a weaker version of the double DES
to give an example of how an attacker can exploit it's weakness. 
Double DES sounds like a good idea but it turns out that it
does not grow the possible key space as expected. 


To implement a double DES, we take the same methods of the DES 
example and apply them twice:
- encrypt message with key 1 to get cipher 1
- encrypt cipher 1 with key 2

Both modes of operation are still applicable:
- ECB: Electronic Code Book
- CBC: Cipher Block Chaining
"""

from pyDES import *
import random

message = "01234567"
key_11 = random.randrange(0, 256)
key_1 = bytes([key_11, 0, 0, 0, 0, 0, 0, 0])
key_21 = random.randrange(0, 256)
key_2 = bytes([key_21, 0, 0, 0, 0, 0, 0, 0])
iv = bytes([0] * 8)

k1 = des(key_1, ECB, iv, pad=None, padmode=PAD_PKCS5)
k2 = des(key_2, ECB, iv, pad=None, padmode=PAD_PKCS5)

# Alice sending the encrypted message
cipher = k1.encrypt(k2.encrypt(message))
print("Key 11:", key_11)
print("Key 21:", key_21)
print("Encrypted", cipher)

# This is Bob
message = k2.decrypt(k1.decrypt(cipher))
print("Decrypted:", message)

# Eve's attack on Double DES
# GOAL: find the keys 1, 2
# assume you have the cipher and you know at least
# part of the message

# loop through the first 256 possible keys
# store the ciphers in a lookup dictionary
lookup = {}  # cipher: key

for i in range(256):
    key = bytes([i, 0, 0, 0, 0, 0, 0, 0])
    k = des(key, ECB, iv, pad=None, padmode=PAD_PKCS5)
    lookup[k.encrypt(message)] = i

for i in range(256):
    key = bytes([i, 0, 0, 0, 0, 0, 0, 0])
    k = des(key, ECB, iv, pad=None, padmode=PAD_PKCS5)
    if k.decrypt(cipher) in lookup:
        print("Key 11:", i)
        print("Key 21:", lookup[k.decrypt(cipher)])
        key_1 = bytes([i, 0, 0, 0, 0, 0, 0, 0])
        key_2 = bytes([lookup[k.decrypt(cipher)], 0, 0, 0, 0, 0, 0, 0])
        k1 = des(key_1, ECB, iv, pad=None, padmode=PAD_PKCS5)
        k2 = des(key_2, ECB, iv, pad=None, padmode=PAD_PKCS5)
        message = k2.decrypt(k1.decrypt(cipher))
        print("Decrypted:", message)
