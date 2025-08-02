for i in range(8):
    a = i & 4
    b = i & 2
    c = i & 1

    a = "2025"
    b = "cat" if b else "CAT"
    c = "network" if c else "NETWORK"

    str = f"{a} {b} {c}"
    print(f"{str} flag{{{md5sum(str.encode()).hex()}}}")
