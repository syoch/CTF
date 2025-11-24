import gmpy2

gmpy2.get_context().precision = 8192

E_MSGS = "encrypted-messages.txt"

with open(E_MSGS, "r") as f:
    content = f.read().strip().split("\n\n")

# (n,e,c)[]
params = [
    (
        int(block.split("\n")[0].split(": ")[1]),
        int(block.split("\n")[1].split(": ")[1]),
        int(block.split("\n")[2].split(": ")[1]),
    )
    for block in content
]

for n, e, c in params:
    m = gmpy2.root(c, e)
    if m**e == c:
        long = int(gmpy2.iroot(c, e)[0])
        flag = long.to_bytes((long.bit_length() + 7) // 8, "big").decode()
        print(f"Found flag: {flag}")
