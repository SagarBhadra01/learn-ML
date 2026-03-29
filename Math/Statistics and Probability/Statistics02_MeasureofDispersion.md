<div align="center">

# <span style="color:#0A2FA8">Measures of Dispersion</span>

<sub>A complete reference covering Range, Variance, Standard Deviation, and IQR - with formulas, derivations, examples, and use cases</sub>

</div>

---

## <span style="color:#1565C0">1. Introduction to Measures of Dispersion</span>

> **Definition:** Measures of Dispersion describe the **spread**, **scatter**, or **variability** of a dataset around a central value (mean, median, or mode).

While measures of central tendency (mean, median, mode) tell us *where* data is centered, they say nothing about how spread out the data is. Two datasets can have the same mean but very different spreads.

**Example:**
- Dataset A: `[10, 10, 10, 10, 10]` → Mean = 10, no spread
- Dataset B: `[2, 5, 10, 15, 18]` → Mean = 10, high spread

### <span style="color:#2E86AB">Why Dispersion Matters</span>

| Reason | Explanation |
|--------|-------------|
| Risk Assessment | High dispersion = high uncertainty (e.g., stock prices) |
| Quality Control | Low dispersion = consistent production |
| Comparison | Compare variability between different datasets |
| Outlier Detection | Large dispersion signals potential outliers |
| Model Building | Variance and std dev are core to ML/statistics |

### <span style="color:#2E86AB">Types of Measures</span>

| Measure | Type | Sensitive to Outliers? |
|---------|------|------------------------|
| Range | Absolute | Yes (highly) |
| Variance | Absolute | Yes |
| Standard Deviation | Absolute | Yes |
| IQR | Absolute | No (robust) |
| Coefficient of Variation | Relative | Moderate |

---

## <span style="color:#1565C0">2. Range</span>

> **Definition:** The Range is the difference between the **largest** and **smallest** values in a dataset.

### <span style="color:#2E86AB">Formula</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">Range = Max − Min</span>

</div>

### <span style="color:#2E86AB">Key Points</span>

- Simplest measure of dispersion
- Uses only two data points (max and min)
- Highly sensitive to outliers - one extreme value distorts the entire measure
- Does not consider the distribution of values between max and min
- Suitable only for quick, rough estimates of spread

### <span style="color:#2E86AB">Worked Example</span>

**Sample:** `[-15, -10, 0, 10, 15]`

```
Mean   = 0
Median = 0
Mode   = No mode (all values unique)

Range = 15 − (−15) = 30
```

### <span style="color:#2E86AB">Use Cases</span>

- Weather reports (daily temperature range)
- Sports statistics (score range across games)
- Quick quality checks in manufacturing
- First-pass data exploration

### <span style="color:#2E86AB">Limitations</span>

- Ignores all intermediate values
- A single outlier can dramatically inflate the range
- Not suitable for comparing datasets of different sizes
- Provides no information about the shape of the distribution

---

## <span style="color:#1565C0">3. Variance</span>

> **Definition:** Variance measures the **average squared distance** of each data point from the mean. It quantifies how far, on average, data points are spread from the central value.

### <span style="color:#2E86AB">Why Square the Deviations?</span>

When computing deviations from mean `(xᵢ − x̄)`:
- Positive and negative deviations cancel out → sum = 0
- Using absolute values `|xᵢ − x̄|` loses mathematical smoothness (not differentiable)
- **Squaring** solves both: eliminates negatives AND penalizes larger deviations more

```
Squaring gives smooth differentiability
Penalizes larger deviations more than smaller ones
```

### <span style="color:#2E86AB">Population vs Sample</span>

#### <span style="color:#5B8DB8">Notation</span>

| Symbol | Meaning |
|--------|---------|
| μ | Population mean |
| σ² | Population variance |
| σ | Population standard deviation |
| x̄ | Sample mean |
| s² | Sample variance |
| s | Sample standard deviation |
| N | Population size |
| n | Sample size |

#### <span style="color:#5B8DB8">Population Variance Formula</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">σ² = Σᵢ₌₁ᴺ (xᵢ − μ)² / N</span>

</div>

#### <span style="color:#5B8DB8">Sample Variance Formula</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">s² = Σᵢ₌₁ⁿ (xᵢ − x̄)² / (n − 1)</span>

</div>

### <span style="color:#2E86AB">Why (n−1) in Sample Variance? - Bessel's Correction</span>

This is one of the most important concepts in statistics.

#### <span style="color:#5B8DB8">The Problem</span>

When computing sample variance, we use **sample mean x̄** instead of the true **population mean μ**. The sample mean is computed from the same data - it is already "pulled toward" the data, making deviations appear smaller than they truly are.

```
Population mean μ is fixed (unknown)
Sample mean x̄ varies with every sample drawn
x̄ always minimizes the sum of squared deviations from the sample
→ This causes underestimation of true variance
```

#### <span style="color:#5B8DB8">Illustration</span>

**Sample:** `[-2, -1, 1, 2]` → Independent sample, x̄ = 0

If we divide by `n = 4`:  
Sum of squares = 4 + 1 + 1 + 4 = 10 → Variance = 10/4 = 2.5

If we divide by `n − 1 = 3`:  
Variance = 10/3 ≈ 3.33 (unbiased estimate)

#### <span style="color:#5B8DB8">The Statistical Reason</span>

> **Degrees of Freedom:** Once we fix the sample mean and know `(n−1)` values, the last value is determined. So we only have `(n−1)` free (independent) pieces of information.

Our goal when computing s²:

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">E[s²] = σ²</span>

</div>

Dividing by `(n−1)` makes sample variance an **unbiased estimator** of population variance.

#### <span style="color:#5B8DB8">Why Sample Mean ≠ Population Mean Causes Bias</span>

```
Case 1: x̄ = μ  →  s² ≠ σ² (rare)
Case 2: x̄ < μ  →  Σ(xᵢ − x̄)² / n  <  Σ(xᵢ − μ)² / n
Case 3: x̄ > μ  →  Σ(xᵢ − x̄)² / n  <  Σ(xᵢ − μ)² / n
```

In all cases, dividing by `n` **underestimates** σ². Dividing by `(n−1)` corrects this.

> **Note:** Bessel's Correction is more significant for smaller samples. As `n → ∞`, the difference between `n` and `(n−1)` becomes negligible.

### <span style="color:#2E86AB">Worked Example - Variance</span>

**Sample:** `[-15, -10, 0, 10, 15]`, Mean = 0

```
Variance = [(-15−0)² + (-10−0)² + (0−0)² + (10−0)² + (15−0)²] / (5−1)
         = [225 + 100 + 0 + 100 + 225] / 4
         = 650 / 4
         = 162.5
```

### <span style="color:#2E86AB">Properties of Variance</span>

| Property | Detail |
|----------|--------|
| Always non-negative | σ² ≥ 0 |
| Unit | Squared units of original data |
| Zero variance | All values are identical |
| Additive | Var(X + Y) = Var(X) + Var(Y) if X, Y independent |
| Scaling | Var(aX) = a²·Var(X) |
| Shift invariance | Var(X + c) = Var(X) |

### <span style="color:#2E86AB">Use Cases</span>

- Foundation for standard deviation
- Used in ANOVA (Analysis of Variance)
- Portfolio risk in finance
- Machine learning: regularization, error analysis
- Hypothesis testing (F-test)

---

## <span style="color:#1565C0">4. Standard Deviation</span>

> **Definition:** Standard Deviation is the **square root of variance**. It measures the average distance of data points from the mean, expressed in the **same units** as the original data.

### <span style="color:#2E86AB">Formula</span>

#### <span style="color:#5B8DB8">Population Standard Deviation</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">σ = √σ²  =  √[ Σ(xᵢ − μ)² / N ]</span>

</div>

#### <span style="color:#5B8DB8">Sample Standard Deviation</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">s = √s²  =  √[ Σ(xᵢ − x̄)² / (n − 1) ]</span>

</div>

### <span style="color:#2E86AB">Why Standard Deviation Over Variance?</span>

| Feature | Variance | Standard Deviation |
|---------|----------|--------------------|
| Units | Squared (e.g., kg²) | Same as data (e.g., kg) |
| Interpretability | Hard to interpret directly | Directly comparable to data values |
| Use in formulas | Preferred mathematically | Preferred for communication |

### <span style="color:#2E86AB">Key Properties & Facts</span>

- Has the **same unit** as the original data → directly interpretable
- Makes it **intuitive to compare** with mean or actual data values
- As observations spread further from the mean, std dev **increases**
- If std dev = 0 → **all data values are identical**
- Significantly affected by **outliers** and **skewed distributions**

### <span style="color:#2E86AB">Step-by-Step Computation</span>

```
Step 1 → Compute the mean (x̄)
Step 2 → Find deviation of each point from mean: (xᵢ − x̄)
Step 3 → Square each deviation: (xᵢ − x̄)²
Step 4 → Sum all squared deviations: Σ(xᵢ − x̄)²
Step 5 → Divide by (n−1) for sample [or N for population]
Step 6 → Take square root → Standard Deviation
```

### <span style="color:#2E86AB">Worked Example</span>

**Sample:** `[-15, -10, 0, 10, 15]`, Mean = 0, Variance = 162.5

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">s = √162.5 ≈ 12.75</span>

</div>

**Interpretation:** On average, each data point is about **12.75 units** away from the mean of 0.

### <span style="color:#2E86AB">Empirical Rule (Normal Distribution)</span>

For bell-shaped (normal) distributions:

| Range | Approximate % of Data |
|-------|----------------------|
| μ ± 1σ | ~68% of data |
| μ ± 2σ | ~95% of data |
| μ ± 3σ | ~99.7% of data |

This is also called the **68-95-99.7 Rule**.

### <span style="color:#2E86AB">Use Cases</span>

- Finance: measuring investment risk (volatility)
- Quality control: Six Sigma processes
- Weather: temperature variability
- Machine learning: feature scaling, normalization
- Research: reporting results (mean ± std dev)
- Z-scores: `z = (x − μ) / σ`

### <span style="color:#2E86AB">Standard Deviation vs Other Measures</span>

| Scenario | Best Measure |
|----------|-------------|
| Symmetric data, no outliers | Standard Deviation |
| Skewed data or outliers present | IQR |
| Quick, rough estimate | Range |
| Comparing datasets of different units | Coefficient of Variation |

---

## <span style="color:#1565C0">5. Interquartile Range (IQR)</span>

> **Definition:** The IQR is the range of the **middle 50%** of data. It measures the spread of the central half of a distribution, making it robust to outliers.

### <span style="color:#2E86AB">Understanding Quartiles</span>

Quartiles divide sorted data into **4 equal parts** of 25% each:

```
|--- 25% ---|--- 25% ---|--- 25% ---|--- 25% ---|
           Q1          Q2          Q3
           (P25)      Median      (P75)
            ↑                      ↑
         First                  Third
        Quartile               Quartile
```

| Quartile | Position | Percentile |
|----------|----------|------------|
| Q1 (First Quartile) | 25th percentile | Bottom 25% boundary |
| Q2 (Second Quartile) | 50th percentile | Median |
| Q3 (Third Quartile) | 75th percentile | Top 25% boundary |

### <span style="color:#2E86AB">Formula</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">IQR = Q3 − Q1</span>

</div>

### <span style="color:#2E86AB">How to Calculate IQR - Step by Step</span>

```
Step 1 → Sort data in ascending order
Step 2 → Find the median (Q2) - splits data into lower and upper halves
Step 3 → Find Q1 = median of the lower half
Step 4 → Find Q3 = median of the upper half
Step 5 → IQR = Q3 − Q1
```

### <span style="color:#2E86AB">Worked Example</span>

**Dataset:** `[3, 7, 8, 12, 14, 18, 21, 25, 30]` (n = 9)

```
Sorted:    3   7   8  [12]  14  [18]  21   25   30
                 Q1         Q2          Q3

Q1 = median of [3, 7, 8, 12]     = (7+8)/2 = 7.5
Q2 = median of full dataset       = 14
Q3 = median of [18, 21, 25, 30]  = (21+25)/2 = 23

IQR = Q3 − Q1 = 23 − 7.5 = 15.5
```

### <span style="color:#2E86AB">IQR and Outlier Detection</span>

IQR is used to define outlier boundaries (Tukey's Fences):

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">Lower Fence = Q1 − 1.5 × IQR</span>
### <span style="color:#D4A017">Upper Fence = Q3 + 1.5 × IQR</span>

</div>

Any point outside these fences is considered a **potential outlier**.

### <span style="color:#2E86AB">Why IQR is a Good Measure of Dispersion</span>

1. **Focuses on middle 50%** - ignores extreme values entirely
2. **Resistant to outliers** - IQR is not impacted by a few extreme values, unlike Range
3. **Describes variability around the median** - pairs naturally with median as center
4. **Robust for skewed distributions** - works well when data is not symmetric

### <span style="color:#2E86AB">Five-Number Summary</span>

IQR is part of the **Five-Number Summary**, the foundation of a box plot:

```
Min → Q1 → Median (Q2) → Q3 → Max
```

| Component | Value (example above) |
|-----------|----------------------|
| Minimum | 3 |
| Q1 | 7.5 |
| Median (Q2) | 14 |
| Q3 | 23 |
| Maximum | 30 |
| IQR | 15.5 |

### <span style="color:#2E86AB">Use Cases</span>

- Box plots and exploratory data analysis (EDA)
- Outlier detection (Tukey's method)
- Salary, income data (skewed distributions)
- Medical data (age, blood pressure)
- When data contains extreme values that distort other measures

---

## <span style="color:#1565C0">6. Coefficient of Variation (CV)</span>

> **Definition:** The CV expresses standard deviation as a **percentage of the mean**, enabling comparison of variability across datasets with different units or scales.

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">CV = (σ / μ) × 100%</span>

</div>

**Example:** Comparing height variability (cm) vs weight variability (kg):
- Heights: mean = 170 cm, σ = 10 cm → CV = 5.9%
- Weights: mean = 70 kg, σ = 15 kg → CV = 21.4%
- **Conclusion:** Weights are more variable relative to their mean

---

## <span style="color:#1565C0">7. Comparison of All Measures</span>

| Property | Range | Variance | Std Dev | IQR |
|----------|-------|----------|---------|-----|
| Formula | Max − Min | Σ(xᵢ−x̄)²/(n−1) | √Variance | Q3 − Q1 |
| Units | Same as data | Squared | Same as data | Same as data |
| Uses all data | No | Yes | Yes | No (middle 50%) |
| Outlier sensitive | Highly | Yes | Yes | No (robust) |
| Complexity | Very simple | Moderate | Moderate | Moderate |
| Best with | Quick estimates | Mathematical work | Normal data | Skewed/outlier data |

---

## <span style="color:#1565C0">8. Real-World Applications</span>

### <span style="color:#2E86AB">Finance & Economics</span>

- **Variance/Std Dev** → Measures investment volatility and portfolio risk
- **IQR** → Compares income distributions across countries
- **CV** → Compares risk-adjusted returns of different assets

### <span style="color:#2E86AB">Healthcare & Medicine</span>

- **Std Dev** → Spread of clinical trial results around mean outcome
- **IQR** → Summarizing patient age, blood pressure, dosage data (skewed)
- **Range** → Reporting min/max safe drug doses

### <span style="color:#2E86AB">Manufacturing & Quality Control</span>

- **Std Dev** → Six Sigma: process capability index (Cpk)
- **Variance** → Statistical Process Control (SPC) charts
- **Range** → Control charts for small samples (R-charts)

### <span style="color:#2E86AB">Machine Learning & Data Science</span>

- **Variance** → Bias-variance tradeoff, regularization
- **Std Dev** → Feature scaling (standardization: z = (x−μ)/σ)
- **IQR** → Robust scaling for features with outliers
- **All measures** → Exploratory Data Analysis (EDA)

---

## <span style="color:#1565C0">9. Common Misconceptions & Notes</span>

| Misconception | Reality |
|---------------|---------|
| Std Dev = Variance | Std Dev = √Variance; they differ by square root and units |
| Higher std dev always means bad | In some contexts (diversity), high spread is desirable |
| Range gives full picture | Range uses only 2 points; ignores rest of distribution |
| IQR is always better | IQR discards 50% of data; std dev uses all data points |
| Variance and std dev are the same for samples and populations | They differ: sample uses (n−1), population uses N |

---

## <span style="color:#1565C0">10. Quick Reference Summary</span>

```
RANGE          = Max − Min
               → Simplest, most sensitive to outliers

VARIANCE       = Σ(xᵢ − x̄)² / (n−1)   [sample]
               = Σ(xᵢ − μ)² / N         [population]
               → Average squared deviation; mathematical foundation

STD DEVIATION  = √Variance
               → Same units as data; most widely used measure

IQR            = Q3 − Q1
               → Spread of middle 50%; robust to outliers
               → Outlier bounds: Q1−1.5×IQR  to  Q3+1.5×IQR

CV             = (σ/μ) × 100%
               → Relative measure; use when comparing different units
```

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