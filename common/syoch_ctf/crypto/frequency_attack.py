from .caesar import caesar
from syoch_ctf.data_processor.charmap import CharMap

FREQUENCY_ORDER = "etaoinshrdlcumwfgypbvkjxqz"


def analyze_frequency(text: str) -> dict[str, int]:
    frequency = {}
    for ch in text.lower():
        if ch.isalpha():
            frequency[ch] = frequency.get(ch, 0) + 1
    return frequency


def frequency_attack_with_caesar(text: str) -> None:
    frequency = analyze_frequency(text)
    sorted_chars = sorted(frequency.items(), key=lambda item: item[1], reverse=True)
    if not sorted_chars:
        print("No alphabetic characters found in the text.")
        return

    most_frequent_char = sorted_chars[0][0]
    assumed_shift = (ord(most_frequent_char) - ord("e")) % 26

    print(f"Most frequent character in ciphertext: '{most_frequent_char}'")
    print(f"Assumed shift (to map '{most_frequent_char}' to 'e'): {assumed_shift}")
    decrypted_text = caesar(text, -assumed_shift)
    print("Decrypted text with assumed shift:")
    print(decrypted_text)


def frequency_attack(text: str) -> None:
    frequency = analyze_frequency(text)
    sorted_chars = sorted(frequency.items(), key=lambda item: item[1], reverse=True)

    charmap = CharMap()
    for (ch, freq), ch_expect in zip(sorted_chars, FREQUENCY_ORDER):
        charmap.add_char_mapping(ch, ch_expect)

    decrypted_text = charmap.translate_text(text)

    print("Decrypted text using frequency analysis:")
    print(decrypted_text)


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Frequency attack tool")
    parser.add_argument("text", help="Text to be processed")
    parser.add_argument(
        "--caesar",
        action="store_true",
        help="Use Caesar cipher frequency attack",
    )
    args = parser.parse_args()
    if args.caesar:
        frequency_attack_with_caesar(args.text)
    else:
        frequency_attack(args.text)


if __name__ == "__main__":
    main()
