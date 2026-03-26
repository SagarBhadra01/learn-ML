<div align="center">

# <span style="color:#0A2FA8">Probability : Mutually Exclusive and Exhaustive Events</span>

<sub>Core notation, definitions, and examples for understanding event relationships in probability</sub>

</div>

---

## <span style="color:#1565C0">Notation</span>

Let **A** and **B** be two events of a random experiment.

### <span style="color:#2E86AB">Key Probability Notations</span>

| Symbol | Also Written As | Meaning |
|:------:|:---------------:|:--------|
| P(A ∩ B) | P(A and B), P(AB) | Probability that **both** A and B occur simultaneously |
| P(A ∪ B) | P(A or B) | Probability that A **or** B (or both) occur |

> **Note:** A ∩ B means the **intersection** (common part) of A and B. A ∪ B means the **union** (everything in A or B).

---

## <span style="color:#1565C0">Mutually Exclusive Events</span>

> **Definition:** Two events are **mutually exclusive** (also called *disjoint*) if they cannot occur at the same time - they share no common outcomes.

**Formally:**

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">A ∩ B = ∅</span>

</div>

**Which means:**

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">P(A ∩ B) = 0</span>

</div>

### <span style="color:#2E86AB">Important Properties</span>

- Mutually exclusive events **cannot** both happen in a single trial
- If A and B are mutually exclusive: **P(A ∪ B) = P(A) + P(B)**
- This is called the **Addition Rule for Mutually Exclusive Events**
- If events are **not** mutually exclusive: **P(A ∪ B) = P(A) + P(B) − P(A ∩ B)**

> **Common Mistake:** Mutually exclusive does NOT mean impossible - each event can still occur on its own. It only means they cannot occur *together*.

---

## <span style="color:#1565C0">Example: Rolling a Die</span>

> **Random Experiment:** Roll a fair six-faced die once.

**Sample Space:**

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">S = {1, 2, 3, 4, 5, 6}</span>

</div>

### <span style="color:#2E86AB">Define Three Events</span>

| Event | Description | Elements | Size |
|:-----:|:-----------:|:--------:|:----:|
| E₁ | Getting an **Even** number | {2, 4, 6} | 3 |
| E₂ | Getting an **Odd** number | {1, 3, 5} | 3 |
| E₃ | Getting a **Prime** number | {2, 3, 5} | 3 |

### <span style="color:#2E86AB">Finding Intersections</span>

```
E₁ ∩ E₂  →  Even ∩ Odd     =  ∅        (no number is both even and odd)
E₁ ∩ E₃  →  Even ∩ Prime   =  {2}      (2 is the only even prime)
E₂ ∩ E₃  →  Odd  ∩ Prime   =  {3, 5}   (3 and 5 are odd and prime)
```

### <span style="color:#2E86AB">Checking Mutual Exclusivity</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">P(E₁ ∩ E₂) = 0</span>

</div>

<span style="color:#27AE60">**E₁ and E₂ ARE mutually exclusive**</span> - a number rolled cannot be both even and odd at the same time.

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">P(E₁ ∩ E₃) = 1/6 ≠ 0</span>

</div>

<span style="color:#C0392B">**E₁ and E₃ are NOT mutually exclusive**</span> - outcome `2` belongs to both.

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">P(E₂ ∩ E₃) = 2/6 = 1/3 ≠ 0</span>

</div>

<span style="color:#C0392B">**E₂ and E₃ are NOT mutually exclusive**</span> - outcomes `3` and `5` belong to both.

### <span style="color:#2E86AB">Summary Table</span>

| Pair | Intersection | P(intersection) | Mutually Exclusive? |
|:----:|:------------:|:---------------:|:-------------------:|
| E₁ ∩ E₂ | ∅ | 0 | Yes |
| E₁ ∩ E₃ | {2} | 1/6 | No |
| E₂ ∩ E₃ | {3, 5} | 2/6 = 1/3 | No |

---

## <span style="color:#1565C0">Exhaustive Events</span>

> **Definition:** A set of events is **exhaustive** if together they cover the **entire sample space** - meaning at least one of them is guaranteed to occur in every trial of the experiment. No outcome is left unaccounted for.

**Formally**, for events A and B:

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">A ∪ B = S</span>

</div>

This directly implies:

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">P(A ∪ B) = 1</span>

</div>

Because S is the certain event - something from S **always** happens.

### <span style="color:#2E86AB">Key Properties</span>

- Exhaustive events together **leave no outcome uncovered**
- At least one exhaustive event **must** occur in every trial
- Exhaustiveness is about **coverage** - it says nothing about overlap
- You can have **more than two** exhaustive events: E₁ ∪ E₂ ∪ ... ∪ Eₙ = S

### <span style="color:#2E86AB">Example: Rolling a Die</span>

Using the same die experiment with S = {1, 2, 3, 4, 5, 6}:

```
E₁ = {2, 4, 6}   (Even)
E₂ = {1, 3, 5}   (Odd)

E₁ ∪ E₂ = {1, 2, 3, 4, 5, 6} = S   → Exhaustive
```

Every roll must land on either an even or odd number - there is no other possibility.

```
E₁ = {2, 4, 6}   (Even)
E₃ = {2, 3, 5}   (Prime)

E₁ ∪ E₃ = {2, 3, 4, 5, 6} ≠ S      → NOT Exhaustive
```

Outcome `1` is not in E₁ ∪ E₃, so if `1` is rolled, neither event occurs. They do **not** cover the full sample space.

### <span style="color:#2E86AB">Exhaustive vs Mutually Exclusive - The Difference</span>

These are **independent properties** - a pair of events can be one, both, or neither:

| | Mutually Exclusive? | Exhaustive? | What it means |
|:-:|:-:|:-:|:--|
| E₁ and E₂ (Even / Odd) | Yes | Yes | No overlap, full coverage → **Complementary** |
| E₁ and E₃ (Even / Prime) | No | No | Overlap exists, and `1` is missed |
| E₂ and E₃ (Odd / Prime) | No | No | Overlap exists ({3,5}), and `4,6` are missed |
| E₁ and E₂ and E₃ together | No | Yes | Union = {1,2,3,4,5,6} = S → Exhaustive as a group |

> **Key Insight:** Exhaustiveness is about **union = S**. Mutual exclusivity is about **intersection = ∅**. They are completely separate conditions.

### <span style="color:#2E86AB">Complementary Events - Special Case</span>

> **Definition:** Two events are **complementary** if they are **both mutually exclusive AND exhaustive** simultaneously.

If A and A' (read: "A complement") are complementary:

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">P(A) + P(A') = 1 &nbsp;→&nbsp; P(A') = 1 − P(A)</span>

</div>

```
A  = {2, 4, 6}   (Even)       → P(A)  = 3/6 = 1/2
A' = {1, 3, 5}   (Not Even)   → P(A') = 3/6 = 1/2

P(A) + P(A') = 1/2 + 1/2 = 1  ✓
```

This formula is extremely useful - if finding P(A) is hard, compute **1 − P(A')** instead.

---

## <span style="color:#1565C0">Quick Reference</span>

| Concept | Condition | Formula |
|:-------:|:---------:|:-------:|
| Mutually Exclusive | A ∩ B = ∅ | P(A ∩ B) = 0 |
| Addition Rule (ME) | A and B mutually exclusive | P(A ∪ B) = P(A) + P(B) |
| General Addition Rule | Any two events | P(A ∪ B) = P(A) + P(B) − P(A ∩ B) |
| Exhaustive | A ∪ B = S | P(A ∪ B) = 1 |
| Complementary | ME + Exhaustive | P(A) + P(A') = 1 → P(A') = 1 − P(A) |

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