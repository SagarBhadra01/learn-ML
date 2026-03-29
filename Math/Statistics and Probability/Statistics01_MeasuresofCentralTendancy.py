# Measures of Central Tendency

# ─────────────────────────────────────────────
# MEAN
# ─────────────────────────────────────────────

def mean_raw(data):
    return sum(data) / len(data)

def mean_frequency(values, frequencies):
    N = sum(frequencies)
    return sum(x * f for x, f in zip(values, frequencies)) / N


# ─────────────────────────────────────────────
# MEDIAN
# ─────────────────────────────────────────────

def median_raw(data):
    data = sorted(data)
    n = len(data)
    mid = n // 2
    if n % 2 == 1:
        return data[mid]
    else:
        return (data[mid - 1] + data[mid]) / 2

def median_grouped(lower_bounds, upper_bounds, frequencies):
    N = sum(frequencies)
    target = N / 2
    cf = 0
    for i, f in enumerate(frequencies):
        cf += f
        if cf >= target:
            l  = lower_bounds[i]
            h  = upper_bounds[i] - lower_bounds[i]
            fc = cf - f
            return l + (h / f) * (target - fc)


# ─────────────────────────────────────────────
# MODE
# ─────────────────────────────────────────────

def mode_raw(data):
    freq = {}
    for val in data:
        freq[val] = freq.get(val, 0) + 1
    max_freq = max(freq.values())
    if max_freq == 1:
        return None  # No mode
    return [val for val, count in freq.items() if count == max_freq]

def mode_grouped(lower_bounds, upper_bounds, frequencies):
    modal_idx = frequencies.index(max(frequencies))
    L  = lower_bounds[modal_idx]
    h  = upper_bounds[modal_idx] - lower_bounds[modal_idx]
    f1 = frequencies[modal_idx]
    f0 = frequencies[modal_idx - 1] if modal_idx > 0 else 0
    f2 = frequencies[modal_idx + 1] if modal_idx < len(frequencies) - 1 else 0
    return L + ((f1 - f0) / (2 * f1 - f0 - f2)) * h


# ─────────────────────────────────────────────
# EXAMPLES
# ─────────────────────────────────────────────

# Raw data
data = [10, 20, 30, 40, 50, 20, 30, 20]
print("Mean (raw)        :", mean_raw(data))
print("Median (raw)      :", median_raw(data))
print("Mode (raw)        :", mode_raw(data))

# Frequency distribution
values      = [10, 20, 30, 40, 50]
frequencies = [3,   5,  2,  4,  1]
print("Mean (frequency)  :", mean_frequency(values, frequencies))

# Grouped data
lower  = [0,  10, 20, 30, 40]
upper  = [10, 20, 30, 40, 50]
freqs  = [5,   8, 12, 10,  5]
print("Median (grouped)  :", median_grouped(lower, upper, freqs))
print("Mode (grouped)    :", mode_grouped(lower, upper, freqs))