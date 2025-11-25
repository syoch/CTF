import hashlib
import numpy as np
from sympy import Matrix, symbols
import gmpy2
import sys
import functools

gmpy2.get_context().precision = 1000000000
sys.set_int_max_str_digits(0)

MOD = 10**10000
N = int(2e7)
ENCRYPTED_FLAG = bytes.fromhex(
    "42cbbce1487b443de1acf4834baed794f4bbd0dfb5885e6c7ed9a3c62b"
)


@functools.cache
def m_func(i):
    if i == 0:
        return 1
    if i == 1:
        return 2
    if i == 2:
        return 3
    if i == 3:
        return 4

    return (
        55692 * m_func(i - 4)
        - 9549 * m_func(i - 3)
        + 301 * m_func(i - 2)
        + 21 * m_func(i - 1)
    )


def diag_mat_pow(D, n):
    return Matrix.diag(*[D[i, i] ** n for i in range(D.shape[0])])


def modpow(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp = exp >> 1
        base = (base * base) % mod
    return result


def prepare():
    """
    m_func を行列式で表現し、対角化して閉形式を求める
    a4 = 21 * a3 + 301 * a2 - 9549 * a1 + 55692 * a0
    a3 =  1 * a3 +   0 * a2 +    0 * a1 +     0 * a0
    a2 =  0 * a3 +   1 * a2 +    0 * a1 +     0 * a0
    a1 =  0 * a3 +   0 * a2 +    1 * a1 +     0 * a0
    """
    # m_func の漸化行列表現
    A = Matrix(
        [
            [21, 301, -9549, 55692],
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
        ]
    )
    V0 = Matrix([4, 3, 2, 1])

    print("Verifying matrix multiplication...")
    initial_v = V0
    next_v = A * initial_v
    a1_calc = next_v[3]
    a1_expected = m_func(1)
    assert a1_calc == a1_expected, f"Expected {a1_expected}, got {a1_calc}"

    print("Diagonalizing matrix...")
    print("Matrix A:")
    print(A)
    P, D = A.diagonalize()
    assert D.is_diagonal()
    assert P * D * P.inv() == A

    print("Preparing closed form expression...")
    n = symbols("n", integer=True)
    An = P * diag_mat_pow(D, n) * P.inv() * V0
    an = An[3]

    print("Verifying closed form expression...")
    assert an.subs(n, 0) == m_func(0)
    assert an.subs(n, 10) == m_func(10)
    assert an.subs(n, 100) == m_func(100)

    print("Simplifying closed form expression...")
    an = an.simplify()

    return an


def calc_cp_mod():
    # (1612*(-21)**n + 981920*12**n - 1082829*13**n + 141933*17**n)/42636
    TERMS = [
        (1612, -21),
        (981920, 12),
        (-1082829, 13),
        (141933, 17),
    ]
    DIVIDER = 42636
    WORK_MOD = MOD * DIVIDER

    numer = 0
    for coeff, base in TERMS:
        print(f"Calculating term for base {base}...")
        term = coeff * modpow(base, N, WORK_MOD)
        numer = (numer + term) % WORK_MOD

    if numer % DIVIDER != 0:
        print("Warning: numer is not divisible by DIVIDER")

    print("division...")
    numer //= DIVIDER

    print("modulo...")
    return numer % MOD


def main():
    # an = prepare()
    # print("an =", an)
    # print("an =", an.factor())
    # exit(0)

    print("N =", N)

    sol = calc_cp_mod()

    sol = sol % MOD
    sol = str(sol)
    sol_md5 = hashlib.md5(sol.encode()).hexdigest()
    sol_sha256 = hashlib.sha256(sol.encode()).hexdigest()

    print("sol_md5:", sol_md5)
    print("sol_sha256:", sol_sha256)

    key = hashlib.sha256(sol.encode()).digest()
    flag = bytearray([char ^ key[i] for i, char in enumerate(ENCRYPTED_FLAG)]).decode()

    print(flag)


if __name__ == "__main__":
    main()
