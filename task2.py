from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# Global variables for key and IV
key = get_random_bytes(16)
iv = get_random_bytes(16)

def pkcs7_pad(data, block_size): #writing my own padding function
   padding_value = block_size - len(data) % block_size
   padded_data = data + bytes([padding_value] * padding_value)
   return padded_data

def pkcs7_unpad(data): #writing my own unpadding function?
    padding = data[-1]
    return data[:-padding]

def cbc_encrypt(plaintext, key, iv): 
    cipher = AES.new(key, AES.MODE_CBC, iv) 
    padded_plaintext = pkcs7_pad(plaintext, AES.block_size)  #padding
    ciphertext = cipher.encrypt(padded_plaintext)
    return ciphertext

def cbc_decrypt(encryptedParams):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    paddedParams = cipher.decrypt(encryptedParams) #decrypt it using cbc
    return pkcs7_unpad(paddedParams)


def submit():
    userInput = "#admin^true#"
    modifiedInput = "userid=456;userdata=" + userInput + ";session-id=31337"
    print("Modified Input: ", modifiedInput)
    
    ciphertext = cbc_encrypt(modifiedInput.encode(), key, iv)
    return ciphertext
    
def verify(encryptedInput):
    #print(encryptedInput, "\n------------------")  # Print the encrypted input directly

    # Perform byte-level manipulation to inject ";admin=true;"
    encryptedInput = bytearray(encryptedInput)
    encryptedInput[4] ^= 24  # XOR operation to change the character from '#' to ';'
    encryptedInput[10] ^= 99  # XOR operation to change the character from '^' to '='
    encryptedInput[15] ^= 24  # XOR operation to change the character from '#' to ';'

    #print(encryptedInput)

    decrypted = cbc_decrypt(encryptedInput)

    #print(decrypted)

    if b";admin=true;" in decrypted:
        return True
    return False



def main():
    encrypted = submit()
    print("encrypted input: " , encrypted)
    print("you are an admin? ", verify(encrypted))


if __name__=="__main__":
    main()
