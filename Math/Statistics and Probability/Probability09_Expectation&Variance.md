<div align="center">

# <span style="color:#0A2FA8">Expectation and Variance in Probability</span>

<sub>A complete note covering Random Variables, Expectation, Variance, Properties, Derivations & Applications</sub>

</div>

---

## <span style="color:#1565C0">1. Random Variables</span>

### <span style="color:#2E86AB">1.1 Definition</span>

> **Definition:** A **Random Variable (R.V.)** is a function that maps outcomes of a random experiment to real numbers. It is denoted by capital letters like X, Y, Z.

### <span style="color:#2E86AB">1.2 Types of Random Variables</span>

| Type | Description | Example |
|------|-------------|---------|
| **Discrete R.V.** | Takes countable values | Number of heads in coin tosses |
| **Continuous R.V.** | Takes uncountable values in an interval | Height of a person |

### <span style="color:#2E86AB">1.3 Probability Functions</span>

| Function | Full Name | Used For |
|----------|-----------|----------|
| PMF | Probability Mass Function | Discrete R.V. |
| PDF | Probability Density Function | Continuous R.V. |
| CDF | Cumulative Distribution Function | Both |

> **PMF:** P(X = xᵢ) gives the probability that X takes the exact value xᵢ.

> **PDF:** f(x) such that P(a ≤ X ≤ b) = ∫[a to b] f(x) dx; note that P(X = x) = 0 for any single point.

---

## <span style="color:#1565C0">2. Expectation (Expected Value)</span>

### <span style="color:#2E86AB">2.1 Description</span>

> **Definition:** The **Expectation** (or **Expected Value**) of a random variable X, written E[X] or μ, is the long-run average value of repetitions of the experiment it represents.

- In probability, expectation is a property of the **probability model**, not of observed (sample) data.
- It represents the **weighted average** of all possible values, weighted by their probabilities.
- If an experiment is repeated infinitely many times, the expectation represents the **long-run average value**.

```
Stat: Mean  ←-→  Probability: Expectation
```

### <span style="color:#2E86AB">2.2 Formulas</span>

#### <span style="color:#5B8DB8">For Discrete Random Variable</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 520px;">

### <span style="color:#D4A017">E[X] = Σ xᵢ · P(X = xᵢ)</span>

</div>

Expanded form:

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 640px;">

### <span style="color:#D4A017">E[X] = x₁·P(x₁) + x₂·P(x₂) + x₃·P(x₃) + ···</span>

</div>

#### <span style="color:#5B8DB8">For Continuous Random Variable</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 520px;">

### <span style="color:#D4A017">E[X] = ∫₋∞^∞ x · f(x) dx</span>

</div>

where f(x) is the Probability Density Function (PDF).

> **Interpretation:** E[X] is the **weighted average** of PMF/PDF - each value of x weighted by its probability.

### <span style="color:#2E86AB">2.3 Expectation of a Function of X</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 580px;">

### <span style="color:#D4A017">E[g(X)] = Σ g(xᵢ) · P(xᵢ) &nbsp;&nbsp; [Discrete]</span>

### <span style="color:#D4A017">E[g(X)] = ∫₋∞^∞ g(x) · f(x) dx &nbsp;&nbsp; [Continuous]</span>

</div>

---

## <span style="color:#1565C0">3. Properties of Expectation</span>

### <span style="color:#2E86AB">3.1 Complete List of Properties</span>

| Property | Formula |
|----------|---------|
| Expectation of a constant | E[c] = c |
| Linearity - constant multiple | E[c·X] = c · E[X] |
| Linearity - sum of variables | E[X + Y] = E[X] + E[Y] |
| Affine transformation | E[aX + b] = a·E[X] + b |
| Expectation of a function | E[g(X)] = Σ g(xᵢ)·P(xᵢ) |
| Non-negativity | If X ≥ 0, then E[X] ≥ 0 |
| Monotonicity | If X ≤ Y, then E[X] ≤ E[Y] |

### <span style="color:#2E86AB">3.2 Key Formulas</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">E[c] = c</span>

</div>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">E[c · X] = c · E[X]</span>

</div>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">E[X + Y] = E[X] + E[Y]</span>

</div>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">E[aX + b] = a · E[X] + b</span>

</div>

### <span style="color:#2E86AB">3.3 Independence Property</span>

> **Note:** If X and Y are **independent**, then E[X · Y] = E[X] · E[Y]. This does **not** hold in general.

---

## <span style="color:#1565C0">4. Derivation: E[X²] and the Shortcut Formula</span>

### <span style="color:#2E86AB">4.1 E[X²]</span>

Using the function rule with g(x) = x²:

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">E[X²] = Σ xᵢ² · P(xᵢ)</span>

</div>

### <span style="color:#2E86AB">4.2 Deriving Var(X) Shortcut</span>

Starting from definition:

```
Var(X) = E[(X - E[X])²]
       = E[X² - 2X·E[X] + (E[X])²]
       = E[X²] - 2·E[X]·E[X] + (E[X])²     [by linearity of expectation]
       = E[X²] - 2·(E[X])² + (E[X])²
       = E[X²] - (E[X])²
```

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">Var(X) = E[X²] − (E[X])²</span>

</div>

This is the **computational shortcut formula** for variance.

---

## <span style="color:#1565C0">5. Variance</span>

### <span style="color:#2E86AB">5.1 Description</span>

> **Definition:** **Variance** of a random variable X, written Var(X) or σ², measures how spread out the values of X are from its mean (expectation).

- Variance is a property of the **probability model**, not of observed/sample data.
- It measures the **average squared deviation** from the mean.
- It is always **non-negative**: Var(X) ≥ 0.
- We calculate the average deviation of random variable values from the mean value.

### <span style="color:#2E86AB">5.2 Formulas</span>

#### <span style="color:#5B8DB8">Definition Formula</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 520px;">

### <span style="color:#D4A017">Var(X) = E[ (X − E[X])² ]</span>

</div>

#### <span style="color:#5B8DB8">Shortcut (Computational) Formula</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">Var(X) = E[X²] − (E[X])²</span>

</div>

#### <span style="color:#5B8DB8">For Discrete R.V.</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 580px;">

### <span style="color:#D4A017">Var(X) = Σ (xᵢ − μ)² · P(xᵢ)</span>

</div>

#### <span style="color:#5B8DB8">For Continuous R.V.</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 580px;">

### <span style="color:#D4A017">Var(X) = ∫₋∞^∞ (x − μ)² · f(x) dx</span>

</div>

### <span style="color:#2E86AB">5.3 Standard Deviation</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">σ = SD(X) = √Var(X)</span>

</div>

> Standard deviation is in the **same units** as X, making it more interpretable than variance.

---

## <span style="color:#1565C0">6. Properties of Variance</span>

### <span style="color:#2E86AB">6.1 Complete List</span>

| Property | Formula | Notes |
|----------|---------|-------|
| Variance of a constant | Var(c) = 0 | Constants don't vary |
| Scaling | Var(c·X) = c² · Var(X) | Coefficient gets squared |
| Affine transformation | Var(aX + b) = a² · Var(X) | Shift b has no effect |
| Sum (independent) | Var(X + Y) = Var(X) + Var(Y) | Only if X, Y independent |
| Non-negativity | Var(X) ≥ 0 | Always true |

### <span style="color:#2E86AB">6.2 Key Property Formulas</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">Var(c) = 0</span>

</div>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">Var(c · X) = c² · Var(X)</span>

</div>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">Var(aX + b) = a² · Var(X)</span>

</div>

> **Why does adding b not affect variance?** Adding a constant shifts all values equally - it doesn't change the spread around the mean. Only scaling (multiplying) changes spread.

### <span style="color:#2E86AB">6.3 Covariance (Extension)</span>

For two random variables X and Y:

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 580px;">

### <span style="color:#D4A017">Cov(X, Y) = E[XY] − E[X]·E[Y]</span>

</div>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 620px;">

### <span style="color:#D4A017">Var(X + Y) = Var(X) + Var(Y) + 2·Cov(X, Y)</span>

</div>

If X and Y are independent: Cov(X, Y) = 0, so Var(X + Y) = Var(X) + Var(Y).

---

## <span style="color:#1565C0">7. Worked Examples</span>

### <span style="color:#2E86AB">7.1 Rolling 2 Dice - Expectation</span>

**Setup:** Roll 2 dice simultaneously. X = sum of outcomes.

**Possible values of X:** {2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}

**Probability table:**

| X | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| P(X) | 1/36 | 2/36 | 3/36 | 4/36 | 5/36 | 6/36 | 5/36 | 4/36 | 3/36 | 2/36 | 1/36 |

**Computation:**

```
E[X] = 2·(1/36) + 3·(2/36) + 4·(3/36) + ... + 12·(1/36)
     = (2 + 6 + 12 + 20 + 30 + 42 + 40 + 36 + 30 + 22 + 12) / 36
     = 252 / 36
     = 7
```

<span style="color:#27AE60">**Result: E[X] = 7** - the expected sum when rolling 2 dice is always 7.</span>

### <span style="color:#2E86AB">7.2 Two Coin Toss - PMF, Expectation & Variance</span>

**Setup:** Toss 2 coins. X = number of heads. Possible values: {0, 1, 2}

| X | 0 | 1 | 2 |
|:---:|:---:|:---:|:---:|
| P(X) | 1/4 | 2/4 | 1/4 |

**Expectation:**

```
E[X] = 0·(1/4) + 1·(2/4) + 2·(1/4)
     = 0 + 0.5 + 0.5  =  1
```

**Variance:**

```
E[X²] = 0²·(1/4) + 1²·(2/4) + 2²·(1/4) = 0 + 0.5 + 1 = 1.5

Var(X) = E[X²] - (E[X])² = 1.5 - 1² = 0.5
```

### <span style="color:#2E86AB">7.3 Applying Variance Properties</span>

**Given:** Var(X) = 4. Find Var(3X + 5).

```
Var(3X + 5) = 3² · Var(X)   [shift +5 has no effect on variance]
            = 9 · 4
            = 36
```

### <span style="color:#2E86AB">7.4 Continuous R.V. - Uniform Distribution</span>

**Setup:** X ~ Uniform[0, 1], so f(x) = 1 for x ∈ [0, 1].

**Expectation:**

```
E[X] = ∫₀¹ x · 1 dx = [x²/2]₀¹ = 1/2
```

**Variance:**

```
E[X²] = ∫₀¹ x² · 1 dx = [x³/3]₀¹ = 1/3

Var(X) = E[X²] - (E[X])² = 1/3 - (1/2)² = 1/3 - 1/4 = 1/12
```

---

## <span style="color:#1565C0">8. Common Distributions - Reference Table</span>

| Distribution | Parameters | E[X] | Var(X) |
|:-------------|:----------:|:----:|:------:|
| Bernoulli(p) | p | p | p(1−p) |
| Binomial(n, p) | n, p | np | np(1−p) |
| Poisson(λ) | λ | λ | λ |
| Uniform[a, b] | a, b | (a+b)/2 | (b−a)²/12 |
| Exponential(λ) | λ | 1/λ | 1/λ² |
| Normal(μ, σ²) | μ, σ² | μ | σ² |
| Geometric(p) | p | 1/p | (1−p)/p² |

---

## <span style="color:#1565C0">9. Moment Generating Functions (MGF)</span>

### <span style="color:#2E86AB">9.1 Definition</span>

> **Definition:** The **Moment Generating Function** (MGF) of X is defined as M(t) = E[e^(tX)], for values of t where this expectation exists.

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">M(t) = E[e^(tX)]</span>

</div>

### <span style="color:#2E86AB">9.2 Why MGFs are Useful</span>

- The **k-th derivative** of M(t) at t = 0 gives the **k-th moment** E[Xᵏ].
- In particular: M'(0) = E[X], and M''(0) = E[X²].

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 520px;">

### <span style="color:#D4A017">E[Xᵏ] = M⁽ᵏ⁾(0) = dᵏM/dtᵏ |_{t=0}</span>

</div>

---

## <span style="color:#1565C0">10. Chebyshev's Inequality</span>

> **Theorem (Chebyshev):** For any random variable X with mean μ and variance σ², the probability of X deviating from its mean by at least k is bounded by:

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 560px;">

### <span style="color:#D4A017">P(|X − μ| ≥ k) ≤ σ² / k²</span>

</div>

Or equivalently (using k standard deviations):

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 560px;">

### <span style="color:#D4A017">P(|X − μ| ≥ kσ) ≤ 1/k²</span>

</div>

**Use:** Provides a distribution-free bound on how far X can stray from its mean, without needing to know the exact distribution.

---

## <span style="color:#1565C0">11. Key Distinctions</span>

### <span style="color:#2E86AB">11.1 Population vs Sample</span>

| Concept | Population (Probability) | Sample (Statistics) |
|---------|:------------------------:|:-------------------:|
| Mean | E[X] = μ (Expectation) | x̄ (Sample Mean) |
| Variance | Var(X) = σ² | s² (Sample Variance) |
| Based on | Probability model | Observed data |

### <span style="color:#2E86AB">11.2 Variance vs Standard Deviation</span>

| Metric | Formula | Units | Interpretation |
|--------|---------|:-----:|----------------|
| Variance | σ² = E[(X−μ)²] | units² | Squared spread |
| Std. Dev. | σ = √Var(X) | units | Spread in original units |

---

## <span style="color:#1565C0">12. Use Cases</span>

### <span style="color:#2E86AB">12.1 Expectation - Applications</span>

| Field | Application |
|-------|-------------|
| Finance | Expected return on investment |
| Insurance | Expected payout calculation |
| Game Theory | Expected payoff of a strategy |
| Engineering | Expected lifetime of a component |
| Machine Learning | Loss function optimization (expected loss) |

### <span style="color:#2E86AB">12.2 Variance - Applications</span>

| Field | Application |
|-------|-------------|
| Finance | Risk measurement (portfolio variance) |
| Quality Control | Process variation monitoring |
| Signal Processing | Noise level quantification |
| Statistics | Confidence interval construction |
| Physics | Quantum mechanical uncertainty |

---

## <span style="color:#1565C0">13. Quick Reference Summary</span>

### <span style="color:#2E86AB">Expectation Properties</span>

```
E[c]       = c
E[cX]      = c · E[X]
E[X + Y]   = E[X] + E[Y]
E[aX + b]  = a·E[X] + b
E[g(X)]    = Σ g(xᵢ)·P(xᵢ)   [discrete]
           = ∫ g(x)·f(x)dx    [continuous]
```

### <span style="color:#2E86AB">Variance Properties</span>

```
Var(c)      = 0
Var(cX)     = c² · Var(X)
Var(aX + b) = a² · Var(X)
Var(X + Y)  = Var(X) + Var(Y)   [if X, Y independent]
Var(X)      = E[X²] - (E[X])²   [shortcut formula]
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