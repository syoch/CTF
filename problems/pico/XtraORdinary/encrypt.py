#!/usr/bin/env python3

from random import randint

random_strs = [
    b"my encryption method",
    b"is absolutely impenetrable",
    b"and you will never",
    b"ever",
    b"ever",
    b"ever",
    b"ever",
    b"ever",
    b"ever",
    b"break it",
]

with open("rt/flag.txt", "rb") as f:
    flag = f.read()

with open("rt/secret-key.txt", "rb") as f:
    key = f.read()


def encrypt(msg, key):
    ctxt = b""
    for i in range(len(msg)):
        a = msg[i]
        b = key[i % len(key)]
        ctxt += bytes([a ^ b])
    return ctxt


ctxt = flag
print(f"ctxt = {ctxt.hex()}")

ctxt = encrypt(flag, key)
print(f"ctxt = {ctxt.hex()} (key: {key})")

for random_str in random_strs:
    ctxt_prev = ctxt
    for i in range(randint(0, pow(2, 8))):
        for j in range(randint(0, pow(2, 6))):
            for k in range(randint(0, pow(2, 4))):
                for l in range(randint(0, pow(2, 2))):
                    for m in range(randint(0, pow(2, 0))):
                        ctxt = encrypt(ctxt, random_str)

    print(f"ctxt = {ctxt.hex()} (str: {random_str})")

with open("rt/output.txt", "w") as f:
    f.write(ctxt.hex())
