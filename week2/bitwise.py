##
# bitwise.py
#
# Ashen Gunaratne
# mail@ashenm.dev
#
##

from secrets import randbits


def xor(a, b):
    return "{:b}".format(int(a, 2) ^ int(b, 2))


def generate_nonce(bits):
    return "".join([str(randbits(1)) for _i in range(bits)])
