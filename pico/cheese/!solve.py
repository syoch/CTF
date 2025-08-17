from concurrent.futures import ThreadPoolExecutor

from pwn import *

cheeses = [
    "gouda",
    "brie",
    "cheddar",
    "gruyere",
    "emmental",
    "provolone",
    "roquefort",
    "gorgonzola",
]


def build_table(pairs: list[tuple[str, bytes]]) -> dict[bytes, str]:
    table = {}
    for m, e in pairs:
        for m_char, e_char in zip(m, e):
            if e_char not in table:
                table[e_char] = m_char
    return table


def apply_table(table: dict[bytes, str], encrypted: bytes) -> str:
    s2 = ""
    for e_char in encrypted:
        if e_char in table:
            s2 += table[e_char]
        else:
            s2 += "."
    return s2


def collect_pattern(debug=False) -> str:
    context.log_level = "error"
    p: tube = remote("verbal-sleep.picoctf.net", 49406)
    context.log_level = "info"
    p.readuntil(b"you'll be able to guess it:  ")
    encrypted = p.readline()
    if debug:
        print(f"Encrypted cheese: {encrypted.decode().strip()}")

    pairs = []
    for m in random.choices(cheeses, k=3):
        p.readuntil(b"What would you like to do?")
        p.sendline(b"e")  # Encrypt
        p.sendline(m.encode())
        p.readuntil(b"Here's your encrypted cheese: ")
        e = p.readline().strip()

        if debug:
            print(f"Encrypted cheese for '{m}': {e.decode()}")

        pairs.append((m, e))

    if debug:
        print(f"pairs: {pairs}")

    table = build_table(pairs)
    if debug:
        print(f"table: {table}")

    s2 = apply_table(table, encrypted.strip())

    if debug:
        print(f"Decrypted cheese: {s2}")

    context.log_level = "error"
    p.close()
    context.log_level = "info"

    return s2


def collect_n(n: int) -> list[str]:
    collected_patterns = []
    for i in range(n):
        s = collect_pattern()
        collected_patterns.append(s)
    return collected_patterns


all_patterns = []

with ThreadPoolExecutor(max_workers=8) as executor:
    futures = [executor.submit(collect_n, 8) for _ in range(16)]
    for future in futures:
        all_patterns.extend(future.result())
        print(f"Collected {len(all_patterns)} patterns so far...")

all_patterns = [s.strip() for s in all_patterns if s.strip()]
all_patterns = [s for s in all_patterns if len(s) > 0]
all_patterns = sorted(all_patterns)
all_patterns = sorted(all_patterns, key=lambda x: len(x))

with open("./pico/list.txt", "w") as f:
    for s in all_patterns:
        f.write(s + "\n")
print(f"Collected {len(all_patterns)} patterns in total.")
