"""
CompareCards: 0x00102a20

0x0000555555556aa6: 00102aa6 (@Random::Random)

b: 00102ab0 (rdi: this)
"""


class Random:
    def __init__(self, first_random: int):
        # 初期化
        self.mul = 0x7777724E
        self.add = 2021
        self.range = 0x7FFFFFFF
        self.last_random = first_random

    def get_random(self) -> int:
        value = self.last_random
        value = (value * self.mul) & 0xFFFFFFFF
        value = (value + self.add) & 0xFFFFFFFF
        value %= self.range
        self.last_random = value
        print(f"Random generated: {value}")
        return value


def int_to_card(x: int) -> str:
    # 整数をカードに変換
    suit = x // 13
    rank = x % 13

    c = "shcd"[suit]
    r = "A23456789XJQK"[rank]

    return f"{c}{r}"


cpu_choice = [*range(52)]
random = Random(first_random=0x6C9DC233)

i = 51
while i != 0:
    rand = random.get_random()  # Randomクラスのget_randomメソッドを呼び出し
    j = (rand & 0xFFFFFFFF) % (i + 1)  # jを計算
    # カードを交換
    tmp = cpu_choice[i]
    cpu_choice[i] = cpu_choice[j]
    cpu_choice[j] = tmp
    i -= 1

s = [int_to_card(cpu_choice[i]) for i in range(52)]
print(" ".join(s))
