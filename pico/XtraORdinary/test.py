#!/usr/bin/env python3

from random import randint


with open("rt/output.txt", "r") as f:
    data = bytes.fromhex(f.read())


def trans_same_length(msg: bytes, key: bytes):
    assert len(msg) == len(key)

    return b"".join(bytes([a ^ b]) for (a, b) in zip(msg, key))


def trans(
    msg: bytes, key: bytes, length: int | None = None, key_length: int | None = None
):
    if length is None:
        length = len(msg)
    if key_length is None:
        key_length = len(key)

    return b"".join(bytes([msg[i] ^ key[i % key_length]]) for i in range(length))


BYTES_A = b"ABCDEFG"
BYTES_B = b"AEOKPKN"

a = trans(BYTES_A, BYTES_B)
a = trans(a, BYTES_B)
assert a == BYTES_A, f"{BYTES_A} != {a}"

random_strs = [
    b"my encryption method",
    b"is absolutely impenetrable",
    b"and you will never",
    b"ever",
    b"break it",
]


def find_xor_pattern():
    for i in range(0, 2 ** len(random_strs)):
        mask = data
        use_map = []
        for str_index, random_str in enumerate(random_strs):
            want_to_take = (i >> str_index) & 1
            use_map.append(want_to_take)

            if want_to_take:
                mask = trans(mask, random_str)

        m = mask

        KNOWN_HEADER = b"picoCTF{"
        estimated_key = trans_same_length(m[0 : len(KNOWN_HEADER)], KNOWN_HEADER)

        print(use_map, estimated_key)


def solve():
    c = data
    for str in [
        b"and you will never",
        b"ever",
        b"break it",
    ]:
        c = trans(c, str)

    c = trans(c, b"Africa!")

    print(c)


solve()
