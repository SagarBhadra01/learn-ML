<div align="center">

# <span style="color:#0A2FA8">Law of Total Probability</span>

<sub>A complete guide to partitioning sample spaces and computing probabilities through conditional reasoning</sub>

</div>

---

## <span style="color:#1565C0">1. Background & Motivation</span>

When we want to find the probability of an event A, it's sometimes impossible or very complicated to compute it directly. However, if we can break the sample space into smaller, non-overlapping pieces, we can compute the probability of A through each piece separately and then add them up. This is the core idea behind the **Law of Total Probability**.

---

## <span style="color:#1565C0">2. Key Concept: Partition of a Sample Space</span>

### <span style="color:#2E86AB">Definition</span>

> **Definition:** A set of events B₁, B₂, B₃, …, Bₙ is called a **partition** of the sample space S if:
> - They are **mutually exclusive**: Bᵢ ∩ Bⱼ = ∅ for i ≠ j (no two events overlap)
> - They are **exhaustive**: B₁ ∪ B₂ ∪ … ∪ Bₙ = S (they cover the entire sample space)
> - Each **P(Bᵢ) > 0**

Think of a partition like slicing a pizza - every slice is distinct (no overlap), and together they make the complete pizza (exhaustive).

### <span style="color:#2E86AB">Example</span>

Rolling a die: Let `B₁ = {1, 2}`, `B₂ = {3, 4}`, `B₃ = {5, 6}`.

These three events are mutually exclusive and exhaustive - they form a partition of `S = {1, 2, 3, 4, 5, 6}`.

---

## <span style="color:#1565C0">3. The Law of Total Probability</span>

### <span style="color:#2E86AB">Theorem</span>

If B₁, B₂, …, Bₙ is a partition of sample space S, then for any event A:

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 520px;">

### <span style="color:#D4A017">P(A) = Σᵢ P(A ∩ Bᵢ) = Σᵢ P(Bᵢ) · P(A | Bᵢ)</span>

</div>

### <span style="color:#2E86AB">Why Does This Work? (Intuition)</span>

Since B₁, B₂, B₃ partition S, we can write:

```
S = B₁ ∪ B₂ ∪ B₃ ∪ …
A = A ∩ S = A ∩ (B₁ ∪ B₂ ∪ B₃ ∪ …)
  → A = (A∩B₁) ∪ (A∩B₂) ∪ (A∩B₃) ∪ …   [by distributive law]
```

Since all the pieces (A ∩ Bᵢ) are mutually exclusive:

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 560px;">

### <span style="color:#D4A017">P(A) = P(A∩B₁) + P(A∩B₂) + P(A∩B₃) + ···</span>

</div>

Applying the **multiplication rule** - P(A ∩ Bᵢ) = P(Bᵢ) · P(A | Bᵢ) - gives us the final formula.

---

## <span style="color:#1565C0">4. Worked Examples</span>

### <span style="color:#2E86AB">Example 1 - Balls in a Bucket</span>

**Problem:** A bucket contains 4 red and 3 white balls. 2 balls are drawn one at a time without replacement. Find the probability that the 2nd ball drawn is red.

#### <span style="color:#5B8DB8">Define Events</span>

| Event | Description |
|:---:|:---|
| A | Drawing a red ball on the 1st attempt |
| Ā | Drawing a white ball on the 1st attempt |
| B | Drawing a red ball on the 2nd attempt |

#### <span style="color:#5B8DB8">Applying the Law of Total Probability</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 560px;">

### <span style="color:#D4A017">P(B) = P(A) · P(B|A) + P(Ā) · P(B|Ā)</span>

</div>

$$= \frac{4}{7} \times \frac{3}{6} + \frac{3}{7} \times \frac{4}{6} = \frac{12}{42} + \frac{12}{42} = \frac{24}{42} = \frac{4}{7}$$

> **Insight:** Intuitively, the probability of picking a red ball on the 2nd draw is the same as on the 1st draw (4/7) - this makes sense by symmetry!

---

### <span style="color:#2E86AB">Example 2 - Bags of Marbles</span>

**Problem:** There are 3 bags, each containing 100 marbles:

| Bag | Red | Blue |
|:---:|:---:|:---:|
| Bag 1 | 75 | 25 |
| Bag 2 | 60 | 40 |
| Bag 3 | 45 | 55 |

A bag is chosen at random, and then one marble is picked randomly. What is the probability the marble is red?

#### <span style="color:#5B8DB8">Define Events</span>

- `B₁, B₂, B₃` = event of choosing Bag 1, Bag 2, Bag 3 respectively
- `R` = event of picking a red marble
- Since bags are chosen equally at random: **P(B₁) = P(B₂) = P(B₃) = 1/3**

#### <span style="color:#5B8DB8">Applying the Law</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 620px;">

### <span style="color:#D4A017">P(R) = P(B₁)·P(R|B₁) + P(B₂)·P(R|B₂) + P(B₃)·P(R|B₃)</span>

</div>

$$= \frac{1}{3} \cdot \frac{75}{100} + \frac{1}{3} \cdot \frac{60}{100} + \frac{1}{3} \cdot \frac{45}{100} = \frac{1}{3}(0.75 + 0.60 + 0.45) = \frac{1}{3}(1.80) = 0.60$$

**Answer: P(R) = 0.60 or 60%**

---

### <span style="color:#2E86AB">Example 3 - Factory Machines</span>

**Problem:** A factory has 3 machines producing bulbs:

| Machine | Production Share | Defective Rate |
|:---:|:---:|:---:|
| M₁ | 50% | 2% |
| M₂ | 30% | 3% |
| M₃ | 20% | 5% |

A bulb is selected at random. What is the probability it is defective?

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 620px;">

### <span style="color:#D4A017">P(D) = P(M₁)·P(D|M₁) + P(M₂)·P(D|M₂) + P(M₃)·P(D|M₃)</span>

</div>

$$= 0.50 \times 0.02 + 0.30 \times 0.03 + 0.20 \times 0.05 = 0.010 + 0.009 + 0.010 = \mathbf{0.029}$$

**Answer: 2.9% chance of a defective bulb.**

---


## <span style="color:#1565C0">5. Key Points to Remember</span>

| Point | Detail |
|:---|:---|
| **Partition is essential** | B₁, B₂,…,Bₙ must be mutually exclusive AND exhaustive |
| **Two equivalent forms** | P(A) = ΣP(A∩Bᵢ) = ΣP(Bᵢ)·P(A\|Bᵢ) - both are the same |
| **It's a weighted average** | P(A) is the weighted average of conditional probabilities P(A\|Bᵢ), weighted by P(Bᵢ) |
| **Works for 2 or more partitions** | With just two: P(A) = P(B)·P(A\|B) + P(B̄)·P(A\|B̄) |
| **Foundation of Bayes'** | Always needed to compute the denominator in Bayes' Theorem |
| **Common mistake** | Forgetting that partitions must be exhaustive - they must cover ALL of S |

---

## <span style="color:#1565C0">6. Step-by-Step Problem-Solving Strategy</span>

```
Step 1 → Identify event A - the event whose probability you want
Step 2 → Find or define a partition B₁, B₂,…,Bₙ of S (verify mutually exclusive + exhaustive)
Step 3 → Find P(Bᵢ) for each partition event
Step 4 → Find P(A|Bᵢ) - conditional probability of A given each Bᵢ
Step 5 → Apply the formula: P(A) = Σ P(Bᵢ) · P(A|Bᵢ)
Step 6 → Sum all terms to get the answer
```

---

## <span style="color:#1565C0">8. Quick Formula Reference</span>

### <span style="color:#2E86AB">General Form</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">P(A) = Σᵢ₌₁ⁿ P(Bᵢ) · P(A | Bᵢ)</span>

<sub>Where B₁, B₂, …, Bₙ is a partition of S</sub>

</div>

### <span style="color:#2E86AB">Special Case (2 Events)</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 520px;">

### <span style="color:#D4A017">P(A) = P(B) · P(A|B) + P(B̄) · P(A|B̄)</span>

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