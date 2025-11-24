import hashlib
from math import gcd
import re
import gmpy2
from pwn import process, remote, tube, info, warn, error, context

gmpy2.get_context().precision = 8192
context.log_level = "debug"


def local_pipe():
    return process("python3 not_my_fault.py", shell=True)


def remote_pipe():
    return remote("mercury.picoctf.net", 27379)


def extract_val1_val2(line1: bytes) -> tuple[bytes, bytes]:
    print(line1)
    reg = rb'Enter a string that starts with "([0-9]{5})"'
    match = re.match(reg, line1)
    if not match:
        raise RuntimeError("Regex not match")
    val1 = match[1]

    val2 = line1.rstrip()[-6:]

    return val1, val2


def find_md5_sum(val1: str, val2: str):
    x = 0
    while True:
        x += 1

        hash_input = val1 + str(x)

        digest = hashlib.md5(hash_input.encode()).hexdigest()
        if digest.endswith(val2):
            return hash_input.encode(), digest


def solve_rsa(n, e):
    m = 1000000000000

    c = pow(m, e, n)
    p = -1
    for dp in range(2**20):
        m2 = pow(c, dp, n)
        gcd_mm2 = gcd(m - m2, n)
        if gcd_mm2 == 1:
            continue

        p = gcd_mm2
        break

    if p == -1:
        raise RuntimeError("p not found")

    q = n // p
    return p + q


def solve(p: tube):
    info("#1")
    line1 = p.recvline()
    val1, val2 = extract_val1_val2(line1)
    info("Finding MD5 Sum with following constraits:")
    info(f"  - Startswith {val1}")
    info(f"  - Endswith {val2}")
    data, data_hash = find_md5_sum(val1.decode(), val2.decode())
    info(f"Found acceptable hash: {data} --> {data_hash}")
    p.sendline(data)

    info("#2")
    p.recvuntil(b"Public Modulus :  ")
    n = int(p.recvline().strip().decode(), 10)
    p.recvuntil(b"Clue :  ")
    e = int(p.recvline().strip().decode(), 10)
    info("RSA Parameter received. Solving problem...")
    p_q = solve_rsa(n, e)
    info(f"p + q = {p_q}")
    p.sendline(str(p_q).encode())

    p.interactive()


if __name__ == "__main__":
    solve(remote_pipe())
