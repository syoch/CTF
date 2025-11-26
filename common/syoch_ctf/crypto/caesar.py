def caesar(text: str, shift: int) -> str:
    result = ""
    for ch in text:
        if ch.islower():
            result += chr(ord("a") + (26 + ord(ch) - ord("a") + shift) % 26)
        elif ch.isupper():
            result += chr(ord("A") + (26 + ord(ch) - ord("A") + shift) % 26)
        else:
            result += ch

    return result


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Caesar cipher tool")
    parser.add_argument("text", help="Text to be processed")
    parser.add_argument(
        "-s", "--shift", type=int, required=True, help="Shift value for Caesar cipher"
    )

    args = parser.parse_args()

    processed_text = caesar(args.text, args.shift)
    print(processed_text)


if __name__ == "__main__":
    main()
