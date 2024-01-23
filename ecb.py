from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def generate_key():
   return get_random_bytes(16)  # 16 bytes bc AES-128 

def pkcs7_pad(data, block_size): #writing my own padding function
   padding_value = block_size - len(data) % block_size
   padded_data = data + bytes([padding_value] * padding_value)
   return padded_data

def ecb_encrypt(plaintext, key):
   cipher = AES.new(key, AES.MODE_ECB) #need to pass it through something
   padded_plaintext = pkcs7_pad(plaintext, AES.block_size) #block size should be 128, so we pad to fit that
   ciphertext = cipher.encrypt(padded_plaintext) #encrypt the padded text
   return ciphertext

def main():
   ofile = open("./cp-logo.bmp", "rb") #run ecb on the cp logo 
   cp = open("logo-ecb_encrypt.bmp", "wb") #binary read and write mode

   og = ofile.read()

   originalHeader = og[:54] #54 byte header as per specs
   data = og[54:]

   padded_data = pkcs7_pad(data, AES.block_size) #pad the data

   key = generate_key() #get a key

   encrypted_data = ecb_encrypt(padded_data, key) #encrypt based on key
   cp.write(originalHeader + encrypted_data) #write everything to the file
   
   ofile.close() #close the files
   cp.close()


if __name__ == "__main__":
    main()