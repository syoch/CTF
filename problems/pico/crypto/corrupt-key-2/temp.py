from syoch_ctf.data_processor.parse_hex_string import parse_hex_string_as_int
from syoch_ctf.crypto.partial_known import find_partial_known_roots

N = parse_hex_string_as_int(
    """
    9500F77C BF15DE1C 0296013A 2D27975A
    C5207D5A 20517756 97528AE3 654C73A2
    67669C3D 9BE3F8DC E6F3CB54 58C499AD
    94EC2B31 761BA85C 0F9A9B54 45FA0C87
"""
)

# b378d7b6 1301606d 922af86c 8886f3ea
# 0013d3ff c316678a e7d3f046 69abc8dd
PARTIAL_P = parse_hex_string_as_int(
    """
    b378d7b6 1301606d 00000000 8886f3ea
    0013d3ff c316678a e7d3f046 00000000
"""
)
PARTS = [
    (20, 4),
    (9, 4),
]

roots = find_partial_known_roots(PARTS, PARTIAL_P, N)
assert len(roots) > 0
p = roots[0]["p"]
assert N % p == 0
print(f"Recovered factor p = {p}")
# 81177510328354442902688041675720469564050848088811991739209309032920900159709
