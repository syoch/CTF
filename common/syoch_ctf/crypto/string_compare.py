def string_compare(s1: str, s2: str):
    for c1, c2 in zip(s1, s2):
        c1 = c1.upper()
        c2 = c2.upper()

        diff = (ord(c1) - ord(c2)) % 26
        xor_diff = (ord(c1) ^ ord(c2)) % 26
        print(f"{c1} <=> {c2}: diff {diff:2d}, xor {xor_diff:2d}")


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Caesar cipher tool")
    parser.add_argument("text1", help="First text to be processed")
    parser.add_argument("text2", help="Second text to be processed")

    args = parser.parse_args()

    string_compare(args.text1, args.text2)


if __name__ == "__main__":
    main()
