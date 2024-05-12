##
# cbc.py
# A simple 3-bit CFB block cipher with ANSI X.923 like padding
#
# Ashen Gunaratne
# mail@ashenm.dev
#
##

import re
from argparse import ArgumentParser
from textwrap import wrap
from week2.bitwise import generate_nonce, xor
from week2.cookbooks import COOKBOOKS
from week2.ecb2 import pad, strip

BLOCK_SIZE = 3


def encrypt(key, iv, plaintext):
    cookbook = COOKBOOKS[key]
    nonce = iv
    results = []

    for block in wrap(pad(plaintext, BLOCK_SIZE), BLOCK_SIZE):
        interim = cookbook[nonce]
        enc = nonce = xor(interim, block).rjust(BLOCK_SIZE, "0")
        results.append(enc)

    return "".join(results)


def decrypt(key, iv, ciphertext):
    cookbook = COOKBOOKS[key]
    nonce = iv
    results = []

    for block in wrap(ciphertext, BLOCK_SIZE):
        interim = cookbook[nonce]
        dnc, nonce = xor(interim, block).rjust(BLOCK_SIZE, "0"), block
        results.append(dnc)

    return strip("".join(results), BLOCK_SIZE)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--iv", action="store", default=generate_nonce(BLOCK_SIZE))
    parser.add_argument("key", action="store", choices=COOKBOOKS.keys())
    parser.add_argument("plaintext", action="store")
    args = vars(parser.parse_args())

    key = args["key"]
    iv = args["iv"]
    plaintext = args["plaintext"]

    if re.findall(r"[^01]", plaintext):
        raise ValueError("input plaintext in non-binary form")

    if not re.match(rf"^[01]{{{BLOCK_SIZE}}}$", iv):
        raise ValueError("IV in non-binary form or non-compliant block size")

    encryption = encrypt(key=key, iv=iv, plaintext=plaintext)
    decryption = decrypt(key=key, iv=iv, ciphertext=encryption)

    print(f"{plaintext} -> {encryption} -> {decryption}")
