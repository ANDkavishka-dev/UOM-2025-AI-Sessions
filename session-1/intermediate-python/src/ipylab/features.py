import numpy as np

def feature_vector(x: np.ndarray) -> list[float]:
    rms = np.sqrt(np.mean(x**2))
    zc = np.sum((x[:-1] * x[1:]) < 0)
    p2p = np.max(x) - np.min(x)
    mad = np.mean(np.abs(np.diff(x)))
    return [rms, zc, p2p, mad]
