##
# ecb1.py
# A simple 3-bit ECB block cipher with ANSI X.923 like padding
#
# Ashen Gunaratne
# mail@ashenm.dev
#
##

import re
from argparse import ArgumentParser
from textwrap import wrap
from week2.cookbooks import COOKBOOKS
from week2.padding import pad, strip

BLOCK_SIZE = 3


def swap(collection):
    return {v: k for k, v in collection.items()}


def encrypt(key, plaintext):
    cookbook = COOKBOOKS[key]
    interim = pad(plaintext, BLOCK_SIZE)
    results = []

    for block in wrap(interim, BLOCK_SIZE):
        results.append(cookbook[block])

    return "".join(results)


def decrypt(key, ciphertext):
    cookbook = swap(COOKBOOKS[key])
    results = []

    for block in wrap(ciphertext, BLOCK_SIZE):
        chunk = cookbook[block]
        results.append(chunk)

    interim = "".join(results)
    return strip(interim, BLOCK_SIZE)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("key", action="store", choices=COOKBOOKS.keys())
    parser.add_argument("plaintext", action="store")
    args = vars(parser.parse_args())

    key = args["key"]
    plaintext = args["plaintext"]

    if re.findall(r"[^01]", plaintext):
        raise ValueError("input plaintext in non-binary form")

    encryption = encrypt(key=key, plaintext=plaintext)
    decryption = decrypt(key=key, ciphertext=encryption)

    print(f"{plaintext} -> {encryption} -> {decryption}")
