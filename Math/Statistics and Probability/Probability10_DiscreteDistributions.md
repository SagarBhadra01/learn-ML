<div align="center">

# <span style="color:#0A2FA8">Types of Discrete Distributions</span>


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
| Mean (Expected Value) | E[X] = Σ x · P(X = x) |
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
| Mean | E[X] | (a + b) / 2 |
| Variance | Var(X) | (n² − 1) / 12 |
| MGF | M(t) | (1/n) · Σ e^(tx) |

### <span style="color:#2E86AB">1.4 Derivation of Mean & Variance</span>

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

**Problem:** A fair die is rolled. Find E[X] and Var(X).

```
n = 6, a = 1, b = 6
E[X]   = (1+6)/2 = 3.5
Var(X) = (36−1)/12 = 35/12 ≈ 2.917
σ      = √(35/12) ≈ 1.708
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
| Mean | p |
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

**Problem:** A biased coin has P(Heads) = 0.7. Find E[X] and Var(X).

```
p = 0.7, q = 0.3
E[X]   = 0.7
Var(X) = 0.7 × 0.3 = 0.21
σ      = √0.21 ≈ 0.458
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
| Mean | np |
| Variance | npq = np(1−p) |
| MGF | (q + pe^t)^n |
| Skewness | (q − p) / √(npq) |
| Kurtosis | (1 − 6pq) / (npq) |

### <span style="color:#2E86AB">3.5 Derivation of Mean</span>

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

**Problem:** A coin is flipped 8 times. P(Heads) = 0.5. Find P(X = 3), E[X], Var(X).

```
n=8, p=0.5, k=3
P(X=3) = C(8,3) · (0.5)³ · (0.5)⁵
        = 56 · 0.125 · 0.03125
        = 56 × 0.003906 ≈ 0.2188

E[X]   = 8 × 0.5 = 4
Var(X) = 8 × 0.5 × 0.5 = 2
σ      = √2 ≈ 1.414
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
| Mean | λ |
| Variance | λ |
| MGF | exp(λ(e^t − 1)) |
| Skewness | 1/√λ |
| Kurtosis | 1/λ |

> **Key fact:** In Poisson distribution, **Mean = Variance = λ**. This is a unique and identifying property.

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

**Problem:** On average, 3 cars arrive at a toll booth per minute. Find P(X = 0), P(X = 2), and P(X ≥ 1).

```
λ = 3

P(X=0) = e^(−3) · 3⁰/0! = e^(−3) ≈ 0.0498

P(X=2) = e^(−3) · 3²/2! = 0.0498 × 9/2 ≈ 0.2240

P(X≥1) = 1 − P(X=0) = 1 − 0.0498 ≈ 0.9502
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
| Mean | 1/p |
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

**Problem:** P(success) = 0.3 per trial. Find P(X = 4) and E[X].

```
p = 0.3, q = 0.7, k = 4

P(X=4) = (0.7)³ × 0.3 = 0.343 × 0.3 = 0.1029

E[X]   = 1/0.3 ≈ 3.33 trials expected
Var(X) = 0.7/(0.3)² = 0.7/0.09 ≈ 7.78
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
| Mean | nK/N |
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

**Problem:** A box has 12 items: 4 defective, 8 good. 3 are randomly selected without replacement. Find P(X = 2 defectives).

```
N=12, K=4, n=3, k=2

P(X=2) = C(4,2) · C(8,1) / C(12,3)
        = 6 × 8 / 220
        = 48/220
        ≈ 0.2182

E[X]   = nK/N = 3×4/12 = 1
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
| Mean | rq/p = r(1−p)/p |
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

**Problem:** A basketball player makes each free throw with probability 0.7. Find the probability that the 3rd success occurs on the 5th attempt.

```
r=3, p=0.7, q=0.3, k=5 (Form 1)

P(X=5) = C(4,2) · (0.7)³ · (0.3)²
        = 6 × 0.343 × 0.09
        = 6 × 0.030870
        ≈ 0.1852
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
| Marginal Mean | E[Xᵢ] = n · pᵢ |
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

**Problem:** A die is rolled 6 times. Find P(each face appears exactly once).

```
n=6, k=6, x₁=x₂=…=x₆=1, p₁=p₂=…=p₆=1/6

P = [6! / (1!1!1!1!1!1!)] · (1/6)⁶
  = 720 · (1/46656)
  = 720/46656
  ≈ 0.01543  (≈ 1.54%)
```

---

## <span style="color:#1565C0">9. Comprehensive Comparison Table</span>

### <span style="color:#2E86AB">9.1 All 8 Distributions at a Glance</span>

| Distribution | Parameter(s) | Support | Mean | Variance | Key Feature |
|:---|:---:|:---:|:---:|:---:|:---|
| Discrete Uniform | a, b | {a,…,b} | (a+b)/2 | (n²−1)/12 | All outcomes equally likely |
| Bernoulli | p | {0, 1} | p | pq | Single binary trial |
| Binomial | n, p | {0,…,n} | np | npq | n independent Bernoulli trials |
| Poisson | λ | {0,1,2,…} | λ | λ | Mean = Variance; rare events |
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