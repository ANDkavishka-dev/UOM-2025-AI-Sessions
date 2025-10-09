import statistics

# Save original median function (just in case we need it)
_original_median = statistics.median

def moving_median(data, window_size):
    """Return list of moving medians for given data and window size."""
    if window_size <= 0:
        raise ValueError("Window size must be positive")
    if window_size > len(data):
        raise ValueError("Window size cannot be larger than data length")
    
    medians = []
    for i in range(len(data) - window_size + 1):
        window = data[i:i + window_size]
        medians.append(_original_median(window))
    return medians

# Override statistics.median
statistics.median = moving_median

# Example usage
data = [5, 2, 8, 1, 7, 3, 9]
print(statistics.median(data, 3))  # moving median with window size 3