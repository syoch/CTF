import string
from syoch_ctf.substitute_attack.charset import CharMap


def word_matches_pattern(word: str, pattern: str, char_map: CharMap) -> CharMap | None:
    char_map = char_map
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
    Finds words matching the given pattern.

    Arguments:
        pattern: A string pattern where same letters represent the same character
                 and different letters represent different characters.
                 For example, "abba" would match "noon" but not "nope".

    Returns:
        A set of words matching the pattern.
    """
    matching_words = set()
    for word in words:
        if len(word) != len(pattern):
            continue

        updated_char_map = word_matches_pattern(word, pattern, char_map)
        if updated_char_map is not None:
            matching_words.add((word, updated_char_map))

    return matching_words
