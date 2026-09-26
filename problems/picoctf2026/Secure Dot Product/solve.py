from typing import Callable
import subprocess
from pwn import *
import z3
from sage.all import *

# context.arch = "i386"
context.terminal = ["tmux", "splitw", "-h"]
# context.log_level = "debug"

# vuln = ELF("./vuln")
KEY_SIZE = 32

MASK64 = (1 << 64) - 1

SHA512_K = [
    0x428A2F98D728AE22,
    0x7137449123EF65CD,
    0xB5C0FBCFEC4D3B2F,
    0xE9B5DBA58189DBBC,
    0x3956C25BF348B538,
    0x59F111F1B605D019,
    0x923F82A4AF194F9B,
    0xAB1C5ED5DA6D8118,
    0xD807AA98A3030242,
    0x12835B0145706FBE,
    0x243185BE4EE4B28C,
    0x550C7DC3D5FFB4E2,
    0x72BE5D74F27B896F,
    0x80DEB1FE3B1696B1,
    0x9BDC06A725C71235,
    0xC19BF174CF692694,
    0xE49B69C19EF14AD2,
    0xEFBE4786384F25E3,
    0x0FC19DC68B8CD5B5,
    0x240CA1CC77AC9C65,
    0x2DE92C6F592B0275,
    0x4A7484AA6EA6E483,
    0x5CB0A9DCBD41FBD4,
    0x76F988DA831153B5,
    0x983E5152EE66DFAB,
    0xA831C66D2DB43210,
    0xB00327C898FB213F,
    0xBF597FC7BEEF0EE4,
    0xC6E00BF33DA88FC2,
    0xD5A79147930AA725,
    0x06CA6351E003826F,
    0x142929670A0E6E70,
    0x27B70A8546D22FFC,
    0x2E1B21385C26C926,
    0x4D2C6DFC5AC42AED,
    0x53380D139D95B3DF,
    0x650A73548BAF63DE,
    0x766A0ABB3C77B2A8,
    0x81C2C92E47EDAEE6,
    0x92722C851482353B,
    0xA2BFE8A14CF10364,
    0xA81A664BBC423001,
    0xC24B8B70D0F89791,
    0xC76C51A30654BE30,
    0xD192E819D6EF5218,
    0xD69906245565A910,
    0xF40E35855771202A,
    0x106AA07032BBD1B8,
    0x19A4C116B8D2D0C8,
    0x1E376C085141AB53,
    0x2748774CDF8EEB99,
    0x34B0BCB5E19B48A8,
    0x391C0CB3C5C95A63,
    0x4ED8AA4AE3418ACB,
    0x5B9CCA4F7763E373,
    0x682E6FF3D6B2B8A3,
    0x748F82EE5DEFB2FC,
    0x78A5636F43172F60,
    0x84C87814A1F0AB72,
    0x8CC702081A6439EC,
    0x90BEFFFA23631E28,
    0xA4506CEBDE82BDE9,
    0xBEF9A3F7B2C67915,
    0xC67178F2E372532B,
    0xCA273ECEEA26619C,
    0xD186B8C721C0C207,
    0xEADA7DD6CDE0EB1E,
    0xF57D4F7FEE6ED178,
    0x06F067AA72176FBA,
    0x0A637DC5A2C898A6,
    0x113F9804BEF90DAE,
    0x1B710B35131C471B,
    0x28DB77F523047D84,
    0x32CAAB7B40C72493,
    0x3C9EBE0A15C9BEBC,
    0x431D67C49C100D4C,
    0x4CC5D4BECB3E42B6,
    0x597F299CFC657E2A,
    0x5FCB6FAB3AD6FAEC,
    0x6C44198C4A475817,
]


def _rotr64(x: int, n: int) -> int:
    return ((x >> n) | (x << (64 - n))) & MASK64


def _sha512_compress(state: list[int], block: bytes) -> list[int]:
    assert len(block) == 128

    w = [int.from_bytes(block[i : i + 8], "big") for i in range(0, 128, 8)]
    for i in range(16, 80):
        s0 = _rotr64(w[i - 15], 1) ^ _rotr64(w[i - 15], 8) ^ (w[i - 15] >> 7)
        s1 = _rotr64(w[i - 2], 19) ^ _rotr64(w[i - 2], 61) ^ (w[i - 2] >> 6)
        w.append((w[i - 16] + s0 + w[i - 7] + s1) & MASK64)

    a, b, c, d, e, f, g, h = state

    for i in range(80):
        S1 = _rotr64(e, 14) ^ _rotr64(e, 18) ^ _rotr64(e, 41)
        ch = (e & f) ^ ((~e) & g)
        temp1 = (h + S1 + ch + SHA512_K[i] + w[i]) & MASK64

        S0 = _rotr64(a, 28) ^ _rotr64(a, 34) ^ _rotr64(a, 39)
        maj = (a & b) ^ (a & c) ^ (b & c)
        temp2 = (S0 + maj) & MASK64

        h = g
        g = f
        f = e
        e = (d + temp1) & MASK64
        d = c
        c = b
        b = a
        a = (temp1 + temp2) & MASK64

    return [
        (state[0] + a) & MASK64,
        (state[1] + b) & MASK64,
        (state[2] + c) & MASK64,
        (state[3] + d) & MASK64,
        (state[4] + e) & MASK64,
        (state[5] + f) & MASK64,
        (state[6] + g) & MASK64,
        (state[7] + h) & MASK64,
    ]


def _digest_to_state(digest_hex: str) -> list[int]:
    raw = bytes.fromhex(digest_hex)
    if len(raw) != 64:
        raise ValueError("SHA-512 digest must be 64 bytes")
    return [int.from_bytes(raw[i : i + 8], "big") for i in range(0, 64, 8)]


def _state_to_digest(state: list[int]) -> str:
    return "".join(x.to_bytes(8, "big").hex() for x in state)


def sha512_length_extend(
    original_hash_hex: str,
    original_message_length: int,
    appended_message: bytes,
) -> tuple[str, bytes]:
    state = _digest_to_state(original_hash_hex)
    glue = sha512_pad(original_message_length)

    forged_total_before_final_pad = (
        original_message_length + len(glue) + len(appended_message)
    )
    continuation = appended_message + sha512_pad(forged_total_before_final_pad)

    for i in range(0, len(continuation), 128):
        state = _sha512_compress(state, continuation[i : i + 128])

    return _state_to_digest(state), glue


def sha512_pad(message_byte_length: int) -> bytes:
    BLOCK_SIZE = 128
    LENGTH_SIZE = 16

    message_bit_length = message_byte_length * 8
    message_remaining_bytes = message_byte_length % BLOCK_SIZE
    padding_length = (BLOCK_SIZE - message_remaining_bytes) % BLOCK_SIZE

    padding = b""
    padding += b"\x80"
    padding += b"\x00" * (padding_length - 1 - LENGTH_SIZE)
    padding += message_bit_length.to_bytes(16, "big")

    return padding


def try_vector(p: tube, vector: bytes, vec_hash: str):
    p.recvuntil(b"Enter your vector: ")
    p.sendline(vector)
    p.recvuntil(b"Enter its salted hash: ")
    p.sendline(vec_hash.encode())
    p.recvuntil(b"The computed dot product is: ")

    return int(p.recvline().strip())


def try_appended_vector(
    p: tube, vector: list[int], vec_hash: str, appended_vector: list[int]
):
    inner = str(vector)[1:-1]

    glue = sha512_pad(256 + len(inner))
    suffix = ", " + ", ".join(str(v) for v in appended_vector)
    glue = "".join(f"\\x{hex(x)[2:].zfill(2)}" for x in glue)

    vector_str = f"[{inner}{glue}{suffix}]".encode()
    hash_str = sha512_length_extend(vec_hash, 256 + len(inner), f"{suffix}".encode())[0]

    return try_vector(p, vector_str, hash_str)


def request_matrix(fact: Callable[[], tube]):
    p = fact()
    p.recvuntil(b"IV: ")
    iv = bytes.fromhex(p.recvline().strip().decode())
    p.recvuntil(b"Ciphertext: ")
    ciphertext = bytes.fromhex(p.recvline().strip().decode())

    p.recvuntil(b"Here are the vectors I trust won't leak my key:\n")

    vectors: list[tuple[list[int], str]] = []
    for _ in range(5):
        line = p.recvline().strip()
        vn, vec_hash = eval(line)

        vectors.append((vn, vec_hash))

    pairs: list[tuple[list[int], int]] = []
    for vn, vec_hash in vectors:
        val = try_vector(p, str(vn).encode(), vec_hash)

        vn = [*[abs(x) for x in vn], *[0] * (KEY_SIZE - len(vn))]
        print(f"vec: {vn}, val: {val}")
        pairs.append((vn, val))

    min_vector, min_hash = min(vectors, key=lambda x: len(x[0]))
    min_value = try_vector(p, str(min_vector).encode(), min_hash)
    if len(min_vector) >= 5:
        print("Too long vector")
        p.close()
        return None

    known_appended_bytes: list[int] = []
    for i in range(KEY_SIZE - len(min_vector)):
        print(f"Trying to append byte {i}... (min_vec len: {len(min_vector)})")
        appended_vector = [0] * (KEY_SIZE - len(min_vector))
        appended_vector[i] = 1
        val = try_appended_vector(p, min_vector, min_hash, appended_vector)
        known_appended_bytes.append(val - min_value)

    # Redacting part of the key that leaked by SHA-512 length extension attack
    partial_key_vector = [0] * len(min_vector) + known_appended_bytes
    reduced_pairs: list[tuple[list[int], int]] = []
    for vn, an in pairs:
        reduced_val = an - sum(v * r for v, r in zip(vn, partial_key_vector))
        reduced_vec = vn[0 : len(min_vector)]
        print(f"reduced vec: {reduced_vec}, reduced val: {reduced_val}")
        reduced_pairs.append((reduced_vec, reduced_val))

    # Solve for the remaining part of the key
    equation_to_use_count = len(min_vector)
    equations = reduced_pairs[:equation_to_use_count]
    A = Matrix(ZZ, [vec for vec, a in equations])
    b = vector(ZZ, [a for vec, a in equations])
    key_part = A.solve_right(b)

    # Reconstruct the key
    key = list(key_part) + known_appended_bytes
    key = bytes(key)

    # Decipher the ciphertext using the recovered key
    from Crypto.Cipher import AES
    from Crypto.Util.Padding import unpad

    cipher = AES.new(key, AES.MODE_CBC, iv)
    flag = unpad(cipher.decrypt(ciphertext), AES.block_size)

    return flag


def ctf_solve(fact: Callable[[], tube]):
    while True:
        res = request_matrix(fact)
        if not res:
            continue

        print("Flag:", res)
        break


def main() -> None:
    # p = lambda: process(["./vuln"])
    # p = lambda: process(["python3", "remote.py"])
    p = lambda: remote("lonely-island.picoctf.net", 64484)
    ctf_solve(p)

    # cmd = ["qemu-i386", "-g", "1234", "./vuln", *payload().split(b" ")]
    # print(cmd)
    # subprocess.run(cmd)


if __name__ == "__main__":
    main()
