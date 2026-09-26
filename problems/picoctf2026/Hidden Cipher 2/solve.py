from os import system
from typing import Callable

from pwn import *

context.arch = "i386"
context.terminal = ["tmux", "splitw", "-h"]
context.log_level = "debug"

elf = ELF("./hiddencipher2")


def solve(fact: Callable[[], tube]) -> None:
    p = fact()
    p.recvuntil(b"What is")
    question = p.recvuntil("? ").strip()

    question = question.replace(b"?", b"")
    answer = eval(question.decode())
    p.sendline(str(answer).encode())

    p.recvuntil(b"Encoded flag values:\n")
    values = p.recvline()
    values = values.strip().split(b", ")
    print(values)
    values = [int(x.decode()) for x in values]
    p.close()

    values = [x // answer for x in values]
    flag = "".join(chr(x) for x in values)
    print("Decrypted flag:", flag)


def main() -> None:
    # gdb.attach(p, gdbscript="display /4i $pc\ncontinue\n")
    # p = lambda: process(["./game"])
    p = lambda: remote("crystal-peak.picoctf.net", 60202)
    solve(p)


if __name__ == "__main__":
    main()
