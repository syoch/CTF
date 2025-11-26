import string


class CharMap:
    def __init__(self, ignore_case: bool = True):
        """A character mapping for substitution ciphers.
        Each index corresponds to a letter in the alphabet (0 = 'a', 1 = 'b', ..., 25 = 'z').
        The value at each index is the mapped character or '_' if unmapped.
        """
        self.map: dict[str, str] = {}
        self.ignore_case = ignore_case

    def resolve_char(self, char: str) -> str | None:
        if self.ignore_case:
            char = char.lower()

        return self.map.get(char, None)

    def add_char_mapping(
        self, from_char: str, to_char: str, verbose: bool = False
    ) -> bool:
        if to_char == " ":
            return True
        if to_char == "(":
            return True
        if to_char == ")":
            return True
        if self.ignore_case:
            from_char = from_char.lower()
            to_char = to_char.lower()

        already_mapped = self.resolve_char(from_char)
        if already_mapped is not None and already_mapped != to_char:
            if verbose:
                print(
                    f"Conflict mapping for {from_char}. Already mapped to {self.map[from_char]} but trying to map to {to_char}"
                )
            return False

        self.map[from_char] = to_char
        return True

    def add_word_mapping(
        self, from_word: str, to_word: str, verbose: bool = False
    ) -> bool:
        if len(from_word) != len(to_word):
            return False

        for f_char, t_char in zip(from_word.lower(), to_word.lower()):
            if not self.add_char_mapping(f_char, t_char, verbose=verbose):
                return False

        return True

    def translate_char(self, char: str, save_case: bool = True) -> str:
        if not char.isalpha():
            return char

        resolved_char = self.resolve_char(char)
        if resolved_char is None or resolved_char == "_":
            return "_"

        if save_case and char.isupper():
            return resolved_char.upper()
        else:
            return resolved_char

    def translate_text(self, text: str, save_case: bool = True) -> str:
        return "".join(self.translate_char(c, save_case=save_case) for c in text)

    def is_all_translatable(self, text: str, alphabet_only: bool = True) -> bool:
        for c in text:
            if alphabet_only and not c.isalpha():
                continue

            if self.resolve_char(c.lower()) is None:
                return False

        return True

    def __str__(self) -> str:
        result = ""

        for i in range(256):
            if i % 16 == 0:
                result += f"{i:03x}: "

            mapped = self.map.get(chr(i), ".")
            if mapped not in string.printable:
                mapped = "."

            if (i + 1) % 16 == 0:
                result += "\n"
            else:
                result += mapped

        return result
