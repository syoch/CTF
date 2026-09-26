def caesar(text: str, shift: int) -> str:
    """シーザー暗号の処理を行う

    Args:
        text (str): 処理対象の文字列
        shift (int): シフト値

    Returns:
        str: 処理後の文字列
    """
    result = ""
    for ch in text:
        if ch.islower():
            result += chr(ord("a") + (26 + ord(ch) - ord("a") + shift) % 26)
        elif ch.isupper():
            result += chr(ord("A") + (26 + ord(ch) - ord("A") + shift) % 26)
        else:
            result += ch

    return result


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Caesar cipher tool")
    parser.add_argument("text", help="Text to be processed")
    parser.add_argument(
        "-s", "--shift", type=int, required=True, help="Shift value for Caesar cipher"
    )

    args = parser.parse_args()

    processed_text = caesar(args.text, args.shift)
    print(processed_text)
