from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes

def generate_key():
   return get_random_bytes(16)  # 16 bytes bc 128 

def pkcs7_pad(data, block_size):
   padding_value = block_size - len(data) % block_size
   padded_data = data + bytes([padding_value] * padding_value)
   return padded_data


def ecb_encrypt(plaintext, key):
   cipher = AES.new(key, AES.MODE_ECB)
   padded_plaintext = pad(plaintext, AES.block_size)
   ciphertext = cipher.encrypt(padded_plaintext)
   return ciphertext

def main():
   ofile = open("./cp-logo.bmp", "rb")
   cp = open("help-cp.bmp", "wb")  # Open in binary write mode

   originalText = ofile.read() #read file

   originalHeader = originalText[:54] #54 byte header
   data = originalText[54:]

   padded_data = pkcs7_pad(data, AES.block_size)

   key = generate_key() #get key

   encrypted_data = ecb_encrypt(padded_data, key) #encrypt based on key
   cp.write(originalHeader + encrypted_data) #write everything to file
   
   ofile.close()
   cp.close()


if __name__ == "__main__":
    main()