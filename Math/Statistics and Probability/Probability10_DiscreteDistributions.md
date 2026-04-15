<div align="center">

# <span style="color:#0A2FA8">Types of Discrete Random Variable Distributions</span>

<sub>Complete notes covering all 8 types - formulas, derivations, properties, examples, and comparisons</sub>

</div>

---

## <span style="color:#1565C0">0. Preliminaries - Discrete Random Variables</span>

> **Definition:** A **Random Variable (RV)** is a function that assigns a numerical value to each outcome of a random experiment. A **Discrete RV** takes a countable (finite or countably infinite) set of values.

> **Definition:** The **Probability Mass Function (PMF)** of a discrete RV X gives P(X = x) for each possible value x.

**Two conditions every valid PMF must satisfy:**

| Condition | Expression |
|:---:|:---:|
| Non-negativity | P(X = x) ≥ 0 for all x |
| Total probability | Σ P(X = x) = 1 |

**Key quantities derived from any discrete distribution:**

| Quantity | Formula |
|:---|:---|
| Expectation | E[X] = Σ x · P(X = x) |
| Variance | Var(X) = E[X²] − (E[X])² |
| Standard Deviation | σ = √Var(X) |
| Moment Generating Function | M(t) = E[e^(tX)] |

---

## <span style="color:#1565C0">1. Discrete Uniform Distribution</span>

### <span style="color:#2E86AB">1.1 Description</span>

> **Definition:** A discrete RV X follows a **Discrete Uniform Distribution** if every value in a finite set {a, a+1, …, b} is equally likely.

This is the simplest distribution - it models complete fairness or equal likelihood among a fixed number of outcomes.

### <span style="color:#2E86AB">1.2 PMF Formula</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">P(X = x) = 1/n,  for x = a, a+1, …, b</span>

</div>

where **n = b − a + 1** is the total number of values.

### <span style="color:#2E86AB">1.3 Key Properties</span>

| Property | Formula | Value (general) |
|:---|:---:|:---:|
| Expectation | E[X] | (a + b) / 2 |
| Variance | Var(X) | (n² − 1) / 12 |
| MGF | M(t) | (1/n) · Σ e^(tx) |

### <span style="color:#2E86AB">1.4 Derivation of Expectation & Variance</span>

```
E[X] = Σ x · (1/n)  from x = a to b
     = (1/n) · [a + (a+1) + ... + b]
     = (1/n) · n(a+b)/2
     = (a + b) / 2
```

```
E[X²] = (1/n) · Σ x²  = (1/n) · [b(b+1)(2b+1)/6 − (a−1)a(2a−1)/6]
Var(X) = E[X²] − (E[X])²  =  (n²−1)/12
```

### <span style="color:#2E86AB">1.5 Use Cases</span>

- Rolling a fair die: X ∈ {1,2,3,4,5,6}
- Drawing a card from a well-shuffled deck (rank only)
- Random selection of one item from a list
- Lottery number selection

### <span style="color:#2E86AB">1.6 Worked Example</span>

**Problem:** A fair die is rolled. Find P(X = x), E[X], E[X²], Var(X), and σ from first principles.

**Step 1 - Identify Parameters**
```
X ∈ {1, 2, 3, 4, 5, 6}   →   a = 1, b = 6, n = b − a + 1 = 6
```

**Step 2 - PMF (verify validity)**
```
P(X = x) = 1/6  for each x ∈ {1,2,3,4,5,6}

Sum check: 1/6 + 1/6 + 1/6 + 1/6 + 1/6 + 1/6 = 6/6 = 1  ✓
```

**Step 3 - Derive E[X] from definition**
```
E[X] = Σ x · P(X = x)
     = 1·(1/6) + 2·(1/6) + 3·(1/6) + 4·(1/6) + 5·(1/6) + 6·(1/6)
     = (1/6) · (1 + 2 + 3 + 4 + 5 + 6)
     = (1/6) · 21
     = 21/6
     = 3.5
```

**Step 4 - Derive E[X²] from definition**
```
E[X²] = Σ x² · P(X = x)
      = (1/6) · (1² + 2² + 3² + 4² + 5² + 6²)
      = (1/6) · (1 + 4 + 9 + 16 + 25 + 36)
      = (1/6) · 91
      = 91/6
      ≈ 15.1667
```

**Step 5 - Derive Var(X) using Var(X) = E[X²] − (E[X])²**
```
Var(X) = E[X²] − (E[X])²
       = 91/6 − (3.5)²
       = 91/6 − 12.25
       = 91/6 − 49/4
       = 182/12 − 147/12
       = 35/12
       ≈ 2.917
```

**Step 6 - Standard Deviation**
```
σ = √Var(X) = √(35/12) = √35 / √12 = 5.916 / 3.464 ≈ 1.708
```

**Step 7 - Verify using formula**
```
Formula: E[X] = (a+b)/2 = (1+6)/2 = 7/2 = 3.5  ✓
Formula: Var(X) = (n²−1)/12 = (36−1)/12 = 35/12  ✓
```

---

## <span style="color:#1565C0">2. Bernoulli Distribution</span>

### <span style="color:#2E86AB">2.1 Description</span>

> **Definition:** A discrete RV X follows a **Bernoulli Distribution** if it models a single trial with exactly two outcomes: **Success (1)** with probability p and **Failure (0)** with probability 1−p.

It is the building block of many other distributions (Binomial, Geometric, Negative Binomial).

### <span style="color:#2E86AB">2.2 PMF Formula</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">P(X = x) = p^x · (1−p)^(1−x),  x ∈ {0, 1}</span>

</div>

Equivalently:
- P(X = 1) = p
- P(X = 0) = 1 − p = q

### <span style="color:#2E86AB">2.3 Key Properties</span>

| Property | Value |
|:---|:---:|
| Expectation | p |
| Variance | p(1−p) = pq |
| MGF | q + p·e^t |
| Skewness | (q − p) / √(pq) |
| Kurtosis | (1 − 6pq) / (pq) |

### <span style="color:#2E86AB">2.4 Conditions (Bernoulli Trial)</span>

```
1. Exactly ONE trial is performed
2. Exactly TWO outcomes: Success / Failure
3. P(Success) = p is fixed and known
4. p ∈ (0, 1)
```

### <span style="color:#2E86AB">2.5 Use Cases</span>

- Flipping a coin once (Heads = success)
- A single exam pass/fail
- A patient recovering or not from a treatment
- A quality control check: defective or non-defective

### <span style="color:#2E86AB">2.6 Worked Example</span>

**Problem:** A biased coin has P(Heads) = 0.7. Find P(X=0), P(X=1), E[X], E[X²], Var(X), and σ from first principles.

**Step 1 - Identify Parameters**
```
X = 1 (Heads = Success),  X = 0 (Tails = Failure)
p = 0.7,   q = 1 − p = 0.3
```

**Step 2 - Compute PMF values**
```
P(X = 1) = p¹ · q^(1−1) = 0.7¹ · 0.3⁰ = 0.7 × 1    = 0.7
P(X = 0) = p⁰ · q^(1−0) = 0.7⁰ · 0.3¹ = 1   × 0.3  = 0.3

Sum check: 0.7 + 0.3 = 1  ✓
```

**Step 3 - Derive E[X] from definition**
```
E[X] = Σ x · P(X = x)
     = 0 · P(X=0)  +  1 · P(X=1)
     = 0 × 0.3     +  1 × 0.7
     = 0 + 0.7
     = 0.7
```

**Step 4 - Derive E[X²] from definition**
```
E[X²] = Σ x² · P(X = x)
      = 0² · P(X=0)  +  1² · P(X=1)
      = 0  × 0.3     +  1  × 0.7
      = 0 + 0.7
      = 0.7

Note: For Bernoulli, E[X²] = E[X] = p, since x² = x for x ∈ {0,1}
```

**Step 5 - Derive Var(X) = E[X²] − (E[X])²**
```
Var(X) = E[X²] − (E[X])²
       = 0.7 − (0.7)²
       = 0.7 − 0.49
       = 0.21
```

**Step 6 - Standard Deviation**
```
σ = √Var(X) = √0.21 ≈ 0.458
```

**Step 7 - Verify using formula**
```
Formula: E[X]   = p        = 0.7   ✓
Formula: Var(X) = p·q      = 0.7 × 0.3 = 0.21  ✓
```

---

## <span style="color:#1565C0">3. Binomial Distribution</span>

### <span style="color:#2E86AB">3.1 Description</span>

> **Definition:** A discrete RV X follows a **Binomial Distribution** B(n, p) if it counts the number of successes in **n independent Bernoulli trials**, each with success probability p.

X is the sum of n independent Bernoulli(p) random variables.

### <span style="color:#2E86AB">3.2 PMF Formula</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">P(X = k) = C(n,k) · p^k · (1−p)^(n−k),  k = 0,1,…,n</span>

</div>

where C(n,k) = n! / (k!(n−k)!) is the binomial coefficient.

### <span style="color:#2E86AB">3.3 Conditions (BINS)</span>

```
B - Binary outcomes only (Success / Failure)
I - Independent trials
N - Fixed number of trials n
S - Same probability p for each trial
```

### <span style="color:#2E86AB">3.4 Key Properties</span>

| Property | Formula |
|:---|:---:|
| Expectation | np |
| Variance | npq = np(1−p) |
| MGF | (q + pe^t)^n |
| Skewness | (q − p) / √(npq) |
| Kurtosis | (1 − 6pq) / (npq) |

### <span style="color:#2E86AB">3.5 Derivation of Expectation</span>

```
X = X₁ + X₂ + ... + Xₙ  (sum of n Bernoulli RVs)
E[X] = E[X₁] + ... + E[Xₙ]  (linearity of expectation)
     = p + p + ... + p  (n times)
     = np
```

### <span style="color:#2E86AB">3.6 Derivation of Variance</span>

```
Var(X) = Var(X₁) + ... + Var(Xₙ)  (independence)
       = pq + pq + ... + pq  (n times)
       = npq
```

### <span style="color:#2E86AB">3.7 Special Cases & Approximations</span>

| Condition | Approximation |
|:---|:---|
| n large, p small, np = λ moderate | Poisson(λ) |
| n large, p not too close to 0 or 1 | Normal(np, npq) |
| n = 1 | Bernoulli(p) |

### <span style="color:#2E86AB">3.8 Use Cases</span>

- Number of heads in 10 coin flips
- Number of defective items in a batch of 100
- Number of patients responding to treatment out of 50
- Number of correct answers in a multiple-choice test

### <span style="color:#2E86AB">3.9 Worked Example</span>

**Problem:** A coin is flipped 8 times. P(Heads) = 0.5. Find P(X = 3), E[X], E[X²], Var(X), and σ from first principles.

**Step 1 - Identify Parameters**
```
n = 8,  p = 0.5,  q = 1 − 0.5 = 0.5
X = number of Heads in 8 flips   →   X ~ Binomial(8, 0.5)
```

**Step 2 - Compute P(X = 3) using PMF**
```
P(X = 3) = C(8, 3) · p³ · q^(8−3)

Step 2a - Compute binomial coefficient C(8,3):
  C(8,3) = 8! / (3! · 5!)
          = (8 × 7 × 6) / (3 × 2 × 1)
          = 336 / 6
          = 56

Step 2b - Compute p³:
  (0.5)³ = 0.5 × 0.5 × 0.5 = 0.125

Step 2c - Compute q⁵:
  (0.5)⁵ = 0.5 × 0.5 × 0.5 × 0.5 × 0.5 = 0.03125

Step 2d - Multiply all parts:
  P(X=3) = 56 × 0.125 × 0.03125
          = 56 × 0.00390625
          = 0.21875
          ≈ 0.2188
```

**Step 3 - Derive E[X] from first principles**
```
E[X] = Σ(k=0 to 8) k · C(8,k) · (0.5)^k · (0.5)^(8−k)

Using the identity: k · C(n,k) = n · C(n−1, k−1)

E[X] = Σ(k=1 to 8) k · C(8,k) · (0.5)⁸
     = 8 · Σ(k=1 to 8) C(7, k−1) · (0.5)⁸
     = 8 · (0.5)⁸ · Σ(j=0 to 7) C(7,j)   [let j = k−1]
     = 8 · (0.5)⁸ · 2⁷                    [binomial theorem: Σ C(7,j) = 2⁷]
     = 8 · (1/256) · 128
     = 8 · 128/256
     = 8 · 0.5
     = 4
```

**Step 4 - Derive E[X²] and Var(X)**
```
Use: Var(X) = E[X(X−1)] + E[X] − (E[X])²

E[X(X-1)] = Σ k(k-1) · C(8,k) · (0.5)⁸
           = 8·7 · (0.5)⁸ · Σ C(6, k-2)  [using k(k-1)·C(n,k) = n(n-1)·C(n-2,k-2)]
           = 56 · (0.5)⁸ · 2⁶
           = 56 · (1/256) · 64
           = 56 · 64/256
           = 56 × 0.25
           = 14

E[X²]  = E[X(X−1)] + E[X] = 14 + 4 = 18

Var(X) = E[X²] − (E[X])²
       = 18 − 4²
       = 18 − 16
       = 2
```

**Step 5 - Standard Deviation**
```
σ = √Var(X) = √2 ≈ 1.414
```

**Step 6 - Verify using formulas**
```
E[X]   = np   = 8 × 0.5         = 4    ✓
Var(X) = npq  = 8 × 0.5 × 0.5  = 2    ✓
```

---

## <span style="color:#1565C0">4. Poisson Distribution</span>

### <span style="color:#2E86AB">4.1 Description</span>

> **Definition:** A discrete RV X follows a **Poisson Distribution** Poisson(λ) if it counts the number of events occurring in a fixed interval of time or space, where events occur independently at a constant average rate λ.

### <span style="color:#2E86AB">4.2 PMF Formula</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">P(X = k) = (e^(−λ) · λ^k) / k!,  k = 0, 1, 2, …</span>

</div>

where λ > 0 is the average rate (mean) of occurrences.

### <span style="color:#2E86AB">4.3 Conditions</span>

```
1. Events occur independently of each other
2. Average rate λ is constant over the interval
3. Two events cannot occur at exactly the same instant
4. λ is the mean number of events per interval
```

### <span style="color:#2E86AB">4.4 Key Properties</span>

| Property | Value |
|:---|:---:|
| Expectation | λ |
| Variance | λ |
| MGF | exp(λ(e^t − 1)) |
| Skewness | 1/√λ |
| Kurtosis | 1/λ |

> **Key fact:** In Poisson distribution, **Expectation = Variance = λ**. This is a unique and identifying property.

### <span style="color:#2E86AB">4.5 Derivation from Binomial (Poisson as Limit)</span>

```
Start with Binomial B(n, p) where n→∞, p→0, np→λ (fixed)

P(X=k) = C(n,k) · p^k · (1−p)^(n−k)

As n→∞:
  C(n,k) · p^k → λ^k / k!       [since p = λ/n]
  (1−p)^(n−k) → e^(−λ)          [standard limit]

Therefore:
  P(X=k) → e^(−λ) · λ^k / k!    ✓ (Poisson PMF)
```

### <span style="color:#2E86AB">4.6 Additive Property</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">If X ~ Poisson(λ₁) and Y ~ Poisson(λ₂), independently, then X+Y ~ Poisson(λ₁+λ₂)</span>

</div>

### <span style="color:#2E86AB">4.7 Use Cases</span>

- Number of calls arriving at a call center per hour
- Number of typos per page in a book
- Number of accidents on a highway per day
- Number of radioactive decays per second
- Number of emails received per hour

### <span style="color:#2E86AB">4.8 Worked Example</span>

**Problem:** On average, 3 cars arrive at a toll booth per minute. Find P(X = 0), P(X = 2), P(X ≥ 1), E[X], E[X²], Var(X), and σ from first principles.

**Step 1 - Identify Parameters**
```
X = number of cars arriving per minute
λ = 3   (average rate)
X ~ Poisson(3)
e^(−3) = 0.049787… ≈ 0.0498
```

**Step 2 - Compute P(X = 0)**
```
P(X = 0) = e^(−λ) · λ⁰ / 0!
          = e^(−3) · 1 / 1
          = e^(−3)
          ≈ 0.0498
```

**Step 3 - Compute P(X = 2)**
```
P(X = 2) = e^(−λ) · λ² / 2!
          = e^(−3) · 3² / 2
          = e^(−3) · 9 / 2
          = 0.0498 × 4.5
          ≈ 0.2240
```

**Step 4 - Compute P(X ≥ 1) using complement**
```
P(X ≥ 1) = 1 − P(X = 0)
          = 1 − e^(−3)
          = 1 − 0.0498
          ≈ 0.9502
```

**Step 5 - Derive E[X] from first principles**
```
E[X] = Σ(k=0 to ∞) k · [e^(−λ) · λ^k / k!]

The k=0 term is 0, so:
E[X] = Σ(k=1 to ∞) k · e^(−λ) · λ^k / k!
     = Σ(k=1 to ∞) e^(−λ) · λ^k / (k−1)!    [cancel k with k!]

Let j = k − 1:
     = e^(−λ) · Σ(j=0 to ∞) λ^(j+1) / j!
     = e^(−λ) · λ · Σ(j=0 to ∞) λ^j / j!
     = e^(−λ) · λ · e^λ                       [Taylor series: Σ λ^j/j! = e^λ]
     = λ

For λ = 3:
E[X] = 3
```

**Step 6 - Derive E[X²] and Var(X)**
```
Use the factorization trick: E[X²] = E[X(X−1)] + E[X]

Derive E[X(X−1)]:
E[X(X−1)] = Σ(k=0 to ∞) k(k−1) · e^(−λ) · λ^k / k!

k=0 and k=1 terms are zero (k(k-1) = 0), so:
         = Σ(k=2 to ∞) e^(−λ) · λ^k / (k−2)!    [cancel k(k-1) with k!]

Let j = k − 2:
         = e^(−λ) · Σ(j=0 to ∞) λ^(j+2) / j!
         = e^(−λ) · λ² · Σ(j=0 to ∞) λ^j / j!
         = e^(−λ) · λ² · e^λ
         = λ²

For λ = 3:
E[X(X−1)] = 9

Therefore:
E[X²]  = E[X(X−1)] + E[X] = 9 + 3 = 12

Var(X) = E[X²] − (E[X])²
       = 12 − 3²
       = 12 − 9
       = 3
```

**Step 7 - Standard Deviation**
```
σ = √Var(X) = √3 ≈ 1.732
```

**Step 8 - Verify using formula**
```
Formula: E[X]   = λ = 3  ✓
Formula: Var(X) = λ = 3  ✓   (Expectation = Variance - unique to Poisson)
```

---

## <span style="color:#1565C0">5. Geometric Distribution</span>

### <span style="color:#2E86AB">5.1 Description</span>

> **Definition:** A discrete RV X follows a **Geometric Distribution** if it counts the number of **Bernoulli trials needed to get the first success**.

Two equivalent forms exist:

| Form | X represents | Support |
|:---|:---|:---:|
| Form 1 | Number of trials until 1st success (inclusive) | {1, 2, 3, …} |
| Form 2 | Number of failures before 1st success | {0, 1, 2, …} |

### <span style="color:#2E86AB">5.2 PMF Formula</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">P(X = k) = (1−p)^(k−1) · p,  k = 1, 2, 3, …  [Form 1]</span>

</div>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">P(X = k) = (1−p)^k · p,  k = 0, 1, 2, …  [Form 2]</span>

</div>

### <span style="color:#2E86AB">5.3 Key Properties (Form 1)</span>

| Property | Formula |
|:---|:---:|
| Expectation | 1/p |
| Variance | (1−p) / p² = q/p² |
| MGF | pe^t / (1 − qe^t), t < −ln(q) |

### <span style="color:#2E86AB">5.4 Memoryless Property</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">P(X > m+n | X > m) = P(X > n)  for all m, n ≥ 0</span>

</div>

> **Key fact:** The Geometric distribution is the **only discrete distribution with the memoryless property**. Past failures do not affect the probability of future success.

```
Proof:
P(X > m+n | X > m) = P(X > m+n) / P(X > m)
                   = q^(m+n) / q^m
                   = q^n
                   = P(X > n)  ✓
```

### <span style="color:#2E86AB">5.5 Use Cases</span>

- Number of times you flip a coin until you get Heads
- Number of interview attempts to get a job offer
- Number of sales calls to make the first sale
- Number of trials before a machine produces a defective item

### <span style="color:#2E86AB">5.6 Worked Example</span>

**Problem:** P(success) = 0.3 per trial. Find P(X = 4), P(X > 4), E[X], E[X²], Var(X), and σ from first principles.

**Step 1 - Identify Parameters**
```
p = 0.3,   q = 1 − p = 0.7
X = number of trials until first success  →  X ~ Geometric(0.3)
```

**Step 2 - Compute P(X = 4)**
```
P(X = 4) = q^(k−1) · p
          = (0.7)^(4−1) · 0.3
          = (0.7)³ · 0.3

(0.7)³ = 0.7 × 0.7 × 0.7 = 0.49 × 0.7 = 0.343

P(X = 4) = 0.343 × 0.3 = 0.1029
```

**Step 3 - Compute P(X > 4) using survival function**
```
P(X > k) = q^k   [all k trials are failures]

P(X > 4) = (0.7)⁴ = 0.343 × 0.7 = 0.2401
```

**Step 4 - Derive E[X] from first principles using geometric series**
```
E[X] = Σ(k=1 to ∞) k · q^(k−1) · p
     = p · Σ(k=1 to ∞) k · q^(k−1)

Recall the identity: Σ(k=1 to ∞) k · x^(k−1) = 1/(1−x)²  for |x| < 1

E[X] = p · 1/(1−q)²
     = p · 1/p²              [since 1−q = p]
     = 1/p

For p = 0.3:
E[X] = 1/0.3 = 10/3 ≈ 3.333
```

**Step 5 - Derive E[X²] and Var(X)**
```
Use: E[X²] = E[X(X+1)] − E[X]

First find E[X(X+1)]:
E[X(X+1)] = Σ(k=1 to ∞) k(k+1) · q^(k−1) · p

Recall: Σ(k=1 to ∞) k(k+1) · x^(k−1) = 2/(1−x)³

E[X(X+1)] = p · 2/(1−q)³
           = p · 2/p³
           = 2/p²

For p = 0.3:
E[X(X+1)] = 2/(0.3)² = 2/0.09 ≈ 22.222

E[X²] = E[X(X+1)] − E[X]
      = 22.222 − 3.333
      = 18.889

Var(X) = E[X²] − (E[X])²
       = 18.889 − (3.333)²
       = 18.889 − 11.111
       = 7.778
```

**Step 6 - Standard Deviation**
```
σ = √Var(X) = √7.778 ≈ 2.789
```

**Step 7 - Verify using formula**
```
Formula: E[X]   = 1/p     = 1/0.3         ≈ 3.333  ✓
Formula: Var(X) = q/p²    = 0.7/(0.3)²   = 0.7/0.09 ≈ 7.778  ✓
```

---

## <span style="color:#1565C0">6. Hyper-Geometric Distribution</span>

### <span style="color:#2E86AB">6.1 Description</span>

> **Definition:** A discrete RV X follows a **Hyper-Geometric Distribution** if it counts the number of successes in a sample of n items drawn **without replacement** from a finite population of N items containing K successes and N−K failures.

Key contrast: Unlike Binomial, trials are **not independent** (sampling without replacement).

### <span style="color:#2E86AB">6.2 PMF Formula</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">P(X = k) = [C(K,k) · C(N−K, n−k)] / C(N, n)</span>

</div>

**Parameters:**

| Symbol | Meaning |
|:---:|:---|
| N | Population size |
| K | Number of success states in population |
| n | Sample size drawn |
| k | Number of observed successes (X = k) |

**Valid range of k:** max(0, n+K−N) ≤ k ≤ min(n, K)

### <span style="color:#2E86AB">6.3 Key Properties</span>

| Property | Formula |
|:---|:---:|
| Expectation | nK/N |
| Variance | n · (K/N) · (1−K/N) · (N−n)/(N−1) |
| FPC factor | (N−n)/(N−1) - finite population correction |

> **Key fact:** The factor **(N−n)/(N−1)** is the **Finite Population Correction (FPC)**. As N→∞ with K/N→p, the Hyper-Geometric approaches the Binomial B(n,p).

### <span style="color:#2E86AB">6.4 Comparison: Hyper-Geometric vs Binomial</span>

| Feature | Hyper-Geometric | Binomial |
|:---|:---:|:---:|
| Sampling type | Without replacement | With replacement |
| Independence | <span style="color:#C0392B">No</span> | <span style="color:#27AE60">Yes</span> |
| Population | Finite | Infinite (or with replacement) |
| Variance | Less (due to FPC) | np(1−p) |

### <span style="color:#2E86AB">6.5 Use Cases</span>

- Drawing cards from a deck (5 cards from 52, without replacing)
- Quality control: inspecting k defective items from a batch
- Ecological sampling: number of tagged fish in a catch
- Blood typing in a group without replacement

### <span style="color:#2E86AB">6.6 Worked Example</span>

**Problem:** A box has 12 items: 4 defective and 8 good. 3 are randomly selected without replacement. Find P(X = 0), P(X = 1), P(X = 2), E[X], Var(X), and σ - all fully derived.

**Step 1 - Identify Parameters**
```
N = 12  (total population)
K = 4   (defectives in population)
N−K = 8 (good items in population)
n = 3   (sample drawn without replacement)
X = number of defectives in the sample
```

**Step 2 - Compute the denominator C(N, n) = C(12, 3)**
```
C(12, 3) = 12! / (3! · 9!)
          = (12 × 11 × 10) / (3 × 2 × 1)
          = 1320 / 6
          = 220
```

**Step 3 - Compute P(X = 0)**
```
P(X=0) = C(4,0) · C(8,3) / C(12,3)

C(4,0) = 1
C(8,3) = (8 × 7 × 6)/(3 × 2 × 1) = 336/6 = 56

P(X=0) = 1 × 56 / 220 = 56/220 ≈ 0.2545
```

**Step 4 - Compute P(X = 1)**
```
P(X=1) = C(4,1) · C(8,2) / C(12,3)

C(4,1) = 4
C(8,2) = (8 × 7)/(2 × 1) = 56/2 = 28

P(X=1) = 4 × 28 / 220 = 112/220 ≈ 0.5091
```

**Step 5 - Compute P(X = 2)**
```
P(X=2) = C(4,2) · C(8,1) / C(12,3)

C(4,2) = (4 × 3)/(2 × 1) = 12/2 = 6
C(8,1) = 8

P(X=2) = 6 × 8 / 220 = 48/220 ≈ 0.2182
```

**Step 6 - Verify PMF sums to 1**
```
P(X=3) = C(4,3)·C(8,0)/C(12,3) = 4×1/220 = 4/220 ≈ 0.0182

Total = 56/220 + 112/220 + 48/220 + 4/220
      = 220/220 = 1  ✓
```

**Step 7 - Derive E[X] from first principles**
```
E[X] = Σ k · P(X = k)
     = 0·(56/220) + 1·(112/220) + 2·(48/220) + 3·(4/220)
     = (0 + 112 + 96 + 12) / 220
     = 220 / 220
     = 1

Using formula verification:
E[X] = nK/N = 3 × 4/12 = 12/12 = 1  ✓
```

**Step 8 - Derive E[X²] and Var(X)**
```
E[X²] = Σ k² · P(X = k)
      = 0²·(56/220) + 1²·(112/220) + 2²·(48/220) + 3²·(4/220)
      = (0 + 112 + 192 + 36) / 220
      = 340 / 220
      ≈ 1.5455

Var(X) = E[X²] − (E[X])²
       = 340/220 − 1²
       = 340/220 − 220/220
       = 120/220
       ≈ 0.5455
```

**Step 9 - Standard Deviation**
```
σ = √(120/220) = √(6/11) ≈ 0.7385
```

**Step 10 - Verify using formula**
```
Var(X) = n · (K/N) · (1 − K/N) · (N−n)/(N−1)
       = 3 · (4/12) · (8/12) · (9/11)
       = 3 · (1/3) · (2/3) · (9/11)
       = 3 · 0.3333 · 0.6667 · 0.8182
       = 3 × 0.18182
       ≈ 0.5455  ✓
```

---

## <span style="color:#1565C0">7. Negative Binomial Distribution</span>

### <span style="color:#2E86AB">7.1 Description</span>

> **Definition:** A discrete RV X follows a **Negative Binomial Distribution** NB(r, p) if it counts the number of **Bernoulli trials needed to achieve the r-th success** (or alternatively, the number of failures before the r-th success).

It is a **generalization of the Geometric distribution** (Geometric = NB with r = 1).

### <span style="color:#2E86AB">7.2 PMF Formula</span>

**Form 1 - Number of trials for r-th success (X = k, k = r, r+1, …):**

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">P(X = k) = C(k−1, r−1) · p^r · (1−p)^(k−r)</span>

</div>

**Form 2 - Number of failures before r-th success (Y = k, k = 0, 1, 2, …):**

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">P(Y = k) = C(k+r−1, k) · p^r · q^k</span>

</div>

### <span style="color:#2E86AB">7.3 Key Properties (Form 2 - failures before r-th success)</span>

| Property | Formula |
|:---|:---:|
| Expectation | rq/p = r(1−p)/p |
| Variance | rq/p² |
| MGF | [p/(1−qe^t)]^r, t < −ln(q) |

### <span style="color:#2E86AB">7.4 Relationship to Other Distributions</span>

```
NB(1, p)   →   Geometric(p)           [r = 1 special case]
NB(r, p) as r→∞, p→1 (suitably) →    Normal distribution
NB(r, p) as r→∞, p→1 with rq→λ →    Poisson(λ)
```

### <span style="color:#2E86AB">7.5 Use Cases</span>

- Number of sales calls to close 5 deals
- Number of coin flips to get 3 heads
- Number of patients screened to find 10 positives
- Modeling over-dispersed count data (Var > Mean), where Poisson fails

### <span style="color:#2E86AB">7.6 Worked Example</span>

**Problem:** A basketball player makes each free throw with probability 0.7. Find P(3rd success on 5th attempt), P(X = 6), E[X], E[X²], Var(X), and σ - all fully derived.

**Step 1 - Identify Parameters**
```
r = 3   (need 3 successes)
p = 0.7 (probability of success per throw)
q = 1 − p = 0.3
X = trial on which the 3rd success occurs  →  X ~ NB(3, 0.7)   [Form 1]
```

**Step 2 - Compute P(X = 5) - 3rd success on 5th attempt**
```
P(X = 5) = C(k−1, r−1) · p^r · q^(k−r)
          = C(5−1, 3−1) · (0.7)³ · (0.3)^(5−3)
          = C(4, 2) · (0.7)³ · (0.3)²

C(4,2) = (4 × 3)/(2 × 1) = 6

(0.7)³ = 0.7 × 0.7 × 0.7 = 0.343
(0.3)² = 0.3 × 0.3        = 0.09

P(X=5) = 6 × 0.343 × 0.09
        = 6 × 0.030870
        = 0.18522 ≈ 0.1852
```

**Step 3 - Compute P(X = 6) - 3rd success on 6th attempt**
```
P(X = 6) = C(5, 2) · (0.7)³ · (0.3)³

C(5,2) = (5 × 4)/(2 × 1) = 10

(0.3)³ = 0.3 × 0.3 × 0.3 = 0.027

P(X=6) = 10 × 0.343 × 0.027
        = 10 × 0.009261
        = 0.09261 ≈ 0.0926
```

**Step 4 - Derive E[X] from first principles**
```
X is the sum of r independent Geometric(p) RVs:
X = G₁ + G₂ + G₃   where each Gᵢ ~ Geometric(p)

By linearity of expectation:
E[X] = E[G₁] + E[G₂] + E[G₃]
     = 1/p + 1/p + 1/p
     = r/p

For r=3, p=0.7:
E[X] = 3/0.7 = 30/7 ≈ 4.286

Interpretation: on average, 4.286 throws needed to get 3 successes.
```

**Step 5 - Derive Var(X) from first principles**
```
Since X = G₁ + G₂ + G₃ (independent Geometric RVs):

Var(X) = Var(G₁) + Var(G₂) + Var(G₃)   [independence]
       = q/p² + q/p² + q/p²
       = r·q/p²

For r=3, q=0.3, p=0.7:
Var(X) = 3 × 0.3 / (0.7)²
       = 0.9 / 0.49
       ≈ 1.837
```

**Step 6 - Derive E[X²]**
```
E[X²] = Var(X) + (E[X])²
      = 1.837 + (4.286)²
      = 1.837 + 18.367
      = 20.204
```

**Step 7 - Standard Deviation**
```
σ = √Var(X) = √1.837 ≈ 1.355
```

**Step 8 - Verify using formulas**
```
Formula: E[X]   = r/p       = 3/0.7        ≈ 4.286  ✓
Formula: Var(X) = r·q/p²    = 3×0.3/0.49  ≈ 1.837  ✓
```

---

## <span style="color:#1565C0">8. Multinomial Distribution</span>

### <span style="color:#2E86AB">8.1 Description</span>

> **Definition:** The **Multinomial Distribution** is the generalization of the Binomial to k > 2 possible outcomes. In n independent trials, each trial results in outcome i with probability pᵢ, and X = (X₁, X₂, …, Xₖ) counts how many times each outcome occurs.

It is a **multivariate** discrete distribution.

### <span style="color:#2E86AB">8.2 PMF Formula</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">P(X₁=x₁, …, Xₖ=xₖ) = [n! / (x₁! x₂! … xₖ!)] · p₁^x₁ · p₂^x₂ · … · pₖ^xₖ</span>

</div>

**Conditions:**
- x₁ + x₂ + … + xₖ = n (all counts must sum to n)
- p₁ + p₂ + … + pₖ = 1 (probabilities sum to 1)
- Each xᵢ ≥ 0

### <span style="color:#2E86AB">8.3 Key Properties</span>

| Property | Formula |
|:---|:---:|
| Marginal Expectation | E[Xᵢ] = n · pᵢ |
| Marginal Variance | Var(Xᵢ) = n · pᵢ · (1−pᵢ) |
| Covariance | Cov(Xᵢ, Xⱼ) = −n · pᵢ · pⱼ  (i ≠ j) |

> **Key fact:** Each marginal Xᵢ ~ Binomial(n, pᵢ). The covariance is **always negative** because if one outcome count increases, others must decrease (since they sum to n).

### <span style="color:#2E86AB">8.4 Relationship to Binomial</span>

```
k = 2 outcomes (p₁ = p, p₂ = 1−p):
  Multinomial(n; p, 1−p) ≡ Binomial(n, p)
```

### <span style="color:#2E86AB">8.5 Multinomial Coefficient</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">C(n; x₁, x₂, …, xₖ) = n! / (x₁! · x₂! · … · xₖ!)</span>

</div>

This counts the number of ways to arrange n objects into k groups of sizes x₁, x₂, …, xₖ.

### <span style="color:#2E86AB">8.6 Use Cases</span>

- Rolling a 6-sided die n times - count of each face
- Election results - votes for k candidates in n ballots
- Classifying n items into k categories
- DNA nucleotide frequency (A, T, G, C)

### <span style="color:#2E86AB">8.7 Worked Example</span>

**Problem:** A fair die is rolled 12 times. Let X₁ = count of 1s, X₂ = count of 2s, X₃ = count of {3,4,5,6}. Find P(X₁=2, X₂=3, X₃=7), E[Xᵢ], Var[Xᵢ], and Cov(X₁, X₂) - all fully derived.

**Step 1 - Identify Parameters**
```
n = 12  (total rolls)
3 categories:
  Category 1: face = 1     →  p₁ = 1/6
  Category 2: face = 2     →  p₂ = 1/6
  Category 3: face ∈{3,4,5,6} → p₃ = 4/6 = 2/3

Verify: p₁ + p₂ + p₃ = 1/6 + 1/6 + 4/6 = 6/6 = 1  ✓
Counts: x₁=2, x₂=3, x₃=7
Verify: x₁ + x₂ + x₃ = 2 + 3 + 7 = 12 = n  ✓
```

**Step 2 - Compute the Multinomial Coefficient**
```
n! / (x₁! · x₂! · x₃!) = 12! / (2! · 3! · 7!)

12! = 479001600
2!  = 2
3!  = 6
7!  = 5040

= 479001600 / (2 × 6 × 5040)
= 479001600 / 60480
= 7920
```

**Step 3 - Compute the probability product**
```
p₁^x₁ · p₂^x₂ · p₃^x₃
= (1/6)² · (1/6)³ · (2/3)⁷

(1/6)² = 1/36
(1/6)³ = 1/216
(2/3)⁷ = 128/2187

Product = (1/36) × (1/216) × (128/2187)
        = 128 / (36 × 216 × 2187)
        = 128 / 17006112
        ≈ 0.000007527
```

**Step 4 - Compute P(X₁=2, X₂=3, X₃=7)**
```
P = Multinomial coefficient × probability product
  = 7920 × (128 / 17006112)
  = 1013760 / 17006112
  ≈ 0.05962
  ≈ 5.96%
```

**Step 5 - Derive E[Xᵢ] for each category**
```
Each Xᵢ ~ Binomial(n, pᵢ)  [marginal distribution]

E[X₁] = n · p₁ = 12 × (1/6)   = 12/6   = 2
E[X₂] = n · p₂ = 12 × (1/6)   = 12/6   = 2
E[X₃] = n · p₃ = 12 × (2/3)   = 24/3   = 8

Cross-check: E[X₁] + E[X₂] + E[X₃] = 2 + 2 + 8 = 12 = n  ✓
```

**Step 6 - Derive Var(Xᵢ) for each category**
```
Var(Xᵢ) = n · pᵢ · (1 − pᵢ)

Var(X₁) = 12 × (1/6) × (5/6)
         = 12 × 5/36
         = 60/36
         = 5/3 ≈ 1.667

Var(X₂) = 12 × (1/6) × (5/6)
         = 5/3 ≈ 1.667   [same as X₁ since p₁ = p₂]

Var(X₃) = 12 × (2/3) × (1/3)
         = 12 × 2/9
         = 24/9
         = 8/3 ≈ 2.667
```

**Step 7 - Derive Cov(X₁, X₂)**
```
Cov(Xᵢ, Xⱼ) = −n · pᵢ · pⱼ   [i ≠ j]

Cov(X₁, X₂) = −12 × (1/6) × (1/6)
             = −12 × 1/36
             = −12/36
             = −1/3
             ≈ −0.333

The negative covariance confirms: if more 1s appear,
fewer 2s can appear (counts must sum to n = 12).
```

**Step 8 - Compute Standard Deviations**
```
σ(X₁) = √(5/3)  ≈ 1.291
σ(X₂) = √(5/3)  ≈ 1.291
σ(X₃) = √(8/3)  ≈ 1.633
```

**Step 9 - Verify using formulas**
```
Formula: E[Xᵢ]       = n·pᵢ              ✓  (all match above)
Formula: Var(Xᵢ)     = n·pᵢ·(1−pᵢ)      ✓  (all match above)
Formula: Cov(Xᵢ,Xⱼ) = −n·pᵢ·pⱼ         ✓  (−1/3 confirmed)
```

---

## <span style="color:#1565C0">9. Comprehensive Comparison Table</span>

### <span style="color:#2E86AB">9.1 All 8 Distributions at a Glance</span>

| Distribution | Parameter(s) | Support | Expectation | Variance | Key Feature |
|:---|:---:|:---:|:---:|:---:|:---|
| Discrete Uniform | a, b | {a,…,b} | (a+b)/2 | (n²−1)/12 | All outcomes equally likely |
| Bernoulli | p | {0, 1} | p | pq | Single binary trial |
| Binomial | n, p | {0,…,n} | np | npq | n independent Bernoulli trials |
| Poisson | λ | {0,1,2,…} | λ | λ | Expectation = Variance; rare events |
| Geometric | p | {1,2,3,…} | 1/p | q/p² | Memoryless; 1st success |
| Hyper-Geometric | N, K, n | {0,…,min(n,K)} | nK/N | (see §6.3) | Without replacement |
| Negative Binomial | r, p | {r,r+1,…} | r/p | rq/p² | r-th success |
| Multinomial | n, p₁…pₖ | x₁+…+xₖ=n | npᵢ | npᵢ(1−pᵢ) | k-category generalization |

### <span style="color:#2E86AB">9.2 Hierarchy & Relationships</span>

```
Bernoulli(p)
   │
   ├──► Binomial(n, p)       ─── [n→∞, p→0, np→λ] ──► Poisson(λ)
   │        │
   │        └── [k=2] ──► Multinomial(n; p₁,…,pₖ)
   │
   ├──► Geometric(p)          ─── [r=1 case] of Negative Binomial
   │
   └──► Negative Binomial(r,p)
            │
            └── [r→∞, p→1, rq→λ] ──► Poisson(λ)

Binomial(n, p) ──► [N→∞] ◄── Hyper-Geometric(N, K, n)
```

### <span style="color:#2E86AB">9.3 Choosing the Right Distribution</span>

| Scenario | Use |
|:---|:---:|
| Fixed n trials, count successes, with replacement | Binomial |
| Fixed n trials, count successes, without replacement | Hyper-Geometric |
| Single trial, two outcomes | Bernoulli |
| Count events in fixed time/space interval | Poisson |
| Trials until first success | Geometric |
| Trials until r-th success | Negative Binomial |
| All outcomes equally likely | Discrete Uniform |
| Multiple categories, fixed n trials | Multinomial |

---

## <span style="color:#1565C0">10. Quick Reference - All Formulas</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 520px;">

### <span style="color:#D4A017">Discrete Uniform:  P(X=x) = 1/n</span>

</div>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 520px;">

### <span style="color:#D4A017">Bernoulli:  P(X=x) = p^x · q^(1−x)</span>

</div>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 520px;">

### <span style="color:#D4A017">Binomial:  P(X=k) = C(n,k) · p^k · q^(n−k)</span>

</div>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 520px;">

### <span style="color:#D4A017">Poisson:  P(X=k) = e^(−λ) · λ^k / k!</span>

</div>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 520px;">

### <span style="color:#D4A017">Geometric:  P(X=k) = q^(k−1) · p</span>

</div>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 520px;">

### <span style="color:#D4A017">Hyper-Geometric:  P(X=k) = C(K,k)·C(N−K,n−k) / C(N,n)</span>

</div>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 520px;">

### <span style="color:#D4A017">Negative Binomial:  P(X=k) = C(k−1,r−1) · p^r · q^(k−r)</span>

</div>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 520px;">

### <span style="color:#D4A017">Multinomial:  P = [n!/(x₁!…xₖ!)] · p₁^x₁ · … · pₖ^xₖ</span>

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