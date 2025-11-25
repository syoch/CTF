from pwn import remote

SQUARE_SIZE = 6


def generate_square(alphabet: str):
    assert len(alphabet) == pow(SQUARE_SIZE, 2)
    matrix: list[list[str]] = []
    row: list[str] = []
    for i, letter in enumerate(alphabet):
        if i % SQUARE_SIZE == 0:
            row = []
        row.append(letter)
        if i % SQUARE_SIZE == (SQUARE_SIZE - 1):
            matrix.append(row)
    return matrix


def get_index(letter: str, matrix: list[list[str]]):
    for row in range(SQUARE_SIZE):
        for col in range(SQUARE_SIZE):
            if matrix[row][col] == letter:
                return (row, col)
    print("letter not found in matrix.")
    exit()


def decrypt_pair(pair: str, matrix: list[list[str]]):
    p1r, p1c = get_index(pair[0], matrix)
    p2r, p2c = get_index(pair[1], matrix)

    if p1r == p2r:
        return (
            matrix[p1r][(p1c - 1) % SQUARE_SIZE] + matrix[p2r][(p2c - 1) % SQUARE_SIZE]
        )
    elif p1c == p2c:
        return (
            matrix[(p1r - 1) % SQUARE_SIZE][p1c] + matrix[(p2r - 1) % SQUARE_SIZE][p2c]
        )
    else:
        return matrix[p1r][p2c] + matrix[p2r][p1c]


def decrypt_string(s: str, matrix: list[list[str]]):
    result = ""
    if len(s) % 2 == 0:
        plain = s
    else:
        plain = s + "lsi28c14ot0vbf7nagh3mpjuxy5kwz6edqr9"[0]
    for i in range(0, len(plain), 2):
        result += decrypt_pair(plain[i : i + 2], matrix)
    return result


def main():
    """
    Here is the alphabet: lsi28c14ot0vbf7nagh3mpjuxy5kwz6edqr9
    Here is the encrypted message: 1x5hqlod8x7oa88h0de1b5r6xja5sd
    What is the plaintext message? 1
    """
    p = remote("mercury.picoctf.net", 19860)

    p.recvuntil(b"Here is the alphabet: ")
    alphabet = p.recvline().strip().decode()
    p.recvuntil(b"Here is the encrypted message: ")
    enc_msg = p.recvline().strip().decode()

    m = generate_square(alphabet)

    msg = decrypt_string(enc_msg, m)

    p.recvuntil(b"What is the plaintext message? ")
    p.sendline(msg.encode())

    p.interactive()


if __name__ == "__main__":
    main()
