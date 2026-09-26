from Crypto.Util.number import long_to_bytes
from Crypto.Cipher import AES
from sage.all import (
    GF,
    PolynomialRing,
    prod,
    Matrix,
    block_matrix,
    vector,
    ZZ,
    identity_matrix,
    zero_matrix,
    QQ,
)


BOUND = 2**256


def load_params():
    with open("output.txt", "r") as f:
        content = f.read().splitlines()
        p: int = eval(content[0].split(" = ")[1])
        pairs: list[tuple[int, int]] = eval(content[1].split(" = ")[1])
        enc_flag: tuple[str, str] = eval(content[2].split(" = ")[1])

    return p, pairs, enc_flag


def coeff_vec(fp, poly, n: int):
    cs = poly.list()  # low -> high
    cs += [fp(0)] * (n - len(cs))
    return [ZZ(int(c)) for c in cs[:n]]


def normalize_coefficient(c: int, p: int) -> int:
    candidates = [ZZ(c), ZZ(c) + ZZ(p), ZZ(c) - ZZ(p)]

    in_range = [x for x in candidates if 0 <= x < BOUND]
    if len(in_range) == 1:
        return in_range[0]

    if len(in_range) > 1:
        return min(in_range, key=lambda x: abs(x))

    return min(candidates, key=lambda x: abs(x))


def solve_master_key(p: int, pairs: list[tuple[int, int]], W: int):
    fp = GF(p)
    R = PolynomialRing(fp, "x")
    x = R.gen()

    pts = [(fp(x), fp(y)) for x, y in pairs]
    g = R.lagrange_polynomial(pts)

    z = prod([x - xn for xn, _ in pts])

    basis_polys = [z * (x**k) for k in range(10)]
    z_cols = [coeff_vec(fp, bp, 30) for bp in basis_polys]
    z_mat = Matrix(ZZ, 30, 10, lambda i, j: z_cols[j][i])

    M = block_matrix(
        ZZ,
        [
            [p * identity_matrix(ZZ, 30), zero_matrix(ZZ, 30, 10)],
            [-z_mat.transpose(), W * identity_matrix(ZZ, 10)],
        ],
    )
    B = Matrix(ZZ, M).LLL()
    g_vec = coeff_vec(fp, g, 30)
    t = vector(ZZ, g_vec + [0] * 10)

    gso, _ = B.gram_schmidt()
    y = vector(QQ, t)
    coeffs = [0] * B.nrows()

    for i in reversed(range(B.nrows())):
        ci = (y * gso[i]) / (gso[i] * gso[i])
        coeffs[i] = ZZ(round(ci))
        y -= coeffs[i] * B[i]

    closest = sum(coeffs[i] * B[i] for i in range(B.nrows()))
    residual = t - closest
    a_candidate = [normalize_coefficient(x, p) for x in residual[:30]]
    print(residual)

    if not all(0 <= c < 2**256 for c in a_candidate):
        raise ValueError("Failed to find a valid candidate")

    coeffs_horner = list(reversed(a_candidate))  # high -> low
    master_key_int = coeffs_horner[0]
    master_key = long_to_bytes(master_key_int).rjust(32, b"\x00")
    print(f"Candidate master key: {master_key.hex()}")

    return master_key


def solve():
    p, pairs, enc_flag = load_params()
    master_key = b""

    for w_shift in range(240, 280):
        print(f"Trying W=2**{w_shift}...")
        try:
            master_key = solve_master_key(p, pairs, W=2**w_shift)
            print(f"Master key found: {master_key.hex()}")
            break
        except ValueError:
            continue
    if not master_key:
        print("Failed to find a valid master key")
        return

    iv = bytes.fromhex(enc_flag[0])
    enc = bytes.fromhex(enc_flag[1])
    cipher = AES.new(master_key, AES.MODE_CBC, iv)
    flag = cipher.decrypt(enc)
    print(flag)


if __name__ == "__main__":
    solve()
