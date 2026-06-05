<div align="center">

# <span style="color:#0A2FA8">Skewness & Kurtosis</span>


</div>

---

## <span style="color:#1565C0">1. Statistical Moments - The Foundation</span>

### <span style="color:#2E86AB">1.1 What are Moments?</span>

> **Definition:** A moment is a quantitative measure that describes the shape of a probability distribution. Each moment captures a different aspect of the distribution's structure.

All four moments are calculated from the same data - they each answer a different question about its shape.

| Moment | Name | What It Describes |
|:---:|:---|:---|
| 1st | Mean (µ) | Center / location of the distribution |
| 2nd | Variance (σ²) | Spread / width of the distribution |
| 3rd | Skewness | Asymmetry / lean direction of the distribution |
| 4th | Kurtosis | Tail heaviness / sharpness of the peak |

Skewness and Kurtosis are the **3rd and 4th standardized moments** respectively. They are both dimensionless, meaning they do not depend on the unit of the data.

---

## <span style="color:#1565C0">2. Skewness</span>

### <span style="color:#2E86AB">2.1 What is Skewness?</span>

> **Definition:** Skewness measures the degree and direction of asymmetry in a distribution. A perfectly symmetric distribution has zero skewness. A positive value means the distribution is stretched to the right; a negative value means it is stretched to the left.

In simple terms - skewness tells you **which side has the longer tail**.

---

### <span style="color:#2E86AB">2.2 Formula</span>

#### <span style="color:#5B8DB8">Fisher's Moment Coefficient of Skewness (Standard Formula)</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 540px;">

### <span style="color:#D4A017">Skewness (γ₁) = [ (1/n) · Σ(xᵢ - µ)³ ] / σ³</span>

</div>

Where:
- `n` = number of data points
- `µ` = mean of the data
- `σ` = standard deviation
- The numerator is the **third central moment**

#### <span style="color:#5B8DB8">Sample Skewness (Adjusted for Small Samples)</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 540px;">

### <span style="color:#D4A017">G₁ = [ n / ((n-1)(n-2)) ] · Σ[ (xᵢ - x̄) / s ]³</span>

</div>

This is the formula used by `pandas` (`df.skew()`) and `scipy.stats.skew()`.

#### <span style="color:#5B8DB8">Pearson's First Coefficient (Quick Approximation)</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">Skewness ≈ (Mean - Mode) / σ</span>

</div>

#### <span style="color:#5B8DB8">Pearson's Second Coefficient</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">Skewness ≈ 3 · (Mean - Median) / σ</span>

</div>

Useful when the mode is undefined or multi-valued. Since the median is more stable, this formula is often more reliable on real datasets.

---

### <span style="color:#2E86AB">2.3 Types of Skewness</span>

#### <span style="color:#5B8DB8">Zero Skewness - Symmetric Distribution</span>

```
       |
      /|\
     / | \
    /  |  \
   /   |   \
──────────────
   Mean = Median = Mode
```

- Skewness = 0
- The distribution is perfectly symmetric
- Both tails are equal in length and weight
- Example: Normal distribution, uniform distribution

#### <span style="color:#5B8DB8">Positive Skewness - Right-Skewed Distribution</span>

```
  |
  |\
  | \
  |  \__________
──────────────────
Mode < Median < Mean
         Long tail on the RIGHT
```

- Skewness > 0
- The right tail is longer and stretched out
- Most data is concentrated on the **left side**
- The **mean is pulled toward the right** by extreme high values
- Real-world examples: Income distribution, house prices, insurance claims, age at death for diseases

#### <span style="color:#5B8DB8">Negative Skewness - Left-Skewed Distribution</span>

```
              |
           /| |
__________/  | |
              |
──────────────────
Mean < Median < Mode
Long tail on the LEFT
```

- Skewness < 0
- The left tail is longer and stretched out
- Most data is concentrated on the **right side**
- The **mean is pulled toward the left** by extreme low values
- Real-world examples: Exam scores (most students score high), retirement age, failure time of high-quality products

---

### <span style="color:#2E86AB">2.4 Interpreting Skewness Values</span>

| Skewness Value | Interpretation |
|:---:|:---|
| = 0 | Perfectly symmetric |
| 0 to +0.5 | Approximately symmetric (slight positive lean) |
| +0.5 to +1.0 | Moderately right-skewed |
| > +1.0 | Highly right-skewed |
| 0 to -0.5 | Approximately symmetric (slight negative lean) |
| -0.5 to -1.0 | Moderately left-skewed |
| < -1.0 | Highly left-skewed |

> **Rule of Thumb:** If |skewness| < 0.5, the data is considered approximately symmetric. If |skewness| > 1.0, transformation is likely needed before using in certain ML models.

---

### <span style="color:#2E86AB">2.5 Mean, Median, Mode Relationship with Skewness</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 520px;">

### <span style="color:#D4A017">Right Skew: Mode < Median < Mean</span>
### <span style="color:#D4A017">Symmetric: Mode = Median = Mean</span>
### <span style="color:#D4A017">Left Skew: Mean < Median < Mode</span>

</div>

This relationship holds for unimodal (single-peak) distributions. The **mean** is the most sensitive to extreme values (outliers), which is why it gets pulled toward the tail. The **median** is more resistant, and the **mode** stays at the peak.

---

## <span style="color:#1565C0">3. Kurtosis</span>

### <span style="color:#2E86AB">3.1 What is Kurtosis?</span>

> **Definition:** Kurtosis measures the "tailedness" of a distribution - how much probability mass is in the tails compared to a normal distribution. It also reflects the sharpness of the central peak, but the tail behavior is the primary statistical interpretation.

In simple terms - kurtosis tells you **how often extreme values (outliers) occur** in your data.

> **Important Clarification:** Kurtosis is often described as measuring "peakedness," but this is an oversimplification. The correct interpretation is about **tail weight** - how extreme the outliers are, and how frequently they appear.

---

### <span style="color:#2E86AB">3.2 Formula</span>

#### <span style="color:#5B8DB8">Population Kurtosis (Fourth Standardized Moment)</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 540px;">

### <span style="color:#D4A017">Kurtosis (β₂) = [ (1/n) · Σ(xᵢ - µ)⁴ ] / σ⁴</span>

</div>

#### <span style="color:#5B8DB8">Excess Kurtosis (Fisher's Kurtosis)</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">Excess Kurtosis = β₂ - 3</span>

</div>

The normal distribution has a kurtosis of exactly **3**. Subtracting 3 gives "excess kurtosis," which measures deviation from the normal distribution.

- A normal distribution has **excess kurtosis = 0**
- This is the value returned by `pandas` (`df.kurt()`) and `scipy.stats.kurtosis()`

---

### <span style="color:#2E86AB">3.3 Types of Kurtosis</span>

#### <span style="color:#5B8DB8">Mesokurtic - Normal Tails</span>

- Kurtosis = 3 (Excess Kurtosis = 0)
- Tails match the normal distribution exactly
- Outliers occur at a normal frequency
- Example: **Normal (Gaussian) distribution**

#### <span style="color:#5B8DB8">Leptokurtic - Heavy Tails</span>

```
         |
        /|\         ← Sharper, taller central peak
       / | \
      /  |  \
_____/   |   \_____  ← Heavier, fatter tails
```

- Kurtosis > 3 (Excess Kurtosis > 0)
- Tails are **heavier** than the normal distribution
- Extreme values occur **more frequently** than expected
- The central peak is typically sharper
- Real-world examples: Stock market returns, financial data, earthquakes, t-distribution

#### <span style="color:#5B8DB8">Platykurtic - Light Tails</span>

```
   _____________
  /             \    ← Flatter, broader central region
 /               \
/                 \  ← Thinner, lighter tails
```

- Kurtosis < 3 (Excess Kurtosis < 0)
- Tails are **lighter** than the normal distribution
- Extreme values occur **less frequently** than expected
- The distribution is flatter and more spread out
- Real-world examples: Uniform distribution, bounded physical measurements

---

### <span style="color:#2E86AB">3.4 Interpreting Kurtosis Values</span>

| Excess Kurtosis | Type | Tail Behavior | Outlier Frequency |
|:---:|:---|:---|:---|
| = 0 | Mesokurtic | Normal tails | Normal |
| > 0 (e.g., +2 to +5) | Leptokurtic | Heavy tails | More outliers than normal |
| > 5 or > 10 | Extreme Leptokurtic | Very heavy tails | Many extreme values |
| < 0 (e.g., -1 to -2) | Platykurtic | Light tails | Fewer outliers than normal |

> **Rule of Thumb:** Excess kurtosis values beyond ±2 indicate meaningful deviation from normality. Values beyond ±3 signal potential issues for models assuming normality.

---

### <span style="color:#2E86AB">3.5 Kurtosis of Common Distributions</span>

| Distribution | Kurtosis (β₂) | Excess Kurtosis | Type |
|:---|:---:|:---:|:---|
| Normal | 3.0 | 0.0 | Mesokurtic |
| Uniform | 1.8 | -1.2 | Platykurtic |
| Logistic | 4.2 | 1.2 | Leptokurtic |
| Laplace (Double Exp) | 6.0 | 3.0 | Leptokurtic |
| t-distribution (df=5) | 9.0 | 6.0 | Leptokurtic |
| Exponential | 9.0 | 6.0 | Leptokurtic |
| Bernoulli (p=0.5) | 1.0 | -2.0 | Platykurtic |

---

## <span style="color:#1565C0">4. Skewness vs Kurtosis - Key Differences</span>

| Property | Skewness | Kurtosis |
|:---|:---|:---|
| Moment | 3rd standardized moment | 4th standardized moment |
| Measures | Asymmetry / direction of lean | Tail heaviness / outlier frequency |
| Normal value | 0 | 3 (excess = 0) |
| Positive value means | Right tail is longer | Heavier tails than normal |
| Negative value means | Left tail is longer | Lighter tails than normal |
| Sensitive to | Asymmetric outliers | Extreme outliers (both sides) |
| Affected by | Mean being pulled in one direction | Frequency of extreme deviations |

---

## <span style="color:#1565C0">5. Detecting Skewness & Kurtosis</span>

### <span style="color:#2E86AB">5.1 Visual Methods</span>

#### <span style="color:#5B8DB8">Histogram</span>
The most direct visualization. A right-skewed histogram has a longer right tail; a left-skewed histogram has a longer left tail.

#### <span style="color:#5B8DB8">Box Plot</span>
The position of the median line within the box indicates skewness. Long whiskers on one side indicate skew. Many points beyond the whiskers indicate high kurtosis (heavy tails).

```
Symmetric Box Plot:    |----[  |  ]-----|

Right-Skewed:          |--[  |   ]---------|   (longer right whisker)

Left-Skewed:     |---------|[   |  ]--|        (longer left whisker)
```

#### <span style="color:#5B8DB8">Q-Q Plot (Quantile-Quantile Plot)</span>

> **Definition:** A Q-Q plot compares the quantiles of your data to the quantiles of a theoretical normal distribution. If the data is normal, all points lie along the diagonal reference line.

| Q-Q Plot Pattern | Interpretation |
|:---|:---|
| Points on the line | Data is normally distributed |
| S-shaped curve | Data is skewed |
| Points curve up at both ends | Heavy tails (Leptokurtic) |
| Points curve inward at both ends | Light tails (Platykurtic) |
| Upper end curves above line | Right skew |
| Lower end curves below line | Left skew |

---

### <span style="color:#2E86AB">5.2 Numerical Detection in Python</span>

```python
import pandas as pd
from scipy import stats

# Skewness
df['feature'].skew()              # pandas
stats.skew(df['feature'])         # scipy

# Kurtosis (excess kurtosis = kurtosis - 3)
df['feature'].kurt()              # pandas → returns excess kurtosis
stats.kurtosis(df['feature'])     # scipy → returns excess kurtosis

# Full distribution description
df['feature'].describe()

# Check all features at once
df.skew()
df.kurt()
```

---

### <span style="color:#2E86AB">5.3 Formal Statistical Tests for Normality</span>

These tests check whether skewness and kurtosis together deviate significantly from normality.

| Test | What It Checks | Best For |
|:---|:---|:---|
| Shapiro-Wilk Test | Overall normality (uses moments) | Small samples (n < 2000) |
| D'Agostino-Pearson Test | Skewness + Kurtosis jointly | General use |
| Jarque-Bera Test | Skewness + Kurtosis, based on moments | Large samples, econometrics |
| Kolmogorov-Smirnov Test | Distance from normal CDF | Large samples |
| Anderson-Darling Test | Weighted CDF distance | Small to medium samples |

#### <span style="color:#5B8DB8">Jarque-Bera Test Formula</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 540px;">

### <span style="color:#D4A017">JB = (n/6) · [ S² + (1/4) · (K - 3)² ]</span>

</div>

Where `S` = skewness, `K` = kurtosis, `n` = sample size. A large JB statistic (p-value < 0.05) rejects the null hypothesis of normality.

---

## <span style="color:#1565C0">6. Transformations to Fix Skewness</span>

### <span style="color:#2E86AB">6.1 Why Transform?</span>

Many ML algorithms perform better - or require - approximately normally distributed features. Skewed features violate these assumptions, introduce bias, and degrade performance. Transformations map the data to a more symmetric distribution.

---

### <span style="color:#2E86AB">6.2 Common Transformations</span>

#### <span style="color:#5B8DB8">Log Transformation</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">x' = log(x)   or   x' = log(x + 1)   if x has zeros</span>

</div>

- Best for: **Highly right-skewed data** (skewness > 1)
- Effect: Compresses large values, expands small values
- Requirement: All values must be **strictly positive**
- Examples: Income, prices, population, exponential growth data

#### <span style="color:#5B8DB8">Square Root Transformation</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">x' = √x   or   x' = √(x + 0.5)   for zero-heavy data</span>

</div>

- Best for: **Moderate right skew** (skewness 0.5 – 1.0)
- Effect: Weaker compression than log; good for count data
- Requirement: All values must be **non-negative**
- Examples: Count data, frequencies, Poisson-distributed features

#### <span style="color:#5B8DB8">Cube Root Transformation</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">x' = x^(1/3)</span>

</div>

- Best for: **Data that includes negative values** with right skew
- Effect: Milder than log; handles negatives and zeros naturally
- Examples: Wind speed deviation, signed differences

#### <span style="color:#5B8DB8">Reciprocal Transformation</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">x' = 1/x</span>

</div>

- Best for: **Extremely right-skewed data** with no zeros
- Effect: Very strong compression of large values; also reverses order
- Caution: Changes interpretation of the variable (rate becomes ratio)

#### <span style="color:#5B8DB8">Box-Cox Transformation</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 540px;">

### <span style="color:#D4A017">x'(λ) = (xλ - 1) / λ   if λ ≠ 0</span>
### <span style="color:#D4A017">x'(λ) = log(x)          if λ = 0</span>

</div>

- Best for: **Any right-skewed positive data**
- Lambda (λ) is estimated automatically by maximizing log-likelihood
- It is a **generalized transformation** - log (λ=0), sqrt (λ=0.5), linear (λ=1), reciprocal (λ=-1)
- Requirement: All values **strictly positive (x > 0)**
- Library: `scipy.stats.boxcox()`

#### <span style="color:#5B8DB8">Yeo-Johnson Transformation</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 540px;">

### <span style="color:#D4A017">Extends Box-Cox to handle x = 0 and x < 0</span>

</div>

- Best for: **Data with zeros or negative values** - the most general power transformation
- Library: `sklearn.preprocessing.PowerTransformer(method='yeo-johnson')`
- Automatically finds optimal λ

---

### <span style="color:#2E86AB">6.3 Transformation Selection Guide</span>

| Condition | Recommended Transformation |
|:---|:---|
| Right skew, all positive, no zeros | Log or Box-Cox |
| Right skew, has zeros | log(x+1) or Yeo-Johnson |
| Right skew, has negatives | Yeo-Johnson |
| Moderate right skew, count data | Square Root |
| Left-skewed data | Square or Cube (reflect + transform) |
| Want automated optimal λ | Box-Cox or Yeo-Johnson |
| Tree-based models | No transformation needed |

```
Check skewness → |skew| > 0.5? → Choose transformation → Apply → Re-check skewness → Validate
```

---

## <span style="color:#1565C0">7. Why & How Skewness and Kurtosis Are Used in ML</span>

### <span style="color:#2E86AB">7.1 Algorithms That Are Sensitive to Skewness & Kurtosis</span>

| Algorithm | Sensitive? | Reason |
|:---|:---:|:---|
| Linear Regression | Yes | Assumes normally distributed residuals; skewed features distort coefficients |
| Logistic Regression | Yes | Feature scaling affected; gradient descent slower on skewed inputs |
| Linear Discriminant Analysis (LDA) | Yes | Explicitly assumes normally distributed features per class |
| Naive Bayes (Gaussian) | Yes | Assumes features are Gaussian - skew breaks this assumption |
| KNN | Yes | Distance metrics (Euclidean) are distorted by outliers from heavy-tailed features |
| K-Means Clustering | Yes | Centroid calculation is mean-based; outliers from heavy tails pull centroids |
| SVM (RBF kernel) | Yes | Kernel distances affected by extreme outliers |
| PCA | Yes | Variance maximization is dominated by skewed/outlier-heavy features |
| Neural Networks | Moderate | Skewed inputs slow gradient descent; activation saturation worsens |
| Decision Trees | <span style="color:#27AE60">No</span> | Split points are rank-based; skew does not affect split finding |
| Random Forest | <span style="color:#27AE60">No</span> | Tree-based; robust to monotonic transformations and skew |
| Gradient Boosting (XGBoost, LightGBM) | <span style="color:#27AE60">No</span> | Rank-based splits; inherently robust to skewness |

---

### <span style="color:#2E86AB">7.2 How Skewness Affects ML - Detailed Mechanisms</span>

#### <span style="color:#5B8DB8">Effect on Feature Scaling</span>

Standard scalers (StandardScaler: subtract mean, divide by std) assume the data is approximately bell-shaped. On a skewed feature, the mean and standard deviation are both distorted, leading to poor normalization. After scaling, the extreme tail values become very large normalized values, still dominating the model.

```
Skewed feature → StandardScaler → Still skewed (just shifted and squeezed)
Skewed feature → Log Transform → StandardScaler → Properly normalized
```

#### <span style="color:#5B8DB8">Effect on Linear Regression Assumptions</span>

Linear regression has four key assumptions: linearity, independence, homoscedasticity (constant variance), and **normality of residuals**. Skewed input features frequently cause skewed residuals, violating the normality assumption. This makes the coefficient estimates inefficient and hypothesis tests (p-values, confidence intervals) unreliable.

#### <span style="color:#5B8DB8">Effect on Gradient Descent Convergence</span>

When features have very different scales and skewed distributions, the loss function landscape becomes elongated (like a narrow valley). Gradient descent must take many small steps to navigate this - slow convergence. Feature transformation (+ scaling) rounds out the loss surface, allowing direct paths to the minimum.

```
Skewed feature space:    Elongated loss surface → zigzag gradient steps → slow
Normalized feature space: Circular loss surface → direct path → fast convergence
```

#### <span style="color:#5B8DB8">Effect of Kurtosis on Distance-Based Models</span>

High kurtosis (heavy tails) means there are frequent extreme values. In KNN and K-Means, Euclidean distance is computed between all points. Extreme outliers from heavy-tailed features dominate these distances, causing distance-based algorithms to cluster around outliers rather than the true data structure.

---

### <span style="color:#2E86AB">7.3 How Skewness Is Used in Feature Engineering</span>

> **Definition in ML Context:** In Feature Engineering and EDA, skewness and kurtosis are used as diagnostic statistics to decide whether a feature needs transformation before being fed into a model.

```
Step 1: Compute skewness for all numeric features  →  df.skew()
Step 2: Flag features with |skewness| > 0.5
Step 3: Visualize flagged features (histogram + Q-Q plot)
Step 4: Apply appropriate transformation (log, sqrt, Box-Cox, Yeo-Johnson)
Step 5: Re-compute skewness to verify improvement
Step 6: Apply same transformation to test set (fit on train, transform both)
```

#### <span style="color:#5B8DB8">Automated Skewness Handling Pattern</span>

```python
from scipy.stats import skew
from sklearn.preprocessing import PowerTransformer

# Flag skewed features
skewed_features = df.apply(lambda x: skew(x)).sort_values(ascending=False)
skewed_features = skewed_features[abs(skewed_features) > 0.5]

# Apply Yeo-Johnson transformation
pt = PowerTransformer(method='yeo-johnson')
df[skewed_features.index] = pt.fit_transform(df[skewed_features.index])
```

---

### <span style="color:#2E86AB">7.4 How Kurtosis Is Used in ML</span>

#### <span style="color:#5B8DB8">Outlier Detection Signal</span>

High positive excess kurtosis is a strong signal that the feature contains extreme outliers. Before training, high kurtosis features should be inspected for:
- Data entry errors
- Genuine rare events that need special handling
- Need for robust scalers (`RobustScaler`) instead of `StandardScaler`

#### <span style="color:#5B8DB8">Choosing the Right Scaler</span>

| Feature Kurtosis | Recommended Scaler | Reason |
|:---|:---|:---|
| Low (excess ≈ 0) | `StandardScaler` | Behaves like normal data |
| High positive (leptokurtic) | `RobustScaler` | Uses median/IQR - resistant to outliers |
| Very high (extreme outliers) | `QuantileTransformer` | Maps to uniform or normal distribution |

#### <span style="color:#5B8DB8">Independent Component Analysis (ICA)</span>

ICA is a dimensionality reduction technique that separates independent sources. It explicitly uses kurtosis: super-Gaussian (leptokurtic) components have kurtosis > 0, sub-Gaussian (platykurtic) have kurtosis < 0. Kurtosis is used as a measure of **non-Gaussianity** to identify independent components.

#### <span style="color:#5B8DB8">Financial ML & Risk Modeling</span>

In financial ML (stock price prediction, portfolio optimization, risk models), kurtosis is crucial. Asset return distributions are consistently leptokurtic - the probability of a large loss (or gain) is much higher than a Gaussian model assumes. Models that ignore this underestimate risk.

---

### <span style="color:#2E86AB">7.5 Skewness & Kurtosis in the ML Pipeline</span>

| Pipeline Stage | How Skewness/Kurtosis Is Used |
|:---|:---|
| EDA | Compute and visualize distribution shape for all features; identify problem features |
| Data Cleaning | High kurtosis → investigate extreme values for errors vs genuine outliers |
| Feature Engineering | Transform skewed features; engineer log/sqrt versions as new features |
| Preprocessing | Choose StandardScaler vs RobustScaler based on kurtosis; apply PowerTransformer |
| Model Selection | Avoid normality-assuming models on untransformed skewed data |
| Evaluation | Check residuals for skewness (linear regression); skewed residuals signal model misfit |
| Feature Importance | Skewed features often have distorted importance scores - transform first |

---

## <span style="color:#1565C0">8. Complete Quick Reference</span>

### <span style="color:#2E86AB">8.1 Skewness Cheat Sheet</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 540px;">

### <span style="color:#D4A017">γ₁ = 0  →  Symmetric  |  γ₁ > 0  →  Right Tail  |  γ₁ < 0  →  Left Tail</span>

</div>

| Question | Answer |
|:---|:---|
| What does it measure? | Asymmetry - which side has the longer tail |
| Normal distribution skewness | 0 |
| Affected by outliers? | Yes - strongly, because it cubes deviations |
| Right skew: where is the mean? | Greater than the median (pulled right) |
| Which ML models care most? | Linear Regression, LDA, Naive Bayes, Neural Networks |
| Fix method | Log, sqrt, Box-Cox, Yeo-Johnson transformation |

---

### <span style="color:#2E86AB">8.2 Kurtosis Cheat Sheet</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 540px;">

### <span style="color:#D4A017">Excess K = 0  →  Normal  |  > 0  →  Heavy Tails  |  < 0  →  Light Tails</span>

</div>

| Question | Answer |
|:---|:---|
| What does it measure? | Tailedness - frequency and extremity of outliers |
| Normal distribution kurtosis | 3 (excess = 0) |
| Pandas/scipy return value | Excess kurtosis (kurtosis - 3) |
| High kurtosis signals | Many extreme values; possible outlier issue |
| Which ML models care most? | KNN, K-Means, PCA, SVM, ICA |
| Fix method | RobustScaler, QuantileTransformer, remove/cap outliers |

---

### <span style="color:#2E86AB">8.3 Decision Flowchart</span>

```
Compute skew() and kurt() for each feature
        |
        v
|skew| > 0.5?
   Yes  →  Check sign
            Positive (right skew) → Log / Box-Cox / Yeo-Johnson
            Negative (left skew)  → Reflect then Log / Square
   No   →  Data is approximately symmetric, proceed
        |
        v
|excess kurtosis| > 2?
   Yes  →  Heavy or light tails detected
            High (+)  →  Use RobustScaler, inspect/cap outliers
            Low  (-)  →  QuantileTransformer or proceed
   No   →  Normal tail behavior, StandardScaler is fine
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