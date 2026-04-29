<div align="center">

# <span style="color:#0A2FA8">Supervised Learning Algorithms</span>

<sub>Linear Regression · Logistic Regression · Decision Trees · Random Forest · SVM · KNN · Naive Bayes · Gradient Boosting</sub>

</div>

---

## <span style="color:#1565C0">Algorithm 1 - Linear Regression</span>

> **Definition:** Linear Regression is a supervised learning algorithm that models the relationship between one or more input features and a continuous numerical output by fitting a straight line (or hyperplane) through the data.

It is the simplest and most foundational regression algorithm - the starting point for understanding all ML models.

---

### <span style="color:#2E86AB">1.1 Intuition</span>

Given a set of data points, the goal is to find the best-fitting line that minimizes the total error between the predicted values and the actual values.

```
Actual data:  (x₁,y₁), (x₂,y₂), ..., (xₙ,yₙ)
Goal:         Find line  ŷ = w₀ + w₁x  that best fits all points
```

**Example:** You have house sizes (sq ft) and their prices. Linear Regression finds the line that best predicts price from size.

---

### <span style="color:#2E86AB">1.2 Simple vs Multiple Linear Regression</span>

| Type | Features | Equation |
|:---|:---:|:---|
| Simple Linear Regression | 1 feature | ŷ = w₀ + w₁x |
| Multiple Linear Regression | n features | ŷ = w₀ + w₁x₁ + w₂x₂ + ... + wₙxₙ |

---

### <span style="color:#2E86AB">1.3 The Hypothesis Function</span>

> **Definition:** The hypothesis function h(x) is the model's prediction for a given input x.

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">ŷ = h(x) = w₀ + w₁x₁ + w₂x₂ + ... + wₙxₙ = wᵀx</span>

</div>

In vector form, adding a bias term x₀ = 1:

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">ŷ = wᵀx &nbsp;where w = [w₀, w₁, ..., wₙ]ᵀ and x = [1, x₁, ..., xₙ]ᵀ</span>

</div>

- `w₀` = bias / intercept (where the line crosses the y-axis)
- `w₁, w₂, ...` = weights / coefficients (slope - how much y changes per unit of x)

---

### <span style="color:#2E86AB">1.4 Cost Function - Mean Squared Error (MSE)</span>

> **Definition:** The cost function measures how wrong the model's predictions are across all training examples. Linear Regression uses Mean Squared Error (MSE).

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">J(w) = (1/2m) Σᵢ (ŷᵢ − yᵢ)² = (1/2m) Σᵢ (wᵀxᵢ − yᵢ)²</span>

</div>

- `m` = number of training examples
- The `1/2` factor is added for convenience - it cancels out when taking the derivative
- Squaring errors penalizes large errors more heavily and ensures the function is always positive
- Goal: Find weights **w** that minimize J(w)

---

### <span style="color:#2E86AB">1.5 Optimization - Gradient Descent</span>

> **Definition:** Gradient Descent is an iterative optimization algorithm that adjusts the model weights in the direction of the steepest descent of the cost function - i.e., in the direction that reduces error fastest.

#### <span style="color:#5B8DB8">Intuition</span>

Imagine standing on a hilly surface and wanting to reach the lowest point (minimum cost). Gradient Descent tells you: look around, find the steepest downhill direction, and take a small step in that direction. Repeat until you reach the bottom.

#### <span style="color:#5B8DB8">Derivative of the Cost Function</span>

Taking the partial derivative of J(w) with respect to weight wⱼ:

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">∂J/∂wⱼ = (1/m) Σᵢ (ŷᵢ − yᵢ) · xᵢⱼ</span>

</div>

#### <span style="color:#5B8DB8">Weight Update Rule</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">wⱼ := wⱼ − α · (∂J/∂wⱼ) = wⱼ − (α/m) Σᵢ (ŷᵢ − yᵢ) · xᵢⱼ</span>

</div>

where `α` (alpha) is the **learning rate** - how large a step to take.

| Learning rate α | Effect |
|:---:|:---|
| Too large | Overshoots minimum - diverges, cost increases |
| Too small | Takes forever to converge - very slow training |
| Just right | Steadily converges to the minimum |

#### <span style="color:#5B8DB8">Types of Gradient Descent</span>

| Type | Description | Pros | Cons |
|:---|:---|:---|:---|
| Batch GD | Uses all m training samples per update | Stable convergence | Very slow for large datasets |
| Stochastic GD (SGD) | Uses 1 random sample per update | Fast, good for large data | Very noisy updates |
| Mini-batch GD | Uses a small batch (32–512 samples) per update | Best of both worlds | Most common in practice |

---

### <span style="color:#2E86AB">1.6 Closed-Form Solution - Normal Equation</span>

> For linear regression, there exists an exact analytical solution - no iterative optimization needed.

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">w* = (XᵀX)⁻¹ Xᵀy</span>

</div>

where `X` is the design matrix (m × n+1), and `y` is the target vector (m × 1).

#### <span style="color:#5B8DB8">Derivation</span>

```
Cost in matrix form:    J(w) = (1/2m) ||Xw − y||²
                             = (1/2m) (Xw − y)ᵀ(Xw − y)

Take derivative:        ∂J/∂w = (1/m) Xᵀ(Xw − y)

Set to zero:            Xᵀ(Xw − y) = 0
                        XᵀXw = Xᵀy
                        w = (XᵀX)⁻¹ Xᵀy
```

| Method | When to use |
|:---|:---|
| Normal Equation | Small to medium datasets (n < 10,000 features) - exact, no tuning |
| Gradient Descent | Large datasets or many features - scalable, but needs tuning |

> **Limitation:** `(XᵀX)⁻¹` requires the matrix to be invertible. If features are linearly dependent (multicollinearity), the inverse does not exist.

---

### <span style="color:#2E86AB">1.7 Assumptions of Linear Regression</span>

| Assumption | Meaning |
|:---|:---|
| Linearity | The relationship between X and y is linear |
| Independence | Training examples are independent of each other |
| Homoscedasticity | Variance of residuals is constant across all values of X |
| Normality of residuals | Residuals (errors) are normally distributed |
| No multicollinearity | Input features are not highly correlated with each other |

> **Violating these assumptions** does not always break the model but does degrade performance and makes interpretations unreliable.

#### <span style="color:#5B8DB8">Checking Assumptions in Practice</span>

| Assumption | How to Check | Fix if Violated |
|:---|:---|:---|
| Linearity | Scatter plot of y vs ŷ, residual vs fitted plot | Add polynomial features, transform y |
| Homoscedasticity | Residual vs fitted plot (funnel shape = violation) | Log-transform y, use WLS |
| Normality of residuals | Q-Q plot, Shapiro-Wilk test | Log/Box-Cox transform |
| Multicollinearity | Variance Inflation Factor (VIF > 10 = problem) | Drop correlated features, use Ridge |
| Independence | Durbin-Watson test (for time series) | Add lag features, use time-series models |

#### <span style="color:#5B8DB8">Variance Inflation Factor (VIF)</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">VIF(xⱼ) = 1 / (1 − R²ⱼ)</span>

</div>

where R²ⱼ is the R² from regressing feature xⱼ on all other features. VIF > 10 indicates severe multicollinearity.

---

### <span style="color:#2E86AB">1.8 Regularization - Ridge, Lasso, Elastic Net</span>

Regularization adds a penalty to the cost function to prevent overfitting by discouraging excessively large weights.

#### <span style="color:#5B8DB8">Ridge Regression (L2 Regularization)</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">J(w) = (1/2m) Σ(ŷᵢ − yᵢ)² + λ Σ wⱼ²</span>

</div>

- Adds the sum of squared weights as penalty
- Shrinks weights toward zero but never exactly to zero
- Keeps all features - reduces their impact
- Use when: all features are potentially relevant

#### <span style="color:#5B8DB8">Lasso Regression (L1 Regularization)</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">J(w) = (1/2m) Σ(ŷᵢ − yᵢ)² + λ Σ |wⱼ|</span>

</div>

- Adds the sum of absolute weights as penalty
- Can drive weights exactly to zero → performs automatic feature selection
- Use when: you suspect only a few features are truly important (sparse model)

#### <span style="color:#5B8DB8">Elastic Net (L1 + L2)</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">J(w) = (1/2m) Σ(ŷᵢ − yᵢ)² + λ₁ Σ|wⱼ| + λ₂ Σwⱼ²</span>

</div>

- Combines L1 and L2 - gets both feature selection and weight shrinkage
- Use when: many features and some are correlated

| Regularization | Penalty | Effect on Weights | Use Case |
|:---|:---:|:---|:---|
| None (OLS) | - | Unconstrained | Small datasets, no overfitting |
| Ridge (L2) | Σwⱼ² | Shrinks toward 0 | All features relevant |
| Lasso (L1) | Σ\|wⱼ\| | Sets some to exactly 0 | Sparse feature importance |
| Elastic Net | L1 + L2 | Both effects | High-dimensional, correlated features |

---

### <span style="color:#2E86AB">1.9 Polynomial Regression</span>

> **Definition:** Polynomial Regression extends linear regression to model non-linear relationships by adding polynomial terms (x², x³, x₁x₂, etc.) as new features. The model is still linear in the weights — only the features are transformed.

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">ŷ = w₀ + w₁x + w₂x² + w₃x³ + ... + wₙxⁿ</span>

</div>

```
Original feature: x
After degree-2 polynomial transform: [1, x, x²]
After degree-2 with interaction (2 features x₁, x₂): [1, x₁, x₂, x₁², x₁x₂, x₂²]
```

| Degree | Fit | Risk |
|:---:|:---|:---|
| 1 (linear) | Straight line | Underfitting if data is curved |
| 2–3 | Gentle curves | Good for most non-linear patterns |
| High (5+) | Wiggly curves | Severe overfitting on training data |

**Rule:** Always combine polynomial features with regularization (Ridge or Lasso) to prevent overfitting.

---

### <span style="color:#2E86AB">1.10 Feature Scaling</span>

> **Why it matters:** Gradient Descent converges much faster when all features are on the same scale. Without scaling, features with large ranges dominate the cost function and the algorithm takes a very long path to the minimum.

#### <span style="color:#5B8DB8">Standardization (Z-score Normalization)</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">x' = (x − μ) / σ</span>

</div>

- Output: mean = 0, std = 1
- Best for: gradient descent, SVM, logistic regression, neural networks
- Not affected by outliers as much as MinMax

#### <span style="color:#5B8DB8">Min-Max Normalization</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">x' = (x − x_min) / (x_max − x_min)</span>

</div>

- Output: range [0, 1]
- Best for: when you need bounded outputs (neural network inputs, image pixels)
- Sensitive to outliers

#### <span style="color:#5B8DB8">Robust Scaler</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">x' = (x − median) / IQR</span>

</div>

- Uses median and interquartile range (IQR) — not affected by outliers
- Best for: datasets with many outliers

| Scaler | Formula | Outlier Robust | Output Range | Best For |
|:---|:---|:---:|:---|:---|
| StandardScaler | (x − μ)/σ | Moderate | No fixed range | Most ML algorithms |
| MinMaxScaler | (x − min)/(max − min) | No | [0, 1] | Neural networks, bounded inputs |
| RobustScaler | (x − median)/IQR | Yes | No fixed range | Data with outliers |

> **Important:** Always fit the scaler on the training set only, then transform both train and test. Fitting on the full dataset causes data leakage.

---

### <span style="color:#2E86AB">1.11 Evaluation Metrics</span>

| Metric | Formula | Interpretation |
|:---|:---|:---|
| MAE | (1/m) Σ \|yᵢ − ŷᵢ\| | Average absolute error - easy to interpret |
| MSE | (1/m) Σ (yᵢ − ŷᵢ)² | Penalizes large errors more |
| RMSE | √MSE | Same unit as y - most interpretable |
| R² | 1 − SS_res/SS_tot | Proportion of variance explained (0 to 1) |
| Adjusted R² | 1 − (1−R²)(m−1)/(m−n−1) | R² penalized for number of features |

> **Adjusted R²** should be used instead of R² when comparing models with different numbers of features — it penalizes adding features that don't improve the model.

---

### <span style="color:#2E86AB">1.12 Advantages and Disadvantages</span>

| <span style="color:#27AE60">Advantages</span> | <span style="color:#C0392B">Disadvantages</span> |
|:---|:---|
| Simple, fast, interpretable | Assumes linear relationship - fails on non-linear data |
| Works well when assumptions hold | Very sensitive to outliers (squared error) |
| Closed-form solution exists | Requires feature scaling for gradient descent |
| Good baseline model | Poor performance with many irrelevant features |
| Coefficients are meaningful | Struggles with multicollinearity |

---

### <span style="color:#2E86AB">1.13 Real-World Use Cases</span>

#### <span style="color:#5B8DB8">When to Use Linear Regression</span>

| Scenario | Why Linear Regression Works |
|:---|:---|
| House price prediction (size, rooms, age → price) | Continuous output, roughly linear relationship with features |
| Sales forecasting (ad spend → revenue) | Linear relationship between budget and return |
| Stock return estimation | Quantitative continuous target |
| Energy consumption prediction | Multiple continuous predictors, interpretability needed |
| Medical dosage prediction | Need interpretable, auditable coefficients |
| Baseline benchmark | Always run as a baseline before trying complex models |

#### <span style="color:#5B8DB8">When NOT to Use Linear Regression</span>

| Scenario | Better Alternative |
|:---|:---|
| Target is a category (spam/not spam) | Logistic Regression, Decision Tree |
| Strong non-linear patterns (exponential growth) | Polynomial Regression, Gradient Boosting |
| Many outliers in target | Huber Regression, tree-based models |
| High-dimensional data (text, images) | Ridge/Lasso, neural networks |
| Time-series with trends/seasonality | ARIMA, LSTM, Prophet |

#### <span style="color:#5B8DB8">Practical Tips</span>

```
1. Always plot y vs each feature first — check if relationship looks linear
2. Check and handle outliers before fitting (they distort coefficients badly)
3. Use VIF to check multicollinearity — drop or combine correlated features
4. If RMSE >> MAE, you likely have outliers driving the MSE up
5. Use Ridge as default regularization; switch to Lasso if you want feature selection
6. Log-transform skewed targets (prices, salaries, counts) — this often linearizes relationships
7. Always run on scaled features when using gradient descent
8. R² alone is misleading — always check residual plots
```

---

## <span style="color:#1565C0">Algorithm 2 - Logistic Regression</span>

> **Definition:** Logistic Regression is a supervised classification algorithm that models the probability that an input belongs to a particular class. Despite the name "regression," it is used for classification - it predicts a probability value between 0 and 1.

---

### <span style="color:#2E86AB">2.1 Why Not Linear Regression for Classification?</span>

If we use linear regression for classification (predicting 0 or 1), the model can output values like `-2.5` or `3.7` - which have no meaning as probabilities. We need a function that squashes any real number into the range `[0, 1]`.

---

### <span style="color:#2E86AB">2.2 The Sigmoid (Logistic) Function</span>

> **Definition:** The sigmoid function maps any real number z to a value between 0 and 1.

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">σ(z) = 1 / (1 + e⁻ᶻ)</span>

</div>

| z value | σ(z) output | Meaning |
|:---:|:---:|:---|
| z → +∞ | σ → 1 | Very confident it's class 1 |
| z = 0 | σ = 0.5 | Completely uncertain |
| z → −∞ | σ → 0 | Very confident it's class 0 |

**Key properties of sigmoid:**
- Output always in (0, 1) - interpretable as probability
- Differentiable - allows gradient descent
- Derivative: `σ'(z) = σ(z) · (1 − σ(z))` - elegant and computationally efficient

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">σ'(z) = σ(z) · (1 − σ(z))</span>

</div>

---

### <span style="color:#2E86AB">2.3 The Hypothesis Function</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">P(y=1 | x; w) = σ(wᵀx) = 1 / (1 + e^(−wᵀx))</span>

</div>

This gives the probability that the input x belongs to class 1.

**Prediction rule:**

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">ŷ = 1 if P(y=1|x) ≥ 0.5 (i.e., wᵀx ≥ 0) &nbsp;|&nbsp; ŷ = 0 otherwise</span>

</div>

---

### <span style="color:#2E86AB">2.4 Decision Boundary</span>

> **Definition:** The decision boundary is the surface (line in 2D, plane in 3D) that separates the two classes in feature space.

For logistic regression: decision boundary is where `wᵀx = 0`

- **Linear decision boundary:** Straight line - when raw features are used
- **Non-linear decision boundary:** Curved - when polynomial features are added (e.g., x₁², x₁x₂)

**Example:**
- `w₀ + w₁x₁ + w₂x₂ = 0` → straight line in 2D
- `w₀ + w₁x₁² + w₂x₂² = 0` → circle in 2D

---

### <span style="color:#2E86AB">2.5 Cost Function - Binary Cross-Entropy (Log Loss)</span>

> MSE cannot be used for logistic regression because the sigmoid function makes the cost function non-convex with many local minima. Instead, Log Loss is used - it is convex and ensures a single global minimum.

**Log Loss for a single example:**

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">L(ŷ, y) = −y·log(ŷ) − (1−y)·log(1−ŷ)</span>

</div>

**Intuition:**
- When y=1: Loss = `−log(ŷ)` → if ŷ→1, loss→0; if ŷ→0, loss→∞ (very wrong prediction)
- When y=0: Loss = `−log(1−ŷ)` → if ŷ→0, loss→0; if ŷ→1, loss→∞

**Full cost function over m examples:**

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">J(w) = −(1/m) Σᵢ [ yᵢ·log(ŷᵢ) + (1−yᵢ)·log(1−ŷᵢ) ]</span>

</div>

---

### <span style="color:#2E86AB">2.6 Gradient Descent for Logistic Regression</span>

Taking the partial derivative of the log loss cost function with respect to wⱼ:

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">∂J/∂wⱼ = (1/m) Σᵢ (ŷᵢ − yᵢ) · xᵢⱼ</span>

</div>

> Note: This has exactly the same form as the gradient for linear regression - the difference is that ŷ now passes through a sigmoid. The update rule is identical: `wⱼ := wⱼ − α · ∂J/∂wⱼ`

---

### <span style="color:#2E86AB">2.7 Odds and Log-Odds (Logit)</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">Odds = P(y=1) / P(y=0) &nbsp;|&nbsp; Log-Odds = log(P / (1−P)) = wᵀx</span>

</div>

This means logistic regression is actually a linear model - it models the log-odds of the outcome as a linear function of the features. The sigmoid is just the inverse of the logit.

**Interpretation of coefficients:** A one-unit increase in feature xⱼ multiplies the odds by `e^(wⱼ)`.

---

### <span style="color:#2E86AB">2.8 Multi-class Logistic Regression</span>

#### <span style="color:#5B8DB8">One-vs-Rest (OvR)</span>

Train K separate binary classifiers - each one learns to distinguish one class from all others. At prediction, use the classifier with the highest confidence.

```
3 classes: Dog, Cat, Bird
→ Classifier 1: Dog vs (Cat + Bird)
→ Classifier 2: Cat vs (Dog + Bird)
→ Classifier 3: Bird vs (Dog + Cat)
→ Predict the class with the highest probability
```

#### <span style="color:#5B8DB8">Softmax Regression (Multinomial Logistic Regression)</span>

> **Definition:** Softmax extends logistic regression to multiple classes by computing a probability distribution over all K classes simultaneously.

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">P(y=k | x) = e^(wₖᵀx) / Σⱼ e^(wⱼᵀx)</span>

</div>

- Outputs sum to 1 across all K classes
- Generalizes sigmoid (sigmoid is softmax for K=2)
- Cost function: Cross-Entropy Loss

---

### <span style="color:#2E86AB">2.9 Classification Evaluation Metrics</span>

> These metrics apply to all classification algorithms, not just logistic regression.

#### <span style="color:#5B8DB8">Confusion Matrix</span>

```
                    Predicted Positive    Predicted Negative
Actual Positive  |   TP (True Pos)    |   FN (False Neg)   |
Actual Negative  |   FP (False Pos)   |   TN (True Neg)    |
```

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">Precision = TP / (TP + FP) &nbsp;|&nbsp; Recall = TP / (TP + FN)</span>

</div>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">F1 Score = 2 · (Precision · Recall) / (Precision + Recall)</span>

</div>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">Accuracy = (TP + TN) / (TP + TN + FP + FN)</span>

</div>

| Metric | Focus | When to use |
|:---|:---|:---|
| Accuracy | Overall correctness | Balanced classes only |
| Precision | Minimize false positives | Spam detection (don't block real emails) |
| Recall | Minimize false negatives | Cancer detection (never miss a positive) |
| F1 Score | Balance precision & recall | Imbalanced datasets |
| AUC-ROC | Probability ranking quality | When threshold doesn't matter |

#### <span style="color:#5B8DB8">ROC Curve and AUC</span>

> **Definition:** The ROC (Receiver Operating Characteristic) curve plots the True Positive Rate (Recall) vs the False Positive Rate at all possible classification thresholds.

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">TPR = TP/(TP+FN) &nbsp;|&nbsp; FPR = FP/(FP+TN) &nbsp;|&nbsp; AUC = area under ROC curve</span>

</div>

| AUC Value | Interpretation |
|:---:|:---|
| 1.0 | Perfect classifier |
| 0.9 – 1.0 | Excellent |
| 0.7 – 0.9 | Good |
| 0.5 | Random guessing (useless model) |
| < 0.5 | Worse than random (labels may be flipped) |

#### <span style="color:#5B8DB8">Threshold Tuning</span>

The default threshold is 0.5, but this is often not optimal.

```
Lower threshold (e.g., 0.3):  Increases Recall, decreases Precision → use for cancer detection
Higher threshold (e.g., 0.7): Increases Precision, decreases Recall → use for spam filtering
```

Use precision-recall curve or business cost analysis to choose the optimal threshold.

---

### <span style="color:#2E86AB">2.10 Class Imbalance</span>

> **Problem:** In many real datasets (fraud detection, disease diagnosis), one class has far fewer examples than the other. A model can achieve 99% accuracy by predicting "not fraud" for every transaction — yet be completely useless.

#### <span style="color:#5B8DB8">Techniques to Handle Imbalance</span>

| Technique | Description | When to Use |
|:---|:---|:---|
| `class_weight='balanced'` | Sklearn auto-adjusts loss weights by class frequency | First thing to try, always |
| Oversampling (SMOTE) | Synthetically generates minority class samples | Moderate imbalance (1:10 to 1:100) |
| Undersampling | Randomly removes majority class samples | When dataset is very large |
| Threshold tuning | Adjust prediction threshold to favor minority class | Always combine with other methods |
| Use F1 / AUC-ROC | Use appropriate metrics instead of accuracy | Always when imbalanced |

```python
# sklearn example
from sklearn.linear_model import LogisticRegression
model = LogisticRegression(class_weight='balanced')
```

---

### <span style="color:#2E86AB">2.11 Advantages and Disadvantages</span>

| <span style="color:#27AE60">Advantages</span> | <span style="color:#C0392B">Disadvantages</span> |
|:---|:---|
| Outputs calibrated probabilities | Assumes linear decision boundary |
| Fast to train, very interpretable | Fails on complex non-linear patterns |
| Works well on linearly separable data | Sensitive to outliers and irrelevant features |
| Strong baseline classifier | Requires feature scaling |
| Regularization (L1/L2) well-supported | Not ideal for high-dimensional sparse data without tuning |

---

### <span style="color:#2E86AB">2.12 Real-World Use Cases</span>

#### <span style="color:#5B8DB8">When to Use Logistic Regression</span>

| Scenario | Why It Works |
|:---|:---|
| Email spam detection (binary) | Linear separability often holds with good features |
| Credit risk scoring (default/no default) | Interpretable coefficients required by regulators |
| Medical diagnosis screening (disease/no disease) | Probability output enables risk stratification |
| Customer churn prediction | Baseline model before trying complex approaches |
| Ad click-through rate prediction | Massive scale, needs fast inference |
| Sentiment analysis (positive/negative) | With TF-IDF features, often works very well |

#### <span style="color:#5B8DB8">When NOT to Use Logistic Regression</span>

| Scenario | Better Alternative |
|:---|:---|
| Target is continuous (price, salary) | Linear Regression |
| Complex non-linear class boundaries | SVM (RBF), Random Forest, XGBoost |
| Image classification | CNN (deep learning) |
| Very high-dimensional, sparse data | Naive Bayes, SVM |
| Strong feature interactions | Tree-based models |

#### <span style="color:#5B8DB8">Practical Tips</span>

```
1. Always use as a baseline — if it performs well, no need for complex models
2. Feature scale before fitting (StandardScaler)
3. Use C (inverse of λ) to control regularization — smaller C = stronger regularization
4. For imbalanced data: class_weight='balanced' is the easiest first fix
5. Examine coefficients to understand which features matter most
6. Use ROC-AUC as your primary metric, not accuracy
7. When adding polynomial features, always add regularization (Ridge/Lasso)
8. For multi-class: use multi_class='multinomial' + solver='lbfgs' in sklearn
```

---

## <span style="color:#1565C0">Algorithm 3 - Decision Trees</span>

> **Definition:** A Decision Tree is a supervised learning algorithm that learns a hierarchical set of if-else rules from the training data to make predictions. It splits the data recursively based on feature values to create a tree structure where each leaf node represents a prediction.

---

### <span style="color:#2E86AB">3.1 Structure of a Decision Tree</span>

```
Root Node (entire dataset)
    ├── Feature split condition (e.g., Age < 30?)
    │       ├── Yes → Internal Node → further splits
    │       └── No  → Internal Node → further splits
    │                       ├── ...
    │                       └── Leaf Node → Final Prediction
```

| Component | Description |
|:---|:---|
| Root node | Top node - represents the entire training dataset |
| Internal node | A node that contains a splitting condition on a feature |
| Branch | The outcome of a split condition (True or False) |
| Leaf node | Terminal node - contains the final prediction (class or value) |
| Depth | Number of levels from root to the deepest leaf |

---

### <span style="color:#2E86AB">3.2 How Does the Tree Decide Where to Split?</span>

The tree must choose: which feature to split on, and at what threshold. It selects the split that best separates the data - measured using impurity metrics.

> **Definition:** Impurity measures how mixed a node's samples are. A pure node contains only one class (zero impurity). A fully impure node has equal representation of all classes (maximum impurity).

---

### <span style="color:#2E86AB">3.3 Impurity Measures</span>

#### <span style="color:#5B8DB8">Gini Impurity</span>

> Used in CART (Classification and Regression Trees) - the algorithm behind scikit-learn's DecisionTreeClassifier.

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">Gini(t) = 1 − Σₖ pₖ²</span>

</div>

where `pₖ` = proportion of samples belonging to class k at node t.

**Example (Binary Classification):**
```
Node has 10 samples: 7 Class A, 3 Class B
p_A = 7/10 = 0.7,  p_B = 3/10 = 0.3
Gini = 1 − (0.7² + 0.3²) = 1 − (0.49 + 0.09) = 1 − 0.58 = 0.42

Pure node (all one class):  Gini = 1 − (1² + 0²) = 0  (perfect)
Maximally impure (50/50):   Gini = 1 − (0.5² + 0.5²) = 0.5
```

#### <span style="color:#5B8DB8">Entropy and Information Gain</span>

> Used in ID3 and C4.5 algorithms.

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">Entropy(t) = − Σₖ pₖ · log₂(pₖ)</span>

</div>

| Situation | Entropy value |
|:---|:---:|
| Pure node (all one class) | 0 (no uncertainty) |
| Maximally impure (equal all classes) | log₂(K) where K = number of classes |
| Binary, 50/50 split | 1.0 bit |

**Information Gain:**

> **Definition:** Information Gain measures how much a split reduces the entropy/impurity of the data.

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">IG(t, split) = Entropy(parent) − Σ (|child| / |parent|) · Entropy(child)</span>

</div>

The split with the **highest Information Gain** is chosen.

**Worked Example:**
```
Parent node: 10 samples, 5 Class A, 5 Class B
Entropy(parent) = −(0.5·log₂0.5 + 0.5·log₂0.5) = −(−0.5 + −0.5) = 1.0

Split on Feature X < 5:
  Left child:  6 samples, 5A, 1B → Entropy = −(5/6·log₂(5/6) + 1/6·log₂(1/6)) ≈ 0.65
  Right child: 4 samples, 0A, 4B → Entropy = 0 (pure)

Weighted entropy after split = (6/10)·0.65 + (4/10)·0 = 0.39

Information Gain = 1.0 − 0.39 = 0.61
```

#### <span style="color:#5B8DB8">Variance Reduction (for Regression Trees)</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">VarReduction = Var(parent) − Σ (|child| / |parent|) · Var(child)</span>

</div>

#### <span style="color:#5B8DB8">Gini vs Entropy — Practical Comparison</span>

| Aspect | Gini Impurity | Entropy |
|:---|:---|:---|
| Computation | Faster (no logarithm) | Slightly slower |
| Behavior | Similar splits in practice | More sensitive to class probabilities |
| Default | scikit-learn default | Used in ID3, C4.5 |
| Recommendation | Prefer Gini for speed | Use Entropy when class probabilities matter more |

> In practice, the two criteria produce very similar trees. Gini is slightly preferred due to lower computational cost.

---

### <span style="color:#2E86AB">3.4 The CART Algorithm</span>

> **Definition:** CART (Classification And Regression Trees) is the algorithm that builds binary decision trees by recursively selecting the best split at each node.

```
CART Algorithm:
1. Start with all training data at the root node
2. For every feature and every possible threshold:
     Compute the weighted Gini impurity (or variance) after the split
3. Choose the feature-threshold pair with lowest weighted impurity
4. Split the data into two child nodes
5. Repeat recursively for each child node
6. Stop when: max depth reached, min samples reached, or node is pure
7. Assign leaf prediction = majority class (classification) or mean value (regression)
```

---

### <span style="color:#2E86AB">3.5 Stopping Criteria and Pruning</span>

A fully grown tree memorizes the training data (overfits). Stopping criteria and pruning prevent this.

#### <span style="color:#5B8DB8">Stopping Criteria (Pre-pruning)</span>

| Hyperparameter | Effect |
|:---|:---|
| `max_depth` | Stop splitting when tree reaches this depth |
| `min_samples_split` | Only split if a node has at least this many samples |
| `min_samples_leaf` | A leaf must have at least this many samples |
| `max_features` | Consider only a subset of features at each split |
| `min_impurity_decrease` | Only split if the impurity decrease is above this threshold |

#### <span style="color:#5B8DB8">Post-pruning (Cost-Complexity Pruning)</span>

> Grow the full tree first, then remove branches that provide little predictive power.

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">Pruning criterion: R_α(T) = R(T) + α · |T_leaves|</span>

</div>

where `R(T)` is training error, `|T_leaves|` is number of leaves, and `α` is the complexity penalty.

---

### <span style="color:#2E86AB">3.6 Feature Importance from Decision Trees</span>

> **Definition:** A feature's importance in a decision tree is the total (weighted) impurity reduction it achieves across all nodes where it is used as a split feature.

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">Importance(fⱼ) = Σ_nodes_using_fⱼ (nₜ/m) · [Impurity(t) − (nₗ/nₜ)·Impurity(tₗ) − (nᵣ/nₜ)·Impurity(tᵣ)]</span>

</div>

- Features used near the root (early splits) generally have higher importance
- Normalized so all importances sum to 1
- A feature with zero importance was never used in any split

---

### <span style="color:#2E86AB">3.7 Advantages and Disadvantages</span>

| <span style="color:#27AE60">Advantages</span> | <span style="color:#C0392B">Disadvantages</span> |
|:---|:---|
| Highly interpretable - easy to visualize | Tends to overfit without pruning |
| No feature scaling needed | Very sensitive to small changes in data |
| Handles both numerical and categorical data | Creates biased trees with imbalanced classes |
| Implicitly performs feature selection | Non-optimal - greedy algorithm, not globally optimal |
| Non-linear decision boundaries | Unstable - high variance (solved by ensembles) |

---

### <span style="color:#2E86AB">3.8 Real-World Use Cases</span>

#### <span style="color:#5B8DB8">When to Use Decision Trees</span>

| Scenario | Why Decision Trees Work |
|:---|:---|
| Medical diagnosis with explainable rules | Rules like "if age > 50 AND cholesterol > 240 → high risk" are directly auditable |
| Customer segmentation | Clear rule-based segments easy to communicate to business stakeholders |
| Fraud detection rule extraction | Single tree can expose clear fraud patterns |
| Feature selection for other models | Use tree feature importances to prune irrelevant features |
| Teaching / understanding ML | Best algorithm for learning how ML splits work |
| Quick prototyping | Fast to train and interpret for exploratory analysis |

#### <span style="color:#5B8DB8">When NOT to Use Decision Trees</span>

| Scenario | Better Alternative |
|:---|:---|
| Need best accuracy on tabular data | Random Forest, XGBoost |
| Continuous smooth prediction surface | Linear/Polynomial Regression |
| High-dimensional data (text, images) | SVM, neural networks |
| Dataset is small and noisy | Logistic Regression (more stable) |

#### <span style="color:#5B8DB8">Practical Tips</span>

```
1. Always visualize the tree (max_depth=3 or 4) to sanity-check splits
2. Use max_depth=3 to 5 as first attempt — avoids immediate overfitting
3. min_samples_leaf=5 to 20 prevents fitting to individual noisy samples
4. Use class_weight='balanced' for imbalanced classification problems
5. Single trees are rarely deployed — use them as components in Random Forest or XGBoost
6. Use cost_complexity_pruning_path() in sklearn to find optimal alpha
7. Decision Trees need no feature scaling — raw features work fine
8. Check feature importances to discover which variables the tree relies on most
```

---

## <span style="color:#1565C0">Algorithm 4 - Random Forest</span>

> **Definition:** Random Forest is an ensemble learning algorithm that builds a large number of decision trees during training and outputs the mode of the classes (classification) or mean prediction (regression) of all individual trees.

It directly addresses the main weakness of Decision Trees - high variance and overfitting.

---

### <span style="color:#2E86AB">4.1 Ensemble Learning - The Core Idea</span>

> **Definition:** Ensemble learning combines multiple models (called base learners or weak learners) to produce a more accurate and robust model than any individual model alone.

**Wisdom of crowds:** Many uncorrelated, moderately accurate models collectively outperform a single highly accurate model.

The two main ensemble strategies:

| Strategy | Idea | Example |
|:---|:---|:---|
| Bagging | Train models in parallel on different data subsets | Random Forest |
| Boosting | Train models sequentially, each correcting previous errors | XGBoost, AdaBoost |

---

### <span style="color:#2E86AB">4.2 Bootstrap Aggregation (Bagging)</span>

> **Definition:** Bootstrapping is sampling with replacement - drawing n samples from a dataset of size n, where a sample can be drawn more than once.

```
Original dataset (n=1000 samples)
    ↓
Bootstrap Sample 1: draw 1000 samples with replacement → ~63% unique
Bootstrap Sample 2: draw 1000 samples with replacement → ~63% unique
...
Bootstrap Sample B: draw 1000 samples with replacement → ~63% unique

Train one Decision Tree on each bootstrap sample → B trees
Final prediction = Majority vote (classification) or Mean (regression)
```

> On average, each bootstrap sample contains approximately 63.2% of unique original samples. The remaining ~36.8% are called **Out-of-Bag (OOB)** samples.

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">P(sample not selected in one draw) = (1 − 1/n)ⁿ → e⁻¹ ≈ 0.368 as n→∞</span>

</div>

---

### <span style="color:#2E86AB">4.3 Random Forest - What Makes It Different from Bagging</span>

Bagging builds trees on different data subsets. Random Forest adds an additional layer of randomness: **at each split, only a random subset of features is considered.**

```
Standard Bagging:
  → Each tree uses all n features at every split

Random Forest:
  → Each tree uses a random subset of √n features (classification) or n/3 features (regression) at every split
```

> **Why does this help?** Without feature randomness, all trees would use the same dominant features and be highly correlated with each other. Correlated trees don't reduce variance. By randomly restricting features at each split, trees become diverse - they learn different patterns, and their errors cancel out.

---

### <span style="color:#2E86AB">4.4 Prediction - Aggregation</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">Classification: ŷ = mode{ h₁(x), h₂(x), ..., hB(x) } &nbsp;(majority vote)</span>

</div>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">Regression: ŷ = (1/B) Σᵦ hᵦ(x) &nbsp;(average of all tree predictions)</span>

</div>

---

### <span style="color:#2E86AB">4.5 Out-of-Bag (OOB) Error</span>

> **Definition:** Since each tree is trained on ~63% of the data, the remaining ~37% (OOB samples) can be used to evaluate that specific tree - without a separate validation set.

```
For each training sample i:
  → Predict using only the trees that did NOT include sample i in their bootstrap
  → Compare prediction to true label
OOB Error = average error across all training samples using their OOB predictions
```

OOB error is a reliable estimate of generalization error - often as good as k-fold cross-validation.

---

### <span style="color:#2E86AB">4.6 Feature Importance</span>

> **Definition:** Random Forest provides a natural way to rank feature importance based on how much each feature reduces impurity across all trees and all splits.

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">Importance(fⱼ) = (1/B) Σᵦ Σ_nodes (impurity_decrease at splits on fⱼ in tree b)</span>

</div>

- Normalized so all importances sum to 1
- Features that appear in early (high-level) splits and reduce impurity a lot are ranked highest

#### <span style="color:#5B8DB8">Permutation Importance</span>

> **Definition:** Permutation importance measures how much model performance drops when a single feature's values are randomly shuffled (destroying its predictive relationship with the target).

```
For each feature fⱼ:
  1. Compute baseline OOB score
  2. Randomly shuffle the values of fⱼ in OOB data
  3. Recompute OOB score
  4. Importance = drop in performance
```

Permutation importance is more reliable than impurity-based importance — impurity importance is biased toward high-cardinality features (features with many unique values).

---

### <span style="color:#2E86AB">4.7 Bias-Variance Tradeoff in Random Forest</span>

> **Definition:** The bias-variance tradeoff describes the tension between a model being too simple (high bias, underfitting) and too flexible (high variance, overfitting).

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">Total Error = Bias² + Variance + Irreducible Noise</span>

</div>

| Model | Bias | Variance | Notes |
|:---|:---:|:---:|:---|
| Single deep Decision Tree | Low | Very High | Overfits badly |
| Single shallow Decision Tree | High | Low | Underfits |
| Random Forest | Low | Low | Averaging reduces variance without increasing bias |

Averaging B uncorrelated predictions reduces variance by factor of 1/B, while keeping bias nearly unchanged.

---

### <span style="color:#2E86AB">4.8 Key Hyperparameters</span>

| Hyperparameter | Effect |
|:---|:---|
| `n_estimators` | Number of trees - more trees = more stable, diminishing returns after ~200 |
| `max_features` | Features considered at each split - lower = more diversity, higher = stronger trees |
| `max_depth` | Maximum depth per tree - controls overfitting |
| `min_samples_leaf` | Minimum samples in a leaf - smooths predictions |
| `bootstrap` | Whether to use bootstrap sampling - True for Random Forest |

---

### <span style="color:#2E86AB">4.9 Advantages and Disadvantages</span>

| <span style="color:#27AE60">Advantages</span> | <span style="color:#C0392B">Disadvantages</span> |
|:---|:---|
| Very high accuracy - one of the best general-purpose algorithms | Less interpretable than a single decision tree |
| Robust to overfitting - variance reduced by averaging | Slow to predict for very large forests |
| Built-in feature importance | High memory usage - stores all B trees |
| Handles missing values and outliers well | Not ideal for very high-dimensional sparse data |
| OOB error provides free cross-validation estimate | Less effective than boosting on structured tabular data |

---

### <span style="color:#2E86AB">4.10 Real-World Use Cases</span>

#### <span style="color:#5B8DB8">When to Use Random Forest</span>

| Scenario | Why Random Forest Works |
|:---|:---|
| Credit scoring / loan default prediction | High accuracy, handles mixed feature types, robust to outliers |
| Medical diagnosis (multi-feature) | Built-in feature importance guides doctors, robust performance |
| Fraud detection | Handles class imbalance well, fast to train |
| Stock price direction prediction | Non-linear patterns, many correlated features |
| Remote sensing / land classification | Handles high-dimensional feature sets |
| Feature selection for downstream models | Use RF importances to filter features before feeding into other models |
| Any tabular dataset as default model | Best "first serious model" for tabular data |

#### <span style="color:#5B8DB8">When NOT to Use Random Forest</span>

| Scenario | Better Alternative |
|:---|:---|
| Need maximum accuracy on tabular data | XGBoost / LightGBM (usually 1-5% better) |
| Need to explain individual predictions | Single Decision Tree or logistic regression |
| Very large dataset (millions of rows) | LightGBM (much faster) |
| Text / NLP data | Naive Bayes, Logistic Regression with TF-IDF, BERT |
| Image data | CNN (deep learning) |

#### <span style="color:#5B8DB8">Practical Tips</span>

```
1. Start with n_estimators=100, then increase if OOB error is still decreasing
2. max_features='sqrt' is best for classification; 'log2' for very high dimensions
3. Always enable oob_score=True to get a free validation score
4. Use permutation_importance (not impurity importance) for reliable feature rankings
5. Random Forest rarely overfits with more trees — but it can overfit with very deep trees
6. For imbalanced classes: class_weight='balanced_subsample' works well
7. Parallelizes perfectly: n_jobs=-1 uses all CPU cores
8. No need for feature scaling — trees are invariant to monotonic transformations
```

---

## <span style="color:#1565C0">Algorithm 5 - Support Vector Machine (SVM)</span>

> **Definition:** Support Vector Machine is a supervised learning algorithm that finds the optimal hyperplane that maximally separates two classes in feature space. It maximizes the margin between the closest data points of each class (called support vectors).

---

### <span style="color:#2E86AB">5.1 The Core Idea - Maximum Margin</span>

Many hyperplanes can separate two classes. SVM finds the one that is furthest from both classes - the hyperplane with the **maximum margin**.

```
Class A (●)  |  Decision Boundary  |  Class B (■)
             |←── Margin width ──→|
         Support vectors define the margin boundaries
```

> **Definition:** The margin is the perpendicular distance between the decision boundary and the nearest data point from each class. Support vectors are the data points lying exactly on the margin boundaries - they are the only points that define and influence the hyperplane.

---

### <span style="color:#2E86AB">5.2 Mathematical Formulation</span>

**The hyperplane equation:**

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">wᵀx + b = 0</span>

</div>

where `w` is the normal vector to the hyperplane and `b` is the bias.

**Decision rule:**
- Class +1 if: `wᵀx + b ≥ +1`
- Class -1 if: `wᵀx + b ≤ −1`

**The width of the margin:**

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">Margin width = 2 / ||w||</span>

</div>

**Maximizing the margin = Minimizing ||w||**

---

### <span style="color:#2E86AB">5.3 The Optimization Problem</span>

**Hard Margin SVM (linearly separable data):**

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">Minimize: (1/2)||w||² &nbsp; Subject to: yᵢ(wᵀxᵢ + b) ≥ 1 for all i</span>

</div>

This is a convex quadratic programming problem - it has a guaranteed unique global optimum.

---

### <span style="color:#2E86AB">5.4 Soft Margin SVM - Handling Non-separable Data</span>

Real data is rarely perfectly linearly separable. Soft Margin SVM allows some misclassifications by introducing **slack variables** ξᵢ ≥ 0.

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">Minimize: (1/2)||w||² + C · Σᵢ ξᵢ &nbsp; Subject to: yᵢ(wᵀxᵢ + b) ≥ 1 − ξᵢ, &nbsp; ξᵢ ≥ 0</span>

</div>

**The C parameter (regularization):**

| C value | Effect |
|:---:|:---|
| Large C | Small margin, fewer misclassifications - may overfit |
| Small C | Large margin, more misclassifications allowed - may underfit |
| C → ∞ | Hard margin SVM (no tolerance for errors) |

---

### <span style="color:#2E86AB">5.5 The Kernel Trick - Non-Linear SVM</span>

> **Definition:** The kernel trick maps data into a higher-dimensional feature space where it becomes linearly separable - without explicitly computing the coordinates in that space.

**The key insight:** The SVM optimization only needs dot products `xᵢᵀxⱼ` - not the individual feature vectors. A kernel function K(xᵢ, xⱼ) computes the dot product in the high-dimensional space directly.

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">K(xᵢ, xⱼ) = φ(xᵢ)ᵀ · φ(xⱼ) &nbsp; (dot product in transformed space)</span>

</div>

**Common Kernels:**

| Kernel | Formula | Use Case |
|:---|:---|:---|
| Linear | K(xᵢ, xⱼ) = xᵢᵀxⱼ | Linearly separable data |
| Polynomial | K(xᵢ, xⱼ) = (γ·xᵢᵀxⱼ + r)^d | Polynomial relationships |
| RBF / Gaussian | K(xᵢ, xⱼ) = exp(−γ·\|\|xᵢ−xⱼ\|\|²) | Most widely used - handles any shape |
| Sigmoid | K(xᵢ, xⱼ) = tanh(γ·xᵢᵀxⱼ + r) | Neural-network-like boundaries |

**RBF kernel intuition:** Points close together (small `||xᵢ−xⱼ||`) get a kernel value near 1 (similar). Points far apart get a value near 0 (different). γ controls the radius of influence of each support vector.

| γ value | Effect |
|:---:|:---|
| Large γ | Small radius - each point influences only its immediate neighbors - may overfit |
| Small γ | Large radius - smooth, wide decision boundaries - may underfit |

---

### <span style="color:#2E86AB">5.6 Multi-class SVM</span>

SVM is natively binary. For K-class problems, two strategies are used:

#### <span style="color:#5B8DB8">One-vs-Rest (OvR)</span>

Train K binary SVMs — each one separates one class from all others. Assign the class whose classifier outputs the largest margin score.

#### <span style="color:#5B8DB8">One-vs-One (OvO)</span>

Train K(K−1)/2 binary SVMs — one for every pair of classes. Use majority voting among all classifiers.

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">OvO classifiers needed = K(K−1)/2 &nbsp;(e.g., 10 classes → 45 classifiers)</span>

</div>

| Strategy | Classifiers | Training Data per Model | Preferred When |
|:---|:---:|:---|:---|
| One-vs-Rest (OvR) | K | Full dataset | K is small |
| One-vs-One (OvO) | K(K−1)/2 | Small subsets (2 classes each) | K is large, SVM default |

> scikit-learn uses OvO by default for multi-class SVM.

---

### <span style="color:#2E86AB">5.7 Support Vector Regression (SVR)</span>

> SVM can also be used for regression. SVR finds a function that fits within an ε-tube around the training data. Predictions outside the tube incur a penalty.

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">SVR: Minimize ||w||² &nbsp; Subject to: |yᵢ − wᵀxᵢ − b| ≤ ε</span>

</div>

---

### <span style="color:#2E86AB">5.8 Advantages and Disadvantages</span>

| <span style="color:#27AE60">Advantages</span> | <span style="color:#C0392B">Disadvantages</span> |
|:---|:---|
| Effective in high-dimensional spaces | Slow to train on large datasets (O(n²) to O(n³)) |
| Kernel trick handles non-linear data | Requires careful kernel and hyperparameter selection |
| Robust - only support vectors matter, not all points | Poor performance on overlapping classes |
| Global optimum guaranteed (convex problem) | Does not directly output probabilities |
| Works well on small-medium datasets | Sensitive to feature scaling (must normalize) |

---

### <span style="color:#2E86AB">5.9 Real-World Use Cases</span>

#### <span style="color:#5B8DB8">When to Use SVM</span>

| Scenario | Why SVM Works |
|:---|:---|
| Text classification (spam, sentiment) | High-dimensional sparse TF-IDF features — linear SVM excels |
| Image classification (small datasets) | Kernel SVM can learn complex boundaries without deep learning |
| Bioinformatics (gene expression classification) | High-dimensional, small n — SVM is ideal |
| Handwritten digit recognition (MNIST) | RBF kernel SVM was state-of-the-art before deep learning |
| Anomaly detection / novelty detection | One-Class SVM learns the boundary of normal data |
| Financial time series classification | Small datasets, well-defined margin problems |

#### <span style="color:#5B8DB8">When NOT to Use SVM</span>

| Scenario | Better Alternative |
|:---|:---|
| Large dataset (> 100K rows) | Logistic Regression, Random Forest, LightGBM |
| Need probability outputs directly | Logistic Regression, Random Forest |
| Many overlapping classes | Gradient Boosting |
| Real-time inference at scale | Logistic Regression (much faster prediction) |
| Mixed numeric + categorical data | Tree-based models |

#### <span style="color:#5B8DB8">Practical Tips</span>

```
1. ALWAYS scale features before SVM — it is mandatory (StandardScaler)
2. Start with linear kernel for text data — often beats RBF with TF-IDF
3. Use RBF kernel as default for tabular data when linear doesn't work
4. Tune C and γ together using GridSearchCV or RandomizedSearchCV
5. For large datasets (>50K): use LinearSVC (much faster than SVC)
6. SVM does not output probabilities — use predict_proba=True (uses Platt scaling)
7. One-Class SVM for outlier detection: train only on normal data, flag deviations
8. With RBF kernel: small γ → underfitting, large γ → overfitting (same as large C)
```

---

## <span style="color:#1565C0">Algorithm 6 - K-Nearest Neighbors (KNN)</span>

> **Definition:** K-Nearest Neighbors is a non-parametric, instance-based supervised learning algorithm that classifies or predicts a new data point based on the K most similar (nearest) training examples in the feature space.

KNN is a lazy learner - it does no explicit training. It memorizes the entire training dataset and makes predictions at query time.

```
Training phase:  Just store all (xᵢ, yᵢ) pairs - no model is built
Prediction phase: For a new point x:
  1. Compute distance from x to all training points
  2. Find the K nearest neighbors
  3. Return majority class (classification) or mean value (regression)
```

---

### <span style="color:#2E86AB">6.1 Distance Metrics</span>

The choice of distance metric fundamentally affects which points are considered "nearest."

#### <span style="color:#5B8DB8">Euclidean Distance (L2)</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">d(x, xᵢ) = √[ Σⱼ (xⱼ − xᵢⱼ)² ]</span>

</div>

- Standard straight-line distance
- Sensitive to scale - features must be normalized
- Most common choice

#### <span style="color:#5B8DB8">Manhattan Distance (L1)</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">d(x, xᵢ) = Σⱼ |xⱼ − xᵢⱼ|</span>

</div>

- Sum of absolute differences - like navigating a city grid
- Less sensitive to outliers than Euclidean

#### <span style="color:#5B8DB8">Minkowski Distance (General Form)</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">d(x, xᵢ) = ( Σⱼ |xⱼ − xᵢⱼ|^p )^(1/p)</span>

</div>

- p=1: Manhattan Distance
- p=2: Euclidean Distance
- p→∞: Chebyshev Distance (maximum single-dimension difference)

#### <span style="color:#5B8DB8">Cosine Similarity</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">cos(x, xᵢ) = (x · xᵢ) / (||x|| · ||xᵢ||)</span>

</div>

- Measures angle between vectors - ignores magnitude
- Best for text/high-dimensional sparse data (TF-IDF, word vectors)

---

### <span style="color:#2E86AB">6.2 Choosing K</span>

| K value | Effect | Risk |
|:---:|:---|:---|
| K = 1 | Memorizes training data exactly | Maximum overfitting - very sensitive to noise |
| K = 3 to 7 | Local decision boundary | Moderate variance and bias |
| Large K | Very smooth decision boundary | Underfitting - too many neighbors dilute local patterns |
| K = n | Predicts the global majority class for every point | Complete underfit |

**Rule of thumb:** Start with K = √n where n is the number of training samples. Always use odd K for binary classification to avoid ties.

**Finding optimal K:** Use cross-validation - plot validation error vs K and pick the K at the elbow point.

---

### <span style="color:#2E86AB">6.3 Weighted KNN</span>

> Standard KNN treats all K neighbors equally. Weighted KNN gives more influence to closer neighbors.

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">Weight of neighbor i = 1 / d(x, xᵢ)² &nbsp; (inverse distance weighting)</span>

</div>

---

### <span style="color:#2E86AB">6.4 Curse of Dimensionality</span>

> **Definition:** In high-dimensional spaces, the concept of "nearest neighbor" breaks down. All points become approximately equidistant from each other, making distance-based comparisons meaningless.

As dimensions increase:
- Volume of space grows exponentially
- Data becomes increasingly sparse
- Distance between nearest and furthest points becomes negligible
- KNN requires exponentially more data to maintain the same density

**Mitigation:** Dimensionality reduction (PCA) before applying KNN.

---

### <span style="color:#2E86AB">6.5 Computational Complexity</span>

| Operation | Standard KNN | KD-Tree / Ball Tree |
|:---|:---:|:---:|
| Training | O(1) | O(n log n) to build |
| Prediction | O(n·d) per query | O(log n · d) per query |

For large datasets, use approximate nearest neighbor structures like Annoy, FAISS, or sklearn's `KDTree`.

---

### <span style="color:#2E86AB">6.6 Advantages and Disadvantages</span>

| <span style="color:#27AE60">Advantages</span> | <span style="color:#C0392B">Disadvantages</span> |
|:---|:---|
| No training phase - simple to implement | Very slow prediction for large datasets |
| Naturally handles multi-class problems | High memory - stores all training data |
| Non-parametric - no assumptions about data shape | Performance degrades in high dimensions |
| Adapts to new data immediately (just add to memory) | Sensitive to irrelevant and redundant features |
| Works well with small, low-dimensional datasets | Requires feature scaling - mandatory |

---

### <span style="color:#2E86AB">6.7 Real-World Use Cases</span>

#### <span style="color:#5B8DB8">When to Use KNN</span>

| Scenario | Why KNN Works |
|:---|:---|
| Recommendation systems (collaborative filtering) | Users with similar rating history → recommend what similar users liked |
| Anomaly detection | Points far from all neighbors = anomalies |
| Image recognition (small datasets) | Pixel similarity works well when n is small |
| Imputing missing values | Replace missing value with average of K nearest neighbors |
| Medical record similarity search | Find patients with similar diagnostic profiles |
| Baseline for small, low-dimensional datasets | Fast to implement, often surprisingly competitive |

#### <span style="color:#5B8DB8">When NOT to Use KNN</span>

| Scenario | Better Alternative |
|:---|:---|
| Large dataset (>50K rows) | Random Forest, Gradient Boosting (much faster) |
| High-dimensional data (text, images) | SVM, neural networks (curse of dimensionality kills KNN) |
| Real-time predictions | Any parametric model (KNN must scan all training data) |
| Irrelevant features present | Remove features first, or use feature-selection + KNN |
| Imbalanced classes | Models with class_weight support (RF, LogReg) |

#### <span style="color:#5B8DB8">Practical Tips</span>

```
1. ALWAYS scale features (StandardScaler or MinMaxScaler) — mandatory for KNN
2. Use odd K values for binary classification to break ties
3. Start with K = sqrt(n_train), then tune via cross-validation
4. Use weights='distance' for weighted KNN (almost always better than uniform)
5. Reduce dimensionality with PCA before KNN if d > 20
6. Use algorithm='kd_tree' or 'ball_tree' for faster prediction (beats brute force)
7. Remove irrelevant features before KNN — they distort distances badly
8. KNN with cosine distance works well for document similarity
```

---

## <span style="color:#1565C0">Algorithm 7 - Naive Bayes</span>

> **Definition:** Naive Bayes is a probabilistic supervised learning algorithm based on Bayes' Theorem. It classifies a new data point by computing the posterior probability of each class and choosing the class with the highest probability. It is "naive" because it assumes all features are conditionally independent given the class label.

---

### <span style="color:#2E86AB">7.1 Bayes' Theorem</span>

> **Definition:** Bayes' Theorem describes the probability of an event given prior knowledge of related conditions.

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">P(y | x) = P(x | y) · P(y) / P(x)</span>

</div>

| Term | Name | Meaning |
|:---|:---|:---|
| P(y \| x) | Posterior | Probability of class y given features x - what we want |
| P(x \| y) | Likelihood | Probability of observing x given it belongs to class y |
| P(y) | Prior | Probability of class y regardless of features |
| P(x) | Evidence | Probability of observing x - same for all classes, can be ignored |

**For classification, we compare posteriors across all classes:**

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">ŷ = argmax_y P(y | x) = argmax_y P(x | y) · P(y)</span>

</div>

---

### <span style="color:#2E86AB">7.2 The Naive Independence Assumption</span>

Computing P(x | y) for a full feature vector x is computationally intractable for large feature spaces. The "naive" assumption solves this:

> **The Naive Assumption:** All features x₁, x₂, ..., xₙ are conditionally independent given the class label y.

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">P(x | y) = P(x₁|y) · P(x₂|y) · ... · P(xₙ|y) = Πᵢ P(xᵢ | y)</span>

</div>

**The full Naive Bayes classifier:**

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">ŷ = argmax_y P(y) · Πᵢ P(xᵢ | y)</span>

</div>

---

### <span style="color:#2E86AB">7.3 Log Probabilities - Avoiding Underflow</span>

Multiplying many small probabilities (each < 1) results in extremely small numbers that underflow to zero in floating-point arithmetic. Convert to log space:

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">ŷ = argmax_y [ log P(y) + Σᵢ log P(xᵢ | y) ]</span>

</div>

Multiplication → Addition in log space. This is how all practical implementations work.

---

### <span style="color:#2E86AB">7.4 Worked Example - Spam Detection</span>

```
Training data:
  Spam emails:     100 emails
  Not-spam emails: 400 emails

Prior probabilities:
  P(Spam) = 100/500 = 0.2
  P(Not-Spam) = 400/500 = 0.8

Word "free":
  P("free" | Spam) = 0.6  (60% of spam emails contain "free")
  P("free" | Not-Spam) = 0.05

Word "meeting":
  P("meeting" | Spam) = 0.02
  P("meeting" | Not-Spam) = 0.4

New email contains: ["free", "meeting"]

P(Spam | email) ∝ P(Spam) · P("free"|Spam) · P("meeting"|Spam)
                = 0.2 × 0.6 × 0.02 = 0.0024

P(Not-Spam | email) ∝ P(Not-Spam) · P("free"|Not-Spam) · P("meeting"|Not-Spam)
                    = 0.8 × 0.05 × 0.4 = 0.016

Since 0.016 > 0.0024 → Prediction: Not Spam ✓
```

---

### <span style="color:#2E86AB">7.5 Laplace Smoothing</span>

> **Problem:** If a word never appeared in training for a given class, its probability is 0. This makes the entire product zero - one unseen word destroys the prediction.

> **Solution (Laplace Smoothing / Add-1 Smoothing):** Add a small count α (typically 1) to every feature count.

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">P(xᵢ | y) = (count(xᵢ, y) + α) / (count(y) + α · |V|)</span>

</div>

where `|V|` is the vocabulary size (number of unique features) and `α = 1` for Laplace smoothing.

---

### <span style="color:#2E86AB">7.6 Types of Naive Bayes</span>

| Type | Assumption for P(xᵢ \| y) | Best for |
|:---|:---|:---|
| Gaussian NB | Features follow a Gaussian (normal) distribution | Continuous numerical features |
| Multinomial NB | Features are counts (word frequencies) | Text classification with word counts |
| Bernoulli NB | Features are binary (word present or absent) | Text classification with binary word flags |
| Complement NB | Uses complement class statistics - better for imbalanced text | Imbalanced text datasets |

**Gaussian Naive Bayes - likelihood:**

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">P(xᵢ | y) = (1 / √(2πσ²_y)) · exp(−(xᵢ − μ_y)² / 2σ²_y)</span>

</div>

---

### <span style="color:#2E86AB">7.7 Naive Bayes with TF-IDF</span>

> **Definition:** TF-IDF (Term Frequency-Inverse Document Frequency) weighs words by their importance in a document relative to the entire corpus.

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">TF-IDF(t, d) = TF(t, d) × log(N / df(t))</span>

</div>

where `TF(t,d)` = frequency of term t in document d, `N` = total documents, `df(t)` = documents containing term t.

- Common words like "the", "is" get low IDF — they appear everywhere
- Rare, specific words get high IDF — they distinguish documents
- Combining TF-IDF vectors with Multinomial or Complement NB gives strong text classification results

```
Pipeline for text classification:
Raw Text → Tokenization → Remove Stopwords → TF-IDF Vectorizer → Naive Bayes Classifier
```

---

### <span style="color:#2E86AB">7.8 Advantages and Disadvantages</span>

| <span style="color:#27AE60">Advantages</span> | <span style="color:#C0392B">Disadvantages</span> |
|:---|:---|
| Extremely fast - O(n·d) training | Naive independence assumption is almost never true |
| Works well with very small datasets | Cannot capture feature correlations |
| Excellent for text classification (spam, sentiment) | Gaussian NB: assumes normal distribution - may not hold |
| Naturally handles multi-class problems | Zero-frequency problem without Laplace smoothing |
| Robust to irrelevant features | Probability estimates are often poorly calibrated |

---

### <span style="color:#2E86AB">7.9 Real-World Use Cases</span>

#### <span style="color:#5B8DB8">When to Use Naive Bayes</span>

| Scenario | Why Naive Bayes Works |
|:---|:---|
| Email spam filtering | Fast, effective with word-presence features (Bernoulli NB) |
| Sentiment analysis (positive/negative reviews) | Word bag features with Multinomial NB |
| News article categorization | High-dimensional text, Multinomial NB excels |
| Real-time text stream classification | Sub-millisecond prediction latency |
| Medical diagnosis (symptom → disease) | When features are genuinely independent (e.g., independent symptoms) |
| Language detection | Character n-gram features + Multinomial NB |
| Very small datasets | Strong prior makes NB work when other models overfit |

#### <span style="color:#5B8DB8">When NOT to Use Naive Bayes</span>

| Scenario | Better Alternative |
|:---|:---|
| Features are strongly correlated | Logistic Regression, SVM, tree models |
| Continuous, non-Gaussian numerical features | SVM, Random Forest |
| Need well-calibrated probability outputs | Logistic Regression (NB probabilities are often extreme) |
| Regression task | Linear Regression |
| Complex interactions between features | Tree-based models, neural networks |

#### <span style="color:#5B8DB8">Practical Tips</span>

```
1. For text data: Multinomial NB + TF-IDF is your fastest, strongest baseline
2. Always apply Laplace smoothing (alpha=1.0) — it is the default in sklearn
3. For binary word features (word present/absent): use BernoulliNB
4. For word counts or TF-IDF weights: use MultinomialNB
5. For continuous features: use GaussianNB
6. For imbalanced text: try ComplementNB — often outperforms MultinomialNB
7. Calibrate probabilities with CalibratedClassifierCV if you need accurate probabilities
8. Feature selection (remove very rare/common words) significantly improves NB
```

---

## <span style="color:#1565C0">Algorithm 8 - Gradient Boosting (XGBoost, LightGBM)</span>

> **Definition:** Gradient Boosting is an ensemble technique that builds models sequentially - each new model is trained to correct the errors (residuals) made by the combination of all previous models. It uses gradient descent in function space to minimize a differentiable loss function.

---

### <span style="color:#2E86AB">8.1 The Boosting Idea</span>

Unlike Bagging (trains models in parallel on different data subsets), Boosting trains models sequentially - each model focuses on the mistakes of its predecessors.

```
Model 1: Trained on original data → makes some errors
Model 2: Trained to fix Model 1's errors → makes different errors
Model 3: Trained to fix Model 1+2's errors → ...
...
Final prediction = weighted sum of all models
```

---

### <span style="color:#2E86AB">8.2 AdaBoost - The Original Boosting Algorithm</span>

> **Definition:** AdaBoost (Adaptive Boosting) trains weak learners sequentially. After each learner, it increases the weight of misclassified examples so the next learner focuses more on them.

```
Initialize: equal weights wᵢ = 1/m for all training examples

For t = 1 to T:
  1. Train weak learner hₜ on weighted data
  2. Compute weighted error: εₜ = Σᵢ wᵢ · 1[hₜ(xᵢ) ≠ yᵢ]
  3. Compute learner weight: αₜ = (1/2) · log((1 − εₜ) / εₜ)
  4. Update example weights: wᵢ ← wᵢ · exp(−αₜ · yᵢ · hₜ(xᵢ))
  5. Normalize weights so they sum to 1

Final prediction: H(x) = sign( Σₜ αₜ · hₜ(x) )
```

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">αₜ = (1/2) · ln( (1 − εₜ) / εₜ ) &nbsp;- higher weight for more accurate learners</span>

</div>

---

### <span style="color:#2E86AB">8.3 Gradient Boosting - The General Framework</span>

> **Definition:** Gradient Boosting generalizes AdaBoost by framing boosting as gradient descent in function space. Each new weak learner is trained to fit the negative gradient of the loss function with respect to the current model's predictions - called pseudo-residuals.

```
Initialize: F₀(x) = argmin_γ Σᵢ L(yᵢ, γ) (constant prediction that minimizes loss)

For t = 1 to T:
  1. Compute pseudo-residuals (negative gradient of loss):
        rᵢₜ = −∂L(yᵢ, F(xᵢ)) / ∂F(xᵢ)   for each training example i

  2. Fit a weak learner (regression tree) hₜ to the pseudo-residuals {(xᵢ, rᵢₜ)}

  3. Compute the optimal step size (learning rate for this tree):
        γₜ = argmin_γ Σᵢ L(yᵢ, Fₜ₋₁(xᵢ) + γ · hₜ(xᵢ))

  4. Update the model:
        Fₜ(x) = Fₜ₋₁(x) + η · γₜ · hₜ(x)

Final model: F_T(x) = F₀(x) + η · Σₜ γₜ · hₜ(x)
```

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">Fₜ(x) = Fₜ₋₁(x) + η · hₜ(x) &nbsp;where hₜ fits pseudo-residuals rᵢₜ = −∂L/∂F</span>

</div>

**For MSE loss (regression):**
```
L(y, F) = (1/2)(y − F)²
∂L/∂F = F − y
Pseudo-residuals = −(F − y) = y − F  ← just the actual residuals
```

So for regression with MSE, gradient boosting simply fits each new tree to the residuals of the previous ensemble. For other loss functions, the pseudo-residuals are the generalized gradients.

**The η (learning rate / shrinkage) parameter:**
- Controls how much each tree contributes to the final model
- Small η = more trees needed but better generalization
- Large η = fewer trees but risk of overfitting
- Typical values: 0.01 to 0.3

---

### <span style="color:#2E86AB">8.4 XGBoost - eXtreme Gradient Boosting</span>

> **Definition:** XGBoost is an optimized, scalable implementation of gradient boosting that adds regularization, second-order gradients, and system-level optimizations to make it faster and more accurate than standard gradient boosting.

#### <span style="color:#5B8DB8">Key Innovations in XGBoost over Standard GBM</span>

**1. Second-order Taylor Approximation of the Loss:**

Standard GBM uses only the first derivative (gradient). XGBoost uses both the gradient and the Hessian (second derivative):

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">L ≈ Σᵢ [gᵢ·f(xᵢ) + (1/2)·hᵢ·f(xᵢ)²] + Ω(f)</span>

</div>

where `gᵢ = ∂L/∂F̂` (first derivative / gradient) and `hᵢ = ∂²L/∂F̂²` (second derivative / Hessian).

Using the Hessian enables more accurate step sizes and faster convergence.

**2. Regularization Term Ω(f) built into the objective:**

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">Ω(f) = γ·T + (1/2)·λ·Σⱼ wⱼ² &nbsp;(T = number of leaves, wⱼ = leaf weights)</span>

</div>

- γ penalizes the number of leaves (tree complexity)
- λ penalizes large leaf weight values (L2 regularization on outputs)

**3. Gain score for split selection:**

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">Gain = (1/2) · [ GL²/(HL+λ) + GR²/(HR+λ) − (GL+GR)²/(HL+HR+λ) ] − γ</span>

</div>

where GL, GR = sum of gradients in left/right child; HL, HR = sum of Hessians.

**4. System-level optimizations:**
- Parallel tree construction (split finding in parallel across features)
- Block structure for out-of-core computing (data larger than RAM)
- Sparsity-aware split finding (handles missing values natively)
- Cache-optimized data access

#### <span style="color:#5B8DB8">Key XGBoost Hyperparameters</span>

| Hyperparameter | Effect |
|:---|:---|
| `n_estimators` | Number of trees |
| `learning_rate` (η) | Shrinkage - smaller = better generalization, more trees needed |
| `max_depth` | Depth of each tree - 3 to 10 typical |
| `min_child_weight` | Minimum sum of Hessian in a leaf - controls overfitting |
| `subsample` | Fraction of training samples for each tree (0.5–1.0) |
| `colsample_bytree` | Fraction of features for each tree |
| `gamma` (γ) | Minimum gain needed for a split |
| `lambda` (λ) | L2 regularization on leaf weights |
| `alpha` | L1 regularization on leaf weights |

---

### <span style="color:#2E86AB">8.5 LightGBM - Light Gradient Boosting Machine</span>

> **Definition:** LightGBM is a gradient boosting framework by Microsoft that uses two novel techniques - Gradient-based One-Side Sampling (GOSS) and Exclusive Feature Bundling (EFB) - to train much faster than XGBoost while maintaining similar accuracy.

#### <span style="color:#5B8DB8">Key Innovations in LightGBM</span>

**1. Leaf-wise (Best-First) Tree Growth** vs XGBoost's Level-wise growth:

```
Level-wise (XGBoost):        Leaf-wise (LightGBM):

Level 0:      [Root]           [Root]
Level 1:   [L1]   [R1]      [L1]   [R1]
Level 2: [LL][LR][RL][RR]  [LL][LR]
                               (only the leaf with highest gain is split)
```

- Level-wise grows the full level before going deeper → balanced tree, safer
- Leaf-wise always splits the leaf with the maximum loss reduction → asymmetric tree, faster, often more accurate

**2. Gradient-based One-Side Sampling (GOSS):**

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">GOSS: Keep top a% large-gradient samples + random b% small-gradient samples</span>

</div>

Instances with large gradients contribute more to information gain. Small-gradient instances can be sampled - this reduces data while preserving information.

**3. Exclusive Feature Bundling (EFB):**

In high-dimensional sparse data (text features, one-hot encoded), many features are mutually exclusive (rarely non-zero at the same time). EFB bundles them into single features - reduces the number of features without loss of information.

#### <span style="color:#5B8DB8">LightGBM vs XGBoost Comparison</span>

| Aspect | XGBoost | LightGBM |
|:---|:---|:---|
| Tree growth | Level-wise | Leaf-wise |
| Training speed | Slower | Much faster (10x+) |
| Memory usage | Higher | Lower |
| Accuracy | Very high | Comparable or higher |
| Large datasets | Good | Excellent |
| Categorical features | Requires encoding | Native support |
| Overfitting risk | Lower | Higher (leaf-wise) - need `num_leaves` tuning |

#### <span style="color:#5B8DB8">Key LightGBM Hyperparameters</span>

| Hyperparameter | Effect |
|:---|:---|
| `n_estimators` | Number of boosting rounds |
| `learning_rate` | Shrinkage - smaller = better generalization |
| `num_leaves` | Maximum number of leaves per tree - key parameter (default 31) |
| `max_depth` | Maximum depth to control `num_leaves` growth |
| `min_child_samples` | Minimum samples in a leaf |
| `subsample` | Row sampling fraction per tree |
| `colsample_bytree` | Feature sampling fraction per tree |
| `reg_alpha` | L1 regularization |
| `reg_lambda` | L2 regularization |

---

### <span style="color:#2E86AB">8.6 CatBoost</span>

> **Definition:** CatBoost (Categorical Boosting) is a gradient boosting library by Yandex that natively handles categorical features without manual encoding, using a technique called ordered target statistics.

#### <span style="color:#5B8DB8">Key Innovations in CatBoost</span>

**1. Ordered Target Statistics (Ordered Encoding):**

Instead of traditional label/one-hot encoding, CatBoost encodes each categorical value using the target mean of previous samples only (to avoid target leakage).

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">cat_encoding(xᵢ) = (Σⱼ<ᵢ [yⱼ | catⱼ = catᵢ] + prior) / (count(catᵢ among j<i) + 1)</span>

</div>

**2. Symmetric (Oblivious) Trees:**

CatBoost builds symmetric trees where the same split condition is used at every node in the same level. This makes prediction very fast (log₂(depth) comparisons) and reduces overfitting.

**3. Ordered Boosting:**

Uses a random permutation of training data so each model is trained on data that hasn't been used to compute its target statistics — prevents target leakage.

#### <span style="color:#5B8DB8">XGBoost vs LightGBM vs CatBoost Comparison</span>

| Aspect | XGBoost | LightGBM | CatBoost |
|:---|:---|:---|:---|
| Categorical features | Manual encoding | Manual encoding | Native support |
| Training speed | Medium | Fast | Medium-Slow |
| Accuracy on tabular | Very high | Very high | Very high |
| Overfitting resistance | Good | Needs tuning | Very good |
| GPU support | Yes | Yes | Yes |
| Best for | General tabular | Large datasets | Datasets with many categoricals |

---

### <span style="color:#2E86AB">8.7 Early Stopping</span>

> **Definition:** Early stopping monitors performance on a validation set during training and halts when performance stops improving — preventing overfitting without manual tuning of `n_estimators`.

```python
# XGBoost example
model = XGBClassifier(n_estimators=1000, learning_rate=0.01)
model.fit(X_train, y_train,
          eval_set=[(X_val, y_val)],
          early_stopping_rounds=50,  # Stop if no improvement for 50 rounds
          verbose=100)

# Best iteration is saved: model.best_iteration
```

| Parameter | Meaning |
|:---|:---|
| `early_stopping_rounds=50` | Stop after 50 consecutive rounds without improvement |
| `eval_metric` | Metric to monitor (logloss, rmse, auc, etc.) |
| `best_iteration` | The optimal number of trees found |

**Best practice workflow:**
```
1. Set n_estimators=1000 (large upper bound)
2. Set learning_rate=0.01 (small — more trees, better generalization)
3. Enable early stopping with a held-out validation set
4. Let the model find the optimal n_estimators automatically
```

---

### <span style="color:#2E86AB">8.8 Advantages and Disadvantages of Gradient Boosting</span>

| <span style="color:#27AE60">Advantages</span> | <span style="color:#C0392B">Disadvantages</span> |
|:---|:---|
| State-of-the-art on tabular / structured data | More hyperparameters to tune than Random Forest |
| Handles mixed data types, missing values | Prone to overfitting with too many trees and large depth |
| Built-in L1/L2 regularization | Harder to interpret than single decision trees |
| Feature importance rankings | Sequential training - cannot be fully parallelized |
| Excellent on small-medium datasets | Slower than Random Forest (especially standard GBM) |

---

### <span style="color:#2E86AB">8.9 Real-World Use Cases</span>

#### <span style="color:#5B8DB8">When to Use Gradient Boosting</span>

| Scenario | Why Gradient Boosting Works |
|:---|:---|
| Kaggle / ML competitions (tabular data) | Consistently wins on structured data tasks |
| Credit default risk prediction | Best accuracy on mixed numerical/categorical data |
| Click-through rate (CTR) prediction | Industry standard at major tech companies |
| Demand/sales forecasting | Strong handling of non-linear patterns and interactions |
| Medical outcome prediction | Mixed data types, high accuracy needed |
| Insurance claim prediction | High-stakes decision requires best accuracy |
| Anomaly/fraud detection | Ensemble catches subtle patterns |

#### <span style="color:#5B8DB8">When NOT to Use Gradient Boosting</span>

| Scenario | Better Alternative |
|:---|:---|
| Need interpretability / regulatory compliance | Logistic Regression, single Decision Tree |
| Image / audio / video data | CNNs, RNNs (deep learning) |
| Text classification | Naive Bayes, BERT, Logistic Regression + TF-IDF |
| Huge datasets (100M+ rows) | LightGBM with careful settings, or distributed systems |
| Real-time ultra-low latency inference | Logistic Regression, linear SVM |
| Very small datasets (<200 samples) | Logistic Regression, SVM, Naive Bayes |

#### <span style="color:#5B8DB8">Practical Tips</span>

```
1. Choose LightGBM as default over XGBoost — it is faster and equally accurate
2. Use CatBoost when you have many categorical features and don't want to preprocess them
3. Always use early stopping — set n_estimators=1000, learning_rate=0.01, early_stopping_rounds=50
4. Tune in this order: max_depth / num_leaves → min_child_weight → subsample → colsample_bytree → learning_rate
5. Start with max_depth=4 to 6 for XGBoost; num_leaves=31 to 63 for LightGBM
6. Subsample=0.8 and colsample_bytree=0.8 often improve generalization
7. Feature importance: use SHAP values for reliable, interpretable importance (not default impurity)
8. Always hold out a validation set — do NOT use cross-validation inside early stopping
```

---

## <span style="color:#1565C0">Master Comparison - All 8 Algorithms</span>

| Algorithm | Type | Interpretable | Scaling Needed | Handles Non-linear | Best Dataset Size | Key Strength |
|:---|:---:|:---:|:---:|:---:|:---:|:---|
| Linear Regression | Regression | Yes | Yes | No | Any | Speed, interpretability |
| Logistic Regression | Classification | Yes | Yes | Limited | Any | Probability output, baseline |
| Decision Tree | Both | Yes | No | Yes | Small-Medium | Interpretable rules |
| Random Forest | Both | Partial | No | Yes | Medium-Large | Robust, general purpose |
| SVM | Both | No | Yes | Yes (kernel) | Small-Medium | High-dimensional, small data |
| KNN | Both | Yes | Yes | Yes | Small | No training, simple |
| Naive Bayes | Classification | Yes | No | No | Any | Text data, speed |
| Gradient Boosting | Both | No | No | Yes | Medium-Large | Best accuracy on tabular data |

---

## <span style="color:#1565C0">Algorithm Selection Guide</span>

```
What is your task?
├── Regression (predict a number)
│     ├── Linear relationship + interpretability needed → Linear Regression
│     ├── Non-linear, tabular data, best accuracy      → XGBoost / LightGBM
│     └── General purpose, robust                      → Random Forest
│
└── Classification (predict a class)
      ├── Need probability + interpretability           → Logistic Regression
      ├── Text / NLP data                              → Naive Bayes
      ├── Small dataset, no training time              → KNN
      ├── High-dimensional, small-medium data          → SVM
      ├── Need human-readable rules                    → Decision Tree
      ├── General purpose, robust                      → Random Forest
      └── Maximum accuracy on tabular data             → XGBoost / LightGBM
```

---

## <span style="color:#1565C0">Cross-Validation Strategies</span>

> **Definition:** Cross-validation is a technique for estimating how well a model will generalize to unseen data by splitting the data into multiple train/validation folds.

### <span style="color:#2E86AB">K-Fold Cross-Validation</span>

```
Data split into K equal folds (K=5 is standard):

Fold 1: [Val][Train][Train][Train][Train]
Fold 2: [Train][Val][Train][Train][Train]
Fold 3: [Train][Train][Val][Train][Train]
Fold 4: [Train][Train][Train][Val][Train]
Fold 5: [Train][Train][Train][Train][Val]

Final score = mean of 5 validation scores
```

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">CV Score = (1/K) Σₖ Score(model trained on K-1 folds, evaluated on fold k)</span>

</div>

| Strategy | When to Use |
|:---|:---|
| K-Fold (K=5 or 10) | Standard for most tasks |
| Stratified K-Fold | Classification with class imbalance — preserves class ratios in each fold |
| Leave-One-Out (LOO) | Very small datasets (each sample is its own validation fold) |
| Time Series Split | Sequential data — never use future data to train on past data |
| Group K-Fold | Samples from the same group must stay in the same fold (patient data, etc.) |

> **Critical rule:** Never fit preprocessing (scalers, encoders) on the full dataset. Fit inside each fold on training data only, then transform validation data.

---

## <span style="color:#1565C0">Practical ML Workflow</span>

> A systematic approach to building ML models in practice, from raw data to deployment-ready model.

### <span style="color:#2E86AB">Step-by-Step Process</span>

```
Step 1: Understand the Problem
  → Regression or classification?
  → What metric matters? (RMSE, AUC, F1, precision, recall?)
  → What are the business constraints? (interpretability, latency, data size?)

Step 2: Explore the Data (EDA)
  → Check shape, data types, missing values
  → Distribution of target variable (skewed? imbalanced?)
  → Correlations between features and target
  → Look for outliers

Step 3: Data Preprocessing
  → Handle missing values (imputation: mean/median/mode, or model-based)
  → Encode categorical features (label encoding, one-hot, target encoding)
  → Scale numerical features (StandardScaler, MinMaxScaler, RobustScaler)
  → Handle class imbalance (SMOTE, class_weight, threshold tuning)

Step 4: Baseline Model
  → Fit simplest model first (Linear/Logistic Regression)
  → Establish baseline score
  → Any model you build next must beat this

Step 5: Feature Engineering
  → Create new features from domain knowledge
  → Polynomial and interaction features
  → Log-transform skewed features
  → Bin continuous features if useful

Step 6: Model Selection and Training
  → Try Random Forest (robust, good first serious model)
  → Try XGBoost/LightGBM (usually best accuracy)
  → Use cross-validation (5-fold stratified) for reliable estimates
  → Avoid evaluating on test set at this stage

Step 7: Hyperparameter Tuning
  → GridSearchCV: exhaustive, small search spaces
  → RandomizedSearchCV: efficient for large search spaces
  → Optuna / Bayesian Optimization: most efficient for expensive models

Step 8: Model Evaluation
  → Evaluate on held-out test set (only once, at the very end)
  → Report the right metrics (AUC, F1, RMSE — not just accuracy)
  → Analyze errors: confusion matrix, residual plots

Step 9: Model Interpretation
  → Feature importances (SHAP values for reliable attribution)
  → LIME for local (per-prediction) explanations
  → Partial Dependence Plots (PDPs) for feature effects

Step 10: Deploy and Monitor
  → Wrap model in a prediction API
  → Monitor for data drift and performance degradation over time
```

---

### <span style="color:#2E86AB">Handling Missing Values</span>

| Strategy | When to Use |
|:---|:---|
| Drop rows | Very few rows missing (< 1–2% of data) |
| Mean/median imputation | Numerical features, missing at random, no strong outliers |
| Mode imputation | Categorical features |
| KNN imputation | Missing not at random, relationships between features exist |
| Model-based imputation | Complex missingness patterns |
| Indicator + imputation | Add a binary "was_missing" flag before imputing — preserves missingness signal |
| Tree models (XGBoost) | Handle NaN natively — no imputation needed |

---

### <span style="color:#2E86AB">Categorical Feature Encoding</span>

| Encoding | Description | When to Use |
|:---|:---|:---|
| One-Hot Encoding | Creates binary column per category | Low-cardinality categoricals (< 10 unique values) |
| Label Encoding | Maps categories to integers (0, 1, 2, ...) | Ordinal features with natural order |
| Target Encoding | Replace category with mean of target | High-cardinality, strong target correlation |
| Frequency Encoding | Replace category with its occurrence frequency | High-cardinality, frequency matters |
| Binary Encoding | Encode integer label in binary bits | High-cardinality, reduces dimensions vs one-hot |

> **Warning:** Target encoding can cause severe data leakage — always compute within cross-validation folds, never on the full dataset.

---

### <span style="color:#2E86AB">Hyperparameter Tuning Methods</span>

| Method | Description | When to Use |
|:---|:---|:---|
| GridSearchCV | Exhaustive search over all combinations | Small search space (< 100 combinations) |
| RandomizedSearchCV | Random sampling from parameter distributions | Medium search space, faster than grid |
| Bayesian Optimization (Optuna) | Uses past results to guide next trial | Expensive models, large search space |
| Halving Search | Trains on subset first, promotes best candidates | Fast alternative to grid search |

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">RandomizedSearchCV: n_iter=50 samples covers most search spaces efficiently</span>

</div>

---

### <span style="color:#2E86AB">SHAP Values — Model Interpretability</span>

> **Definition:** SHAP (SHapley Additive exPlanations) values fairly attribute a model's prediction to each feature based on game theory — each feature's contribution is averaged over all possible feature orderings.

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">prediction = base_value + Σⱼ SHAP(fⱼ) for all features j</span>

</div>

| SHAP Plot Type | What it Shows |
|:---|:---|
| Summary plot (beeswarm) | Global feature importance + direction of effect |
| Force plot | Single prediction breakdown (local explanation) |
| Dependence plot | Effect of one feature on prediction across all samples |
| Waterfall plot | How each feature pushes prediction from base value |

> SHAP works for any model (tree, linear, neural network) and gives consistent, theoretically grounded explanations.

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