#!/usr/bin/env python3
import struct


def uuid_to_bytes(uuid_str):
    hex_str = uuid_str.replace("-", "")

    data1 = struct.pack("<I", int(hex_str[0:8], 16))
    data2 = struct.pack("<H", int(hex_str[8:12], 16))
    data3 = struct.pack("<H", int(hex_str[12:16], 16))
    data4 = bytes.fromhex(hex_str[16:32])

    return data1 + data2 + data3 + data4


with open("sh.txt", "r") as f:
    uuid_lines = [line.strip() for line in f if line.strip()]

shellcode_bytes = b""
for uuid_str in uuid_lines:
    shellcode_bytes += uuid_to_bytes(uuid_str)

with open("shellcode.bin", "wb") as f:
    f.write(shellcode_bytes)
