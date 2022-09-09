"""
File integrity and sender verification can be done with a combination of 
document hasing and digital signature. One common routine to achieve this:

Sending file
1. Hash document 
2. Encrypt hash with the sender's PRIVATE KEY. This is the digital signature.
3. Encrypt the document with the RECIPIENTS'S PUBLIC KEY

Upon file receipt
1. Decrypt file with the recipient's PRIVATE KEY
2. Use the sender's public key to decrypt the hash (digital signature).
    - if this step fails, the file was not sent by the sender that was expected
3. Has the file to compare with the provided hash. If both hashes are the same, file 
    is the same as the one the sender intended to send. 


"""
import rsa

PUBLIC_KEY_FILE = 'data/005_public_key_file.pem'
PRIVATE_KEY_FILE = 'data/005_private_key_file.pem'

def create_keys():

    public_key, private_key = rsa.newkeys(2048)

    with open(PUBLIC_KEY_FILE, 'wb') as file:
        file.write(public_key.save_pkcs1('PEM'))
    
    with open(PRIVATE_KEY_FILE, 'wb') as file:
        file.write(private_key.save_pkcs1('PEM'))

def sign_document():
    """
    Hash document and user sender's private key to sign/encrypt the hash

    """
    # bring up the private key
    with open(PRIVATE_KEY_FILE, 'rb') as file:
        private_key = rsa.PrivateKey.load_pkcs1(file.read())

    # load the document to sign
    with open('data/001_plaintext.txt', 'rb') as file:
        plaintext = file.read()

    # sign file use SHA-1 hash

    signature_file = rsa.sign(plaintext, private_key, 'SHA-1')

    print(len(signature_file)) # should be 256

    # save signature file
    with open('data/005_signature_file', 'wb') as file:
        file.write(signature_file)

def verify_signed_document():
    """
    Use the sender's public key to verify document signature
    
    """ 

    # load public key
    with open(PUBLIC_KEY_FILE, 'rb') as file:
        public_key = rsa.PublicKey.load_pkcs1(file.read())

    # load original document (assuming this has already been decrypted)
    with open('data/001_plaintext.txt', 'rb') as file:
        plaintext = file.read()
    
    # load signature file
    with open('data/005_signature_file', 'rb') as file:
        signature_file = file.read()

    # decrypt signature with pub key, check hash against plaintext doc hash
    # will return rsa.pkcs1.VerificationError: Verification failed if there are issues
    verify_file = rsa.verify(plaintext, signature_file, public_key)

    print(verify_file) # prints the hash method used

if __name__ == '__main__':

    # create_keys()
    # sign_document()
    verify_signed_document()