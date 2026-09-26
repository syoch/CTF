from Crypto.Util.number import long_to_bytes
from sage.all import *


def polygcd(a, b):
    if b == 0:
        return a.monic()
    else:
        return polygcd(b, a % b)


with open("output.txt", "r") as f:
    content = f.read().splitlines()

    c1 = int(content[0])
    c2 = int(content[1])
    diff = int(content[2])
    N = int(content[3])

PR = PolynomialRing(Zmod(N), "x")
x = PR.gen()

e = 0x11
f = x**e - c1
g = (x - diff) ** e - c2

d = polygcd(f, g)
print(d)
m1 = int(d.coefficients()[0])
m1 = N - m1
print(long_to_bytes(m1).decode())

m2 = m1 - diff
print(long_to_bytes(m2).decode())
