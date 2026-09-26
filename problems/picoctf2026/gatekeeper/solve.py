from typing import Callable

from pwn import *

context.arch = "i386"
context.terminal = ["tmux", "splitw", "-h"]
context.log_level = "debug"

elf = ELF("./gatekeeper")


def solve(fact: Callable[[], tube]) -> None:
    p = fact()
    p.recvuntil(b"Enter a numeric code (must be > 999 ): ")
    p.sendline(b"fff")
    p.recvuntil(b"Access granted: ")
    result = p.recvline().strip()
    p.close()

    result = result.replace(b"ftc_oc_ip", b"")
    print("".join(chr(x) for x in reversed(result)))


def main() -> None:
    # gdb.attach(p, gdbscript="display /4i $pc\ncontinue\n")
    # p = lambda: process(["./game"])
    p = lambda: remote("green-hill.picoctf.net", 53653)
    solve(p)


if __name__ == "__main__":
    main()
