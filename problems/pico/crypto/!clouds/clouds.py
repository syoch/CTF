ROUNDS = 5
BLOCK_LEN = 8


def load_key():
    key_data = open("./key", "rb").read()

    key_blocks = [
        key_data[i : i + BLOCK_LEN] for i in range(0, len(key_data) - 1, BLOCK_LEN)
    ]
    assert len(key_blocks) == ROUNDS, (
        f"Got {len(key_blocks)} key blocks. Expected: {ROUNDS}"
    )

    print(f"D: Loaded {len(key_blocks)} key blocks.")
    for i, block in enumerate(key_blocks):
        print(f"D: Key {i}: {block.hex()}")

    keys = [int(block.hex(), 16) for block in key_blocks]

    return keys


keys = load_key()


def pad(p: bytes):
    """
    Adds multiple b'0' to BLOCK_LEN boundary
    """
    if len(p) % BLOCK_LEN != 0:
        return p + b"\0" * (BLOCK_LEN - (len(p) % BLOCK_LEN))
    else:
        return p


def bit_reverse(data_in: int):
    result = bin(data_in).lstrip("0b").rstrip("L").rjust(BLOCK_LEN * 8, "0")
    return int(result[::-1], 2)


def encrypt_block(block: int):
    global keys
    # print(f"D: Encrypting block: {block:016x}")
    # assert (block.bit_length() / 8 * ROUNDS) == len(keys) * BLOCK_LEN

    result = block
    for key in keys:
        result_next = (bit_reverse(result ^ key) * (key | 1)) % (1 << 64)
        # print(f"D: Result: {result:016x} <-- {key:016x} ==> {result_next:016x}")
        result = result_next
    return result


def encrypt(msg: bytes):
    plain = pad(msg)
    plain_blocks = [
        plain[i : i + 1 * BLOCK_LEN] for i in range(0, len(plain), BLOCK_LEN)
    ]

    result = "".join(
        hex(encrypt_block(int(block.hex(), 16)))
        .lstrip("0x")
        .rstrip("L")
        .rjust(2 * BLOCK_LEN, "0")
        for block in plain_blocks
    )
    return result


def test():
    base_b = 0x00000000_00000000
    b = base_b
    e1 = encrypt_block(b)
    print(
        f"Input bit  {hex(b)[2:].zfill(16)} --> {bin(e1)[2:].zfill(64).replace('0', ' ').replace('1', '#')}"
    )
    b = base_b ^ 1
    e2 = encrypt_block(b)
    print(
        f"Input bit  {hex(b)[2:].zfill(16)} --> {bin(e2)[2:].zfill(64).replace('0', ' ').replace('1', '#')}"
    )
    b = base_b ^ 2
    e1 = encrypt_block(b)
    print(
        f"Input bit  {hex(b)[2:].zfill(16)} --> {bin(e1)[2:].zfill(64).replace('0', ' ').replace('1', '#')}"
    )
    b = base_b ^ 4
    e2 = encrypt_block(b)
    print(
        f"Input bit  {hex(b)[2:].zfill(16)} --> {bin(e2)[2:].zfill(64).replace('0', ' ').replace('1', '#')}"
    )


def enc_pg():
    while True:
        msg = bytes.fromhex(input("> "))
        e_msg = encrypt(msg)
        print(e_msg)


if __name__ == "__main__":
    test()
    # enc_pg()
