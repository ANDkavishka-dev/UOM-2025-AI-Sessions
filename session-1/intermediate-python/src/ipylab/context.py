from contextlib import contextmanager
import time
import logging
from typing import Iterator, Type

logger = logging.getLogger(__name__)  # use module-level logger

@contextmanager
def timer(label: str) -> Iterator[None]:
    start = time.perf_counter()
    try:
        yield
    finally:
        elapsed_ms = (time.perf_counter() - start) * 1000
        logger.info(f"{label} took {elapsed_ms:.2f} ms")


@contextmanager
def suppress_and_log(*exc_types: Type[BaseException]) -> Iterator[None]:
    try:
        yield
    except exc_types as e:
        logger.exception(f"Suppressed exception: {e}")
