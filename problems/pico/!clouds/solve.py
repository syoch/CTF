from z3 import *
import random

# --- 設定 ---
N = 64
MASK = (1 << N) - 1


def bit_rev_int(x, n=N):
    b = bin(x)[2:].zfill(n)
    return int(b[::-1], 2)


# --- Z3 実装 ---


def z3_bit_rev(x, n=N):
    return Concat(*[Extract(i, i, x) for i in range(n)])


# 新しい定義に基づく Z3 の R 関数
def R_z3(x, k, n=N):
    # 1. XOR
    val = x ^ k
    # 2. Bit Reverse
    val = z3_bit_rev(val, n)
    # 3. Multiply by (k | 1)
    val = val * (k | 1)
    return val


def solve_with_differential():
    s = Solver()
    keys = [BitVec(f"k_{i}", N) for i in range(5)]

    print("[*] Generating Differential Pairs (LSB flip)...")

    known_pairs = [
        (0x0000000000000000, 0x97F464B12ECC0DBB),
        (0x0000000000000001, 0xB18492CCC7E9E27D),
        (0x0000000000000002, 0x762230E5218CC02B),
        (0x0000000000000003, 0x233AC8A1D24189C8),
    ]

    for x_in, y_out in known_pairs:
        val = BitVecVal(x_in, N)
        for k in keys:
            val = R_z3(val, k, N)
        s.add(val == BitVecVal(y_out, N))

    print("[*] Solving...")
    set_param("parallel.enable", True)
    set_param("parallel.threads.max", 6)
    if s.check() == sat:
        print("[!] SAT! Model found.")
        m = s.model()
        rec_keys = [m[keys[i]].as_long() for i in range(5)]
        return rec_keys
    else:
        print("[x] UNSAT")
        return None


# --- 逆算 (Decrypt) ---


def modinv(a, m=1 << N):
    return pow(a, -1, m)


def R_inv(y, k, n=N):
    # y = bit_rev(x ^ k) * (k | 1)
    # let M = (k | 1)
    # y * M^-1 = bit_rev(x ^ k)
    # bit_rev(y * M^-1) = x ^ k
    # x = bit_rev(y * M^-1) ^ k

    multiplier = k | 1
    inv_mult = modinv(multiplier, 1 << n)

    val = (y * inv_mult) & MASK
    val = bit_rev_int(val, n)
    x = val ^ k
    return x


# --- 実行 ---
rec_keys = solve_with_differential()

if rec_keys:
    print(f"Recovered Keys: {rec_keys}")
    print(f"True Keys:      {TRUE_KEYS}")

    # 検証: ターゲットの値から逆算
    target_x = 0x123456789ABC
    target_y = F_oracle(target_x)

    print(f"\nTarget y: {hex(target_y)}")

    # 復号プロセス
    val = target_y
    for k in reversed(rec_keys):
        val = R_inv(val, k)

    print(f"Decrypted x: {hex(val)}")
    print(f"Original  x: {hex(target_x)}")

    if val == target_x:
        print("SUCCESS")
    else:
        print("FAIL")
