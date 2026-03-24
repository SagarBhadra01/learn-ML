<div align="center">

# <span style="color:#0A2FA8">Conditional Probability</span>

<sub>Complete notes covering definition, properties, chain rule, and related theorems with examples</sub>

</div>

---

## <span style="color:#1565C0">Definition</span>

> **Definition:** Conditional Probability is the probability of an event occurring **given that another event has already occurred**. It answers the question: *"If we know B has happened, what is the probability that A also happens?"*

### <span style="color:#2E86AB">Formula</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">P(A|B) = P(A ∩ B) / P(B),  provided P(B) > 0</span>

</div>

Where:
- `P(A|B)` = Probability of A **given** B
- `P(A ∩ B)` = Probability of both A and B occurring
- `P(B)` = Probability of B (the condition)

### <span style="color:#2E86AB">Derived Multiplication Rules</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">P(A ∩ B) = P(A) · P(B|A)</span>
### <span style="color:#D4A017">P(A ∩ B) = P(B) · P(A|B)</span>

</div>

> **Example:** A bag contains 5 red and 3 blue balls. Two balls are drawn without replacement. What is the probability the second ball is red, given the first was red?
>
> After removing one red ball: 4 red remain out of 7 total.
>
> **P(2nd red | 1st red) = 4/7**

---

## <span style="color:#1565C0">Worked Example — Rolling 2 Dice</span>

**Experiment:** Rolling 2 dice. Sample space n(S) = 6 × 6 = **36**

- **A** = Getting 4 on the 1st die = {(4,1), (4,2), (4,3), (4,4), (4,5), (4,6)} → n(A) = 6
- **B** = Sum of outcomes is 6 = {(1,5), (2,4), (3,3), (4,2), (5,1)} → n(B) = 5

**Find:** P(B|A) — probability that sum is 6, given 1st die shows 4.

```
A ∩ B = {(4,2)}  →  P(A ∩ B) = 1/36
P(A) = 6/36 = 1/6
```

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">P(B|A) = P(A ∩ B) / P(A) = (1/36) / (6/36) = 1/6</span>

</div>

---

## <span style="color:#1565C0">Dependent vs Independent Events</span>

### <span style="color:#2E86AB">② Dependent Events</span>

> **Definition:** Two events are dependent if the occurrence of one affects the probability of the other. P(B|A) ≠ P(B).

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">P(A ∩ B) = P(A) · P(B|A)</span>

</div>

> **Example:** Drawing 2 cards from a deck without replacement.
>
> P(both Aces) = P(1st Ace) × P(2nd Ace | 1st Ace) = (4/52) × (3/51) = **1/221**

### <span style="color:#2E86AB">③ Independent Events</span>

> **Definition:** Two events are independent if the occurrence of one gives no information about the other.

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">P(B|A) = P(B)</span>
### <span style="color:#D4A017">∴ P(A ∩ B) = P(A) · P(B)</span>

</div>

> **Example:** Tossing a coin and rolling a die. Getting Heads doesn't affect the die outcome.
>
> P(Heads ∩ getting 6) = (1/2) × (1/6) = **1/12**

---

## <span style="color:#1565C0">Properties of Conditional Probability</span>

| # | Property | Formula |
|:---:|---|:---:|
| 1 | Probability of B given B | `P(B\|B) = 1` |
| 2 | Mutually exclusive events | `P(A₁∪A₂∪A₃\|B) = P(A₁\|B) + P(A₂\|B) + P(A₃\|B)` |
| 3 | Sample space given any event | `P(S\|A) = 1` |
| 4 | Complement rule | `P(Ā\|B) = 1 − P(A\|B)` |
| 5 | Addition rule | `P(A∪B\|C) = P(A\|C) + P(B\|C) − P(A∩B\|C)` |
| 6 | Subset rule | `If A ⊆ B, then P(A\|C) ≤ P(B\|C)` |

---

## <span style="color:#1565C0">Chain Rule (Multiplication Rule for Multiple Events)</span>

### <span style="color:#2E86AB">For Two Events</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">P(A ∩ B) = P(A) · P(B|A)  — (i)</span>

</div>

### <span style="color:#2E86AB">For Three Events</span>

Derivation flow:
```
P(B ∩ C) = P(B) · P(C|B)
→ P(A ∩ (B ∩ C)) = P(A) · P(B ∩ C | A)
→ P(A ∩ B ∩ C) = P(A) · P(B|A) · P(C|A,B)
```

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">P(A ∩ B ∩ C) = P(A) · P(B|A) · P(C|A,B)</span>

</div>

### <span style="color:#2E86AB">For n Events — General Chain Rule</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 600px;">

### <span style="color:#D4A017">P(A₁ ∩ A₂ ∩ ... ∩ Aₙ) = P(A₁) · P(A₂|A₁) · P(A₃|A₂,A₁) · ... · P(Aₙ|Aₙ₋₁, Aₙ₋₂, ..., A₁)</span>

</div>

> **Example:** A box has 10 balls: 6 red, 4 blue. Draw 3 without replacement. Find probability all 3 are red.
>
> P(all 3 red) = (6/10) × (5/9) × (4/8) = 120/720 = **1/6**


---

## <span style="color:#1565C0">Quick Formula Reference</span>

| Formula | Meaning |
|---|:---:|
| `P(A\|B) = P(A∩B) / P(B)` | Definition |
| `P(A∩B) = P(A) · P(B\|A)` | Multiplication rule |
| `P(Ā\|B) = 1 − P(A\|B)` | Complement rule |
| `P(A∪B\|C) = P(A\|C) + P(B\|C) − P(A∩B\|C)` | Addition rule |
| `P(B\|A) = P(B)` | Independence condition |
| `P(A\|B) = P(B\|A) · P(A) / P(B)` | Bayes' Theorem |
| `P(A) = Σ P(A\|Bᵢ) · P(Bᵢ)` | Law of Total Probability |

---

## <span style="color:#1565C0">Key Points to Remember</span>

- Conditional probability **reduces the sample space** to only the given condition.
- `P(A|B) ≠ P(B|A)` in general — **order matters**.
- If `P(B) = 0`, then `P(A|B)` is **undefined**.
- For independent events, conditioning has **no effect**: `P(A|B) = P(A)`.
- The chain rule is fundamental in probability trees, Bayesian networks, and machine learning.
- All standard probability axioms hold **within** conditional probability.
- Complement, addition, and multiplication rules all have **conditional analogs**.
- Bayes' Theorem is built on both the multiplication rule and the law of total probability.

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