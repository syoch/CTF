import os
from pwn import process, remote, info, warn, context
from sympy.ntheory.modular import crt
import gmpy2

context.log_level = "debug"

KEY_LEN = 50000


def on_remote():
    return remote("mercury.picoctf.net", 28517)


def get_nec(p):
    p.recvuntil(b"Good Luck!\n\n\n")
    n = int(p.recvline().strip().decode().split(": ")[1])
    e = int(p.recvline().strip().decode().split(": ")[1])
    c = int(p.recvline().strip().decode().split(": ")[1])

    return n, e, c


def main():
    p = on_remote()
    n, e, c = get_nec(p)

    p.recvuntil(b"Give me ciphertext to decrypt: ")
    p.sendline(str(c + n).encode())
    p.recvuntil(b"Here you go: ")
    m = int(p.recvline().strip().decode())

    flag = m.to_bytes((m.bit_length() + 7) // 8, "big")
    info(f"Flag: {flag.decode()}")


if __name__ == "__main__":
    main()
