<div align="center">

# <span style="color:#0A2FA8">Independent & Dependent Events</span>

<sub>Complete notes on probability theory - independent events, dependent events, and conditional probability</sub>

</div>

---

## <span style="color:#1565C0">Independent Events</span>

### <span style="color:#2E86AB">Definition</span>

> **Definition:** Two events A and B are said to be **independent** if the occurrence or non-occurrence of one event does not affect the probability of the other event occurring.

In simple terms: Knowing that A happened gives you no information about whether B will happen.

### <span style="color:#2E86AB">Formula</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">P(A ∩ B) = P(A) · P(B)</span>

</div>

This is valid **only** when A and B are independent.

---

### <span style="color:#2E86AB">Example 1 - Tossing 2 Coins</span>

- `A` = Getting a Head on the first toss
- `B` = Getting a Tail on the second toss

**Sample Space:** S = {HH, HT, TH, TT} → n(S) = 4

| Event | Outcomes | Probability |
| :---: | :---: | :---: |
| A | {HH, HT} | 2/4 = 1/2 |
| B | {HT, TT} | 2/4 = 1/2 |
| A ∩ B | {HT} | 1/4 |

**Verification:**

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">P(A) · P(B) = 1/2 × 1/2 = 1/4 = P(A ∩ B) ✓</span>

</div>

<span style="color:#27AE60">Events are Independent</span>

---

### <span style="color:#2E86AB">Example 2 - Rolling a Die Twice</span>

- `A` = Getting an even number on the first roll → {2, 4, 6} → P(A) = 3/6 = **1/2**
- `B` = Getting a number > 4 on the second roll → {5, 6} → P(B) = 2/6 = **1/3**

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">P(A ∩ B) = 1/2 × 1/3 = 1/6</span>

</div>

The result of the first roll has no effect on the second roll → **Independent.**

---

## <span style="color:#1565C0">Dependent Events</span>

### <span style="color:#2E86AB">Definition</span>

> **Definition:** Two events A and B are **dependent** if the occurrence of one event changes (affects) the probability of the other event occurring.

In simple terms: Knowing that A happened does give you information about whether B will happen - it changes its probability.

### <span style="color:#2E86AB">Formula</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">P(A ∩ B) = P(A) · P(B|A)</span>

</div>

Where `P(B|A)` is the **Conditional Probability** of B given that A has already occurred.

---

## <span style="color:#1565C0">Example - Drawing Cards Without Replacement</span>

**Setup:** A standard deck of 52 cards.

- `A` = First card drawn is an ACE
- `B` = Second card drawn is also an ACE

**Sample Space:** n(S) = 52 × 51 (order matters, no replacement)

### <span style="color:#2E86AB">Finding P(A)</span>

There are 4 Aces in the deck.

```
n(A) = 4 × 51   (first card is ace, second can be anything)
P(A) = (4 × 51) / (52 × 51) = 4/52
```

### <span style="color:#2E86AB">Finding P(B|A) - Two Cases</span>

| Case | Condition | Remaining Aces | P(B\|A) |
| :---: | :--- | :---: | :---: |
| Case 1 | First card **was** an Ace | 3 out of 51 | 3/51 |
| Case 2 | First card was **NOT** an Ace | 4 out of 51 | 4/51 |

### <span style="color:#2E86AB">Finding P(A ∩ B) - Both Cards are Aces</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">P(A ∩ B) = P(A) · P(B|A) = (4/52) × (3/51) = 12/2652 = 1/221</span>

</div>

Since the outcome of the first draw directly affects the second → these are **Dependent Events.**

---

## <span style="color:#1565C0">Key Difference - Independent vs Dependent</span>

| Feature | Independent | Dependent |
| :--- | :---: | :---: |
| Effect on each other | None | Yes |
| Formula | P(A ∩ B) = P(A) · P(B) | P(A ∩ B) = P(A) · P(B\|A) |
| P(B\|A) equals | <span style="color:#27AE60">P(B)</span> | <span style="color:#C0392B">≠ P(B)</span> |
| Common scenario | With replacement / separate trials | Without replacement |

---

## <span style="color:#1565C0">Mutually Exclusive vs Independent</span>

This is a very common point of confusion:

| Concept | Meaning | Formula |
| :--- | :--- | :---: |
| **Mutually Exclusive** | A and B cannot happen at the same time | P(A ∩ B) = 0 |
| **Independent** | A and B can happen together; one doesn't affect the other | P(A ∩ B) = P(A) · P(B) |

> **Important:** Mutually exclusive events (with non-zero probabilities) are actually **dependent** - because if A occurs, B definitely cannot, which changes B's probability.

---

## <span style="color:#1565C0">Key Points to Remember</span>

| # | Rule |
| :---: | :--- |
| 1 | **Test for Independence:** Check if P(A ∩ B) = P(A) · P(B). If yes → Independent. |
| 2 | **With Replacement** → usually leads to Independent events (probabilities reset). |
| 3 | **Without Replacement** → usually leads to Dependent events (sample space shrinks). |
| 4 | `P(B\|A) = P(B)` is an alternative way to verify independence. |
| 5 | Conditional probability is only needed for dependent events. |
| 6 | Independence is **symmetric**: if A is independent of B, then B is independent of A. |
| 7 | For three independent events A, B, C: P(A ∩ B ∩ C) = P(A) · P(B) · P(C) |

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 560px;">

### <span style="color:#D4A017">For three independent events A, B, C:</span>
### <span style="color:#D4A017">P(A ∩ B ∩ C) = P(A) · P(B) · P(C)</span>

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