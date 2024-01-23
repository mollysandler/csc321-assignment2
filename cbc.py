from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def generate_key():
    return get_random_bytes(16)  # 16 bytes for AES-128

def cbc_encrypt(plaintext, key, iv):
    cipher = AES.new(key, AES.MODE_ECB)
    blocks = [plaintext[i:i+AES.block_size] for i in range(0, len(plaintext), AES.block_size)]
    ciphertext = b""
    previous_block = iv

    for block in blocks:
        xored_block = bytes([a ^ b for a, b in zip(block, previous_block)])
        encrypted_block = cipher.encrypt(xored_block)
        ciphertext += encrypted_block
        previous_block = encrypted_block

    return ciphertext

def main():
    ofile = open("./mustang.bmp", "rb")
    cp_cbc = open("cbc_encrypted.bmp", "wb")  # Open in binary write mode

    # Read the entire file content
    original_text = ofile.read()

    # Separate header and data
    original_header = original_text[:54]
    data = original_text[54:]

    # Padding the data
    padded_data = pad(data, AES.block_size)

    # Generate key and IV
    key = generate_key()
    iv = get_random_bytes(AES.block_size)

    # Encryption using CBC mode
    encrypted_cbc = cbc_encrypt(padded_data, key, iv)
    cp_cbc.write(original_header + encrypted_cbc)

    # Close the files
    ofile.close()
    cp_cbc.close()

if __name__ == "__main__":
    main()
