from typing import Generator
from .. import it

Placement = tuple[int, int, int, int]


def reform_bits(
    bits: Generator[int], switch: int, placement: Placement
) -> Generator[int]:
    s0 = switch >> 3
    s1 = (switch >> 2) & 1
    s2 = (switch >> 1) & 1
    s3 = switch & 1
    while True:
        try:
            b0 = next(bits) ^ s0
            b1 = next(bits) ^ s1
            b2 = next(bits) ^ s2
            b3 = next(bits) ^ s3
            bit = (b0, b1, b2, b3)
        except StopIteration:
            break

        yield bit[placement[0]]
        yield bit[placement[1]]
        yield bit[placement[2]]
        yield bit[placement[3]]


assert [*reform_bits(it((0, 1, 0, 1)), 0b0101, (0, 1, 2, 3))] == [0, 0, 0, 0]  # type: ignore
assert [*reform_bits(it((0, 1, 0, 1)), 0b1010, (0, 1, 2, 3))] == [1, 1, 1, 1]  # type: ignore
assert [*reform_bits(it((0, 1, 0, 1)), 0b0000, (0, 1, 2, 3))] == [0, 1, 0, 1]  # type: ignore
assert [*reform_bits(it((0, 1, 0, 1)), 0b0000, (1, 2, 3, 0))] == [1, 0, 1, 0]  # type: ignore
assert [*reform_bits(it((0, 0, 0, 1)), 0b0000, (1, 2, 3, 0))] == [0, 0, 1, 0]  # type: ignore
assert [*reform_bits(it((0, 0, 0, 1)), 0b0000, (1, 2, 0, 2))] == [0, 0, 0, 0]  # type: ignore
