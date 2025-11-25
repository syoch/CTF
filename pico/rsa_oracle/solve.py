import sys
from pwn import remote, tube, context
import gmpy2

context.log_level = "debug"
gmpy2.get_context().precision = 8192
sys.set_int_max_str_digits(1000000)


def remote_pipe():
    return remote("titan.picoctf.net", 58177)


def encrypt(m: int) -> int:
    m_bytes = m.to_bytes((m.bit_length() + 7) // 8, "big")

    p.recvuntil(b"E --> encrypt D")
    p.recvline()
    p.sendline(b"e")
    p.recvuntil(b"enter text to encrypt (encoded length must be less than keysize): ")
    p.sendline(m_bytes)
    p.recvuntil(b"ciphertext (m ^ e mod n) ")
    return int(p.recvline().strip())


def decrypt(c: int) -> int:
    p.recvuntil(b"E --> encrypt D")
    p.recvline()
    p.sendline(b"d")
    p.recvuntil(b"Enter text to decrypt: ")
    p.sendline(str(c).encode())
    p.recvuntil(b"decrypted ciphertext as hex (c ^ d mod n): ")
    return int(p.recvline().strip(), 16)


def solve(p: tube):
    max_hex_m_eg = "696a616765696f6a6567696f6a656167696f6a656761696f6a6765616f696a67656f696a6765616f696a6761656f696a6765616f6a69676561696a6167656f696a676165696765616f696765616f696a6765616f696a6761656f696a67656f696a6765616f696a676165"
    MAX_MESSAGE_LENGTH = len(max_hex_m_eg) * 4
    with open("password.enc", "r") as f:
        encrypted_password = int(f.read().strip())

    print("Encrypted password:", encrypted_password)
    print("  - Length (bits):", encrypted_password.bit_length())
    print("Max message length (bits):", MAX_MESSAGE_LENGTH)

    test_msg = 2
    test_cipher = encrypt(test_msg)
    print("Test message:", test_msg)
    print("Test ciphertext:", test_cipher)

    mc = decrypt(encrypted_password * test_cipher)
    print("Decrypted 2*m:", mc)
    # Recover m
    if mc % 2 != 0:
        print("Error: mc is not even!")
        return
    recovered_m = mc // 2
    print("Recovered m:", recovered_m)

    hex_m = hex(recovered_m)[2:]
    if len(hex_m) % 2 != 0:
        hex_m = "0" + hex_m
    password = bytes.fromhex(hex_m).decode()
    print("Password:", password)


if __name__ == "__main__":
    p = remote_pipe()
    solve(p)
