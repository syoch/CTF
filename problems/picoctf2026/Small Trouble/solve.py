from gmpy2 import iroot, get_context, invert, powmod
from syoch_ctf.crypto.wieners_attack import wieners_attack

get_context().precision = 8192

with open("message.txt", "r") as f:
    content = f.read()

    n, e, c = [int(line.split(" = ")[1]) for line in content.splitlines()]

for candidate in wieners_attack(e, n, c):
    print(candidate)
