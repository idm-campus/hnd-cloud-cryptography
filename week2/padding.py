##
# padding.py
# A simple ANSI X.923-like padding scheme implementation
#
# Ashen Gunaratne
# mail@ashenm.dev
#
##


def pad(bits, block_size):
    padding_length = block_size - (len(bits) % block_size)
    padding_marker = f"{padding_length:0{block_size}b}"
    return bits + "0" * padding_length + padding_marker


def strip(bits, block_size):
    padding_marker = int(bits[-block_size:], 2)
    padding_start_index = -1 * (block_size + padding_marker)
    return bits[:padding_start_index]
