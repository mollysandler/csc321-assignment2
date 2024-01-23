from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def generate_key():
    return get_random_bytes(16)  # 16 bytes for AES-128

def pkcs7_pad(data, block_size): #writing my own padding function
   padding_value = block_size - len(data) % block_size
   padded_data = data + bytes([padding_value] * padding_value)
   return padded_data

def cbc_encrypt(plaintext, key, iv): 
    cipher = AES.new(key, AES.MODE_ECB) 
    blocks = [plaintext[i:i+AES.block_size] for i in range(0, len(plaintext), AES.block_size)]
    ciphertext = b"" 
    previous_block = iv

    for block in blocks:
        xored_block = bytes([a ^ b for a, b in zip(block, previous_block)]) #exclusive or function 
        encrypted_block = cipher.encrypt(xored_block)
        ciphertext += encrypted_block #adding the blocks 
        previous_block = encrypted_block

    return ciphertext

def main():
    ofile = open("./mustang.bmp", "rb") #mustang getting edited for cbc
    cp_cbc = open("mustang_cbc.bmp", "wb") 

    # Read the entire file content
    og = ofile.read()

    original_header = og[:54] #54 byte header as per specs
    data = og[54:]

    padded_data = pkcs7_pad(data, AES.block_size) #pad the data

    key = generate_key() #get the key
    iv = get_random_bytes(AES.block_size) #should be 128 

    encrypted_cbc = cbc_encrypt(padded_data, key, iv) #encrypt based on key
    cp_cbc.write(original_header + encrypted_cbc) #write everything to the file
    
    ofile.close() #close files
    cp_cbc.close()

if __name__ == "__main__":
    main()
