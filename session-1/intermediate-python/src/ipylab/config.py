from dataclasses import dataclass

@dataclass(frozen=True)
class LabConfig:
    """
    Configuration for the lab.

    Fields:
        sample_rate: int       -> Sampling rate in Hz
        duration_s: float      -> Duration of the signal in seconds
        noise_std: float       -> Standard deviation of added noise
        median_window: int     -> Window size for moving median
        cache_size: int        -> Size for LRU cache (stretch goal)
    """

    sample_rate: int = 1000
    duration_s: float = 2.0
    noise_std: float = 0.15
    median_window: int = 11
    cache_size: int = 256
