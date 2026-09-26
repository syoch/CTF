from .caesar import caesar


def caesar_brute(text: str, hints: list[str] | None = None) -> list[tuple[int, str]]:
    """シーザー暗号について、ヒント付きの総当たり攻撃を行う。
    シーザー暗号を行ったときに、ヒント文字列が 1 つ以上含まれていたら、そのシフト値と復号文を返却する。

    Args:
        text (str): 暗号文
        hints (list[str] | None): ヒント文字列のリスト。None の場合は、すべてのシフト値を返却する。

    Returns:
        list[tuple[int, str]]: シフト値と復号文のペアのリスト

    """

    results = []
    for shift in range(26):
        decrypted_text = caesar(text, shift)
        if hints is None:
            results.append((shift, decrypted_text))
            continue

        if any(hint in decrypted_text for hint in hints):
            results.append((shift, decrypted_text))
    return results


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Caesar cipher tool")
    parser.add_argument("--text", help="Text to be processed")
    parser.add_argument("--hints", nargs="*", help="Hints to filter results")

    args = parser.parse_args()

    processed_texts = caesar_brute(args.text, args.hints)
    for shift, processed_text in processed_texts:
        print(f"Shift: {shift}\n{processed_text}\n")
