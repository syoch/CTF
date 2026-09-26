from collections import Counter


with open("whitepages.txt", "rb") as f:
    bits = []
    while byte := f.read(1):
        if byte == b"\x20":  # space character
            bits.append("1")
        elif byte == b"\xe2":
            assert f.read(2) == b"\x80\x83"
            bits.append("0")
        else:
            raise ValueError("Unexpected byte encountered: {}".format(byte))

    parts = ["".join(bits[i : i + 8]) for i in range(0, len(bits), 8)]
    message = "".join([chr(int(part, 2)) for part in parts])
    print(message)
