from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import urllib.parse
import binascii
from binascii import unhexlify

# Global variables for key and IV
key = get_random_bytes(16)
iv = get_random_bytes(16)

def cbc_encrypt(plaintext, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_plaintext = pad(plaintext, AES.block_size)
    ciphertext = cipher.encrypt(padded_plaintext)
    return ciphertext

def decrypt(encryptedParams):
	cipher = AES.new(key, AES.MODE_CBC,iv)
	paddedParams = cipher.decrypt(unhexlify(encryptedParams))
	return (unpad(paddedParams, 16, style = 'pkcs7'))


def submit():
    userInput = input("Enter a string: ")
    urlEncoded = urllib.parse.quote(userInput, safe="")
    modifiedInput = "userid=456;userdata=" + urlEncoded + ";session-id=31337"

    print(modifiedInput)
    encrypted = (cbc_encrypt(modifiedInput.encode(), key, iv))
    return encrypted
    

def verify(encryptedInput):
    decrypted = decrypt(encryptedInput)

    if b";admin=true;" in decrypted:
        return True

    return False



def main():
    encrypted = submit()
    print(verify(encrypted))

if __name__=="__main__":
    main()