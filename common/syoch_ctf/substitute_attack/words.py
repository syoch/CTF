from requests import request

WORDS_URL = "https://github.com/dwyl/english-words/raw/refs/heads/master/words.txt"
WORDS_FILE = "words.txt"


def _load_words() -> set[str]:
    try:
        with open(WORDS_FILE, "r") as f:
            words = {line.strip() for line in f}
    except FileNotFoundError:
        print("Downloading word list...")
        resp = request("GET", WORDS_URL)
        resp.raise_for_status()
        words = {line.strip() for line in resp.text.splitlines()}
        with open(WORDS_FILE, "w") as f:
            f.write("\n".join(words))

    words = {
        word.lower()
        for word in words
        if word.isalpha()
        if "." not in word
        if "'" not in word
    }
    return words


WORDS = _load_words()


def get_alphabetic_words() -> set[str]:
    return WORDS


__all__ = ["get_alphabetic_words"]
