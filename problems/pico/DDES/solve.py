from Crypto.Cipher import DES


def pad(msg):
    block_len = 8
    over = len(msg) % block_len
    pad = block_len - over
    return (msg + " " * pad).encode()


def get_key_candidates():
    for i in range(0, 10**6):
        yield pad(str(i).zfill(6))


def des_enc(m: bytes, k: bytes) -> bytes:
    des = DES.new(k, DES.MODE_ECB)
    return des.encrypt(m)


def des_dec(m: bytes, k: bytes) -> bytes:
    des = DES.new(k, DES.MODE_ECB)
    return des.decrypt(m)


def calc_key12(m1: bytes, c1: bytes):
    print("Generating Key1 table...")
    key1_lookup_table = {des_enc(m1, key): key for key in get_key_candidates()}

    print("Generating Key2 table...")
    key2_lookup_table = {des_dec(c1, key): key for key in get_key_candidates()}

    print("Generating intersecting...")
    key_candidates = key1_lookup_table.keys() & key2_lookup_table.keys()

    print("Key1, Key2 candidates:")
    candidates = []
    for middle in key_candidates:
        key1 = key1_lookup_table[middle]
        key2 = key2_lookup_table[middle]

        candidates.append((key1, key2))
        print(f"- {key1} {key2}")

    if candidates:
        return candidates[0]

    raise


m1 = bytes.fromhex("0123012301230123")
c1 = bytes.fromhex("d0d5da053d0d393f")
key1, key2 = calc_key12(m1, c1)
key1 = b"137377  "
key2 = b"195159  "
print(f"Using {key1} {key2} to solve")

cipher = bytes.fromhex(
    "6d35867d57951768e58647e7aadd717bb2c9b7864e16c2f9197f858fa9e0da43f7881c7a8c9a847c"
)
des2 = DES.new(key2, DES.MODE_ECB)
des1 = DES.new(key1, DES.MODE_ECB)
middle = des2.decrypt(cipher)
message = des1.decrypt(middle).rstrip().decode()
print("The flag is:")
print(f"  - {message}")
