from .charset import (
    CharMap,
    EMPTY_MAP,
    charmap_to_translate_table,
    is_all_translatable,
    find_words_with_pattern,
)

from typing import Generator


class Solver:
    def __init__(self, ciphertext: str):
        self.ciphertext = ciphertext
        self.sorted_words = sorted(
            set(
                word
                for word in self.ciphertext.split()
                if all(c.isalpha() for c in word)
            ),
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
            if not is_all_translatable(word, current_charmap):
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

        pattern = find_words_with_pattern(word_to_process, current_charmap)
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
        self, initial_map: CharMap = EMPTY_MAP
    ) -> Generator[tuple[CharMap, str], None, None]:
        word_max_length = max(len(word) for word in self.sorted_words)
        print(f"Max word length: {word_max_length}")

        for charmap in self.charmaps(word_max_length, initial_map=initial_map):
            decoded = self.ciphertext.translate(
                str.maketrans(charmap_to_translate_table(charmap))
            )
            yield charmap, decoded
