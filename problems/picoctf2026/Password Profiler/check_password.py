import hashlib

HASH_FILE = "hash.txt"
WORDLIST_FILE = "alice.txt"  # wordlist that was generated using CUPP


def load_hash():
    with open(HASH_FILE, "r") as f:
        return f.read().strip()


def crack_password(target_hash: str):
    with open(WORDLIST_FILE, "r") as f:
        for password in f:
            password = password.strip()
            if hashlib.sha1(password.encode()).hexdigest() == target_hash:
                return password
    return None


if __name__ == "__main__":
    target_hash = load_hash()
    result = crack_password(target_hash)
    if result:
        print(f"Password found: picoCTF{{{result}}}")
    else:
        print("No match found.")
