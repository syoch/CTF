import ast
import hashlib
import os
import random
import secrets
import sys
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

KEY_SIZE = 32
SALT_SIZE = 256


def parse_vector(vector: str) -> list[int] | None:
    sanitized = "".join(c if c in "0123456789,[]" else "" for c in vector)
    try:
        parsed = ast.literal_eval(sanitized)
    except (ValueError, SyntaxError, TypeError):
        return None

    if isinstance(parsed, list):
        return parsed
    return None


def take_hash(salt: bytes, in_str: str):
    vector_encoding = in_str[1:-1].encode("latin-1")
    return hashlib.sha512(salt + vector_encoding).digest().hex()


def dot_product(key: list[int], vector: list[int]):
    return sum(vector_entry * key_entry for vector_entry, key_entry in zip(vector, key))


class SecureDotProductService:
    def __init__(self, key: bytes):
        self.key_vector = list(key)
        self.salt = secrets.token_bytes(SALT_SIZE)

        trusted_vectors = []
        for _ in range(5):
            length = random.randint(1, 32)
            vector = [random.randint(-(2**8), 2**8) for _ in range(length)]
            trusted_vectors.append((vector, take_hash(self.salt, str(vector))))

        self.trusted_vectors = trusted_vectors

    def run(self):
        print("============== Secure Dot Product Service ==============")
        print(f"[DEBUG LEAK {self.key_vector}]")
        print(
            "I will compute the dot product of my key vector with any trustworthy vector you choose!"
        )
        print("Here are the vectors I trust won't leak my key:")

        for pair in self.trusted_vectors:
            print(pair)

        while True:
            print("========================================================")
            vector_input = (
                input("Enter your vector: ").encode().decode("unicode_escape")
            )

            # Parse
            vector = parse_vector(vector_input)
            if not vector:
                print("Invalid vector! Please enter your vector as a list of ints.")
                continue

            # Check hash
            vector_hash = take_hash(self.salt, vector_input)
            input_hash = input("Enter its salted hash: ")

            if vector_hash != input_hash:
                print("Untrusted vector detected!")
                break

            # Result
            res = dot_product(self.key_vector, vector)

            print("The computed dot product is: " + str(res))


def read_flag():
    flag_path = "flag.txt"

    if os.path.exists(flag_path):
        with open(flag_path, "r") as f:
            flag = f.read().strip()
    else:
        print("flag.txt not found in the current directory.")
        sys.exit()

    return flag


def encrypt_flag(flag: str, key: bytes):
    iv = secrets.token_bytes(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(flag.encode(), AES.block_size))

    return iv, ciphertext


def main():
    flag = read_flag()
    key = secrets.token_bytes(KEY_SIZE)
    iv, ciphertext = encrypt_flag(flag, key)

    print("==================== Encrypted Flag ====================")
    print(f"IV: {iv.hex()}")
    print(f"Ciphertext: {ciphertext.hex()}")

    service = SecureDotProductService(key)
    service.run()


if __name__ == "__main__":
    main()
