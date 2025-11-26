from syoch_ctf.data_processor.charmap import CharMap
from pwn import remote


def remote_pipe():
    return remote("verbal-sleep.picoctf.net", 59906)


def estimate_encryption_params(charmap: CharMap):
    chars = [*charmap.map.keys()][:2]
    x1 = ord(chars[0].upper()) - ord("A")
    x2 = ord(chars[1].upper()) - ord("A")
    y1 = ord(charmap.map[chars[0]].upper()) - ord("A")
    y2 = ord(charmap.map[chars[1]].upper()) - ord("A")

    # determine scale, offset that satisfies:
    #   y1 = (scale * x1 + offset) % 26
    #   y2 = (scale * x2 + offset) % 26
    # implies:
    #  scale = (y2 - y1) (x2 - x1)^-1 (mod 26)
    #  offset = (y1 - scale * x1 + 26) % 26

    dy = (y2 - y1) % 26
    dx = (x2 - x1) % 26
    dx_inv = pow(dx, -1, 26)
    scale = (dy * dx_inv) % 26
    offset = (y1 - scale * x1 + 26) % 26

    assert (scale * x1 + offset) % 26 == y1
    assert (scale * x2 + offset) % 26 == y2

    return scale, offset


def do_transform_char(c: str, scale: int, offset: int) -> str:
    if not c.isalpha():
        return c
    y = ord(c.upper()) - ord("A")
    # y = scale * x + offset (mod 26)
    # x = scale^-1 * (y - offset) (mod 26)
    scale_inv = pow(scale, -1, 26)
    y = (scale_inv * (y - offset + 26)) % 26
    return chr(y + ord("A"))


def transform_text(text: str, scale: int, offset: int) -> str:
    return "".join(do_transform_char(c, scale, offset) for c in text)


def solve():
    with open("words.txt") as f:
        words = set(f.read().splitlines())
    print(f"Loaded {len(words)} words")

    p = remote_pipe()
    p.recvuntil(b"you'll be able to guess it:  ")
    cheese_e = p.recvline().decode().strip()
    print(f"Encrypted cheese to decode: {cheese_e}")

    test_msg = "BRA"
    test_cipher = ""
    p.recvuntil(b"What would you like to do?")
    p.recvline()

    p.sendline(b"e")
    p.sendline(test_msg.encode())

    p.recvuntil(b"Here's your encrypted cheese:  ")
    test_cipher = p.recvline().decode().strip()

    print("Building character map... from index 0, 2")
    char_map = CharMap(ignore_case=True)
    char_map.add_char_mapping(test_msg[0], test_cipher[0])
    char_map.add_char_mapping(test_msg[2], test_cipher[2])

    print("Character map built:")
    print(char_map)

    scale, offset = estimate_encryption_params(char_map)
    print(f"Estimated encryption params: scale={scale}, offset={offset}")

    transformed_cheese = transform_text(cheese_e, scale, offset)
    print(f"Transformed cheese: {transformed_cheese}")

    p.recvuntil(b"What would you like to do?")
    p.recvline()
    p.sendline(b"g")
    p.recvuntil(b"So...what's my cheese?")
    p.sendline(transformed_cheese.encode())

    p.recvuntil(b"cloning room:  ")
    flag = p.recvall().decode().strip()

    print(f"Flag: {flag}")


if __name__ == "__main__":
    solve()
