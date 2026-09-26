import random

from gmpy2 import iroot, get_context, invert, powmod

get_context().precision = 8192

with open("message.txt", "r") as f:
    content = f.read()

    n, e, c = [int(line.split(" = ")[1]) for line in content.splitlines()]

p, q, r, s = [
    9671406556917033397931773,
    9671406556917033398314601,
    9671406556917033398439721,
    9671406556917033398454847,
]
assert p * q * r * s == n


phi = (p - 1) * (q - 1) * (r - 1) * (s - 1)
d = invert(e, phi)
assert (d * e) % phi == 1

m = powmod(c, d, n)

print(p, q, n, d, e)
assert powmod(m, e, n) == c

m_h = hex(m)[2:]
if len(m_h) % 2 == 1:
    m_h = "0" + m_h
m_b = bytes.fromhex(m_h)
print(m_b)
