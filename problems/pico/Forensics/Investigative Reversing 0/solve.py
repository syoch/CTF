with open("mystery.png", "rb") as f:
    data = f.read()

flag_encrypted = data[-26:]
assert len(flag_encrypted) == 26

# [0, 5]: +0
# [6, 14]: +5
# [15]: -3
# [16, 25]: +0
flag_decrypted = bytearray(26)
for i in range(0, 6):
    flag_decrypted[i] = flag_encrypted[i]
for i in range(6, 15):
    flag_decrypted[i] = flag_encrypted[i] - 5
flag_decrypted[15] = flag_encrypted[15] + 3
for i in range(16, 26):
    flag_decrypted[i] = flag_encrypted[i]

print(flag_decrypted.decode())
