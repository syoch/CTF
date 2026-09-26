from os import system
from typing import Callable

from pwn import *

context.arch = "i386"
context.terminal = ["tmux", "splitw", "-h"]
context.log_level = "debug"

elf = ELF("./hiddencipher")


def solve(fact: Callable[[], tube]) -> None:
    # Receive the encrypted flag
    p = fact()
    p.recvuntil(b"Here your encrypted flag:\n")
    encrypted_flag_hex = p.recvline().strip()
    p.close()

    # Generate binary file as flag.txt
    encrypted_flag = bytes.fromhex(encrypted_flag_hex.decode())
    with open("flag.txt", "wb") as f:
        f.write(encrypted_flag)

    p = process(["./hiddencipher"])
    p.recvuntil(b"Here your encrypted flag:\n")
    decrypted_flag_hex = p.recvline().strip()
    p.close()

    # Show the decrypted flag
    decrypted_flag = bytes.fromhex(decrypted_flag_hex.decode())
    print("Decrypted flag:", decrypted_flag.decode())


def main() -> None:
    # gdb.attach(p, gdbscript="display /4i $pc\ncontinue\n")
    # p = lambda: process(["./game"])
    p = lambda: remote("candy-mountain.picoctf.net", 49179)
    solve(p)


if __name__ == "__main__":
    main()
