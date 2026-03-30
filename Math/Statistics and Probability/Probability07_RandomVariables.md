<div align="center">

# <span style="color:#0A2FA8">Introduction to Random Variables</span>

<sub>A complete reference covering definitions, types, distributions, formulas, and examples</sub>

</div>

---

## <span style="color:#1565C0">Why Do We Need Random Variables?</span>

> **Motivation:** In probability, outcomes of experiments are often non-numeric (e.g., "Heads", "Tails"). Random variables provide a way to map these outcomes to numbers so that mathematical analysis becomes possible.

**Key Reasons:**

1. **Turns outcomes into numbers** - A random variable maps each outcome of a random experiment to a numerical value, enabling computation of probabilities using arithmetic.
2. **Models whole experiments at once** - Instead of computing P(E₁), P(E₂), P(E₃) separately, we can use P(x = 2), P(x = 3), P(x = 4) uniformly.

**Flow of a Random Experiment:**

```
Random Experiment → Outcomes → Map to Number (R.V.) → Compute Probability
```

---

## <span style="color:#1565C0">Functions - A Quick Review</span>

> **Definition:** A function is a relation between an Input Set (domain) and an Output Set (co-domain) such that each input is related to exactly one output.

**Examples:**
- `f(x) = 3x + 4`
- `f(x) = x²`

---

## <span style="color:#1565C0">Random Experiment</span>

> **Definition:** An experiment for which we don't know the outcome in advance, but we know the range of all possible outcomes.

**Examples:** Tossing a coin, rolling a die, flipping 3 fair coins.

---

## <span style="color:#1565C0">Random Variable - Definition</span>

> **Definition:** A Random Variable is a function that assigns a numerical (numeric) value to each outcome in the Sample Space of a random experiment.

**Notation:**

```
x : S → R
```

| Symbol | Meaning |
|--------|---------|
| `S` | Sample Space |
| `R` | Set of Real Numbers |
| `x` | Random Variable |

A random variable is typically denoted by uppercase letters X, Y, Z (values by lowercase x, y, z).

### <span style="color:#2E86AB">Example: Tossing 2 Coins</span>

```
S = {HH, HT, TH, TT}
x = number of heads
```

| Outcome | x (No. of Heads) |
|---------|:---------------:|
| HH | 2 |
| HT | 1 |
| TH | 1 |
| TT | 0 |

---

## <span style="color:#1565C0">Probability Distribution of a Random Variable</span>

> **Definition:** When we try to assign probability to each possible value of a Random Variable X, it is called the **Probability Distribution** of the Random Variable.

### <span style="color:#2E86AB">Example: Flipping 3 Fair Coins</span>

Sample Space:

```
S = {HHH, HHT, HTH, THH, HTT, THT, TTH, TTT}
```

Let `x` = number of tails in the outcome.

| x | Count | Probability |
|:---:|:---:|:---:|
| 0 | 1 | 1/8 |
| 1 | 3 | 3/8 |
| 2 | 3 | 3/8 |
| 3 | 1 | 1/8 |

**Verification - Sum of all probabilities:**

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 580px;">

### <span style="color:#D4A017">P(x=0) + P(x=1) + P(x=2) + P(x=3) = 1/8 + 3/8 + 3/8 + 1/8 = 1</span>

</div>

---

## <span style="color:#1565C0">Types of Random Variables</span>

Random variables are broadly classified into two types:

| Feature | <span style="color:#2E86AB">Discrete R.V.</span> | <span style="color:#2E86AB">Continuous R.V.</span> |
|---------|:------:|:------:|
| Values | Finite or countably infinite | Infinitely many (uncountable) |
| Nature | Countable set of values | Takes value in an interval |
| Example | No. of heads tossing 3 coins | Time taken to complete a task |
| Example | Sum of outcomes rolling 2 dice | Lifetime of a car |
| Functions | PMF, CDF | PDF, CDF |

---

## <span style="color:#1565C0">Discrete Random Variable</span>

> **Definition:** A Random Variable that can take a finite (or countably infinite) number of distinct values.

**Key Points:**
- Takes values from a countable set
- Each value has a specific probability assigned to it
- Sum of all probabilities = 1

### <span style="color:#2E86AB">Probability Mass Function (PMF)</span>

> **Definition:** A function that gives the probability that a discrete random variable X takes exactly a given value x.

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">P(X = x) = p(x), for all valid x</span>

</div>

**Properties of PMF:**

| Property | Rule |
|----------|------|
| Non-negativity | P(X = x) ≥ 0 for all x |
| Normalization | Σ P(X = x) = 1 |

### <span style="color:#2E86AB">Cumulative Distribution Function (CDF) - Discrete</span>

> **Definition:** CDF gives the probability that X takes a value less than or equal to x.

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 540px;">

### <span style="color:#D4A017">F(x) = P(X ≤ x) = Σ P(X = k), for k ≤ x</span>

</div>



### <span style="color:#1565C0">Types of Discrete Distributions</span>

#### <span style="color:#2E86AB">1. Discrete Uniform Distribution</span>
#### <span style="color:#2E86AB">2. Bernoulli Distribution</span>
#### <span style="color:#2E86AB">3. Binomial Distribution</span>
#### <span style="color:#2E86AB">4. Poisson Distribution</span>
#### <span style="color:#2E86AB">5. Geomatric Distribution</span>
#### <span style="color:#2E86AB">6. Hyper-Geometric Distribution</span>
#### <span style="color:#2E86AB">7. Negative Binomial Distribution</span>
#### <span style="color:#2E86AB">8. Multinomial Distribution</span>

---




## <span style="color:#1565C0">Continuous Random Variable</span>

> **Definition:** A Random Variable that can take an **infinite (uncountable) number of values** within an interval or range.

**Key Points:**
- Takes values in a continuous interval
- Probability at a single point = 0: `P(X = a) = 0`
- Probability is measured over an interval

### <span style="color:#2E86AB">Probability Density Function (PDF)</span>

> **Definition:** A function f(x) such that the probability of X falling in an interval [a, b] equals the area under the curve between a and b.

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">P(a ≤ X ≤ b) = ∫[a to b] f(x) dx</span>

</div>

**Properties of PDF:**

| Property | Rule |
|----------|------|
| Non-negativity | f(x) ≥ 0 for all x |
| Normalization | ∫[−∞ to +∞] f(x) dx = 1 |

### <span style="color:#2E86AB">Cumulative Distribution Function (CDF) - Continuous</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 500px;">

### <span style="color:#D4A017">F(x) = P(X ≤ x) = ∫[−∞ to x] f(t) dt</span>

</div>

---

### <span style="color:#1565C0">Types of Continuous Distributions</span>
#### <span style="color:#2E86AB">1. Continuous Uniform Distribution</span>
#### <span style="color:#2E86AB">2. Exponential Distribution</span>
#### <span style="color:#2E86AB">3. Normal Distribution</span>
#### <span style="color:#2E86AB">4. Standard Normal Distribution</span>
#### <span style="color:#2E86AB">5. t-Distribution</span>
#### <span style="color:#2E86AB">6. Chi-Squared Distribution</span>
#### <span style="color:#2E86AB">7. Logistic Distribution</span>
#### <span style="color:#2E86AB">8. Beta Distribution</span>
#### <span style="color:#2E86AB">9. Gama Distribution</span>


---

## <span style="color:#1565C0">Key Formulas Summary</span>

| Concept | Formula |
|---------|---------|
| PMF (discrete) | P(X = x) = p(x) |
| CDF (discrete) | F(x) = P(X ≤ x) = Σ p(k) |
| PDF (continuous) | P(a ≤ X ≤ b) = ∫[a,b] f(x) dx |
| CDF (continuous) | F(x) = ∫[−∞, x] f(t) dt |
| Expected Value (discrete) | E[X] = Σ x · P(X = x) |
| Expected Value (continuous) | E[X] = ∫ x · f(x) dx |
| Variance | Var(X) = E[X²] − (E[X])² |
| Std Deviation | σ = √Var(X) |
| Z-score | Z = (X − μ) / σ |

---

## <span style="color:#1565C0">Expected Value and Variance - Derivation</span>

### <span style="color:#2E86AB">Expected Value (Mean)</span>

> **Definition:** The weighted average of all possible values of X, weighted by their probabilities.

**For Discrete R.V.:**

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">E[X] = Σ xᵢ · P(X = xᵢ)</span>

</div>

**For Continuous R.V.:**

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 520px;">

### <span style="color:#D4A017">E[X] = ∫[−∞ to +∞] x · f(x) dx</span>

</div>

### <span style="color:#2E86AB">Variance - Derivation</span>

> **Definition:** Measures the spread of the distribution - how far values are from the mean on average.

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">Var(X) = E[X²] − (E[X])²</span>

</div>

**Step-by-step derivation:**

```
Var(X) = E[(X − μ)²]
       = E[X² − 2μX + μ²]
       = E[X²] − 2μ·E[X] + μ²
       = E[X²] − 2μ² + μ²
       = E[X²] − μ²
       = E[X²] − (E[X])²
```

---

## <span style="color:#1565C0">Real-World Use Cases</span>

| Domain | Random Variable | Distribution Used |
|--------|:-------------:|:---------------:|
| Finance | Stock returns | Normal |
| Medical | Drug response (success/fail) | Bernoulli / Binomial |
| Telecom | Call arrivals per hour | Poisson |
| Engineering | Equipment lifespan | Exponential |
| Quality Control | Defect counts in a batch | Poisson / Binomial |
| ML / Statistics | Test statistics | t-distribution, χ² |
| Insurance | Claim amounts | Normal / Exponential |

---

## <span style="color:#1565C0">Quick Classification Tree</span>

```
Random Variable
    |
    |----> Discrete R.V. (countable values)
    |           |
    |           |---> Discrete Uniform
    |           |---> Bernoulli
    |           |---> Binomial
    |           |---> Poisson
    |           |---> Geometric
    |           |---> Hyper-Geometric
    |           |---> Negative Binomial
    |           |---> Multinomial
    |
    |----> Continuous R.V. (uncountable values in interval)
                |
                |---> Continuous Uniform
                |---> Exponential
                |---> Normal
                |---> Standard Normal
                |---> t-distribution
                |---> Chi-Squared
                |---> Logistic
                |---> Beta
                |---> Gama
```

---

## <span style="color:#1565C0">Common Mistakes to Avoid</span>

| <span style="color:#C0392B">Wrong</span> | <span style="color:#27AE60">Correct</span> |
|------|---------|
| Assuming P(X = a) > 0 for continuous R.V. | P(X = a) = 0 always for continuous R.V. |
| Using PMF logic for continuous variables | Use PDF and integrate over intervals |
| Forgetting Σ P(X = x) = 1 check | Always verify probabilities sum to 1 |
| Computing Var(X) manually as E[(X−μ)²] term by term | Use shortcut: Var(X) = E[X²] − (E[X])² |

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