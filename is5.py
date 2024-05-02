import random

# Function to compute the greatest common divisor (gcd) of two numbers
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Function to compute the multiplicative inverse using the extended Euclidean algorithm
def multiplicative_inverse(e, phi):
    original_phi = phi
    x1, x2, y1 = 0, 1, 1
    d = 0
    while e > 0:
        temp_phi, temp1 = phi, phi // e
        phi, e = e, phi - temp1 * e
        x1, x2 = x2 - temp1 * x1, x1
        y1, d = d - temp1 * y1, y1
    if phi == 1:
        return d + original_phi

# Function to generate an RSA keypair
def generate_keypair(p, q):
    if p == q:
        raise ValueError("p and q must be distinct prime numbers.")
    n = p * q
    phi = (p - 1) * (q - 1)
    e = random.randrange(2, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(2, phi)
    d = multiplicative_inverse(e, phi)
    return ((e, n), (d, n))

# Function to encrypt a message using a public key
def encrypt(pk, plaintext):
    key, n = pk
    cipher = [(ord(char) ** key) % n for char in plaintext]
    return cipher

# Function to decrypt a ciphertext using a private key
def decrypt(pk, ciphertext):
    key, n = pk
    plain = [chr((char ** key) % n) for char in ciphertext]
    return ''.join(plain)

# Main function
if __name__ == '__main__':
    # Input validation for prime numbers p and q
    p = int(input("Enter a prime number (p): "))
    q = int(input("Enter another prime number (q): "))
    
    # Generating keypair
    public, private = generate_keypair(p, q)
    print("Public key:", public)
    print("Private key:", private)
    
    # Input validation for message to encrypt
    message = input("Enter a message to encrypt: ")
    
    # Encrypting message
    encrypted_message = encrypt(public, message)
    print("Encrypted message:", ''.join(map(str, encrypted_message)))
    
    # Decrypting message
    decrypted_message = decrypt(private, encrypted_message)
    print("Decrypted message:", decrypted_message)
