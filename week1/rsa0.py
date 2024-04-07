def encrypt(message, public_key):
    e, n = public_key
    return pow(message, e, n)


def decrypt(ciphertext, private_key):
    d, n = private_key
    return pow(ciphertext, d, n)


public_key = (13, 85)
private_key = (5, 85)
plaintext = 42

ciphertext = encrypt(plaintext, public_key)
decrypted_text = decrypt(ciphertext, private_key)

print("Public key:", public_key)
print("Private key:", private_key)
print("Plaintext:", plaintext)
print("Ciphertext:", ciphertext)
print("Decrypted text:", decrypted_text)
