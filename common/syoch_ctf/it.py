from typing import Generator, TypeVar

T = TypeVar("T")


def it(x: tuple[T]) -> Generator[T, None, None]:
    for item in x:
        yield item
