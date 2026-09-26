def continued_fraction(numer: int, denom: int):
    """分数を連分数に展開する
    Args:
        numer (int): 分子
        denom (int): 分母
    Returns:
        list[int]: 連分数の係数のリスト

    Example:
        >>> continued_fraction(7, 3)
        [2, 3]
    """
    a = []
    while denom != 0:
        a.append(numer // denom)
        numer, denom = denom, numer % denom
    return a


def contract(a):
    """連分数を分数に縮約する
    Args:
        a (list[int]): 連分数の係数のリスト
    Returns:
        list[int]: 分数の分子と分母のリスト [numer, denom]

    Example:
        >>> contract([2, 3])
        [7, 3]
    """
    if len(a) == 1:
        return [a[0], 1]
    else:
        numerator = [a[0], a[0] * a[1] + 1]
        denominator = [1, a[1]]
        for ai in a[2:]:
            numerator[0], numerator[1] = numerator[1], ai * numerator[1] + numerator[0]
            denominator[0], denominator[1] = (
                denominator[1],
                ai * denominator[1] + denominator[0],
            )
        return [numerator[1], denominator[1]]


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Continued fraction tool")
    parser.add_argument(
        "--expand",
        help="Expand a fraction into a continued fraction with format: numer/denom",
    )
    parser.add_argument(
        "--contract",
        nargs="?",
        help="Contract a continued fraction into a fraction with format: a0,a1,a2,...",
    )
    args = parser.parse_args()

    if args.expand:
        numer, denom = map(int, args.expand.split("/"))
        cf = continued_fraction(numer, denom)
        print(f"<{', '.join(map(str, cf))}>")
    elif args.contract:
        a = list(map(int, args.contract.split(",")))
        numer, denom = contract(a)
        print(f"{numer}/{denom}")


if __name__ == "__main__":
    main()
