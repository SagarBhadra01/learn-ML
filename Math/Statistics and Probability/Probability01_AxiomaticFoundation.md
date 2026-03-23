<div align="center">

# <span style="color:#0A2FA8">Probability Theory : Axiomatic Foundation</span>

<sub>Core axioms, derived formulas, and key results in probability theory</sub>

</div>

---

## <span style="color:#1565C0">What is an Axiom?</span>

> **Definition:** An axiom is a statement that is accepted as true without proof. It serves as the starting point or foundation upon which an entire theory is built.

In probability theory, **Kolmogorov (1933)** laid down three fundamental axioms that define what a valid probability measure must satisfy. Everything else in probability is derived from these three axioms.

---

## <span style="color:#1565C0">The Three Axioms of Probability</span>

### <span style="color:#2E86AB">Axiom 1 : Non-Negativity</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">P(A) ≥ 0</span>

</div>

The probability of any event A is always greater than or equal to zero. Probability can **never** be negative.

> **Key Point:** Probability lives in the range [0, 1]. It can be 0 (impossible event) but never negative.

---

### <span style="color:#2E86AB">Axiom 2 : Normalization (Unit Measure)</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">P(S) = 1</span>

</div>

The probability of the entire sample space S is always equal to 1.

> **Key Point:** Something from the sample space must always happen. The total probability of all possible outcomes adds up to exactly 1.

---

### <span style="color:#2E86AB">Axiom 3 : Countable Additivity</span>

If A₁, A₂ are **mutually exclusive (disjoint)** events, then:

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">P(A₁ ∪ A₂) = P(A₁) + P(A₂)</span>

</div>

**Generalized form** — If A₁, A₂, A₃, ... Aₙ are n mutually exclusive events:

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">P(A₁ ∪ A₂ ∪ ... ∪ Aₙ) = Σ P(Aᵢ),  i = 1 to n</span>

</div>

> **Key Point:** You can only directly add probabilities when the events cannot happen at the same time (no overlap).

---

## <span style="color:#1565C0">Important Terms</span>

| Term | Definition |
|:---|:---|
| **Sample Space (S)** | The set of all possible outcomes of an experiment |
| **Event (A)** | Any subset of the sample space |
| **Mutually Exclusive Events** | Two events that cannot occur simultaneously — A₁ ∩ A₂ = φ |
| **Disjoint Events** | Another name for mutually exclusive events |
| **Impossible Event** | An event with zero probability — the empty set φ |
| **Certain Event** | An event that always occurs — the sample space S |

---

## <span style="color:#1565C0">Key Results & Derived Formulas from the Axioms</span>

> These are not assumed — they are **proved** directly using the three axioms above.

### <span style="color:#2E86AB">1. Probability of Impossible Event</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">P(φ) = 0</span>

</div>

The empty set (impossible event) has zero probability.

---

### <span style="color:#2E86AB">2. Complement Rule</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">P(Aᶜ) = 1 − P(A)</span>

</div>

The probability that event A does NOT happen equals 1 minus the probability that it does.

---

### <span style="color:#2E86AB">3. Probability Bounds</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">0 ≤ P(A) ≤ 1</span>

</div>

Probability is always between 0 and 1, inclusive.

---

### <span style="color:#2E86AB">4. General Addition Rule</span>

(For any two events — not necessarily mutually exclusive)

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">P(A ∪ B) = P(A) + P(B) − P(A ∩ B)</span>

</div>

> **Note:** When A and B are mutually exclusive, P(A ∩ B) = 0, and this reduces to Axiom 3.

---

### <span style="color:#2E86AB">5. Subset Rule</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">If A ⊆ B, then P(A) ≤ P(B)</span>

</div>

If event A is contained within event B, then B is at least as likely as A.

---

### <span style="color:#2E86AB">6. Difference Rule</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">P(B − A) = P(B) − P(A ∩ B)</span>

</div>

The probability of B occurring without A occurring.

---

### <span style="color:#2E86AB">7. Inclusion-Exclusion Principle (3 Events)</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">P(A ∪ B ∪ C) = P(A) + P(B) + P(C) − P(A∩B) − P(B∩C) − P(A∩C) + P(A∩B∩C)</span>

</div>

---

## <span style="color:#1565C0">Summary Tables</span>

### <span style="color:#2E86AB">The Three Axioms</span>

| Axiom | Name | Formula |
|:---:|:---|:---:|
| 1 | Non-Negativity | `P(A) ≥ 0` |
| 2 | Normalization | `P(S) = 1` |
| 3 | Countable Additivity (mutually exclusive) | `P(A₁ ∪ A₂) = P(A₁) + P(A₂)` |

### <span style="color:#2E86AB">Derived Results at a Glance</span>

| Result | Formula |
|:---|:---:|
| Impossible event | `P(φ) = 0` |
| Complement rule | `P(Aᶜ) = 1 − P(A)` |
| Probability bounds | `0 ≤ P(A) ≤ 1` |
| General addition rule | `P(A∪B) = P(A) + P(B) − P(A∩B)` |
| Subset rule | `If A⊆B → P(A) ≤ P(B)` |
| Difference rule | `P(B−A) = P(B) − P(A∩B)` |

---

## <span style="color:#1565C0">Why These Axioms Matter</span>

- They give probability a **rigorous mathematical definition**, removing all ambiguity.
- Every probability formula used in statistics, machine learning, engineering, and science is ultimately derived from these three axioms.
- They apply to both **discrete** (countable outcomes) and **continuous** (infinite outcomes) probability spaces.
- They ensure **internal consistency** — no contradictions can arise in probability calculations.

```
Axioms (3 rules)
    → Derived results (complement, bounds, addition rule...)
        → Entire theory of probability, statistics, and inference
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