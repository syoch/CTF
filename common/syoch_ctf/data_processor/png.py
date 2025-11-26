from typing import Generator

# PNG
Pixel = tuple[int, int, int, int]
Chunk = tuple[bytes, bytes]


def read_png(png_data: bytes) -> Generator[Chunk]:
    # hdr = png_data[0:8]
    png_data = png_data[8:]

    while png_data:
        length = int.from_bytes(png_data[0:4], "big")
        name = png_data[4:8]
        png_data = png_data[8:]
        data = png_data[:length]
        png_data = png_data[length + 4 :]

        yield (name, data)


def get_pixels_left(row_data: bytes) -> Generator[Pixel]:
    current_pixel: Pixel = (0, 0, 0, 0)

    while row_data:
        current_pixel = (
            (current_pixel[0] + row_data[0]) % 0x100,
            (current_pixel[1] + row_data[1]) % 0x100,
            (current_pixel[2] + row_data[2]) % 0x100,
            (current_pixel[3] + row_data[3]) % 0x100,
        )
        row_data = row_data[4:]
        yield current_pixel
