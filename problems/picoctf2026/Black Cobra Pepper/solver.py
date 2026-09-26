from pwn import xor

pt = ""
key = ""


def split(full_key):
    k = full_key
    k1 = ""
    k2 = ""
    k3 = ""
    k4 = ""
    sub_keys = [k1, k2, k3, k4]
    for i in range(len(k)):
        sub_keys[i % 4] = str(sub_keys[i % 4]) + str(k[0])
        k = k[1:]
    return sub_keys


def glue(parts):
    k = ""
    for i in range(32):
        k = str(k) + str(parts[i % 4][0])
        parts[i % 4] = str(parts[i % 4][1:])
    return k


def rot_word(word):
    return str(word[2:]) + str(word[0:2])


def sub_word(word):
    return word


def rcon(word):
    return word


def gen_keys(master_key):
    keys = []
    rounds = 0
    k = master_key

    while rounds < 11:
        keys.append(k)
        sub_keys = split(k)
        sub_keys[-1] = rot_word(sub_keys[-1])
        sub_keys[-1] = sub_word(sub_keys[-1])
        sub_keys[-1] = rcon(sub_keys[-1])
        sub_keys[0] = xor(bytes.fromhex(sub_keys[0]), bytes.fromhex(sub_keys[-1])).hex()
        sub_keys[1] = xor(bytes.fromhex(sub_keys[1]), bytes.fromhex(sub_keys[0])).hex()
        sub_keys[2] = xor(bytes.fromhex(sub_keys[2]), bytes.fromhex(sub_keys[1])).hex()
        sub_keys[3] = xor(bytes.fromhex(sub_keys[3]), bytes.fromhex(sub_keys[2])).hex()
        k = glue(sub_keys)
        rounds += 1

    return keys


def to_matrix(key):
    bytes_list = [int(key[i : i + 2], 16) for i in range(0, 32, 2)]

    array = [[0] * 4 for _ in range(4)]
    for i in range(16):
        row = i % 4
        col = i // 4
        array[row][col] = hex(bytes_list[i])[2:]

    return array


def from_matrix(matrix):
    reconstructed = ""
    for col in range(4):
        for row in range(4):
            reconstructed += matrix[row][col].zfill(2)
    return reconstructed


def sub_bytes(state):
    return state


def shift_rows(state):
    placeholder = state[1][0]
    state[1][0], state[1][1], state[1][2], state[1][3] = (
        state[1][1],
        state[1][2],
        state[1][3],
        state[1][0],
    )
    state[2][0], state[2][1], state[2][2], state[2][3] = (
        state[2][2],
        state[2][3],
        state[2][0],
        state[2][1],
    )
    state[3][0], state[3][1], state[3][2], state[3][3] = (
        state[3][3],
        state[3][0],
        state[3][1],
        state[3][2],
    )
    return state


# adopted and insipred by the code from the wikipedia article Rijndael MixColumns.
def gmul(a, b):
    b = int(b, 16)
    p = 0
    for c in range(8):
        if b & 1:
            p ^= a
        a <<= 1
        if a & 0x100:
            a ^= 0x11B
        b >>= 1
    return p


def mix_columns(s):
    ss = [[0] * 4 for _ in range(4)]

    for c in range(4):
        ss[0][c] = hex(
            gmul(0x02, s[0][c])
            ^ gmul(0x03, s[1][c])
            ^ int(s[2][c], 16)
            ^ int(s[3][c], 16)
        )[2:].zfill(2)
        ss[1][c] = hex(
            int(s[0][c], 16)
            ^ gmul(0x02, s[1][c])
            ^ gmul(0x03, s[2][c])
            ^ int(s[3][c], 16)
        )[2:].zfill(2)
        ss[2][c] = hex(
            int(s[0][c], 16)
            ^ int(s[1][c], 16)
            ^ gmul(0x02, s[2][c])
            ^ gmul(0x03, s[3][c])
        )[2:].zfill(2)
        ss[3][c] = hex(
            gmul(0x03, s[0][c])
            ^ int(s[1][c], 16)
            ^ int(s[2][c], 16)
            ^ gmul(0x02, s[3][c])
        )[2:].zfill(2)

    for i in range(4):
        for j in range(4):
            s[i][j] = ss[i][j]
    return s


def AES(plaintext, key):
    ciphertext = plaintext
    round_keys = gen_keys(key)
    ciphertext = xor(bytes.fromhex(round_keys[0]), bytes.fromhex(ciphertext)).hex()
    for i in range(1, 10):
        ciphertext = to_matrix(ciphertext)
        sub_bytes(ciphertext)
        shift_rows(ciphertext)
        mix_columns(ciphertext)
        ciphertext = from_matrix(ciphertext)
        ciphertext = xor(bytes.fromhex(round_keys[i]), bytes.fromhex(ciphertext)).hex()
    ciphertext = to_matrix(ciphertext)
    sub_bytes(ciphertext)
    shift_rows(ciphertext)
    ciphertext = from_matrix(ciphertext)
    ciphertext = xor(bytes.fromhex(round_keys[10]), bytes.fromhex(ciphertext)).hex()
    return ciphertext


# EDITed following
def xor_bytes(a: bytes, b: bytes) -> bytes:
    return bytes(x ^ y for x, y in zip(a, b))


def shift_rows_rev(state):
    placeholder = state[1][3]
    state[1][0], state[1][1], state[1][2], state[1][3] = (
        state[1][3],
        state[1][0],
        state[1][1],
        state[1][2],
    )
    state[2][0], state[2][1], state[2][2], state[2][3] = (
        state[2][2],
        state[2][3],
        state[2][0],
        state[2][1],
    )
    state[3][0], state[3][1], state[3][2], state[3][3] = (
        state[3][1],
        state[3][2],
        state[3][3],
        state[3][0],
    )
    return state


def mix_columns_rev(s):
    ss = [[0] * 4 for _ in range(4)]

    for c in range(4):
        ss[0][c] = hex(
            gmul(0x0E, s[0][c])
            ^ gmul(0x0B, s[1][c])
            ^ gmul(0x0D, s[2][c])
            ^ gmul(0x09, s[3][c])
        )[2:].zfill(2)
        ss[1][c] = hex(
            gmul(0x09, s[0][c])
            ^ gmul(0x0E, s[1][c])
            ^ gmul(0x0B, s[2][c])
            ^ gmul(0x0D, s[3][c])
        )[2:].zfill(2)
        ss[2][c] = hex(
            gmul(0x0D, s[0][c])
            ^ gmul(0x09, s[1][c])
            ^ gmul(0x0E, s[2][c])
            ^ gmul(0x0B, s[3][c])
        )[2:].zfill(2)
        ss[3][c] = hex(
            gmul(0x0B, s[0][c])
            ^ gmul(0x0D, s[1][c])
            ^ gmul(0x09, s[2][c])
            ^ gmul(0x0E, s[3][c])
        )[2:].zfill(2)

    for i in range(4):
        for j in range(4):
            s[i][j] = ss[i][j]
    return s


def mix_bits_rev(state):
    state = shift_rows_rev(state)

    for _ in range(1, 10):
        state = mix_columns_rev(state)
        state = shift_rows_rev(state)
    return state


def main():
    pt1 = bytes.fromhex("72616e646f6d64617461313131313131")
    print(pt1)
    ct1 = bytes.fromhex("d7481d89f1aaf5a857f56edd2ae8994c")
    print(ct1)
    ct1_k0 = bytes.fromhex(AES(pt1.hex(), "00000000000000000000000000000000"))
    print(ct1_k0)

    ct2 = bytes.fromhex("8c7d66558130eb5796d131beb43c9934")
    print(ct2)

    filt = xor_bytes(ct1, ct1_k0)
    m = xor_bytes(ct2, filt)
    print(m)

    m = mix_bits_rev(to_matrix(m.hex()))
    pt2 = bytes.fromhex(from_matrix(m))
    print(pt2)


if __name__ == "__main__":
    main()
