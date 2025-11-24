import os
from pwn import process, remote, info, warn, context

KEY_LEN = 50000


def local_test():
    import random

    FLAG = "FLAG{this_is_a_test_flag}\n"
    key = os.urandom(KEY_LEN)

    print("[+] Generating test environment...")
    print(f"  - Key of flag encryption: {key[0 : len(FLAG)].hex()}")

    # Generate key file
    with open("key", "wb") as f:
        f.write(key)
    # Generate flag file
    with open("flag", "w") as f:
        f.write(FLAG)

    return process("python3 otp.py", shell=True)


def on_remote():
    return remote("mercury.picoctf.net", 64260)


def main():
    p = on_remote()
    p.recvuntil(b"This is the encrypted flag!\n")
    encrypted_flag_hex = p.recvline().strip().decode()
    p.recvline()
    encrypted_flag = bytes.fromhex(encrypted_flag_hex)

    info(f"Encrypted flag (hex): {encrypted_flag_hex} ({len(encrypted_flag)} bytes)")

    p.recvuntil(b"What data would you like to encrypt? ")
    p.sendline(b"0" * (KEY_LEN - len(encrypted_flag)))
    p.recvuntil(b"Here ya go!\n")
    _ = p.recvline()

    p.recvuntil(b"What data would you like to encrypt? ")
    p.sendline(b"0" * len(encrypted_flag))
    p.recvuntil(b"Here ya go!\n")
    key_hex = p.recvline().strip().decode()
    key = bytes([c ^ ord("0") for c in bytes.fromhex(key_hex)])

    info(f"Key (hex): {key_hex} ({len(key)} bytes)")

    decrypted_flag = bytes([ef ^ k for ef, k in zip(encrypted_flag, key)])
    info(f"Decrypted flag: {decrypted_flag.decode()}")


if __name__ == "__main__":
    main()
