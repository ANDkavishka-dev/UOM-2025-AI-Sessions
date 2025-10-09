from typing import Sequence
import numpy as np
import math

def python_rms(seq: Sequence[float]) -> float:
    """
    Compute the Root Mean Square (RMS) value of a sequence using plain Python.
    
    RMS = sqrt( (x1² + x2² + ... + xn²) / n )

    Example:
        >>> python_rms([1, 2, 3])
        2.160246899469287
    """
    # handle empty sequence safely
    if not seq:
        return 0.0

    # sum of squares
    total = 0.0
    for x in seq:
        total += x * x

    # mean of squares
    mean_square = total / len(seq)

    # square root of mean square
    rms = math.sqrt(mean_square)

    return rms

def numpy_rms(arr: np.ndarray) -> float:
    """
    Compute RMS using NumPy's vectorized operations.
    
    Example:
        >>> import numpy as np
        >>> numpy_rms(np.array([1, 2, 3]))
        2.160246899469287
    """
    if arr.size == 0:
        return 0.0

    # Elementwise square -> mean -> sqrt
    rms = np.sqrt(np.mean(arr ** 2))

    # ensure it’s a plain float (not NumPy float32/float64)
    return float(rms)
