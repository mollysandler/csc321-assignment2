from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from Crypto.Random import get_random_bytes

# Global variables for key and IV
key = get_random_bytes(16)
iv = get_random_bytes(16)


def pkcs7_pad(data, block_size): #writing my own padding function
   padding_value = block_size - len(data) % block_size #16 bytes-remaining space
   padded_data = data + bytes([padding_value] * padding_value) # create bytes object
   return padded_data

def unpad_pkcs7(data):
    padding = data[-1]
    return data[:-padding]

def cbc_encrypt(plaintext, key, iv): 
    cipher = AES.new(key, AES.MODE_CBC, iv)  # create AES cipher object, Use CBC mode 
    padded_plaintext = pkcs7_pad(plaintext, AES.block_size)  # Pad the plaintext
    ciphertext = cipher.encrypt(padded_plaintext) # encrypt the padded plaintext
    return ciphertext

def decrypt(encryptedText):
    decipher = AES.new(key, AES.MODE_CBC, iv)
    paddedText = decipher.decrypt(encryptedText)
    original = unpad_pkcs7(paddedText)
    return original

def submit():
    userInput = "#admin^true#"
    modifiedInput = "userid=456;userdata=" + userInput + ";session-id=31337"
    print("Modified Input: ", modifiedInput)
    print("\n")
    
    ciphertext = cbc_encrypt(modifiedInput.encode(), key, iv)
    return ciphertext
    
def modify(cipher):
    
    # Perform byte-level manipulation to inject ";admin=true;"
    cipher = bytearray(cipher)
    cipher[4] ^= 24  # XOR operation to change the character from '#' to ';'
    cipher[10] ^= 99  # XOR operation to change the character from '^' to '='
    cipher[15] ^= 24  # XOR operation to change the character from '#' to ';'
    return bytes(cipher)
    
def verify(encryptedInput):
    #print("encrypted input: ", encryptedInput, "\n------------------")  # Print the encrypted input directly
    
    modified = modify(encryptedInput)
    print("modified input: ", modified)
    print("\n")

    decrypted = decrypt(modified)

    print("Decrypted: ", decrypted)
    print("\n")

    if b";admin=true;" in decrypted:
        return True
    return False

def main():
    encrypted = submit()
    print("original: ", encrypted)

    print("verification:", verify(encrypted))


if __name__=="__main__":
    main()