pairs = [
    (38, 0x7B),
    (20, 0x67),
    (46, 0x5F),
    (3, 0x21),
    (18, 0x63),
    (119, 0x6E),
    (51, 0x5F),
    (59, 0x79),
    (9, 0x34),
    (4, 0x57),
    (37, 0x35),
    (12, 0x33),
    (111, 0x62),
    (45, 0x63),
    (97, 0x7D),
    (54, 0x30),
    (112, 0x74),
    (106, 0x31),
    (43, 0x66),
    (17, 0x34),
    (98, 0x34),
    (120, 0x54),
    (25, 0x5F),
    (127, 0x6C),
    (26, 0x41),
]
stir = lambda x: (37 * (x ^ 0x5A5A) + 23) % 101

pairs = [(stir(i), v) for (i, v) in pairs]
pairs.sort(key=lambda x: x[0])

flag = "".join(chr(v) for (i, v) in pairs)
print(flag)
