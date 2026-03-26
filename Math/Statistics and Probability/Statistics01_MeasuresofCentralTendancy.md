<div align="center">

# <span style="color:#0A2FA8">Measures of Central Tendency</span>

<sub>Complete notes covering Mean, Median, and Mode - with formulas, comparisons, and examples</sub>

</div>

---

## <span style="color:#1565C0">1. What is Central Tendency?</span>

> **Definition:** A measure of central tendency is a single value that attempts to describe a dataset by identifying the central position within that dataset. It shows the "average" or most representative value of a set of numbers.

The three main measures are:
- **Mean** - the arithmetic average
- **Median** - the middle value
- **Mode** - the most frequently occurring value

---

## <span style="color:#1565C0">2. Mean</span>

> **Definition:** Mean is the average of all values in a dataset. It is calculated by summing all observations and dividing by the count.

### <span style="color:#2E86AB">2.1 Formula</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">Mean = (x₁ + x₂ + x₃ + ... + xₙ) / n</span>

</div>

### <span style="color:#2E86AB">2.2 Population vs Sample</span>

| Property | Population | Sample |
|:---|:---:|:---:|
| Count | N | n |
| Mean symbol | μ (mu) | x̄ (x-bar) |
| Variance | σ² | s² |
| Std. Deviation | σ | s |

### <span style="color:#2E86AB">2.3 Key Properties</span>

- Uses **all** data values in the calculation
- Highly sensitive to **outliers** (extreme values)
- Mean is **highly affected** by skewed data
- Best used when data is **normally distributed**

### <span style="color:#2E86AB">2.4 Example (Raw Data)</span>

Dataset: `{5, 5, 2, 4, 5, 5, 2}`

```
Sum = 5 + 5 + 2 + 4 + 5 + 5 + 2 = 28
n   = 7
Mean = 28 / 7 = 4
```

### <span style="color:#2E86AB">2.5 Mean for Frequency Distribution (Grouped Data)</span>

> **Definition:** When data is given as a frequency table (each value xᵢ with its frequency fᵢ), the mean is calculated using the weighted formula below.

> Where **N = f₁ + f₂ + ··· + fₙ** = total of all frequencies

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 520px;">

### <span style="color:#D4A017">x̄ = (x₁f₁ + x₂f₂ + ··· + xₙfₙ) / N = (1/N) Σᵢ xᵢfᵢ</span>

</div>

#### <span style="color:#5B8DB8">How it works:</span>
- Each value `xᵢ` is **multiplied by its frequency** `fᵢ` - giving it a "weight" proportional to how often it occurs
- All these weighted values are summed and divided by the **total frequency N**
- This is essentially the same as adding every individual data point, but in a compact form

#### <span style="color:#5B8DB8">Example - Frequency Distribution Mean</span>

| Value (xᵢ) | Frequency (fᵢ) | xᵢ × fᵢ |
|:---:|:---:|:---:|
| 10 | 3 | 30 |
| 20 | 5 | 100 |
| 30 | 2 | 60 |
| 40 | 4 | 160 |
| 50 | 1 | 50 |
| **Total** | **N = 15** | **Σxᵢfᵢ = 400** |

```
x̄ = Σxᵢfᵢ / N
x̄ = 400 / 15
x̄ = 26.67
```

> The mean score from the frequency table is **26.67**.

---

## <span style="color:#1565C0">3. Median</span>

> **Definition:** Median is the middle value in a sorted (ascending or descending) dataset. It divides the data into two equal halves.

### <span style="color:#2E86AB">3.1 How to Find the Median</span>

**Step 1:** Sort the data in ascending order.
**Step 2:** Apply the appropriate formula based on whether n is odd or even.

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">If n is ODD → Median = value at position ((n+1)/2)</span>

</div>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">If n is EVEN → Median = average of values at positions (n/2) and (n/2 + 1)</span>

</div>

### <span style="color:#2E86AB">3.2 Cases</span>

#### <span style="color:#5B8DB8">Case 1 - n is Odd</span>

- Median = **middle value** (single value)

**Example:** Dataset (sorted): `{2, 4, 5, 5, 5, 5, 2}` → sorted: `{2, 2, 4, 5, 5, 5, 5}`
```
n = 7 (odd)
Position = (7+1)/2 = 4th value
Median = 5
```

#### <span style="color:#5B8DB8">Case 2 - n is Even</span>

- Median = **average of the two middle values**

**Example:** Dataset: `{2, 3, 4, 5, 5, 2}` → sorted: `{2, 2, 3, 4, 5, 5}`
```
n = 6 (even)
Middle positions = 3rd and 4th → values: 3 and 4
Median = (3 + 4) / 2 = 3.5
```

### <span style="color:#2E86AB">3.3 Key Properties</span>

- **Not affected by outliers** - only depends on the middle value(s)
- Best measure for **skewed distributions**
- Used for **ordinal data** (ranked data)
- Median is the value at the **50th percentile**

### <span style="color:#2E86AB">3.4 Median for Grouped / Continuous Data</span>

> When data is presented as a grouped frequency distribution (class intervals), we cannot directly identify a single middle value. Instead, we use the **interpolation formula**.

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 520px;">

### <span style="color:#D4A017">Median = l + (h/f) × (N/2 − fc)</span>

</div>

#### <span style="color:#5B8DB8">Variables explained:</span>

| Symbol | Meaning |
|:---:|:---|
| `l` | Lower limit (lower boundary) of the **median class** |
| `h` | Class width (size of the interval) |
| `f` | Frequency of the **median class** |
| `N` | Total frequency (sum of all frequencies) |
| `fc` | Cumulative frequency of the class **preceding** the median class |

#### <span style="color:#5B8DB8">Steps to find grouped Median:</span>

```
Step 1: Find N/2 (half of total frequency)
Step 2: Build a cumulative frequency (CF) column
Step 3: Find the class where CF first exceeds N/2 → this is the MEDIAN CLASS
Step 4: Note l, h, f, fc for the median class
Step 5: Apply the formula: Median = l + (h/f) × (N/2 − fc)
```

#### <span style="color:#5B8DB8">Example - Grouped Median</span>

| Class Interval | Frequency (f) | Cumulative Frequency (CF) |
|:---:|:---:|:---:|
| 0 – 10 | 5 | 5 |
| 10 – 20 | 8 | 13 |
| 20 – 30 | 12 | 25 |
| 30 – 40 | 10 | 35 |
| 40 – 50 | 5 | 40 |
| **Total** | **N = 40** | |

```
Step 1: N/2 = 40/2 = 20

Step 2: Find where CF first exceeds 20
        CF of 20–30 class = 25 → first CF ≥ 20 → MEDIAN CLASS = 20–30

Step 3: Identify values:
        l  = 20   (lower boundary of median class)
        h  = 10   (class width = 30 − 20)
        f  = 12   (frequency of median class)
        fc = 13   (CF of class BEFORE median class, i.e., 10–20)

Step 4: Apply formula:
        Median = l + (h/f) × (N/2 − fc)
        Median = 20 + (10/12) × (20 − 13)
        Median = 20 + (10/12) × 7
        Median = 20 + 5.83
        Median ≈ 25.83
```

> The median of this grouped dataset is approximately **25.83**.

### <span style="color:#2E86AB">3.5 Real-World Example from Notes</span>

> Placement CTC for 10 students in a class: `{5, 5, 2, 4, 5, 5, 2}` - mean = 45/10 = 4.5 LPA
> Mean is **not the best** measure here if there are outliers. Median would be more representative.

---

## <span style="color:#1565C0">4. Mode</span>

> **Definition:** Mode is the value that appears **most frequently** in a dataset. It is the only measure of central tendency that can be used with **categorical (nominal) data**.

### <span style="color:#2E86AB">4.1 Key Properties</span>

- A dataset can have **no mode**, **one mode (unimodal)**, or **multiple modes (bimodal / multimodal)**
- Not affected by extreme values
- Useful for identifying the most common/popular value
- Best for **categorical data** (e.g., most common eye color, most sold product)

### <span style="color:#2E86AB">4.2 Cases</span>

| Case | Description | Example |
|:---|:---|:---|
| No mode | No number repeats | `{1, 2, 4, 6, 8}` → no mode |
| One mode | One value repeats most | `{1, 2, 2, 3, 5}` → mode = 2 |
| Two modes (bimodal) | Two values repeat equally | `{1, 1, 2, 3, 3}` → modes = 1, 3 |
| Multimodal | More than two modes | `{1, 1, 2, 2, 3, 3}` → modes = 1, 2, 3 |

### <span style="color:#2E86AB">4.3 Example</span>

Dataset: `{2, 3, 5, 2, 9}`

```
Count of each value:
  2 → appears 2 times  ← most frequent
  3 → appears 1 time
  5 → appears 1 time
  9 → appears 1 time

Mode = 3  (appears 3 times - i.e., 3 times repeated)
```

> From notes example: `{2, 3, 5, 2, 9}` → mode = **3** (3 times repeated, making 3 the most frequent)

### <span style="color:#2E86AB">4.4 Mode for Grouped / Continuous Data</span>

> When data is in grouped form (class intervals), mode is estimated using the **interpolation formula** based on surrounding class frequencies.

> **Modal Class** = the class interval with the **highest frequency**

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 540px;">

### <span style="color:#D4A017">Mode = L + [ (f₁ − f₀) / (2f₁ − f₀ − f₂) ] × h</span>

</div>

#### <span style="color:#5B8DB8">Variables explained:</span>

| Symbol | Meaning |
|:---:|:---|
| `L` | Lower limit of the **modal class** |
| `f₁` | Frequency of the **modal class** (highest frequency) |
| `f₀` | Frequency of the class **before** the modal class |
| `f₂` | Frequency of the class **after** the modal class |
| `h` | Class width |

#### <span style="color:#5B8DB8">Steps to find grouped Mode:</span>

```
Step 1: Find the class with the HIGHEST frequency → Modal Class
Step 2: Note L, f₁, f₀, f₂, and h
Step 3: Apply the formula: Mode = L + [(f₁ − f₀) / (2f₁ − f₀ − f₂)] × h
```

#### <span style="color:#5B8DB8">Example - Grouped Mode</span>

| Class Interval | Frequency (f) |
|:---:|:---:|
| 0 – 10 | 4 |
| 10 – 20 | 7 |
| 20 – 30 | **15** ← highest |
| 30 – 40 | 9 |
| 40 – 50 | 5 |

```
Step 1: Modal Class = 20–30 (highest frequency = 15)

Step 2: Identify values:
        L  = 20   (lower boundary of modal class)
        f₁ = 15   (frequency of modal class)
        f₀ = 7    (frequency of class BEFORE → 10–20)
        f₂ = 9    (frequency of class AFTER  → 30–40)
        h  = 10   (class width)

Step 3: Apply formula:
        Mode = L + [(f₁ − f₀) / (2f₁ − f₀ − f₂)] × h
        Mode = 20 + [(15 − 7) / (2×15 − 7 − 9)] × 10
        Mode = 20 + [8 / (30 − 7 − 9)] × 10
        Mode = 20 + [8 / 14] × 10
        Mode = 20 + 5.71
        Mode ≈ 25.71
```

> The mode of this grouped dataset is approximately **25.71**.

---

| Feature | Mean | Median | Mode |
|:---|:---:|:---:|:---:|
| Definition | Average of all values | Middle value (sorted) | Most frequent value |
| Formula needed | Yes | Yes | No (just count) |
| Affected by outliers | <span style="color:#C0392B">Yes - highly</span> | <span style="color:#27AE60">No</span> | <span style="color:#27AE60">No</span> |
| Works with categorical data | No | No | <span style="color:#27AE60">Yes</span> |
| Unique value always? | Yes | Yes | Not always |
| Best for | Symmetric data | Skewed data | Categorical / frequency data |
| Uses all data points | <span style="color:#27AE60">Yes</span> | <span style="color:#C0392B">No</span> | <span style="color:#C0392B">No</span> |

---

## <span style="color:#1565C0">6. When to Use Which?</span>

### <span style="color:#2E86AB">Use Mean when:</span>
- Data is **symmetrically distributed** (no extreme outliers)
- You need to use **all data values** in the calculation
- Performing further **statistical calculations** (variance, SD)

### <span style="color:#2E86AB">Use Median when:</span>
- Data is **skewed** (income, house prices, placement CTCs)
- There are **outliers** that would distort the mean
- Dealing with **ordinal data** (rankings)

### <span style="color:#2E86AB">Use Mode when:</span>
- Dealing with **categorical/nominal data** (colors, brands, names)
- You want the **most common** value in a dataset
- Data has **no meaningful arithmetic average** (e.g., most popular shirt size)

---

## <span style="color:#1565C0">7. Quick Reference - All Formulas</span>

### <span style="color:#2E86AB">Mean</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 560px;">

### <span style="color:#D4A017">Raw Data:   x̄ = Σxᵢ / n</span>

### <span style="color:#D4A017">Freq. Data: x̄ = (1/N) Σ xᵢfᵢ</span>

</div>

### <span style="color:#2E86AB">Median</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 560px;">

### <span style="color:#D4A017">Raw (odd n):   Median = x at position (n+1)/2</span>

### <span style="color:#D4A017">Raw (even n):  Median = [ x(n/2) + x(n/2+1) ] / 2</span>

### <span style="color:#D4A017">Grouped:       Median = l + (h/f) × (N/2 − fc)</span>

</div>

### <span style="color:#2E86AB">Mode</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 560px;">

### <span style="color:#D4A017">Raw Data: Mode = most frequent value</span>

### <span style="color:#D4A017">Grouped:  Mode = L + [(f₁ − f₀) / (2f₁ − f₀ − f₂)] × h</span>

</div>

---

## <span style="color:#1565C0">8. Raw Data vs Grouped Data - Formula Comparison</span>

| Measure | Raw Data | Grouped / Frequency Data |
|:---|:---|:---|
| **Mean** | Σxᵢ / n | (1/N) Σ xᵢfᵢ |
| **Median** | Middle value after sorting | l + (h/f)(N/2 − fc) |
| **Mode** | Most repeated value | L + [(f₁−f₀)/(2f₁−f₀−f₂)] × h |
| **When used** | Small, individual datasets | Frequency tables / class intervals |

---

## <span style="color:#1565C0">9. Population vs Sample Notation (Extended)</span>

> **Population:** Entire group being studied. Count = **N**, Mean = **μ**, Variance = **σ²**, Std. Dev = **σ**

> **Sample:** A subset drawn from the population. Count = **n**, Mean = **x̄**, Variance = **s²**, Std. Dev = **s**

| Notation | Population | Sample |
|:---|:---:|:---:|
| Count | N | n |
| Mean | μ | x̄ |
| Variance | σ² | s² |
| Std. Deviation | σ | s |


---

<div align="center">

<sub>These notes were written and compiled by</sub>

### **Sagar Bhadra**

<sub>Connect with me on</sub>

<br>

[![GitHub](https://img.shields.io/badge/GitHub-SagarBhadra01-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/SagarBhadra01)&nbsp;
[![X (Twitter)](https://img.shields.io/badge/Twitter-SagarBhadra01-000000?style=for-the-badge&logo=x&logoColor=white)](https://x.com/SagarBhadra01)&nbsp;
[![LinkedIn](https://img.shields.io/badge/LinkedIn-sagarbhadra01-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/sagarbhadra01)&nbsp;
[![Gmail](https://img.shields.io/badge/Gmail-sagarbhadra404@gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:sagarbhadra404@gmail.com)

</div>