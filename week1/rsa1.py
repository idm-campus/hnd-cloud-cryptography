def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1


def generate_keypair(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 65537  # Common Fermat prime choice for public exponent
    if gcd(phi, e) != 1:
        raise ValueError("e is not coprime with phi(n)")
    d = mod_inverse(e, phi)
    return ((e, n), (d, n))


def encrypt(message, public_key):
    e, n = public_key
    return pow(message, e, n)


def decrypt(ciphertext, private_key):
    d, n = private_key
    return pow(ciphertext, d, n)


p = 61  # Prime number
q = 53  # Prime number
plaintext = 42

public_key, private_key = generate_keypair(p, q)
ciphertext = encrypt(plaintext, public_key)
decrypted_text = decrypt(ciphertext, private_key)

print("Public key:", public_key)
print("Private key:", private_key)
print("Plaintext:", plaintext)
print("Ciphertext:", ciphertext)
print("Decrypted text:", decrypted_text)
