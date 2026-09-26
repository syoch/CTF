from sys import argv
from typing import Generator
import zlib
from base64 import b64decode
from copy import deepcopy
from itertools import permutations

from syoch_ctf import Placement, bits2bytes, reform_bits
from syoch_ctf.png import read_png, get_pixels_left, Pixel

base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="

with open("red.png", "rb") as f:
    red = f.read()


def get_bits(pixels) -> Generator[int]:
    for r, g, b, a in pixels:
        if r != 0xFE and r != 0xFF:
            raise ValueError(f"Unexpected red value: {r}")
        if g != 0x01 and g != 0x00:
            raise ValueError(f"Unexpected green value: {g}")
        if b != 0x01 and b != 0x00:
            raise ValueError(f"Unexpected blue value: {b}")
        if a != 0xFE and a != 0xFF:
            raise ValueError(f"Unexpected alpha value: {a}")

        yield 1 if r == 0xFF else 0
        yield 1 if g == 0x00 else 0
        yield 1 if b == 0x00 else 0
        yield 1 if a == 0xFE else 0


def decrypt(
    pixels: list[Pixel], switch: int = 0, placement: Placement = (0, 1, 2, 3)
) -> bytes:
    return bits2bytes(reform_bits(get_bits(pixels), switch, placement))


idat_compressed = [c for n, c in read_png(red) if n == b"IDAT"][0]
idat = zlib.decompress(idat_compressed)
pixels = [*get_pixels_left(idat[1 : 1 + 4 * 0x80])]

for switch in range(16):
    for placement in permutations(range(4), 4):
        s = decrypt(deepcopy(pixels), switch, placement)
        decrypted = s.decode("utf-8", errors="ignore")
        if all(c in base64_chars for c in decrypted):
            print(f"Switch: {switch:04b}, Placement: {placement}")
            print(f"  Decrypted: {decrypted}")
            if len(decrypted) % 4 == 0:
                flag = b64decode(decrypted).decode("utf-8", errors="ignore")
                print(f"       Flag: {flag}")
            break
