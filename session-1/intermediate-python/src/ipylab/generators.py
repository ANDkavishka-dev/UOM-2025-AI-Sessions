from collections import deque
from statistics import median
from typing import Iterable, Iterator, TypeVar, Deque, Optional

T = TypeVar("T", int, float)

def chunks(iterable: Iterable[T], size: int) -> Iterator[list[T]]:
    buffer = []
    for item in iterable:
        buffer.append(item)
        if len(buffer) == size:
            yield buffer
            buffer = []
    if buffer:
        yield buffer

def moving_average(window: int) -> Iterator[float]:
    data: Deque[float] = deque(maxlen=window)
    value: Optional[float] = yield
    while True:
        data.append(value)
        value = yield sum(data) / len(data)

def moving_median(window: int) -> Iterator[float]:
    data: Deque[float] = deque(maxlen=window)
    value: Optional[float] = yield
    while True:
        data.append(value)
        value = yield median(data)
