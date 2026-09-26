from Crypto.Random import get_random_bytes


def steplfsr(lfsr: int):
    b7 = (lfsr >> 7) & 1
    b5 = (lfsr >> 5) & 1
    b4 = (lfsr >> 4) & 1
    b3 = (lfsr >> 3) & 1

    feedback = b7 ^ b5 ^ b4 ^ b3
    lfsr = (feedback << 7) | (lfsr >> 1)
    return lfsr


def encrypt_lfsr(pt_bytes: bytes, lfsr: int):
    output = bytearray()
    for p in pt_bytes:
        lfsr = steplfsr(lfsr)
        output.append(p ^ lfsr)
    return bytes(output)


with open("output.txt", "r") as f:
    ct = bytes.fromhex(f.read())

for i in range(256):
    m = encrypt_lfsr(ct, i)
    if m.startswith(b"picoCTF{"):
        print(m)
        break
