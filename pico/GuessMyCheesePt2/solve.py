import hashlib


def solve():
    with open("cheese_list.txt") as f:
        words = set(f.read().splitlines())
    print(f"Loaded {len(words)} words")

    want_hash = bytes.fromhex(
        "51e0b0ec12ed5649243138fe1abee9704b0a092e485fae42c30fbf7249723e44"
    )

    for salt in range(256):
        salt_bytes = hex(salt)[2:].zfill(2).encode()
        salt_bytes_raw = bytes([salt])

        for word in words:
            word_bytes = word.encode()

            for insert_pos_1 in range(len(word_bytes) + 1):
                candidate = (
                    word_bytes[:insert_pos_1] + salt_bytes + word_bytes[insert_pos_1:]
                )
                if hashlib.sha256(candidate.lower()).digest() == want_hash:
                    print("Found!")
                    print(f"Salt: {salt_bytes}")
                    print(f"Word: {word}")
                    print(f"Candidate: {candidate.lower()}")
                    return
                if hashlib.sha256(candidate).digest() == want_hash:
                    print("Found!")
                    print(f"Salt: {salt_bytes}")
                    print(f"Word: {word}")
                    print(f"Candidate: {candidate}")
                    return
                if hashlib.sha256(candidate.upper()).digest() == want_hash:
                    print("Found!")
                    print(f"Salt: {salt_bytes}")
                    print(f"Word: {word}")
                    print(f"Candidate: {candidate.upper()}")
                    return
                candidate = (
                    word_bytes[:insert_pos_1]
                    + salt_bytes_raw
                    + word_bytes[insert_pos_1:]
                )
                if hashlib.sha256(candidate.lower()).digest() == want_hash:
                    print("Found!")
                    print(f"Salt: {salt_bytes}")
                    print(f"Word: {word}")
                    print(f"Candidate: {candidate.lower()}")
                    return
                if hashlib.sha256(candidate).digest() == want_hash:
                    print("Found!")
                    print(f"Salt: {salt_bytes}")
                    print(f"Word: {word}")
                    print(f"Candidate: {candidate}")
                    return
                if hashlib.sha256(candidate.upper()).digest() == want_hash:
                    print("Found!")
                    print(f"Salt: {salt_bytes}")
                    print(f"Word: {word}")
                    print(f"Candidate: {candidate.upper()}")
                    return

    print("Not found")


if __name__ == "__main__":
    solve()
