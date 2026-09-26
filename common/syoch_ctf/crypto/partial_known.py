from sage.all import var
import cuso


def find_partial_known_roots(
    parts: list[tuple[int, int]],
    known: int,
    modulo: int,
):
    """有限体上での部分的に既知の整数の小さな根を見つける
    この関数は以下の方程式の解を見つけ、それを返却する
        known + sum(x_i * 2^(8 * offset_i)) ≡ 0 (mod modulo)

    Args:
        parts (list[tuple[int, int]]): 既知の整数の部分的な情報 [(offset, size), ...]
        known (int): 既知の整数
        modulo (int): モジュロ

    Returns:
        list[dict]: 既知の整数の部分的な情報に基づく 既知の整数の小さな根のリスト
    """
    unknown_vars = [var(f"x{i}") for i in range(len(parts))]
    recovered = known + sum(
        v * 2 ** (8 * _offset) for (v, (_offset, _)) in zip(unknown_vars, parts)
    )
    bounds = {v: (0, 2 ** (8 * size)) for (v, (_, size)) in zip(unknown_vars, parts)}

    sol = cuso.find_small_roots(
        [recovered],
        bounds=bounds,
        modulus="p",
        modulus_multiple=modulo,
        modulus_lower_bound=2**255,
    )

    return sol
