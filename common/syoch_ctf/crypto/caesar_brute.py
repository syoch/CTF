from .caesar import caesar


def caesar_brute(text: str, hints: list[str] | None = None) -> list[tuple[int, str]]:
    results = []
    for shift in range(26):
        decrypted_text = caesar(text, shift)
        if hints is None:
            results.append((shift, decrypted_text))
            continue

        if any(hint in decrypted_text for hint in hints):
            results.append((shift, decrypted_text))
    return results


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Caesar cipher tool")
    parser.add_argument("--text", help="Text to be processed")
    parser.add_argument("--hints", nargs="*", help="Hints to filter results")

    args = parser.parse_args()

    processed_texts = caesar_brute(args.text, args.hints)
    for shift, processed_text in processed_texts:
        print(f"Shift: {shift}\n{processed_text}\n")


if __name__ == "__main__":
    main()
