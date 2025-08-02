from typing import Generator


def bits2bytes(bits: Generator[int]) -> bytes:
    byte = 0
    count = 0

    result = bytearray()
    for bit in bits:
        byte = (byte << 1) | bit
        count += 1
        if count == 8:
            result.append(byte)
            byte = 0
            count = 0

    if count > 0:
        result.append(byte << (8 - count))

    return bytes(result)


assert bits2bytes((1, 0, 1, 0, 1, 0, 1, 0)) == b"\xaa"  # type: ignore
assert bits2bytes((1, 0, 1, 0, 1, 0, 1)) == b"\xaa"  # type: ignore
assert bits2bytes((0, 1, 0, 1, 0, 1, 0, 1)) == b"\x55"  # type: ignore
