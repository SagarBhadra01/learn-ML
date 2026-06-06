<div align="center">

# <span style="color:#0A2FA8">Covariance & Correlation</span>

</div>

---

## <span style="color:#1565C0">1. Why Variable Relationships Matter</span>

### <span style="color:#2E86AB">1.1 The Core Idea</span>

> **Definition:** In statistics and ML, we are not just interested in individual variables in isolation - we want to understand how variables **move together**. Do they rise and fall in sync? Do they move in opposite directions? Or are they completely unrelated?

Two statistics answer this:
- **Covariance** - measures the *direction* and *magnitude* of the joint variability of two variables
- **Correlation** - standardizes covariance into a universal, unit-free scale so the strength is directly comparable

Understanding variable relationships is critical at every stage of ML - from EDA and feature selection to model training and interpretation.

---

## <span style="color:#1565C0">2. Covariance</span>

### <span style="color:#2E86AB">2.1 What is Covariance?</span>

> **Definition:** Covariance measures how much two variables change together. If both variables tend to be above their mean at the same time, covariance is positive. If one tends to be above its mean when the other is below, covariance is negative.

In simple terms - covariance answers: **"When X goes up, does Y tend to go up or down?"**

---

### <span style="color:#2E86AB">2.2 Formula</span>

#### <span style="color:#5B8DB8">Population Covariance</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 540px;">

### <span style="color:#D4A017">Cov(X, Y) = (1/N) · Σ (xᵢ - µₓ)(yᵢ - µᵧ)</span>

</div>

#### <span style="color:#5B8DB8">Sample Covariance (used in practice)</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 540px;">

### <span style="color:#D4A017">Cov(X, Y) = (1/(n-1)) · Σ (xᵢ - x̄)(yᵢ - ȳ)</span>

</div>

Where:
- `N` = population size, `n` = sample size
- `µₓ`, `µᵧ` = population means; `x̄`, `ȳ` = sample means
- Division by `n-1` (not `n`) is **Bessel's correction** - removes bias in sample estimation
- Each term `(xᵢ - x̄)(yᵢ - ȳ)` captures how far both variables deviate from their means simultaneously

#### <span style="color:#5B8DB8">Intuition Behind the Formula</span>

```
Both above mean  → (xᵢ - x̄) > 0, (yᵢ - ȳ) > 0 → product is POSITIVE → contributes +ve
Both below mean  → (xᵢ - x̄) < 0, (yᵢ - ȳ) < 0 → product is POSITIVE → contributes +ve
One up, one down → opposite signs                  → product is NEGATIVE → contributes -ve
No pattern       → positives and negatives cancel  → sum ≈ 0
```

---

### <span style="color:#2E86AB">2.3 Interpreting Covariance</span>

| Sign | Value | Meaning |
|:---:|:---|:---|
| Positive | Cov > 0 | X and Y move in the same direction |
| Negative | Cov < 0 | X and Y move in opposite directions |
| Zero | Cov = 0 | No linear relationship between X and Y |

> **Critical Limitation:** The magnitude of covariance is **scale-dependent**. A covariance of 500 between two variables measured in meters is not comparable to a covariance of 5 between variables measured in kilometers - they describe the same relationship. This makes raw covariance values meaningless for comparing relationship strength across different pairs of variables.

---

### <span style="color:#2E86AB">2.4 Properties of Covariance</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">Cov(X, X) = Var(X)</span>

</div>

Covariance of a variable with itself equals its variance. This connects covariance to the broader framework of variance.

| Property | Formula |
|:---|:---|
| Symmetry | Cov(X, Y) = Cov(Y, X) |
| Self-covariance | Cov(X, X) = Var(X) |
| Linearity | Cov(aX + b, Y) = a · Cov(X, Y) |
| Additivity | Cov(X + Y, Z) = Cov(X, Z) + Cov(Y, Z) |
| Constant | Cov(X, c) = 0 (constant c has no variability) |
| Independence | If X ⊥ Y, then Cov(X, Y) = 0 (converse not always true) |

---

### <span style="color:#2E86AB">2.5 Covariance Matrix</span>

> **Definition:** The covariance matrix (also called the variance-covariance matrix) is a square, symmetric matrix that contains all pairwise covariances between variables. Diagonal entries are variances; off-diagonal entries are covariances.

For `p` variables, the covariance matrix **Σ** is a `p × p` matrix:

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 560px;">

### <span style="color:#D4A017">Σ = [ Cov(Xᵢ, Xⱼ) ]  where diagonal = Var(Xᵢ)</span>

</div>

```
        X₁          X₂          X₃
X₁  [ Var(X₁)   Cov(X₁,X₂)  Cov(X₁,X₃) ]
X₂  [ Cov(X₂,X₁)  Var(X₂)   Cov(X₂,X₃) ]
X₃  [ Cov(X₃,X₁)  Cov(X₃,X₂)  Var(X₃)  ]
```

Properties of the covariance matrix:
- Always **symmetric**: Σ = Σᵀ
- Always **positive semi-definite**: all eigenvalues ≥ 0
- Diagonal entries are always non-negative (variance ≥ 0)

This matrix is the foundation of **PCA**, **LDA**, **Mahalanobis distance**, and **multivariate Gaussian distributions**.

---

## <span style="color:#1565C0">3. Correlation</span>

### <span style="color:#2E86AB">3.1 What is Correlation?</span>

> **Definition:** Correlation is a standardized measure of the linear relationship between two variables. It divides covariance by the product of both standard deviations, resulting in a dimensionless value always between -1 and +1.

Correlation solves covariance's biggest problem - it removes the effect of the variables' scales, making strength of relationship directly comparable across any pair of variables.

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">Correlation = Covariance / (Scale of both variables)</span>

</div>

---

### <span style="color:#2E86AB">3.2 Pearson's Correlation Coefficient</span>

> **Definition:** Pearson's correlation coefficient (r) measures the strength and direction of the **linear** relationship between two continuous variables. It is the most widely used correlation measure.

#### <span style="color:#5B8DB8">Formula</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 540px;">

### <span style="color:#D4A017">r = Cov(X, Y) / (σₓ · σᵧ)</span>

</div>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 540px;">

### <span style="color:#D4A017">r = Σ(xᵢ - x̄)(yᵢ - ȳ) / √[Σ(xᵢ - x̄)² · Σ(yᵢ - ȳ)²]</span>

</div>

- `σₓ`, `σᵧ` = standard deviations of X and Y respectively
- The denominator normalizes the numerator to the range [-1, +1]
- `r` is also known as the **Pearson product-moment correlation coefficient**

#### <span style="color:#5B8DB8">Interpreting Pearson's r</span>

| Value of r | Strength | Direction |
|:---:|:---|:---|
| +1.0 | Perfect | Positive (both move exactly together) |
| +0.7 to +0.9 | Strong | Positive |
| +0.4 to +0.6 | Moderate | Positive |
| +0.1 to +0.3 | Weak | Positive |
| 0.0 | None | No linear relationship |
| -0.1 to -0.3 | Weak | Negative |
| -0.4 to -0.6 | Moderate | Negative |
| -0.7 to -0.9 | Strong | Negative |
| -1.0 | Perfect | Negative (one rises exactly as other falls) |

#### <span style="color:#5B8DB8">Assumptions of Pearson's r</span>

| Assumption | What It Means |
|:---|:---|
| Linearity | The relationship between X and Y is linear |
| Continuous data | Both variables must be continuous (interval or ratio scale) |
| Normality | Both variables should be approximately normally distributed |
| No significant outliers | Outliers heavily distort r |
| Homoscedasticity | Variance of Y should be constant across values of X |

> **Key Warning:** `r = 0` means **no linear relationship** - it does NOT mean no relationship at all. Two variables can have a perfect curved (non-linear) relationship and still have `r ≈ 0`.

---

### <span style="color:#2E86AB">3.3 Spearman's Rank Correlation</span>

> **Definition:** Spearman's rank correlation (ρ, rho) measures the strength and direction of the **monotonic** relationship between two variables. It works by converting data to ranks and then computing Pearson's correlation on those ranks.

#### <span style="color:#5B8DB8">Formula</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 540px;">

### <span style="color:#D4A017">ρ = 1 - (6 · Σdᵢ²) / (n(n² - 1))</span>

</div>

Where `dᵢ` = difference in ranks of corresponding values of X and Y, and `n` = number of observations.

**Step-by-step process:**
```
Original values: X = [10, 20, 30, 40],  Y = [15, 5, 35, 25]
Rank X:              [1,   2,  3,  4 ]
Rank Y:              [2,   1,  4,  3 ]
dᵢ = Rank(X) - Rank(Y):  [-1, 1, -1, 1]
dᵢ²:                      [1,  1,   1, 1]
Σdᵢ² = 4  →  ρ = 1 - (6·4)/(4·(16-1)) = 1 - 24/60 = 0.60
```

#### <span style="color:#5B8DB8">When to Use Spearman vs Pearson</span>

| Condition | Use Pearson | Use Spearman |
|:---|:---:|:---:|
| Both variables continuous and normal | Yes | Can use either |
| Data is ordinal (ranked categories) | No | Yes |
| Data has significant outliers | No | Yes |
| Relationship is monotonic but non-linear | No | Yes |
| Small sample size with non-normal data | No | Yes |

> **Monotonic relationship:** Y consistently increases (or decreases) as X increases - not necessarily at a constant rate. Spearman captures this; Pearson does not.

---

### <span style="color:#2E86AB">3.4 Kendall's Tau (τ)</span>

> **Definition:** Kendall's Tau measures the ordinal association between two variables by counting concordant and discordant pairs. It is more robust than Spearman's for small samples and tied ranks.

#### <span style="color:#5B8DB8">Formula</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 540px;">

### <span style="color:#D4A017">τ = (Concordant Pairs - Discordant Pairs) / (n(n-1)/2)</span>

</div>

- **Concordant pair:** Both X and Y are in the same order (Xᵢ > Xⱼ and Yᵢ > Yⱼ)
- **Discordant pair:** X and Y are in opposite order (Xᵢ > Xⱼ but Yᵢ < Yⱼ)
- Range: [-1, +1] - same interpretation as Pearson and Spearman

| Feature | Kendall's τ | Spearman's ρ |
|:---|:---|:---|
| Basis | Pairwise comparisons | Ranks |
| Robustness to ties | Better | Moderate |
| Interpretation | Probability of concordance | Rank correlation |
| Common use | Small samples, tied data | General non-parametric |

---

### <span style="color:#2E86AB">3.5 Point-Biserial Correlation</span>

> **Definition:** Point-Biserial correlation measures the relationship between one **continuous** variable and one **binary** (dichotomous) variable. It is mathematically equivalent to Pearson's r applied to binary data.

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 580px;">

### <span style="color:#D4A017">r_pb = (M₁ - M₀) / Sₙ · √(n₁·n₀ / n²)</span>

</div>

Where `M₁`, `M₀` = means of continuous variable for binary groups 1 and 0; `n₁`, `n₀` = group sizes; `Sₙ` = overall standard deviation.

Real-world example: Correlation between exam score (continuous) and pass/fail result (binary 1/0).

---

### <span style="color:#2E86AB">3.6 Phi Coefficient (φ)</span>

> **Definition:** The Phi coefficient measures the association between two **binary** categorical variables. It is mathematically equivalent to Pearson's r applied to two binary variables.

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 560px;">

### <span style="color:#D4A017">φ = (AD - BC) / √[(A+B)(C+D)(A+C)(B+D)]</span>

</div>

Where A, B, C, D are the four cells of a 2×2 contingency table.

---

### <span style="color:#2E86AB">3.7 Choosing the Right Correlation Method</span>

| Data Type of X | Data Type of Y | Method to Use |
|:---|:---|:---|
| Continuous (normal) | Continuous (normal) | Pearson's r |
| Continuous (non-normal or ordinal) | Continuous (non-normal or ordinal) | Spearman's ρ |
| Continuous or ordinal | Continuous or ordinal (small n / ties) | Kendall's τ |
| Continuous | Binary (0/1) | Point-Biserial |
| Binary (0/1) | Binary (0/1) | Phi coefficient (φ) |
| Categorical (multi-level) | Categorical (multi-level) | Cramér's V |

---

## <span style="color:#1565C0">4. Covariance vs Correlation - Key Differences</span>

| Property | Covariance | Correlation |
|:---|:---|:---|
| Range | (-∞, +∞) - unbounded | [-1, +1] - always bounded |
| Unit | Product of X and Y units | Dimensionless (unit-free) |
| Scale-dependent | Yes - changes with scale of data | No - invariant to scale |
| Tells direction | Yes | Yes |
| Tells strength | No - magnitude is uninterpretable | Yes - directly comparable |
| Comparable across pairs | No | Yes |
| Used in PCA | Yes (covariance matrix) | Yes (correlation matrix = standardized) |

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 560px;">

### <span style="color:#D4A017">r(X, Y) = Cov(X, Y) / (σₓ · σᵧ)   →   Correlation IS standardized Covariance</span>

</div>

---

## <span style="color:#1565C0">5. Correlation Matrix</span>

### <span style="color:#2E86AB">5.1 What is a Correlation Matrix?</span>

> **Definition:** A correlation matrix is a square, symmetric matrix that shows the pairwise correlation coefficients between all variables in a dataset. The diagonal is always 1 (every variable is perfectly correlated with itself).

```
         Age    Income   Score   Height
Age    [  1.00   0.72   -0.15    0.03 ]
Income [  0.72   1.00   -0.08    0.01 ]
Score  [ -0.15  -0.08    1.00    0.22 ]
Height [  0.03   0.01    0.22    1.00 ]
```

Reading the matrix:
- **Diagonal** = 1.00 always (self-correlation)
- **Upper triangle** = mirror of lower triangle (symmetric)
- **Off-diagonal values** = pairwise correlation strength and direction

---

### <span style="color:#2E86AB">5.2 Computing in Python</span>

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import pearsonr, spearmanr, kendalltau

# Pearson correlation matrix
corr_matrix = df.corr(method='pearson')   # default

# Spearman correlation matrix
corr_matrix = df.corr(method='spearman')

# Kendall correlation matrix
corr_matrix = df.corr(method='kendall')

# Single pair with p-value
r, p_value = pearsonr(df['X'], df['Y'])
rho, p_value = spearmanr(df['X'], df['Y'])

# Covariance matrix
cov_matrix = df.cov()

# Heatmap visualization
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm',
            vmin=-1, vmax=1, center=0, fmt='.2f')
plt.title('Correlation Matrix')
plt.show()
```

---

## <span style="color:#1565C0">6. Statistical Significance of Correlation</span>

### <span style="color:#2E86AB">6.1 The Core Problem</span>

A calculated correlation of `r = 0.4` might look meaningful - but is it real, or could it just be noise from a small sample? Statistical significance testing answers this question.

### <span style="color:#2E86AB">6.2 Hypothesis Test for Correlation</span>

- **H₀ (Null Hypothesis):** The true population correlation ρ = 0 (no linear relationship)
- **H₁ (Alternative Hypothesis):** ρ ≠ 0 (a linear relationship exists)

#### <span style="color:#5B8DB8">t-Statistic for Pearson's r</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">t = r · √(n - 2) / √(1 - r²)</span>

</div>

This t-statistic follows a t-distribution with `n - 2` degrees of freedom. If `p-value < 0.05`, reject H₀ - the correlation is statistically significant.

> **Critical Warning:** Statistical significance ≠ practical significance. With a very large dataset (n = 10,000), a tiny correlation like `r = 0.02` can be statistically significant but is practically meaningless for feature selection. Always look at both the r value and the p-value together.

---

### <span style="color:#2E86AB">6.3 Confidence Interval Using Fisher's Z-Transformation</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">z = (1/2) · ln[(1 + r) / (1 - r)]</span>

</div>

The transformed z follows an approximately normal distribution with standard error `1/√(n-3)`. Back-transform the CI endpoints to get the correlation CI.

---

## <span style="color:#1565C0">7. Spurious Correlation & Causation</span>

### <span style="color:#2E86AB">7.1 Correlation Does NOT Imply Causation</span>

> **Definition:** Spurious correlation is a mathematical relationship between two variables that appears to be causal but is actually caused by a confounding third variable, coincidence, or data artifact.

```
Ice cream sales and drowning rates are positively correlated
→ NOT because ice cream causes drowning
→ BOTH are caused by a third variable: HOT WEATHER (confound)
```

Classic spurious examples:
- Nicolas Cage films released per year vs swimming pool drownings (r ≈ 0.67)
- Per capita cheese consumption vs deaths by bedsheet tangling (r ≈ 0.95)
- Number of pirates globally vs global average temperature (strong negative correlation)

### <span style="color:#2E86AB">7.2 Types of Misleading Correlations</span>

| Type | Description | Example |
|:---|:---|:---|
| Spurious | Caused by confounding variable | Ice cream + drowning (weather confound) |
| Coincidental | Pure statistical coincidence | Cage films + pool drownings |
| Reverse Causation | Causation direction is flipped | "Rich people are healthier" - or are healthy people wealthier? |
| Selection Bias | Sample is not representative | Correlation in data that wasn't randomly sampled |
| Ecological Fallacy | Group-level correlation applied to individuals | Country literacy vs country income ≠ individual-level fact |

---

## <span style="color:#1565C0">8. Multicollinearity</span>

### <span style="color:#2E86AB">8.1 What is Multicollinearity?</span>

> **Definition:** Multicollinearity occurs when two or more predictor features in a regression model are highly correlated with each other. This causes instability in coefficient estimates - the model cannot reliably separate the individual effect of each correlated feature.

```
Feature A and Feature B are highly correlated (r = 0.95)
→ Model cannot determine: "Is the outcome due to A, B, or both?"
→ Coefficients become large, unstable, and flip signs
→ Adding/removing one correlated feature drastically changes others
```

---

### <span style="color:#2E86AB">8.2 Variance Inflation Factor (VIF)</span>

> **Definition:** VIF quantifies how much the variance of a regression coefficient is inflated due to multicollinearity with other features. It is the primary diagnostic tool for detecting multicollinearity.

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">VIF(Xᵢ) = 1 / (1 - R²ᵢ)</span>

</div>

Where `R²ᵢ` is the R² from regressing feature `Xᵢ` on all other features.

| VIF Value | Interpretation | Action |
|:---:|:---|:---|
| 1 | No multicollinearity | Safe to use |
| 1 – 5 | Low to moderate | Generally acceptable |
| 5 – 10 | High multicollinearity | Investigate; consider removing |
| > 10 | Severe multicollinearity | Remove or combine the feature |

```python
from statsmodels.stats.outliers_influence import variance_inflation_factor

vif_data = pd.DataFrame()
vif_data["Feature"] = X.columns
vif_data["VIF"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
```

---

### <span style="color:#2E86AB">8.3 Effects and Remedies for Multicollinearity</span>

| Effect | Description |
|:---|:---|
| Unstable coefficients | Small data changes cause large coefficient changes |
| Wrong signs | Coefficient signs may be opposite to logic |
| Inflated standard errors | Makes individual coefficients appear insignificant |
| Reduced interpretability | Cannot isolate each feature's true effect |

| Remedy | Description |
|:---|:---|
| Remove one of the correlated features | Drop the one with lower feature importance |
| PCA / Dimensionality Reduction | Transform correlated features into uncorrelated principal components |
| Ridge Regression (L2) | Regularization shrinks correlated coefficients together |
| Partial Least Squares (PLS) | Finds components that predict target, handles multicollinearity |
| Feature combining | Create a single ratio or composite feature from two correlated ones |

---

## <span style="color:#1565C0">9. Why & How Used in Machine Learning</span>

### <span style="color:#2E86AB">9.1 Feature Selection Using Correlation</span>

> **Definition in ML Context:** Correlation-based feature selection removes redundant features that are strongly correlated with each other (multicollinearity) and keeps features that are strongly correlated with the target variable (useful signal).

```
Step 1: Compute correlation matrix of all features
Step 2: Find all feature pairs with |r| > threshold (e.g., 0.85 or 0.90)
Step 3: Of each highly correlated pair, keep the one with higher target correlation
Step 4: Drop the other
Step 5: Re-check - repeat until no pair exceeds threshold
```

```python
# Find highly correlated feature pairs
def remove_correlated_features(df, threshold=0.85):
    corr_matrix = df.corr().abs()
    upper = corr_matrix.where(
        np.triu(np.ones(corr_matrix.shape), k=1).astype(bool)
    )
    to_drop = [col for col in upper.columns if any(upper[col] > threshold)]
    return df.drop(columns=to_drop)
```

---

### <span style="color:#2E86AB">9.2 Target Correlation for Feature Ranking</span>

The correlation between each feature and the target variable is one of the simplest and fastest feature selection methods.

```python
# Correlation of all features with target
target_corr = df.corr()['target'].drop('target').abs().sort_values(ascending=False)
```

| Target Correlation | Feature Quality |
|:---:|:---|
| > 0.5 | Strong signal - likely useful |
| 0.2 – 0.5 | Moderate signal - worth exploring |
| < 0.1 | Weak signal - may not help the model |

> **Important:** Low Pearson correlation does not mean the feature is useless - there may be a non-linear relationship. Check Spearman's ρ as well, and evaluate feature importance from tree-based models.

---

### <span style="color:#2E86AB">9.3 Covariance Matrix in PCA</span>

> **Definition:** Principal Component Analysis (PCA) uses the covariance matrix of the features to find the directions (principal components) of maximum variance in the data. These directions are the eigenvectors of the covariance matrix.

```
Step 1: Standardize features (zero mean, unit variance)
Step 2: Compute covariance matrix Σ  (p × p matrix)
Step 3: Compute eigenvectors and eigenvalues of Σ
Step 4: Eigenvectors = principal component directions
        Eigenvalues  = variance explained by each component
Step 5: Sort by eigenvalue (descending) - largest explains most variance
Step 6: Project data onto top k eigenvectors → reduced representation
```

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">Σ · v = λ · v</span>

### <span style="color:#D4A017">v = eigenvector (direction),  λ = eigenvalue (variance)</span>

</div>

Why covariance matrix and not correlation matrix in PCA?
- **Covariance matrix PCA**: Preserves scale - features with larger variance dominate. Use when all features are in the same unit and scale matters.
- **Correlation matrix PCA**: Normalizes scale - all features contribute equally. Use when features are in different units.

---

### <span style="color:#2E86AB">9.4 Mahalanobis Distance - Covariance in Distance Metrics</span>

> **Definition:** Mahalanobis distance is a scale-invariant distance metric that accounts for the covariance structure of the data. Unlike Euclidean distance, it treats correlated features differently, down-weighting redundant dimensions.

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">D_M(x) = √[(x - µ)ᵀ · Σ⁻¹ · (x - µ)]</span>

</div>

Used in: outlier detection, LDA, Gaussian Mixture Models, anomaly detection.

---

### <span style="color:#2E86AB">9.5 Correlation in the Context of Different ML Algorithms</span>

| Algorithm | Role of Correlation / Covariance |
|:---|:---|
| Linear Regression | Correlated features inflate coefficient variance; VIF check is required |
| Logistic Regression | Same as linear regression; multicollinearity makes coefficients unreliable |
| PCA | Covariance matrix is the core - eigenvectors give principal components |
| LDA | Uses within-class and between-class covariance matrices to find discriminant directions |
| Naive Bayes | Assumes all features are independent (zero covariance); correlated features break this assumption |
| KNN | High pairwise correlation means redundant dimensions distort distances equally |
| Neural Networks | Correlated inputs slow convergence; correlations decay during training |
| Random Forest / XGBoost | Feature importance accounts for correlation; correlated features split importance across themselves |
| Gaussian Mixture Models | The covariance matrix shape parameter controls cluster shape (spherical, diagonal, full) |

---

### <span style="color:#2E86AB">9.6 Correlation in EDA - Standard ML Workflow</span>

```
1. Load data and inspect dtypes
2. Compute df.corr() (Pearson) and df.corr(method='spearman') for all feature pairs
3. Plot heatmap → identify clusters of highly correlated features
4. Compute target correlation → rank features by predictive signal
5. Flag feature pairs with |r| > 0.85 → investigate for redundancy
6. Compute VIF for linear models → flag VIF > 10
7. Apply remedies: drop, PCA, combine, or use regularization
8. Re-check correlation matrix after transformation
```

---

### <span style="color:#2E86AB">9.7 Correlation Matrix vs Covariance Matrix - When to Use Which in ML</span>

| Use Case | Use Covariance Matrix | Use Correlation Matrix |
|:---|:---:|:---:|
| PCA (same-unit features) | Yes | Can use |
| PCA (different-unit features) | No | Yes |
| Mahalanobis distance | Yes | No |
| Feature redundancy detection | No | Yes |
| Gaussian Mixture Models | Yes | No |
| LDA | Yes | No |
| Feature selection step | No | Yes |

---

## <span style="color:#1565C0">10. Anscombe's Quartet - Why Visualization Always Matters</span>

### <span style="color:#2E86AB">10.1 The Famous Warning</span>

> **Definition:** Anscombe's Quartet is a set of four datasets that have nearly identical summary statistics (mean, variance, and Pearson's r ≈ 0.816) but completely different distributions and patterns when visualized.

| Dataset | Pattern | r value |
|:---:|:---|:---:|
| I | Linear relationship with noise | ~0.816 |
| II | Clear curved (non-linear) relationship | ~0.816 |
| III | Perfectly linear with one large outlier | ~0.816 |
| IV | Vertical cluster with one outlier | ~0.816 |

**Lesson:** Pearson's `r = 0.816` describes all four datasets equally well mathematically - yet they are completely different visually. Always plot your data. Never rely on correlation alone.

---

## <span style="color:#1565C0">11. Complete Quick Reference</span>

### <span style="color:#2E86AB">11.1 Covariance Cheat Sheet</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 560px;">

### <span style="color:#D4A017">Cov(X,Y) = (1/(n-1)) · Σ(xᵢ - x̄)(yᵢ - ȳ)</span>

</div>

| Question | Answer |
|:---|:---|
| What does it measure? | Direction and joint magnitude of two variables changing together |
| Range | Unbounded (-∞ to +∞) |
| Positive covariance | Variables move in the same direction |
| Negative covariance | Variables move in opposite directions |
| Zero covariance | No linear co-movement (not necessarily independent) |
| Main limitation | Scale-dependent; magnitude is not interpretable alone |
| Used in | PCA, LDA, Mahalanobis distance, Gaussian models |

---

### <span style="color:#2E86AB">11.2 Correlation Cheat Sheet</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">r = Cov(X,Y) / (σₓ · σᵧ)     Range: [-1, +1]</span>

</div>

| Question | Answer |
|:---|:---|
| What does it measure? | Strength and direction of linear relationship |
| r = +1 | Perfect positive linear relationship |
| r = -1 | Perfect negative linear relationship |
| r = 0 | No linear relationship (may still have non-linear) |
| Scale-dependent? | No - always in [-1, +1] regardless of units |
| Pearson assumes | Linearity, normality, continuous data, no outliers |
| Spearman used when | Ordinal data, outliers, non-linear monotonic relationship |
| r ≠ causation | Correlation never implies causation |

---

### <span style="color:#2E86AB">11.3 ML Application Decision Table</span>

| Task | What to Compute | Threshold / Rule |
|:---|:---|:---|
| Feature redundancy removal | Pearson r between all feature pairs | Drop if |r| > 0.85 |
| Feature ranking for target | Pearson/Spearman with target | Higher |r| = stronger signal |
| Multicollinearity check | VIF per feature | Drop if VIF > 10 |
| PCA input | Covariance or correlation matrix | Use correlation if different units |
| Outlier detection | Mahalanobis distance via Cov matrix | Flag if D_M > threshold |
| Non-normal data | Spearman's ρ | Use instead of Pearson |
| Two binary features | Phi coefficient | Analogous to Pearson for binary |
| Model with normality assumption | Check Pearson normality assumption first | Transform if violated |

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