<div align="center">

# <span style="color:#0A2FA8">Types of Continuous Random Variable Distributions</span>

<sub>Complete notes covering all types - PDFs, CDFs, derivations, properties, examples, and comparisons</sub>

</div>

---

## <span style="color:#1565C0">0. Preliminaries - Continuous Random Variables</span>

> **Definition:** A **Continuous Random Variable (RV)** is a random variable that can take any value in an interval or union of intervals. Unlike discrete RVs, individual point probabilities are zero - probability is assigned to intervals.

> **Definition:** The **Probability Density Function (PDF)** f(x) of a continuous RV X satisfies P(a ≤ X ≤ b) = ∫[a to b] f(x) dx for any interval [a, b].

**Two conditions every valid PDF must satisfy:**

| Condition | Expression |
|:---:|:---:|
| Non-negativity | f(x) ≥ 0 for all x |
| Total probability | ∫(−∞ to ∞) f(x) dx = 1 |

**Key quantities derived from any continuous distribution:**

| Quantity | Formula |
|:---|:---|
| Expectation | E[X] = ∫(−∞ to ∞) x · f(x) dx |
| Variance | Var(X) = E[X²] − (E[X])² |
| Standard Deviation | σ = √Var(X) |
| CDF | F(x) = P(X ≤ x) = ∫(−∞ to x) f(t) dt |
| Moment Generating Function | M(t) = E[e^(tX)] = ∫(−∞ to ∞) e^(tx) · f(x) dx |

> **Key distinction:** For any continuous RV, P(X = c) = 0 for any single point c. Only intervals carry nonzero probability.

---

## <span style="color:#1565C0">1. Continuous Uniform Distribution</span>

### <span style="color:#2E86AB">1.1 Description</span>

> **Definition:** A continuous RV X follows a **Continuous Uniform Distribution** U(a, b) if every value in the interval [a, b] is equally likely, meaning the PDF is constant over that interval.

It is the continuous analogue of the Discrete Uniform distribution and models complete uncertainty over a bounded range.

### <span style="color:#2E86AB">1.2 PDF & CDF Formulas</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">f(x) = 1 / (b − a),   for a ≤ x ≤ b   (0 otherwise)</span>

</div>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">F(x) = (x − a) / (b − a),   for a ≤ x ≤ b</span>

</div>

### <span style="color:#2E86AB">1.3 Key Properties</span>

| Property | Formula |
|:---|:---:|
| Expectation | (a + b) / 2 |
| Variance | (b − a)² / 12 |
| Standard Deviation | (b − a) / √12 |
| MGF | (e^(tb) − e^(ta)) / (t(b − a)),  t ≠ 0 |
| Median | (a + b) / 2 |

### <span style="color:#2E86AB">1.4 Derivation of Expectation & Variance</span>

```
E[X] = ∫[a to b] x · [1/(b−a)] dx
     = [1/(b−a)] · [x²/2] from a to b
     = [1/(b−a)] · (b²−a²)/2
     = [1/(b−a)] · (b−a)(b+a)/2
     = (a + b) / 2
```

```
E[X²] = ∫[a to b] x² · [1/(b−a)] dx
      = [1/(b−a)] · [x³/3] from a to b
      = (b³ − a³) / [3(b−a)]
      = (b² + ab + a²) / 3

Var(X) = E[X²] − (E[X])²
       = (b² + ab + a²)/3 − [(a+b)/2]²
       = (b² + ab + a²)/3 − (a² + 2ab + b²)/4
       = [4(b² + ab + a²) − 3(a² + 2ab + b²)] / 12
       = (b² − 2ab + a²) / 12
       = (b − a)² / 12
```

### <span style="color:#2E86AB">1.5 Use Cases</span>

- Random number generation on [0, 1]
- Bus arrival time when you only know the time window
- Rounding error in numerical computation
- Random point selection on a line segment

### <span style="color:#2E86AB">1.6 Worked Example</span>

**Problem:** A bus arrives uniformly between 10:00 and 10:20 (i.e., X ~ U(0, 20) minutes). Find f(x), F(x), P(5 ≤ X ≤ 15), E[X], E[X²], Var(X), and σ from first principles.

**Step 1 - Identify Parameters**
```
a = 0,  b = 20
b − a = 20
X ~ U(0, 20)
```

**Step 2 - Write the PDF and verify**
```
f(x) = 1/20   for 0 ≤ x ≤ 20

Validity check: ∫[0 to 20] (1/20) dx = (1/20) × 20 = 1  ✓
```

**Step 3 - Write the CDF**
```
F(x) = ∫[0 to x] (1/20) dt = x/20   for 0 ≤ x ≤ 20
```

**Step 4 - Compute P(5 ≤ X ≤ 15)**
```
P(5 ≤ X ≤ 15) = ∫[5 to 15] (1/20) dx
              = (1/20) × (15 − 5)
              = 10/20
              = 0.5
```

**Step 5 - Derive E[X]**
```
E[X] = ∫[0 to 20] x · (1/20) dx
     = (1/20) · [x²/2] from 0 to 20
     = (1/20) · (400/2)
     = (1/20) · 200
     = 10
```

**Step 6 - Derive E[X²]**
```
E[X²] = ∫[0 to 20] x² · (1/20) dx
      = (1/20) · [x³/3] from 0 to 20
      = (1/20) · (8000/3)
      = 8000/60
      = 400/3
      ≈ 133.333
```

**Step 7 - Derive Var(X)**
```
Var(X) = E[X²] − (E[X])²
       = 400/3 − 10²
       = 400/3 − 100
       = 400/3 − 300/3
       = 100/3
       ≈ 33.333
```

**Step 8 - Standard Deviation**
```
σ = √Var(X) = √(100/3) = 10/√3 ≈ 5.774
```

**Step 9 - Verify using formulas**
```
Formula: E[X]   = (a+b)/2    = (0+20)/2       = 10       ✓
Formula: Var(X) = (b−a)²/12  = (20)²/12 = 400/12 = 100/3 ✓
```

---

## <span style="color:#1565C0">2. Exponential Distribution</span>

### <span style="color:#2E86AB">2.1 Description</span>

> **Definition:** A continuous RV X follows an **Exponential Distribution** Exp(λ) if it models the time between events in a Poisson process, where events occur continuously and independently at a constant average rate λ.

It is the continuous analogue of the Geometric distribution and is the only continuous distribution with the memoryless property.

### <span style="color:#2E86AB">2.2 PDF & CDF Formulas</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">f(x) = λ · e^(−λx),   x ≥ 0   (λ > 0)</span>

</div>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">F(x) = 1 − e^(−λx),   x ≥ 0</span>

</div>

where λ > 0 is the **rate parameter** (events per unit time). The scale parameter is θ = 1/λ.

### <span style="color:#2E86AB">2.3 Key Properties</span>

| Property | Formula |
|:---|:---:|
| Expectation | 1/λ |
| Variance | 1/λ² |
| Standard Deviation | 1/λ |
| MGF | λ/(λ − t),   t < λ |
| Median | ln(2)/λ |
| Mode | 0 |

### <span style="color:#2E86AB">2.4 Memoryless Property</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">P(X > s + t | X > s) = P(X > t)   for all s, t ≥ 0</span>

</div>

> **Key fact:** The Exponential distribution is the **only continuous distribution with the memoryless property**. Knowing that no event has occurred up to time s gives no information about future waiting time.

```
Proof:
P(X > s + t | X > s) = P(X > s + t) / P(X > s)
                     = e^(−λ(s+t)) / e^(−λs)
                     = e^(−λt)
                     = P(X > t)  ✓
```

### <span style="color:#2E86AB">2.5 Derivation of Expectation & Variance</span>

```
E[X] = ∫[0 to ∞] x · λe^(−λx) dx

Integration by parts: u = x, dv = λe^(−λx) dx
  → du = dx, v = −e^(−λx)

E[X] = [−x·e^(−λx)] from 0 to ∞  +  ∫[0 to ∞] e^(−λx) dx
     = 0  +  [−(1/λ)·e^(−λx)] from 0 to ∞
     = 0  +  (0 − (−1/λ))
     = 1/λ
```

```
E[X²] = ∫[0 to ∞] x² · λe^(−λx) dx

Applying integration by parts twice (or using the Gamma integral identity):
     = 2/λ²

Var(X) = E[X²] − (E[X])²
       = 2/λ² − (1/λ)²
       = 2/λ² − 1/λ²
       = 1/λ²
```

### <span style="color:#2E86AB">2.6 Relationship to Poisson</span>

```
If arrivals follow Poisson(λ) per unit time,
then inter-arrival times follow Exp(λ).

More precisely: if X₁, X₂, … are i.i.d. Exp(λ) waiting times,
then the number of events in [0, t] follows Poisson(λt).
```

### <span style="color:#2E86AB">2.7 Use Cases</span>

- Time between phone calls arriving at a call center
- Lifetime of electronic components
- Time until radioactive decay
- Waiting time in a queue (service time)
- Time between earthquakes

### <span style="color:#2E86AB">2.8 Worked Example</span>

**Problem:** Calls arrive at a rate of λ = 2 per minute. Find f(x), P(X > 1), P(0.5 ≤ X ≤ 2), E[X], E[X²], Var(X), and σ from first principles.

**Step 1 - Identify Parameters**
```
λ = 2  (calls per minute)
X = waiting time until next call  →  X ~ Exp(2)
```

**Step 2 - Write the PDF**
```
f(x) = 2e^(−2x)   for x ≥ 0

Validity: ∫[0 to ∞] 2e^(−2x) dx = 2 · [−(1/2)e^(−2x)] from 0 to ∞
        = 2 · (0 − (−1/2)) = 2 × 1/2 = 1  ✓
```

**Step 3 - Compute P(X > 1) using survival function**
```
P(X > 1) = 1 − F(1) = e^(−λ·1) = e^(−2) ≈ 0.1353
```

**Step 4 - Compute P(0.5 ≤ X ≤ 2)**
```
P(0.5 ≤ X ≤ 2) = F(2) − F(0.5)
               = (1 − e^(−4)) − (1 − e^(−1))
               = e^(−1) − e^(−4)
               = 0.3679 − 0.0183
               ≈ 0.3496
```

**Step 5 - Derive E[X] from first principles**
```
E[X] = ∫[0 to ∞] x · 2e^(−2x) dx

Let u = x, dv = 2e^(−2x) dx → du = dx, v = −e^(−2x)

E[X] = [−x·e^(−2x)] from 0 to ∞  +  ∫[0 to ∞] e^(−2x) dx
     = 0  +  [−(1/2)e^(−2x)] from 0 to ∞
     = 0  +  (0 − (−1/2))
     = 1/2
     = 0.5 minutes
```

**Step 6 - Derive E[X²]**
```
E[X²] = ∫[0 to ∞] x² · 2e^(−2x) dx

Using integration by parts twice:
Let u = x², dv = 2e^(−2x) dx → du = 2x dx, v = −e^(−2x)

E[X²] = [−x²·e^(−2x)] from 0 to ∞  +  ∫[0 to ∞] 2x·e^(−2x) dx
      = 0  +  2 · ∫[0 to ∞] x·e^(−2x) dx

Now ∫[0 to ∞] x·e^(−2x) dx = 1/(2²) = 1/4  [using ∫x·e^(−ax)dx = 1/a²]

E[X²] = 2 × (1/4) = 1/2
```

**Step 7 - Derive Var(X)**
```
Var(X) = E[X²] − (E[X])²
       = 1/2 − (1/2)²
       = 1/2 − 1/4
       = 1/4
```

**Step 8 - Standard Deviation**
```
σ = √Var(X) = √(1/4) = 1/2 = 0.5 minutes
```

**Step 9 - Verify using formulas**
```
Formula: E[X]   = 1/λ   = 1/2   = 0.5   ✓
Formula: Var(X) = 1/λ²  = 1/4   = 0.25  ✓
Note: σ = E[X] = 1/λ  - Expectation equals Standard Deviation for Exponential
```

---

## <span style="color:#1565C0">3. Normal Distribution</span>

### <span style="color:#2E86AB">3.1 Description</span>

> **Definition:** A continuous RV X follows a **Normal Distribution** N(μ, σ²) if its PDF is the symmetric bell-shaped curve centred at μ with spread controlled by σ². It is the most important distribution in statistics due to the Central Limit Theorem.

### <span style="color:#2E86AB">3.2 PDF Formula</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 560px;">

### <span style="color:#D4A017">f(x) = (1 / (σ√(2π))) · exp(−(x − μ)² / (2σ²)),   x ∈ (−∞, ∞)</span>

</div>

where μ ∈ (−∞, ∞) is the location parameter (mean) and σ > 0 is the scale parameter (standard deviation).

### <span style="color:#2E86AB">3.3 Key Properties</span>

| Property | Formula |
|:---|:---:|
| Expectation | μ |
| Variance | σ² |
| Standard Deviation | σ |
| MGF | exp(μt + σ²t²/2) |
| Median | μ |
| Mode | μ |
| Skewness | 0 (perfectly symmetric) |
| Kurtosis | 3 (excess kurtosis = 0) |

### <span style="color:#2E86AB">3.4 Empirical Rule (68–95–99.7 Rule)</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">P(μ − σ < X < μ + σ)   ≈ 68.27%</span>

### <span style="color:#D4A017">P(μ − 2σ < X < μ + 2σ)  ≈ 95.45%</span>

### <span style="color:#D4A017">P(μ − 3σ < X < μ + 3σ)  ≈ 99.73%</span>

</div>

### <span style="color:#2E86AB">3.5 Symmetry & Standardisation</span>

```
Symmetry:  f(μ + x) = f(μ − x)  for all x  →  symmetric about μ

Standardisation: If X ~ N(μ, σ²), then
  Z = (X − μ) / σ  ~  N(0, 1)  (Standard Normal)

Linear combination: If X ~ N(μ, σ²), then
  aX + b  ~  N(aμ + b, a²σ²)
```

### <span style="color:#2E86AB">3.6 Reproductive Property</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">If X ~ N(μ₁, σ₁²) and Y ~ N(μ₂, σ₂²) independently, then X + Y ~ N(μ₁+μ₂, σ₁²+σ₂²)</span>

</div>

### <span style="color:#2E86AB">3.7 Use Cases</span>

- Heights, weights, and many biological measurements
- Measurement errors in scientific experiments
- IQ scores and standardised test results
- Stock returns over short time intervals (approximate)
- Sampling distributions by the Central Limit Theorem

### <span style="color:#2E86AB">3.8 Worked Example</span>

**Problem:** X ~ N(50, 100) (μ = 50, σ² = 100, so σ = 10). Find P(40 ≤ X ≤ 70), E[X], Var(X), and σ. Also find the value c such that P(X ≤ c) = 0.975.

**Step 1 - Identify Parameters**
```
μ = 50,   σ² = 100,   σ = 10
X ~ N(50, 100)
```

**Step 2 - Standardise to compute P(40 ≤ X ≤ 70)**
```
Convert X to Z = (X − μ)/σ:

Lower: Z₁ = (40 − 50)/10 = −10/10 = −1
Upper: Z₂ = (70 − 50)/10 = 20/10  = +2

P(40 ≤ X ≤ 70) = P(−1 ≤ Z ≤ 2)
               = Φ(2) − Φ(−1)
               = Φ(2) − (1 − Φ(1))     [symmetry: Φ(−z) = 1 − Φ(z)]
               = 0.9772 − (1 − 0.8413)
               = 0.9772 − 0.1587
               = 0.8185
```

**Step 3 - State E[X] and Var(X)**
```
E[X]   = μ   = 50
Var(X) = σ²  = 100
σ      = 10
```

**Step 4 - Find c such that P(X ≤ c) = 0.975**
```
P(X ≤ c) = 0.975
→ P(Z ≤ (c − 50)/10) = 0.975
→ (c − 50)/10 = z₀.₉₇₅ = 1.96   [from standard normal table]
→ c = 50 + 10 × 1.96
→ c = 50 + 19.6
→ c = 69.6
```

**Step 5 - Apply the 68–95–99.7 Rule**
```
P(40 < X < 60) = P(μ−σ < X < μ+σ)  ≈ 68.27%
P(30 < X < 70) = P(μ−2σ < X < μ+2σ) ≈ 95.45%
P(20 < X < 80) = P(μ−3σ < X < μ+3σ) ≈ 99.73%
```

---

## <span style="color:#1565C0">4. Standard Normal Distribution</span>

### <span style="color:#2E86AB">4.1 Description</span>

> **Definition:** A continuous RV Z follows the **Standard Normal Distribution** N(0, 1) if it is a Normal distribution with expectation 0 and variance 1. It is the cornerstone of all normal probability calculations via the Z-score transformation.

### <span style="color:#2E86AB">4.2 PDF & CDF Formulas</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">φ(z) = (1/√(2π)) · e^(−z²/2),   z ∈ (−∞, ∞)</span>

</div>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">Φ(z) = P(Z ≤ z) = ∫(−∞ to z) φ(t) dt</span>

</div>

Note: Φ(z) has no closed form and is evaluated using standard normal tables or software.

### <span style="color:#2E86AB">4.3 Key Properties</span>

| Property | Value |
|:---|:---:|
| Expectation | 0 |
| Variance | 1 |
| Standard Deviation | 1 |
| MGF | e^(t²/2) |
| Median | 0 |
| Mode | 0 |
| Symmetry | φ(z) = φ(−z) |

### <span style="color:#2E86AB">4.4 Critical Symmetry Relations</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">Φ(−z) = 1 − Φ(z)   (symmetry about 0)</span>

### <span style="color:#D4A017">P(a ≤ Z ≤ b) = Φ(b) − Φ(a)</span>

### <span style="color:#D4A017">P(|Z| ≤ z) = 2Φ(z) − 1</span>

</div>

### <span style="color:#2E86AB">4.5 Z-Score Transformation</span>

```
For X ~ N(μ, σ²), the Z-score is:

Z = (X − μ) / σ   ~  N(0, 1)

This transforms any normal probability question into a
standard normal table lookup.

Inverse: X = μ + σZ   →   X ~ N(μ, σ²)
```

### <span style="color:#2E86AB">4.6 Commonly Used Critical Values</span>

| Confidence Level | α | z_(α/2) |
|:---:|:---:|:---:|
| 90% | 0.10 | 1.645 |
| 95% | 0.05 | 1.960 |
| 99% | 0.01 | 2.576 |

### <span style="color:#2E86AB">4.7 Worked Example</span>

**Problem:** Z ~ N(0, 1). Find P(Z ≤ 1.5), P(Z > −0.8), P(−1.2 ≤ Z ≤ 1.96), and the 90th percentile z₀.₉.

**Step 1 - Compute P(Z ≤ 1.5)**
```
P(Z ≤ 1.5) = Φ(1.5) = 0.9332
```

**Step 2 - Compute P(Z > −0.8)**
```
P(Z > −0.8) = 1 − Φ(−0.8)
            = 1 − (1 − Φ(0.8))    [symmetry]
            = Φ(0.8)
            = 0.7881
```

**Step 3 - Compute P(−1.2 ≤ Z ≤ 1.96)**
```
P(−1.2 ≤ Z ≤ 1.96) = Φ(1.96) − Φ(−1.2)
                    = Φ(1.96) − (1 − Φ(1.2))
                    = 0.9750 − (1 − 0.8849)
                    = 0.9750 − 0.1151
                    = 0.8599
```

**Step 4 - Find 90th percentile z₀.₉**
```
P(Z ≤ z₀.₉) = 0.90
→ z₀.₉ = 1.282   [from standard normal table]
```

**Step 5 - State E[Z] and Var(Z)**
```
E[Z]   = 0
Var(Z) = 1
σ(Z)   = 1
```

---

## <span style="color:#1565C0">5. t-Distribution</span>

### <span style="color:#2E86AB">5.1 Description</span>

> **Definition:** A continuous RV T follows a **t-Distribution** t(ν) with ν degrees of freedom if T = Z / √(V/ν), where Z ~ N(0, 1) and V ~ χ²(ν) are independent. It is used in inference when the population variance is unknown and the sample size is small.

### <span style="color:#2E86AB">5.2 PDF Formula</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 560px;">

### <span style="color:#D4A017">f(t) = [Γ((ν+1)/2) / (√(νπ) · Γ(ν/2))] · (1 + t²/ν)^(−(ν+1)/2),   t ∈ (−∞, ∞)</span>

</div>

where ν > 0 is the degrees of freedom and Γ(·) is the Gamma function.

### <span style="color:#2E86AB">5.3 Key Properties</span>

| Property | Formula | Condition |
|:---|:---:|:---:|
| Expectation | 0 | ν > 1 |
| Variance | ν / (ν − 2) | ν > 2 |
| MGF | Does not exist | - |
| Symmetry | f(t) = f(−t) | Always |
| Kurtosis | 6/(ν−4) + 3 | ν > 4 |

### <span style="color:#2E86AB">5.4 Relationship to Normal Distribution</span>

```
As ν → ∞:   t(ν)  →  N(0, 1)

For ν ≥ 30: t-distribution is well-approximated by Standard Normal

ν = 1: t(1) is the Cauchy distribution (no defined expectation or variance)
```

### <span style="color:#2E86AB">5.5 Comparison: t-Distribution vs Normal</span>

| Feature | t-Distribution | Standard Normal |
|:---|:---:|:---:|
| Tails | Heavier | Thinner |
| Peak | Lower | Higher |
| Variance | ν/(ν−2) > 1 | 1 |
| Degrees of freedom | Finite ν | ν → ∞ |
| Used when | σ unknown, small n | σ known, large n |

### <span style="color:#2E86AB">5.6 One-Sample t-Statistic</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">t = (X̄ − μ₀) / (S / √n)   ~  t(n − 1)</span>

</div>

where X̄ is the sample mean, S is the sample standard deviation, n is the sample size, and μ₀ is the hypothesised population mean.

### <span style="color:#2E86AB">5.7 Use Cases</span>

- One-sample, two-sample, and paired t-tests
- Confidence intervals for μ when σ is unknown
- Regression coefficient significance tests
- Any inference with small samples (n < 30)

### <span style="color:#2E86AB">5.8 Worked Example</span>

**Problem:** A sample of n = 16 observations gives X̄ = 52 and S = 8. Test H₀: μ = 50 at the 5% significance level (two-tailed). Also compute E[T] and Var(T).

**Step 1 - Identify Parameters**
```
n = 16,   X̄ = 52,   S = 8,   μ₀ = 50
Degrees of freedom: ν = n − 1 = 15
T ~ t(15)
```

**Step 2 - Compute the t-statistic**
```
t = (X̄ − μ₀) / (S/√n)
  = (52 − 50) / (8/√16)
  = 2 / (8/4)
  = 2 / 2
  = 1.0
```

**Step 3 - Find critical value**
```
Two-tailed test, α = 0.05, ν = 15:
t_(0.025, 15) = 2.131   [from t-table]

Decision rule: reject H₀ if |t| > 2.131
|t| = 1.0 < 2.131  →  Fail to reject H₀
```

**Step 4 - State E[T] and Var(T)**
```
E[T]   = 0         (ν = 15 > 1, so expectation exists)
Var(T) = ν/(ν−2)  = 15/13 ≈ 1.154   (ν = 15 > 2, so variance exists)
σ(T)   = √(15/13) ≈ 1.074
```

**Step 5 - Interpretation**
```
The sample mean of 52 is only 1.0 standard errors above the hypothesised
mean of 50. With ν = 15 degrees of freedom, this is not statistically
significant at the 5% level.
```

---

## <span style="color:#1565C0">6. Chi-Squared Distribution</span>

### <span style="color:#2E86AB">6.1 Description</span>

> **Definition:** A continuous RV X follows a **Chi-Squared Distribution** χ²(k) with k degrees of freedom if X = Z₁² + Z₂² + … + Zₖ², where Z₁, Z₂, …, Zₖ are independent standard normal RVs.

It is a special case of the Gamma distribution and arises naturally in variance estimation and goodness-of-fit tests.

### <span style="color:#2E86AB">6.2 PDF Formula</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 560px;">

### <span style="color:#D4A017">f(x) = x^(k/2 − 1) · e^(−x/2) / (2^(k/2) · Γ(k/2)),   x > 0</span>

</div>

where k > 0 is the degrees of freedom (a positive integer in most applications) and Γ(·) is the Gamma function.

### <span style="color:#2E86AB">6.3 Key Properties</span>

| Property | Formula |
|:---|:---:|
| Expectation | k |
| Variance | 2k |
| Standard Deviation | √(2k) |
| MGF | (1 − 2t)^(−k/2),   t < 1/2 |
| Mode | max(k − 2, 0) |
| Skewness | √(8/k) |

> **Key fact:** χ²(k) is a special case of Gamma(k/2, 2). As k → ∞, the chi-squared distribution approaches Normal by the Central Limit Theorem.

### <span style="color:#2E86AB">6.4 Additive Property</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">If X ~ χ²(k₁) and Y ~ χ²(k₂) independently, then X + Y ~ χ²(k₁ + k₂)</span>

</div>

### <span style="color:#2E86AB">6.5 Sample Variance Connection</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">(n − 1)S² / σ²  ~  χ²(n − 1)</span>

</div>

This result is fundamental to confidence intervals and hypothesis tests for the population variance σ².

### <span style="color:#2E86AB">6.6 Use Cases</span>

- Testing goodness-of-fit (observed vs expected frequencies)
- Tests of independence in contingency tables
- Confidence intervals for population variance
- Likelihood ratio tests in statistics

### <span style="color:#2E86AB">6.7 Worked Example</span>

**Problem:** A sample of n = 21 gives S² = 12 from a Normal population with unknown σ². Construct a 95% confidence interval for σ². Also state E[X] and Var(X) for X ~ χ²(20).

**Step 1 - Identify Parameters**
```
n = 21,   S² = 12
Degrees of freedom: ν = n − 1 = 20
X = (n−1)S²/σ²  ~  χ²(20)
```

**Step 2 - State E[X] and Var(X)**
```
E[X]   = k    = 20
Var(X) = 2k   = 40
σ(X)   = √40  ≈ 6.325
```

**Step 3 - Find critical values for 95% CI**
```
For χ²(20) at 95% CI:
  χ²_(0.025, 20) = 34.170   (upper critical value)
  χ²_(0.975, 20) = 9.591    (lower critical value)
```

**Step 4 - Construct the confidence interval**
```
95% CI for σ²:

[ (n−1)S² / χ²_upper ,  (n−1)S² / χ²_lower ]

= [ 20 × 12 / 34.170 ,  20 × 12 / 9.591 ]
= [ 240 / 34.170 ,  240 / 9.591 ]
= [ 7.024 ,  25.023 ]

We are 95% confident that σ² lies between 7.024 and 25.023.
```

**Step 5 - Interpret**
```
The chi-squared distribution is skewed right, so the CI is not symmetric
around S² = 12. The interval extends further to the right.
```

---

## <span style="color:#1565C0">7. Logistic Distribution</span>

### <span style="color:#2E86AB">7.1 Description</span>

> **Definition:** A continuous RV X follows a **Logistic Distribution** with location parameter μ and scale parameter s > 0 if its CDF is the logistic (sigmoid) function. It resembles the Normal distribution but has heavier tails and a closed-form CDF.

### <span style="color:#2E86AB">7.2 PDF & CDF Formulas</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 560px;">

### <span style="color:#D4A017">f(x) = e^(−(x−μ)/s) / [ s · (1 + e^(−(x−μ)/s))² ],   x ∈ (−∞, ∞)</span>

</div>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">F(x) = 1 / (1 + e^(−(x−μ)/s))   (Sigmoid / Logistic function)</span>

</div>

For the standard case (μ = 0, s = 1):

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">f(x) = e^(−x) / (1 + e^(−x))²,   F(x) = 1 / (1 + e^(−x))</span>

</div>

### <span style="color:#2E86AB">7.3 Key Properties</span>

| Property | Formula |
|:---|:---:|
| Expectation | μ |
| Variance | s²π²/3 |
| Standard Deviation | sπ/√3 |
| MGF | e^(μt) · B(1−st, 1+st)  (for |st| < 1) |
| Median | μ |
| Mode | μ |
| Skewness | 0 (symmetric) |
| Kurtosis | 4.2 (excess kurtosis = 1.2) |

### <span style="color:#2E86AB">7.4 Comparison: Logistic vs Normal</span>

| Feature | Logistic | Normal |
|:---|:---:|:---:|
| Symmetry | Yes | Yes |
| Tail weight | Heavier | Thinner |
| CDF | Closed form (sigmoid) | No closed form |
| Kurtosis (excess) | 1.2 | 0 |
| Variance | s²π²/3 ≈ 3.29s² | σ² |

### <span style="color:#2E86AB">7.5 Relationship to Logistic Regression</span>

```
In logistic regression, the probability of a binary outcome is modelled as:

P(Y=1 | x) = F(β₀ + β₁x) = 1 / (1 + e^(−(β₀ + β₁x)))

This is precisely the CDF of the Logistic distribution evaluated
at the linear predictor - connecting the distribution directly
to the most widely used classification model.
```

### <span style="color:#2E86AB">7.6 Use Cases</span>

- Binary outcome modelling (logistic regression)
- Population growth models (logistic growth curve)
- Chess rating systems (Elo rating)
- Item response theory in education testing
- Neural network activation function (sigmoid)

### <span style="color:#2E86AB">7.7 Worked Example</span>

**Problem:** X ~ Logistic(μ = 5, s = 2). Find f(5), F(7), P(3 ≤ X ≤ 7), E[X], Var(X), and σ.

**Step 1 - Identify Parameters**
```
μ = 5,   s = 2
X ~ Logistic(5, 2)
```

**Step 2 - Compute f(5) (PDF at the centre)**
```
f(5) = e^(−(5−5)/2) / [2 · (1 + e^(−(5−5)/2))²]
     = e^0 / [2 · (1 + e^0)²]
     = 1 / [2 · (1 + 1)²]
     = 1 / [2 · 4]
     = 1/8
     = 0.125
```

**Step 3 - Compute F(7) using the CDF**
```
F(7) = 1 / (1 + e^(−(7−5)/2))
     = 1 / (1 + e^(−1))
     = 1 / (1 + 0.3679)
     = 1 / 1.3679
     ≈ 0.7311
```

**Step 4 - Compute F(3)**
```
F(3) = 1 / (1 + e^(−(3−5)/2))
     = 1 / (1 + e^1)
     = 1 / (1 + 2.7183)
     = 1 / 3.7183
     ≈ 0.2689
```

**Step 5 - Compute P(3 ≤ X ≤ 7)**
```
P(3 ≤ X ≤ 7) = F(7) − F(3)
             ≈ 0.7311 − 0.2689
             = 0.4622

Note: By symmetry about μ = 5, F(7) = 1 − F(3),
so P(3 ≤ X ≤ 7) = F(7) − F(3) = 2F(7) − 1 = 2(0.7311) − 1 = 0.4622  ✓
```

**Step 6 - State E[X] and Var(X)**
```
E[X]   = μ       = 5
Var(X) = s²π²/3  = 4 × 9.8696 / 3 = 39.478/3 ≈ 13.159
σ      = sπ/√3   = 2π/√3 ≈ 2 × 3.1416/1.7321 ≈ 3.628
```

---

## <span style="color:#1565C0">8. Beta Distribution</span>

### <span style="color:#2E86AB">8.1 Description</span>

> **Definition:** A continuous RV X follows a **Beta Distribution** Beta(α, β) if its support is the unit interval [0, 1] and its shape is controlled by two positive parameters α and β. It is extremely flexible and can model any shape on [0, 1] - uniform, U-shaped, J-shaped, or bell-shaped.

### <span style="color:#2E86AB">8.2 PDF Formula</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 560px;">

### <span style="color:#D4A017">f(x) = x^(α−1) · (1−x)^(β−1) / B(α, β),   0 ≤ x ≤ 1</span>

</div>

where the **Beta function** B(α, β) is the normalising constant:

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">B(α, β) = Γ(α)Γ(β) / Γ(α + β) = ∫[0 to 1] x^(α−1)(1−x)^(β−1) dx</span>

</div>

### <span style="color:#2E86AB">8.3 Key Properties</span>

| Property | Formula |
|:---|:---:|
| Expectation | α / (α + β) |
| Variance | αβ / [(α+β)²(α+β+1)] |
| Mode | (α − 1) / (α + β − 2),   for α,β > 1 |
| Skewness | 2(β−α)√(α+β+1) / [(α+β+2)√(αβ)] |

### <span style="color:#2E86AB">8.4 Special Cases</span>

| Parameters | Shape | Equivalent |
|:---|:---|:---:|
| α = 1, β = 1 | Flat / uniform | U(0, 1) |
| α = β | Symmetric about 0.5 | - |
| α < 1, β < 1 | U-shaped | - |
| α > 1, β > 1 | Unimodal bell-shaped | - |
| α = 1, β > 1 | Right-skewed J-shape | - |
| α > 1, β = 1 | Left-skewed J-shape | - |

### <span style="color:#2E86AB">8.5 Derivation of Expectation</span>

```
E[X] = ∫[0 to 1] x · x^(α−1)(1−x)^(β−1) / B(α,β)  dx
     = (1/B(α,β)) · ∫[0 to 1] x^α (1−x)^(β−1) dx
     = B(α+1, β) / B(α, β)

Using B(α+1, β) = Γ(α+1)Γ(β)/Γ(α+β+1) and Γ(α+1) = αΓ(α):

E[X] = [αΓ(α)Γ(β) / Γ(α+β+1)] / [Γ(α)Γ(β) / Γ(α+β)]
     = α · Γ(α+β) / Γ(α+β+1)
     = α · Γ(α+β) / [(α+β)Γ(α+β)]
     = α / (α + β)
```

### <span style="color:#2E86AB">8.6 Use Cases</span>

- Modelling proportions, probabilities, or rates (values in [0, 1])
- Bayesian inference: Beta is the conjugate prior for Binomial
- Project completion percentages
- Modelling batting averages or click-through rates
- Order statistics of the Uniform distribution

### <span style="color:#2E86AB">8.7 Worked Example</span>

**Problem:** X ~ Beta(2, 5). Find f(x), E[X], Var(X), σ, and the mode. Also compute P(X ≤ 0.3) using the CDF.

**Step 1 - Identify Parameters**
```
α = 2,   β = 5
α + β = 7
```

**Step 2 - Compute the normalising constant B(2, 5)**
```
B(α, β) = Γ(α)Γ(β) / Γ(α+β)
         = Γ(2)·Γ(5) / Γ(7)

Γ(2) = 1! = 1
Γ(5) = 4! = 24
Γ(7) = 6! = 720

B(2, 5) = (1 × 24) / 720 = 24/720 = 1/30
```

**Step 3 - Write the PDF**
```
f(x) = x^(2−1) · (1−x)^(5−1) / B(2,5)
     = x · (1−x)⁴ / (1/30)
     = 30 · x · (1−x)⁴,   0 ≤ x ≤ 1

Validity check:
∫[0 to 1] 30x(1−x)⁴ dx = 30 · B(2,5) = 30 × (1/30) = 1  ✓
```

**Step 4 - Derive E[X]**
```
E[X] = α/(α+β) = 2/7 ≈ 0.2857
```

**Step 5 - Derive Var(X)**
```
Var(X) = αβ / [(α+β)²(α+β+1)]
       = (2 × 5) / [(7)² × (8)]
       = 10 / (49 × 8)
       = 10 / 392
       ≈ 0.02551
```

**Step 6 - Standard Deviation and Mode**
```
σ = √0.02551 ≈ 0.1597

Mode = (α−1)/(α+β−2) = (2−1)/(7−2) = 1/5 = 0.2

Interpretation: The distribution peaks at x = 0.2 but has
expectation at 0.286 - right-skewed as expected for α < β.
```

**Step 7 - Compute P(X ≤ 0.3) by direct integration**
```
P(X ≤ 0.3) = ∫[0 to 0.3] 30x(1−x)⁴ dx

Expand (1−x)⁴ = 1 − 4x + 6x² − 4x³ + x⁴:

30 ∫[0 to 0.3] x(1 − 4x + 6x² − 4x³ + x⁴) dx
= 30 ∫[0 to 0.3] (x − 4x² + 6x³ − 4x⁴ + x⁵) dx
= 30 · [x²/2 − 4x³/3 + 6x⁴/4 − 4x⁵/5 + x⁶/6] from 0 to 0.3

At x = 0.3:
  (0.3)²/2 = 0.045
  4(0.3)³/3 = 4(0.027)/3 = 0.036
  6(0.3)⁴/4 = 6(0.0081)/4 = 0.01215
  4(0.3)⁵/5 = 4(0.00243)/5 = 0.001944
  (0.3)⁶/6 = 0.000729/6 = 0.0001215

Sum = 0.045 − 0.036 + 0.01215 − 0.001944 + 0.0001215
    = 0.019328

P(X ≤ 0.3) = 30 × 0.019328 ≈ 0.5798
```

---

## <span style="color:#1565C0">9. Gamma Distribution</span>

### <span style="color:#2E86AB">9.1 Description</span>

> **Definition:** A continuous RV X follows a **Gamma Distribution** Γ(α, β) with shape parameter α > 0 and scale parameter β > 0 if it models the total waiting time for α events in a Poisson process with rate 1/β. It generalises both the Exponential and Chi-Squared distributions.

### <span style="color:#2E86AB">9.2 PDF Formula</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 560px;">

### <span style="color:#D4A017">f(x) = x^(α−1) · e^(−x/β) / (β^α · Γ(α)),   x > 0</span>

</div>

where the **Gamma function** Γ(α) satisfies:

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">Γ(α) = ∫[0 to ∞] t^(α−1) · e^(−t) dt,   Γ(n) = (n−1)!  for positive integers</span>

</div>

### <span style="color:#2E86AB">9.3 Key Properties</span>

| Property | Formula |
|:---|:---:|
| Expectation | αβ |
| Variance | αβ² |
| Standard Deviation | β√α |
| MGF | (1 − βt)^(−α),   t < 1/β |
| Mode | (α − 1)β,   for α ≥ 1 |
| Skewness | 2/√α |

### <span style="color:#2E86AB">9.4 Special Cases</span>

| Parameters | Equivalent Distribution |
|:---|:---:|
| α = 1 | Exponential(1/β)  →  Exp(λ) with λ = 1/β |
| α = k/2, β = 2 | Chi-Squared χ²(k) |
| α = n (integer) | Erlang(n, 1/β) - sum of n Exponentials |

### <span style="color:#2E86AB">9.5 Additive Property</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">If X ~ Γ(α₁, β) and Y ~ Γ(α₂, β) independently, then X + Y ~ Γ(α₁+α₂, β)</span>

</div>

### <span style="color:#2E86AB">9.6 Derivation of Expectation & Variance</span>

```
E[X] = ∫[0 to ∞] x · [x^(α−1) e^(−x/β)] / [β^α Γ(α)]  dx
     = (1/(β^α Γ(α))) · ∫[0 to ∞] x^α e^(−x/β) dx

Let u = x/β → x = βu, dx = β du:

     = (1/(β^α Γ(α))) · ∫[0 to ∞] (βu)^α e^(−u) β du
     = (β^(α+1)) / (β^α Γ(α)) · ∫[0 to ∞] u^α e^(−u) du
     = (β / Γ(α)) · Γ(α+1)
     = (β / Γ(α)) · αΓ(α)
     = αβ
```

```
E[X²] = (β² / Γ(α)) · Γ(α+2)
      = β² · α(α+1)

Var(X) = E[X²] − (E[X])²
       = β²α(α+1) − (αβ)²
       = α(α+1)β² − α²β²
       = αβ²(α + 1 − α)
       = αβ²
```

### <span style="color:#2E86AB">9.7 Use Cases</span>

- Total waiting time for multiple events (Poisson process)
- Rainfall amounts and flood modelling
- Insurance claim sizes
- Reliability engineering and failure time analysis
- Bayesian inference (conjugate prior for Poisson rate)

### <span style="color:#2E86AB">9.8 Worked Example</span>

**Problem:** Customer service calls last an average of 6 minutes each, exponentially distributed. X = total time for 4 calls, so X ~ Γ(4, 6). Find f(x), E[X], E[X²], Var(X), σ, the mode, and P(X ≤ 12).

**Step 1 - Identify Parameters**
```
α = 4  (shape - number of calls)
β = 6  (scale - average time per call in minutes)
X = total time for 4 calls  →  X ~ Γ(4, 6)
Γ(4) = 3! = 6
```

**Step 2 - Write the PDF**
```
f(x) = x^(4−1) · e^(−x/6) / (6⁴ · Γ(4))
     = x³ · e^(−x/6) / (1296 × 6)
     = x³ · e^(−x/6) / 7776,   x > 0
```

**Step 3 - Derive E[X]**
```
E[X] = αβ = 4 × 6 = 24 minutes
```

**Step 4 - Derive E[X²]**
```
E[X²] = Var(X) + (E[X])²   [rearranged]

First find Var(X):
Var(X) = αβ² = 4 × 36 = 144

E[X²] = 144 + (24)² = 144 + 576 = 720
```

**Step 5 - Standard Deviation and Mode**
```
σ = √Var(X) = √144 = 12 minutes

Mode = (α − 1)β = (4 − 1) × 6 = 3 × 6 = 18 minutes
```

**Step 6 - Compute P(X ≤ 12) using the incomplete Gamma**
```
Standardise: let Y = X/β = X/6  →  Y ~ Γ(4, 1)

P(X ≤ 12) = P(Y ≤ 12/6) = P(Y ≤ 2)

For integer α = 4, the Gamma CDF has a closed form:
P(Y ≤ y) = 1 − e^(−y) · Σ(k=0 to α−1) y^k/k!

P(Y ≤ 2) = 1 − e^(−2) · [2⁰/0! + 2¹/1! + 2²/2! + 2³/3!]
          = 1 − e^(−2) · [1 + 2 + 2 + 4/3]
          = 1 − e^(−2) · [1 + 2 + 2 + 1.333]
          = 1 − 0.1353 × 6.333
          = 1 − 0.8569
          ≈ 0.1431
```

**Step 7 - Verify using formulas**
```
Formula: E[X]   = αβ   = 4 × 6    = 24    ✓
Formula: Var(X) = αβ²  = 4 × 36   = 144   ✓
```

---

## <span style="color:#1565C0">10. Comprehensive Comparison Table</span>

### <span style="color:#2E86AB">10.1 All 9 Distributions at a Glance</span>

| Distribution | Parameters | Support | Expectation | Variance | Key Feature |
|:---|:---:|:---:|:---:|:---:|:---|
| Continuous Uniform | a, b | [a, b] | (a+b)/2 | (b−a)²/12 | Constant density on interval |
| Exponential | λ | [0, ∞) | 1/λ | 1/λ² | Memoryless; inter-event time |
| Normal | μ, σ² | (−∞, ∞) | μ | σ² | Bell-shaped; Central Limit Theorem |
| Standard Normal | - | (−∞, ∞) | 0 | 1 | Z-score standard; tabulated |
| t-Distribution | ν | (−∞, ∞) | 0 (ν>1) | ν/(ν−2) (ν>2) | Heavy tails; small-sample inference |
| Chi-Squared | k | (0, ∞) | k | 2k | Sum of squared normals; variance tests |
| Logistic | μ, s | (−∞, ∞) | μ | s²π²/3 | Sigmoid CDF; logistic regression |
| Beta | α, β | [0, 1] | α/(α+β) | αβ/[(α+β)²(α+β+1)] | Flexible; models proportions |
| Gamma | α, β | (0, ∞) | αβ | αβ² | Generalises Exponential and χ² |

### <span style="color:#2E86AB">10.2 Hierarchy & Relationships</span>

```
Continuous Uniform(a, b)
   └──► Special case of Beta(1, 1) on any interval

Exponential(λ)
   ├──► Special case of Gamma(1, 1/λ)
   └──► Inter-arrival time of Poisson(λ) process

Normal(μ, σ²)
   ├──► Standardise → Standard Normal N(0, 1)
   └──► Sum of many i.i.d. RVs  →  N  (Central Limit Theorem)

Standard Normal N(0, 1)
   ├──► Z²  ~  χ²(1)
   └──► t(ν) = N(0,1) / √(χ²(ν)/ν)

Chi-Squared χ²(k)
   ├──► Special case of Gamma(k/2, 2)
   └──► Sum of k independent N(0,1)² RVs

Gamma(α, β)
   ├──► α = 1         →  Exponential(1/β)
   ├──► α = k/2, β=2  →  Chi-Squared χ²(k)
   └──► α = n integer →  Erlang(n, 1/β)

Beta(α, β)
   ├──► α = 1, β = 1  →  Uniform(0, 1)
   └──► Conjugate prior for Binomial proportion p
```

### <span style="color:#2E86AB">10.3 Choosing the Right Continuous Distribution</span>

| Scenario | Use |
|:---|:---:|
| Equal likelihood on a bounded interval | Continuous Uniform |
| Time/distance until the next event (Poisson process) | Exponential |
| Symmetric, bell-shaped data around a central value | Normal |
| Standardised normal computations or Z-tests | Standard Normal |
| Small-sample inference when σ is unknown | t-Distribution |
| Tests on variance or goodness-of-fit | Chi-Squared |
| Binary outcomes, sigmoid probabilities | Logistic |
| Modelling probabilities, proportions, or rates | Beta |
| Waiting time for multiple events; skewed positive data | Gamma |

### <span style="color:#2E86AB">10.4 Discrete vs Continuous - Key Contrasts</span>

| Feature | Discrete RV | Continuous RV |
|:---|:---:|:---:|
| Probability at a point | P(X = x) > 0 possible | P(X = x) = 0 always |
| Probability function | PMF | PDF |
| Cumulative function | Σ P(X = xᵢ) | ∫ f(x) dx |
| Support | Countable set | Interval or union of intervals |
| Expectation | Σ x · P(X=x) | ∫ x · f(x) dx |

---

## <span style="color:#1565C0">11. Quick Reference - All PDFs</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 540px;">

### <span style="color:#D4A017">Continuous Uniform:  f(x) = 1/(b−a)</span>

</div>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 540px;">

### <span style="color:#D4A017">Exponential:  f(x) = λ · e^(−λx)</span>

</div>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 540px;">

### <span style="color:#D4A017">Normal:  f(x) = (1/(σ√(2π))) · exp(−(x−μ)²/(2σ²))</span>

</div>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 540px;">

### <span style="color:#D4A017">Standard Normal:  φ(z) = (1/√(2π)) · e^(−z²/2)</span>

</div>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 540px;">

### <span style="color:#D4A017">t-Distribution:  f(t) = [Γ((ν+1)/2) / (√(νπ)·Γ(ν/2))] · (1+t²/ν)^(−(ν+1)/2)</span>

</div>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 540px;">

### <span style="color:#D4A017">Chi-Squared:  f(x) = x^(k/2−1) · e^(−x/2) / (2^(k/2) · Γ(k/2))</span>

</div>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 540px;">

### <span style="color:#D4A017">Logistic:  f(x) = e^(−(x−μ)/s) / [s·(1+e^(−(x−μ)/s))²]</span>

</div>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 540px;">

### <span style="color:#D4A017">Beta:  f(x) = x^(α−1)·(1−x)^(β−1) / B(α,β)</span>

</div>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 540px;">

### <span style="color:#D4A017">Gamma:  f(x) = x^(α−1)·e^(−x/β) / (β^α · Γ(α))</span>

</div>

---

<div align="center">

### **Sagar Bhadra**

<sub>Connect with me on</sub>

<br>

[![GitHub](https://img.shields.io/badge/GitHub-SagarBhadra01-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/SagarBhadra01)&nbsp;
[![X (Twitter)](https://img.shields.io/badge/Twitter-SagarBhadra01-000000?style=for-the-badge&logo=x&logoColor=white)](https://x.com/SagarBhadra01)&nbsp;
[![LinkedIn](https://img.shields.io/badge/LinkedIn-sagarbhadra01-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/sagarbhadra01)&nbsp;
[![Gmail](https://img.shields.io/badge/Gmail-sagarbhadra404@gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:sagarbhadra404@gmail.com)

</div>