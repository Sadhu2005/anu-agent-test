"""Tiny stateful helper used by integration stubs."""


class Counter:
    def __init__(self, start: int = 0) -> None:
        self.value = int(start)

    def inc(self, n: int = 1) -> int:
        self.value += int(n)
        return self.value

    def reset(self) -> None:
        self.value = 0
