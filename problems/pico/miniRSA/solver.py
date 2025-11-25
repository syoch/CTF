from gmpy2 import iroot, get_context, invert

get_context().precision = 8192

with open("ciphertext", "r") as f:
    content = f.read()

    n, e, c = [int(line.split(": ")[1]) for line in content.splitlines()]

m, _ = iroot(c, e)
m_h = hex(m)[2:]
m_b = bytes.fromhex(m_h)
print(m_b)
