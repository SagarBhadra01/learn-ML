<div align="center">

# <span style="color:#0A2FA8">Probability Functions: PMF, CDF & PDF</span>

<sub>A complete notes on Probability Mass Function, Cumulative Distribution Function, and Probability Density Function for Discrete and Continuous Random Variables</sub>

</div>

---

## <span style="color:#1565C0">1. Random Variables - Quick Recap</span>

> **Definition:** A Random Variable (R.V.) is a function that maps outcomes of a random experiment to real numerical values.

| Type | Description | Example |
|:---:|:---|:---|
| **Discrete R.V.** | Takes countable, finite or countably infinite values | No. of heads in coin tosses |
| **Continuous R.V.** | Takes uncountably infinite values over an interval | Height, weight, temperature |

---

## <span style="color:#1565C0">2. Probability Mass Function (PMF)</span>

### <span style="color:#2E86AB">2.1 Description</span>

For a **discrete random variable X**, the PMF gives the probability that X takes **exactly** a specific value x. It describes how the total probability mass is distributed across all possible values.

> **Definition:** The PMF of a discrete R.V. X is:
> P_X(x) = P(X = x), for all x in R_X

Where **R_X** is the **support** of X - the set of all values X can take.

---

### <span style="color:#2E86AB">2.2 Formula</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">P_X(x) = P(X = x)</span>

</div>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">∑ P_X(x) = 1 &nbsp;&nbsp; (sum over all x in R_X)</span>

</div>

---

### <span style="color:#2E86AB">2.3 Properties of PMF</span>

| # | Property | Expression |
|:---:|:---|:---|
| 1 | Non-negativity | P_X(x) ≥ 0 for all x |
| 2 | Normalization | ∑_x P_X(x) = 1 |
| 3 | Zero outside support | P_X(x) = 0 for x ∉ R_X |
| 4 | Bounded above | P_X(x) ≤ 1 for all x |

---

### <span style="color:#2E86AB">2.4 Key Points</span>

- PMF is also called the **probability distribution** of a discrete R.V.
- Defined only at discrete points - not between them.
- Can be represented as a table, formula, or **bar chart**.
- Each bar height = exact probability at that value.

---

### <span style="color:#2E86AB">2.5 Example - Coin Tossed 5 Times</span>

**Experiment:** A fair coin is tossed 5 times. Let X = number of heads.

- R_X = {0, 1, 2, 3, 4, 5}, &nbsp; n(S) = 2⁵ = 32

**PMF (Binomial formula):**

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">P_X(x) = C(5, x) · (1/2)⁵ = C(5,x) / 32</span>

</div>

**Find P(X = 3):**

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">P_X(3) = C(5,3) / 32 = 10/32 = 5/16</span>

</div>

**Full PMF Table:**

| x | 0 | 1 | 2 | 3 | 4 | 5 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| P_X(x) | 1/32 | 5/32 | 10/32 | 10/32 | 5/32 | 1/32 |

Verification: 1 + 5 + 10 + 10 + 5 + 1 = 32, so ∑ = 32/32 = 1 ✓

---

### <span style="color:#2E86AB">2.6 Use Cases of PMF</span>

- Modeling number of defective items in a batch (Binomial)
- Number of successes in Bernoulli trials
- Rare events per unit time (Poisson distribution)
- Sampling without replacement (Hypergeometric)

---

## <span style="color:#1565C0">3. Cumulative Distribution Function (CDF) - Discrete R.V.</span>

### <span style="color:#2E86AB">3.1 Description</span>

The CDF gives the **cumulative** probability that X takes a value **less than or equal to** some value x_k.

> **Definition:** F_X(x_k) = P(X ≤ x_k) = ∑ P_X(x) for all x ≤ x_k

---

### <span style="color:#2E86AB">3.2 Formula</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">F_X(x_k) = P(X ≤ x_k) = ∑_{x ≤ x_k} P_X(x)</span>

</div>

---

### <span style="color:#2E86AB">3.3 Properties of CDF (Discrete)</span>

| # | Property | Expression |
|:---:|:---|:---|
| 1 | Non-decreasing | F_X(a) ≤ F_X(b) if a ≤ b |
| 2 | Right-continuous | Step (staircase) function |
| 3 | Bounded | 0 ≤ F_X(x) ≤ 1 for all x |
| 4 | Left limit | F_X(−∞) = 0 |
| 5 | Right limit | F_X(+∞) = 1 |
| 6 | Jump magnitude | Jump at x = P_X(x) |

---

### <span style="color:#2E86AB">3.4 Computing Probabilities from CDF (Discrete)</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 520px;">

### <span style="color:#D4A017">P(a < X ≤ b) = F_X(b) − F_X(a)</span>

</div>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 520px;">

### <span style="color:#D4A017">P(X > x) = 1 − F_X(x)</span>

</div>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 520px;">

### <span style="color:#D4A017">P_X(x) = F_X(x) − F_X(x − 1)</span>

</div>

---

### <span style="color:#2E86AB">3.5 Example - CDF of Coin Experiment</span>

Using the same coin-toss experiment (n=5), **compute F_X(3) = P(X ≤ 3):**

```
F_X(3) = P_X(0) + P_X(1) + P_X(2) + P_X(3)
       = 1/32 + 5/32 + 10/32 + 10/32
       = 26/32 = 13/16
```

**Recover P(X = 3) from CDF:**
```
P(X = 3) = F_X(3) − F_X(2) = 26/32 − 16/32 = 10/32 ✓
```

---

## <span style="color:#1565C0">4. Probability Density Function (PDF) - Continuous R.V.</span>

### <span style="color:#2E86AB">4.1 Description</span>

For a **continuous R.V.**, P(X = x) = 0 for every single point. Probability is computed only over **intervals** using the PDF.

> **Definition:** The PDF f_X(x) is a function such that for any interval [a, b]:
> P(a ≤ X ≤ b) = ∫_a^b f_X(x) dx

The PDF describes the **density** (concentration) of probability around a value x - not the probability itself.

---

### <span style="color:#2E86AB">4.2 Formula</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 520px;">

### <span style="color:#D4A017">P(a ≤ X ≤ b) = ∫_a^b f_X(x) dx</span>

</div>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 520px;">

### <span style="color:#D4A017">∫_{−∞}^{+∞} f_X(x) dx = 1</span>

</div>

---

### <span style="color:#2E86AB">4.3 Interpretation</span>

- `f_X(x)` is **NOT** a probability - it is a **probability density**.
- `f_X(x) dx ≈ P(x ≤ X ≤ x + dx)` for infinitesimally small dx.
- `f_X(x)` **can exceed 1** - area under the entire curve must equal 1.
- Sharper, taller peaks mean probability is more concentrated around that x.

---

### <span style="color:#2E86AB">4.4 Properties of PDF</span>

| # | Property | Expression |
|:---:|:---|:---|
| 1 | Non-negativity | f_X(x) ≥ 0 for all x |
| 2 | Normalization | ∫_{−∞}^{+∞} f_X(x) dx = 1 |
| 3 | Single point | P(X = x) = 0 for any x |
| 4 | Interval equality | P(a < X < b) = P(a ≤ X ≤ b) |
| 5 | Can exceed 1 | f_X(x) > 1 is valid |

---

### <span style="color:#2E86AB">4.5 Graphical View</span>

```
   f_X(x)
    |         .....
    |       ..     ..
    |     ..         ..
    |   ..             ..
    | ..                 ..
    +----+---+---+-----------> x
        160  180  200

  Height = density value (NOT probability)
  Shaded area between two x values = Probability
```

---

### <span style="color:#2E86AB">4.6 Common Continuous Distributions</span>

| Distribution | PDF f(x) | Support |
|:---|:---|:---:|
| Uniform(a, b) | 1/(b−a) | [a, b] |
| Normal(μ, σ²) | (1/σ√2π) exp(−(x−μ)²/2σ²) | (−∞, +∞) |
| Exponential(λ) | λ e^(−λx) | x ≥ 0 |
| Gamma(α, β) | x^(α−1) e^(−x/β) / (β^α Γ(α)) | x ≥ 0 |
| Beta(α, β) | x^(α−1)(1−x)^(β−1) / B(α,β) | [0, 1] |

---

### <span style="color:#2E86AB">4.7 Use Cases of PDF</span>

- Modeling heights, weights, IQ scores (Normal distribution)
- Modeling waiting/service times (Exponential)
- Reliability engineering and survival analysis
- Finance: modeling asset price returns (Log-normal)
- Physics: Maxwell-Boltzmann speed distribution

---

## <span style="color:#1565C0">5. CDF - Continuous R.V.</span>

### <span style="color:#2E86AB">5.1 Description</span>

> **Definition:** F_X(x_k) = P(X ≤ x_k) = ∫_{−∞}^{x_k} f_X(t) dt

Same concept as discrete CDF, but uses **integration** instead of summation. The result is a smooth, continuous curve.

---

### <span style="color:#2E86AB">5.2 Properties of CDF (Continuous)</span>

| # | Property | Expression |
|:---:|:---|:---|
| 1 | Non-negativity | F_X(x) ≥ 0 for all x |
| 2 | Right limit | F_X(+∞) = 1 |
| 3 | Interval probability | P(a ≤ X ≤ b) = F_X(b) − F_X(a) |
| 4 | Smooth (no jumps) | F_X is continuous everywhere |
| 5 | Non-decreasing | F_X(a) ≤ F_X(b) if a ≤ b |

---

### <span style="color:#2E86AB">5.3 Relationship: PDF ↔ CDF</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 520px;">

### <span style="color:#D4A017">PDF → CDF (Integrate): &nbsp; F_X(x) = ∫_{−∞}^{x} f_X(t) dt</span>

</div>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 520px;">

### <span style="color:#D4A017">CDF → PDF (Differentiate): &nbsp; f_X(x) = d/dx [F_X(x)]</span>

</div>

---

### <span style="color:#2E86AB">5.4 CDF Graph - Continuous R.V.</span>

```
F_X(x)
  1 |                      ___________
    |                   ../
    |                 ./
    |              ../
    |           ../
    |        ../
    |     ../
    | __./
    +---------------------------------> x
  Smooth S-shaped (sigmoidal) curve, no jumps
```

---

### <span style="color:#2E86AB">5.5 Computing Probabilities (Continuous)</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 520px;">

### <span style="color:#D4A017">P(a ≤ X ≤ b) = F_X(b) − F_X(a)</span>

</div>

Since P(X = x) = 0 for continuous R.V.:
```
P(a < X < b) = P(a ≤ X < b) = P(a < X ≤ b) = P(a ≤ X ≤ b)
```

---

## <span style="color:#1565C0">6. Derivations</span>

### <span style="color:#2E86AB">6.1 PMF from CDF (Discrete)</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 520px;">

### <span style="color:#D4A017">P_X(x) = F_X(x) − F_X(x − 1)</span>

</div>

General form: P_X(x) = F_X(x) − lim_{t → x⁻} F_X(t) (left-hand limit)

---

### <span style="color:#2E86AB">6.2 Expected Value from PMF</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 520px;">

### <span style="color:#D4A017">E[X] = ∑_x x · P_X(x)</span>

</div>

---

### <span style="color:#2E86AB">6.3 Expected Value from PDF</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 520px;">

### <span style="color:#D4A017">E[X] = ∫_{−∞}^{+∞} x · f_X(x) dx</span>

</div>

---

### <span style="color:#2E86AB">6.4 Variance from PMF / PDF</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 520px;">

### <span style="color:#D4A017">Var(X) = E[X²] − (E[X])²</span>

</div>

Discrete: Var(X) = ∑_x (x − μ)² · P_X(x)

Continuous: Var(X) = ∫_{−∞}^{+∞} (x − μ)² · f_X(x) dx

---

## <span style="color:#1565C0">7. Key Differences</span>

### <span style="color:#2E86AB">7.1 PMF vs PDF</span>

| Feature | <span style="color:#27AE60">PMF (Discrete)</span> | <span style="color:#C0392B">PDF (Continuous)</span> |
|:---|:---:|:---:|
| R.V. type | Discrete | Continuous |
| Output | Probability | Probability density |
| Value at a point | P(X = x) > 0 possible | P(X = x) = 0 always |
| Can exceed 1? | No | Yes |
| Total | Sum = 1 | Integral = 1 |
| Graph | Bar chart (spikes) | Smooth density curve |
| Probability over interval | ∑ over interval | ∫ over interval |

---

### <span style="color:#2E86AB">7.2 CDF Discrete vs CDF Continuous</span>

| Feature | <span style="color:#27AE60">CDF - Discrete</span> | <span style="color:#C0392B">CDF - Continuous</span> |
|:---|:---:|:---:|
| Shape | Step function (staircase) | Smooth S-curve |
| Jump size at x | Equals P_X(x) | No jumps |
| Derived from | Summation of PMF | Integration of PDF |
| P(X = x) | Jump at that point | 0 (no jump) |
| Invertible | Lookup table | Smooth inverse F⁻¹(p) |

---

## <span style="color:#1565C0">8. Special Cases and Edge Cases</span>

#### <span style="color:#5B8DB8">P(X = a) for continuous R.V.:</span>
Always 0 - single points have zero area under the PDF curve.

#### <span style="color:#5B8DB8">Endpoint irrelevance (Continuous):</span>
P(a < X < b) = P(a ≤ X ≤ b) since P(X = a) = P(X = b) = 0.

#### <span style="color:#5B8DB8">PDF value > 1:</span>
Perfectly valid. Example: Uniform(0, 0.5) has f(x) = 2 on [0, 0.5], yet ∫ f dx = 2 × 0.5 = 1 ✓

#### <span style="color:#5B8DB8">CDF at boundaries:</span>
F_X(−∞) = 0 always; F_X(+∞) = 1 always - for both discrete and continuous.

---

## <span style="color:#1565C0">9. Unified Quick Reference</span>

| Property | PMF | PDF | CDF |
|:---:|:---:|:---:|:---:|
| R.V. type | Discrete | Continuous | Both |
| Notation | P_X(x) | f_X(x) | F_X(x) |
| At a point | P(X=x) | 0 (always) | P(X ≤ x) |
| Total | ∑ = 1 | ∫ = 1 | 0 to 1 |
| Interval prob. | ∑ over interval | ∫ over interval | F(b) − F(a) |
| Graph | Bar chart | Smooth curve | Staircase / S-curve |

---

### <span style="color:#2E86AB">9.1 Master Formula Sheet</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 580px;">

### <span style="color:#D4A017">PMF: &nbsp; P_X(x) = P(X = x) &nbsp;|&nbsp; ∑ P_X(x) = 1</span>

</div>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 580px;">

### <span style="color:#D4A017">CDF (Discrete): &nbsp; F_X(x_k) = ∑_{x ≤ x_k} P_X(x)</span>

</div>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 580px;">

### <span style="color:#D4A017">PDF: &nbsp; ∫_{−∞}^{+∞} f_X(x) dx = 1</span>

</div>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 580px;">

### <span style="color:#D4A017">CDF (Continuous): &nbsp; F_X(x) = ∫_{−∞}^{x} f_X(t) dt</span>

</div>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 580px;">

### <span style="color:#D4A017">PDF ↔ CDF: &nbsp; f_X(x) = d/dx [F_X(x)]</span>

</div>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 580px;">

### <span style="color:#D4A017">Interval Prob: &nbsp; P(a ≤ X ≤ b) = F_X(b) − F_X(a)</span>

</div>

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