with open("message.txt", "r") as f:
    lines = f.read().splitlines()
    g = int(lines[0].split(" = ")[1])
    p = int(lines[1].split(" = ")[1])
    A = int(lines[2].split(" = ")[1])
    b = int(lines[3].split(" = ")[1])
    enc = bytes.fromhex(lines[4].split(" = ")[1])

shared = pow(A, b, p)

flag = bytes([x ^ (shared % 256) for x in enc])
print(flag.decode())
