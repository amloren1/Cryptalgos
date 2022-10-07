from email import message
from pyDES import *


def exapmple_1():
    """
    Uses DES algorithm to encrypt repeated 8 byte blocks.

    We attempt the encryption with two modes:
        ECB
        CBC

    When using ECB, we see that the resulting cipher of the first block
    is identical to that of the second block. This is an inherent flaw of this
    encryption mode. Each block is taken individually without relation to neighboring
    blocks. Another example of this flaw is encrypting an image with a uniform background
    the background and subject are clearly shown if ECB mode is used.

    This is in contrast to CBC mode which takes in an initialization vector to xor the plaintext
    before encryption. Each subsequent block is xord with the previous block, creating
    more entropy.
    """
    message = "0123456701234567"
    key = "DESCRYPT"
    iv = bytes([0] * 8)
    # create the cipher here
    k = des(key, CBC, iv, pad=None, padmode=PAD_PKCS5)
    cipher = k.encrypt(message)
    message = k.decrypt(cipher)
    # Alice sending the encrypted message
    # encrypt the message to cipher
    print("Length of plain text:", len(message))
    print("Length of cipher text:", len(cipher))

    # Bob decrypting the cipher text
    # decrypt the cipher to message
    print("Decrypted:", message)


def modification(cipher):
    mod = [0] * len(cipher)

    mod[9] = ord(" ") ^ ord("1")
    # mod[11] = ord(' ') ^ ord('0')
    # mod[12] = ord('1') ^ ord('0')

    return bytes([mod[i] ^ cipher[i] for i in range(len(cipher))])


def example_2_modifying_data():
    """
    This example attempts to show the results of modifying the cipher
    in the same way we did with the stream cipher.

    We modify the data one byte at a time. This fails because DES is a block cipher
    so any modification on one byte will destroy the within the block.

    Again, we see a difference here with the two modes we are exploring ECB, CBC.
    With ECB because the blocks are independent, modifying one byte will only
    scramble one block.  Modifying one byte in CBC mode will modify the same byte position in the next block,
    furthering the disruption of the original message.
    """

    message_org = "Give Bob:   10$ and send them to him"

    ###
    # Try this first with ECB
    ###
    key = "DESCRYPT"
    iv = bytes([0] * 8)
    # create the cipher here
    k = des(key, ECB, iv, pad=None, padmode=PAD_PKCS5)
    cipher = k.encrypt(message_org)
    # Alice sending the encrypted message
    # encrypt the message to cipher
    print("Length of plain text:", len(message_org))
    print("Length of cipher text:", len(cipher))

    # modify the cipher before decryption
    cipher = modification(cipher)

    # Bank decrypting the cipher text
    # decrypt the cipher to message
    message = k.decrypt(cipher)
    print("Decrypted:", message)

    ###
    # try again with CBC mode
    ###
    print("\nTrying the same modification with CBC:\n")
    k = des(key, CBC, iv, pad=None, padmode=PAD_PKCS5)
    cipher = k.encrypt(message_org)
    # Alice sending the encrypted message
    # encrypt the message to cipher
    print("Length of plain text:", len(message))
    print("Length of cipher text:", len(cipher))

    # modify the cipher before decryption
    cipher = modification(cipher)

    # Bank decrypting the cipher text
    # decrypt the cipher to message
    message = k.decrypt(cipher)
    print("Decrypted:", message)


example_2_modifying_data()
