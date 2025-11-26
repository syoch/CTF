from syoch_ctf.require_file import require_file

WORDS_URL = "https://github.com/dwyl/english-words/raw/refs/heads/master/words.txt"


def get_alphabetic_words(words_file: str) -> set[str]:
    require_file(words_file, WORDS_URL)

    with open(words_file, "r") as f:
        words = {line.strip() for line in f}

    words = {word.lower() for word in words if word.isalpha()}
    return words


__all__ = ["get_alphabetic_words"]
