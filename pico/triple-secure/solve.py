from gmpy2 import iroot, get_context, invert

get_context().precision = 8192

with open("public-key.txt", "r") as f:
    content = f.read()

    n1, n2, n3, e, c = [int(line.split(": ")[1]) for line in content.splitlines()]

# Since n1, n2, n3 are defined as following:
#   n1 = p * q
#   n2 = p * r
#   n3 = q * r
p, _ = iroot((n1 * n2) // n3, 2)
q, _ = iroot((n1 * n3) // n2, 2)
r, _ = iroot((n2 * n3) // n1, 2)

assert p * q == n1
assert p * r == n2
assert q * r == n3


def decrypt_rsa(p: int, q: int, e: int, c: int):
    n = p * q
    phi = (p - 1) * (q - 1)
    d = invert(e, phi)
    return pow(c, d, n)


m = c
m = decrypt_rsa(q, r, e, m)
m = decrypt_rsa(p, r, e, m)
m = decrypt_rsa(p, q, e, m)

m_h = hex(m)[2:]
if len(m_h) % 2 == 1:
    m_h = "0" + m_h

m_b = bytes.fromhex(m_h)
print(m_b)
