import time
import logging
import functools
from typing import Callable, TypeVar, Optional, ParamSpec

P = ParamSpec("P")
T = TypeVar("T")

logger = logging.getLogger(__name__)

def timed(threshold_ms: Optional[float] = None):
    def decorate(fn: Callable[P, T]) -> Callable[P, T]:
        @functools.wraps(fn)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
            start = time.perf_counter()
            result = fn(*args, **kwargs)
            elapsed_ms = (time.perf_counter() - start) * 1000
            if threshold_ms is not None and elapsed_ms > threshold_ms:
                logger.warning(f"SLOW: {fn.__name__} took {elapsed_ms:.2f} ms")
            else:
                logger.info(f"{fn.__name__} took {elapsed_ms:.2f} ms")
            return result
        return wrapper
    return decorate
