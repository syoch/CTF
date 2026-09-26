from typing import Generator
from syoch_ctf.crypto import continued_fraction


def wieners_attack(e: int, n: int, c: int) -> Generator[bytes, None, None]:
    """Wiener's attackを実行する (d が小さい場合, e が大きい場合に有効)
    Args:
        e (int): 公開鍵の指数
        n (int): 公開鍵の法
        c (int): 暗号文
    Yields:
        bytes: 復号された平文のバイト列
    """
    a = continued_fraction.continued_fraction(e, n)
    for i in range(1, len(a)):
        k, d = continued_fraction.contract(a[:i])
        if k == 0:
            continue

        val1 = e * d - 1

        if val1 % k != 0:
            continue

        phi = val1 // k
        s = n - phi + 1
        if s * s - 4 * n < 0:
            continue

        m = pow(c, d, n)

        plaintext = m.to_bytes((m.bit_length() + 7) // 8, "big")
        yield plaintext


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Wiener's attack tool")
    parser.add_argument("e", type=int, help="Public exponent e")
    parser.add_argument("n", type=int, help="Modulus n")
    parser.add_argument("c", type=int, help="Cipher c")
    args = parser.parse_args()

    for plaintext in wieners_attack(args.e, args.n, args.c):
        print(plaintext)


if __name__ == "__main__":
    main()
