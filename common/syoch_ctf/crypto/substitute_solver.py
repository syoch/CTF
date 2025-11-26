from typing import Generator

from syoch_ctf.data_processor.charmap import CharMap
from syoch_ctf.data_processor.pattern import find_words_with_pattern


class SubstituteSolver:
    def __init__(self, cipher_text: str):
        self.ciphertext = cipher_text
        self.words = set(
            word for word in self.ciphertext.split() if all(c.isalpha() for c in word)
        )
        self.sorted_words = sorted(
            self.words,
            key=len,
            reverse=True,
        )
        print(f"Loaded {len(self.sorted_words)} unique words from ciphertext.")

    def find_unmapped_word(
        self, current_charmap: CharMap, max_length: int
    ) -> str | None:
        word_to_process = None
        for word in self.sorted_words:
            if len(word) > max_length:
                continue
            if not current_charmap.is_all_translatable(word):
                word_to_process = word
                break
        if word_to_process is None:
            return None

        return word_to_process

    def solve_charmap(
        self, current_charmap: CharMap, max_length: int = 1000
    ) -> Generator[CharMap, None, None]:
        word_to_process = self.find_unmapped_word(current_charmap, max_length)
        if word_to_process is None:
            yield current_charmap
            return

        pattern = find_words_with_pattern(self.words, word_to_process, current_charmap)
        if not pattern:
            return

        for _, updated_charmap in pattern:
            yield from self.solve_charmap(updated_charmap)

        return

    def charmaps(
        self, word_max_length: int, initial_map: CharMap
    ) -> Generator[CharMap, None, None]:
        find_max_length = word_max_length

        while find_max_length > 0:
            yield from self.solve_charmap(initial_map, max_length=find_max_length)
            find_max_length -= 1

    def solve(
        self, initial_map: CharMap = CharMap()
    ) -> Generator[tuple[CharMap, str], None, None]:
        word_max_length = max(len(word) for word in self.sorted_words)
        print(f"Max word length: {word_max_length}")

        for charmap in self.charmaps(word_max_length, initial_map=initial_map):
            decoded = charmap.translate_text(self.ciphertext)
            yield charmap, decoded
