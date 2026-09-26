import string
from syoch_ctf.data_processor.charmap import CharMap


def word_matches_pattern(word: str, pattern: str, char_map: CharMap) -> CharMap | None:
    """
    単語が指定されたパターンに一致するかどうかを確認し、一致する場合は更新された CharMap を返す。

    Args:
        word (str): 確認する単語
        pattern (str): パターン文字列
        char_map (CharMap): 現在の文字マッピング
    Returns:
        CharMap | None: 単語がパターンに一致する場合は更新された CharMap を返す。一致しない場合は None を返す。
    例:
        word = "hello"
        pattern = "abccd"
        char_map = CharMap()
        result = word_matches_pattern(word, pattern, char_map)
        if result is not None:
            print("The word matches the pattern.")
        else:
            print("The word does not match the pattern.")
        # --> The word matches the pattern.
    """
    for p_char, w_char in zip(pattern, word.lower()):
        if w_char in string.punctuation + string.whitespace:
            continue

        resolved_char = char_map.resolve_char(p_char)
        if resolved_char and resolved_char != w_char:
            # print(f"Conflict for {p_char}: {resolved_char} vs {w_char}")
            return None

        if resolved_char == w_char:
            continue

        if not char_map.add_char_mapping(p_char, w_char):
            # print(f"Failed to map {p_char} to {w_char}")
            return None

    return char_map


def find_words_with_pattern(
    words: set[str], pattern: str, char_map: CharMap
) -> set[tuple[str, CharMap]]:
    """
    指定されたパターンに一致する単語を見つける

    Args:
        words (set[str]): 単語の集合
        pattern (str): パターン文字列
        char_map (CharMap): 現在の文字マッピング

    Returns:
        set[tuple[str, CharMap]]: パターンに一致する単語と更新された CharMap のタプルの集合
    """
    matching_words = set()
    for word in words:
        if len(word) != len(pattern):
            continue

        updated_char_map = word_matches_pattern(word, pattern, char_map)
        if updated_char_map is not None:
            matching_words.add((word, updated_char_map))

    return matching_words
