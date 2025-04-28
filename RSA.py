import random
import sympy

def generate_prime(bits):
    """Generate a random prime number of the given bit length."""
    return sympy.randprime(2**(bits-1), 2**bits)

def gcd(a, b):
    """Compute the greatest common divisor of a and b."""
    while b:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    """Compute modular inverse of e modulo phi using Extended Euclidean Algorithm."""
    a, m = e, phi
    m0, y, x = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        y, x = x - q * y, y
    return x + m0 if x < 0 else x

def generate_keys(bits):
    """Generate RSA public and private keys with the specified bit length."""
    p, q = generate_prime(bits), generate_prime(bits)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = random.randrange(2, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(2, phi)
    d = mod_inverse(e, phi)
    return ((e, n), (d, n))

def encrypt(plaintext, public_key):
    """Encrypt a plaintext message using the public key."""
    e, n = public_key
    return [pow(ord(char), e, n) for char in plaintext]

def decrypt(ciphertext, private_key):
    """Decrypt a ciphertext message using the private key."""
    d, n = private_key
    return ''.join(chr(pow(char, d, n)) for char in ciphertext)

# User input for key length
bits = int(input("Enter the key length (e.g., 512, 1024, 2048): "))
#print("\nGenerating RSA keys...")
public_key, private_key = generate_keys(bits)

# Display generated keys
print("\nPublic Key (e, n):", public_key)
print("Private Key (d, n):", private_key)

# Message encryption and decryption
message = input("\nEnter the message to encrypt: ")
ciphertext = encrypt(message, public_key)
decrypted_message = decrypt(ciphertext, private_key)

print("\nEncrypted Message:", ciphertext)
print("Decrypted Message:", decrypted_message)
