##
# ecb1.py
# A simple 3-bit ECB block cipher with zero-padding
#
# Ashen Gunaratne
# mail@ashenm.dev
#
##

import re
from argparse import ArgumentParser
from textwrap import wrap
from week2.cookbooks import COOKBOOKS

BLOCK_SIZE = 3


def swap(collection):
    return {v: k for k, v in collection.items()}


def encrypt(key, plaintext):
    cookbook = COOKBOOKS[key]
    results = []

    for chunk in wrap(plaintext, BLOCK_SIZE):
        block = chunk.ljust(BLOCK_SIZE, "0")
        results.append(cookbook[block])

    return "".join(results)


def decrypt(key, ciphertext):
    cookbook = swap(COOKBOOKS[key])
    results = []

    for block in wrap(ciphertext, BLOCK_SIZE):
        chunk = cookbook[block].rstrip("0")
        results.append(chunk)

    return "".join(results)


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
