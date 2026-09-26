import sys

data = sys.stdin.buffer.read()

content = b""
for i in range(0, len(data), 8):
    byte = data[i : i + 8]
    content += bytes([int(byte, 2)])

sys.stdout.buffer.write(content)
