from typing import Generator, TypeVar

T = TypeVar("T")


def it(x: tuple[T]) -> Generator[T, None, None]:
    """
    指定されたタプルの要素を順に生成するジェネレーター
    """
    for item in x:
        yield item
