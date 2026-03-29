import math
import statistics


# ── MEAN ──────────────────────────────────────────────────────────────────────

def mean(data):
    return sum(data) / len(data)


# ── RANGE ─────────────────────────────────────────────────────────────────────

def data_range(data):
    return max(data) - min(data)


# ── VARIANCE ──────────────────────────────────────────────────────────────────

def population_variance(data):
    mu = mean(data)
    return sum((x - mu) ** 2 for x in data) / len(data)

def sample_variance(data):
    x_bar = mean(data)
    return sum((x - x_bar) ** 2 for x in data) / (len(data) - 1)


# ── STANDARD DEVIATION ────────────────────────────────────────────────────────

def population_std(data):
    return math.sqrt(population_variance(data))

def sample_std(data):
    return math.sqrt(sample_variance(data))


# ── QUARTILES & IQR ───────────────────────────────────────────────────────────

def quartiles(data):
    data = sorted(data)
    n = len(data)
    mid = n // 2
    q2 = statistics.median(data)
    lower = data[:mid]
    upper = data[mid + 1:] if n % 2 != 0 else data[mid:]
    return statistics.median(lower), q2, statistics.median(upper)

def iqr(data):
    q1, _, q3 = quartiles(data)
    return q3 - q1

def outlier_fences(data):
    q1, _, q3 = quartiles(data)
    iq = q3 - q1
    return q1 - 1.5 * iq, q3 + 1.5 * iq

def outliers(data):
    lf, uf = outlier_fences(data)
    return [x for x in data if x < lf or x > uf]


# ── GROUPED DATA ──────────────────────────────────────────────────────────────

def grouped_mean(midpoints, frequencies):
    return sum(m * f for m, f in zip(midpoints, frequencies)) / sum(frequencies)

def grouped_population_variance(midpoints, frequencies):
    mu = grouped_mean(midpoints, frequencies)
    total = sum(frequencies)
    return sum(f * (m - mu) ** 2 for m, f in zip(midpoints, frequencies)) / total

def grouped_sample_variance(midpoints, frequencies):
    mu = grouped_mean(midpoints, frequencies)
    total = sum(frequencies)
    return sum(f * (m - mu) ** 2 for m, f in zip(midpoints, frequencies)) / (total - 1)

def grouped_population_std(midpoints, frequencies):
    return math.sqrt(grouped_population_variance(midpoints, frequencies))

def grouped_sample_std(midpoints, frequencies):
    return math.sqrt(grouped_sample_variance(midpoints, frequencies))


# ── FULL REPORT ───────────────────────────────────────────────────────────────

def report(data, label="Data"):
    q1, q2, q3 = quartiles(data)
    lf, uf = outlier_fences(data)
    out = outliers(data)

    print(f"\n{'='*50}")
    print(f"  {label}")
    print(f"  Data: {sorted(data)}")
    print(f"{'='*50}")
    print(f"  Mean              : {round(mean(data), 4)}")
    print(f"  Range             : {round(data_range(data), 4)}")
    print(f"  Pop. Variance     : {round(population_variance(data), 4)}")
    print(f"  Sample Variance   : {round(sample_variance(data), 4)}")
    print(f"  Pop. Std Dev      : {round(population_std(data), 4)}")
    print(f"  Sample Std Dev    : {round(sample_std(data), 4)}")
    print(f"  Q1 / Q2 / Q3      : {q1} / {q2} / {q3}")
    print(f"  IQR               : {round(iqr(data), 4)}")
    print(f"  Outlier Fences    : [{round(lf,2)}, {round(uf,2)}]")
    print(f"  Outliers          : {out if out else 'None'}")
    print(f"{'='*50}")


def grouped_report(midpoints, frequencies, label="Grouped Data"):
    print(f"\n{'='*50}")
    print(f"  {label}")
    print(f"  Midpoints   : {midpoints}")
    print(f"  Frequencies : {frequencies}")
    print(f"{'='*50}")
    print(f"  Mean              : {round(grouped_mean(midpoints, frequencies), 4)}")
    print(f"  Pop. Variance     : {round(grouped_population_variance(midpoints, frequencies), 4)}")
    print(f"  Sample Variance   : {round(grouped_sample_variance(midpoints, frequencies), 4)}")
    print(f"  Pop. Std Dev      : {round(grouped_population_std(midpoints, frequencies), 4)}")
    print(f"  Sample Std Dev    : {round(grouped_sample_std(midpoints, frequencies), 4)}")
    print(f"{'='*50}")


# ── CASES ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":

    # Case 1: Symmetric data (from notes)
    report([-15, -10, 0, 10, 15], "Case 1: Symmetric")

    # Case 2: Positively skewed
    report([2, 3, 5, 7, 8, 10, 45], "Case 2: Positively Skewed")

    # Case 3: Negatively skewed
    report([-40, 10, 15, 18, 20, 22, 25], "Case 3: Negatively Skewed")

    # Case 4: With outliers
    report([10, 12, 13, 14, 15, 16, 17, 18, 20, 95], "Case 4: With Outlier")

    # Case 5: All same values (zero spread)
    report([7, 7, 7, 7, 7], "Case 5: Zero Spread")

    # Case 6: Large dataset
    report([4, 8, 15, 16, 23, 42, 55, 60, 72, 88, 91, 100], "Case 6: Large Dataset")

    # Case 7: Grouped frequency distribution
    grouped_report([5, 15, 25, 35, 45], [3, 7, 12, 8, 5], "Case 7: Grouped Data")