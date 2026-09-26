import string


class CharMap:
    """
    替字暗号のための文字マッピングを表すクラス。
    各インデックスはアルファベットの文字に対応する (0 = 'a', 1 = 'b', ..., 25 = 'z')
    値はマッピングされた文字、または未マッピングの場合は '_' となる

    Attributes:
        map (dict[str, str]): 文字マッピングを保持する辞書
        ignore_case (bool): 大文字小文字を区別するかどうか
    """

    def __init__(self, ignore_case: bool = True):
        self.map: dict[str, str] = {}
        self.ignore_case = ignore_case

    def resolve_char(self, char: str) -> str | None:
        """
        指定された文字のマッピングを解決する

        Args:
            char (str): マッピングを解決する文字

        Returns:
            str | None: マッピングされた文字、または未マッピングの場合は None
        """
        if self.ignore_case:
            char = char.lower()

        return self.map.get(char, None)

    def add_char_mapping(
        self, from_char: str, to_char: str, verbose: bool = False
    ) -> bool:
        """
        文字マップに新しいマッピングを追加する

        Args:
            from_char (str): マッピング元の文字
            to_char (str): マッピング先の文字
            verbose (bool): True の場合、マッピングの競合が発生した場合に詳細な情報を出力する

        Returns:
            bool: マッピングが成功した場合は True、競合が発生した場合は False
        """
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
        """
        文字マップに単語のマッピングを追加する

        Args:
            from_word (str): マッピング元の単語
            to_word (str): マッピング先の単語
            verbose (bool): True の場合、マッピングの競合が発生した場合に詳細な情報を出力する

        Returns:
            bool: マッピングが成功した場合は True、競合が発生した場合は False
        """
        if len(from_word) != len(to_word):
            return False

        for f_char, t_char in zip(from_word.lower(), to_word.lower()):
            if not self.add_char_mapping(f_char, t_char, verbose=verbose):
                return False

        return True

    def translate_char(self, char: str, save_case: bool = True) -> str:
        """
        指定された文字をマッピングに基づいて変換する

        Args:
            char (str): 変換する文字
            save_case (bool): True の場合、大文字小文字を保持する

        Returns:
            str: 変換された文字、または未マッピングの場合は '_' を返す
        """
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
        """
        指定されたテキストをマッピングに基づいて変換する

        Args:
            text (str): 変換するテキスト
            save_case (bool): True の場合、大文字小文字を保持する

        Returns:
            str: 変換されたテキスト
        """
        return "".join(self.translate_char(c, save_case=save_case) for c in text)

    def is_all_translatable(self, text: str, alphabet_only: bool = True) -> bool:
        """
        指定されたテキストのすべての文字がマッピング可能かどうかを確認する

        Args:
            text (str): 確認するテキスト
            alphabet_only (bool): True の場合、アルファベットのみを確認する

        Returns:
            bool: すべての文字がマッピング可能な場合は True、そうでない場合は False
        """
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
