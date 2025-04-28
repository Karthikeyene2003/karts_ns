Python RSA Implementation:
This project is a simple implementation of RSA encryption and decryption in Python, built as a part of the CS1702 (Network Security) coursework in the 6th Semester. The aim is to break down the core mechanics of RSA without hiding behind bulky libraries — making the cryptographic math transparent and easy to follow.

Aim:
The primary goal was to implement the RSA in Python, to gain a practical understanding of key generation, encryption and decryption.

Implementation Overview:

Key Generation:

Randomly generate two large prime numbers (p and q).

Compute the modulus n = p × q and Euler’s totient ϕ(n) = (p-1)(q-1).

Select a public exponent e such that 1 < e < ϕ(n) and gcd(e, ϕ(n)) = 1.

Calculate the private exponent d, the modular inverse of e mod ϕ(n).

Encryption:

Each character of the plaintext is converted to its ASCII value.

Encryption is performed using:
cipher = (messageᵉ) mod n

Decryption:

Each element of the ciphertext is decrypted using:
message = (cipherᵈ) mod n

ASCII values are then converted back to characters.

Key Components

generate_prime(bits): Generates a prime number of specified bit size using the sympy library.

gcd(a, b): Calculates the Greatest Common Divisor using the Euclidean algorithm.

mod_inverse(e, phi): Finds the modular inverse using the Extended Euclidean Algorithm.

generate_keys(bits): Produces a valid RSA public-private key pair.

encrypt(plaintext, public_key): Encrypts a string into a list of integers.

decrypt(ciphertext, private_key): Decrypts a list of integers back into a readable string.

Results:

The program successfully generates public and private keys for a user-defined key length (512, 1024, or 2048 bits), encrypts a message, and decrypts it back to its original form.
Both encryption and decryption are demonstrated on user input, verifying the correctness of the implementation.
