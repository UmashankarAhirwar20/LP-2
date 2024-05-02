from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def encrypt_data(key, plaintext):
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(plaintext.encode())
    nonce = cipher.nonce
    return ciphertext, tag, nonce

def decrypt_data(key, ciphertext, nonce, tag):
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    try:
        plaintext = cipher.decrypt_and_verify(ciphertext, tag)
        return plaintext.decode()
    except ValueError:
        return "Decryption failed. Data may have been tampered with."

def main():
    key = b'1234455fghdhdfrs' 
    plaintext = "This is experiment 4 AES"
    ciphertext, tag, nonce = encrypt_data(key, plaintext)
    print(f"Ciphertext: {ciphertext}")
    print(f"Tag: {tag}")
    print(f"Nonce: {nonce}")
    decrypted_text = decrypt_data(key, ciphertext, nonce, tag)
    print(f"Decrypted Plaintext: {decrypted_text}")

if __name__ == "__main__":
    main()
