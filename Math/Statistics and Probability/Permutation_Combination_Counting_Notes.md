<div align="center">

# <span style="color:#0A2FA8">Permutation, Combination & Fundamental Counting</span>

<sub>A structured reference guide covering core counting principles, formulas, and applications</sub>

</div>

---

## <span style="color:#1565C0">1. Fundamental Problem Counting</span>

> **Definition:** A concept used to determine the total number of possible outcomes in a situation. There are 2 core rules used depending on whether tasks are done alternatively or sequentially.

### <span style="color:#2E86AB">Event & Sample Space</span>

| Term | Meaning | Example |
|------|---------|---------|
| **Event** | An outcome of an experiment | Getting a 4 when rolling a die |
| **Sample Space** | The set of all possible outcomes | Rolling a die → S = {1, 2, 3, 4, 5, 6} |

### <span style="color:#2E86AB">Types of Events</span>

| Event Type | Description | Linked Rule |
|------------|-------------|-------------|
| **Mutually Exclusive** | Cannot occur at the same time | Addition Rule |
| **Mutually Independent** | One event does not affect the other | Multiplication Rule |
| **Exhaustive** | Together cover all possible outcomes | — |
| **Complementary** | Mutually exclusive + exhaustive; P(A) + P(Aᶜ) = 1 | — |

---

### <span style="color:#2E86AB">The 2 Core Counting Rules</span>

#### <span style="color:#5B8DB8">Addition Rule (OR)</span>

> If a task can be done in one of several **mutually exclusive** ways, the total number of ways = **sum** of individual ways.

Use when: Task A **OR** Task B (alternatives, not both at once)

- **Example 1:** Bus (3 routes) **OR** Train (2 routes) → Total = 3 + 2 = **5 ways**
- **Example 2:** Door A (4 ways) **OR** Door B (3 ways) → Total = 4 + 3 = **7 ways**

---

#### <span style="color:#5B8DB8">Multiplication Rule (AND)</span>

> If a task consists of multiple **independent subtasks**, the total number of ways = **product** of the ways each subtask can be done.

Use when: Task A **AND then** Task B (sequential steps)

- **Example 1 — Multi-step journey:** A→B (3 roads) × B→C (4 roads) = **12 ways**
- **Example 2 — Forming 2-digit numbers:** 5 × 5 = **25 numbers** (digits {1–5}, repetition allowed)
- **Example 3 — Lock combinations:** 10 × 10 × 10 = **1000 combinations**

---

#### <span style="color:#5B8DB8">Combined Rule Example</span>

- **Outfits:** 3 shirts × 2 trousers × 2 shoes = **12 outfits**

> **Key Distinction:** Use **Addition** for OR (mutually exclusive alternatives). Use **Multiplication** for AND (sequential independent steps).

---

## <span style="color:#1565C0">2. Factorial</span>

> **Definition:** The factorial of a non-negative integer n, written as **n!**, is the product of all positive integers from 1 to n.

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">n! = n × (n−1) × (n−2) × … × 2 × 1</span>

</div>

### <span style="color:#2E86AB">Special Values</span>

| Expression | Value | Note |
|:----------:|:-----:|------|
| 0! | 1 | By definition — 1 way to arrange nothing |
| 1! | 1 | |
| 2! | 2 | |
| 3! | 6 | |
| 4! | 24 | |
| 5! | 120 | |
| 6! | 720 | |
| 7! | 5040 | |
| 8! | 40320 | |
| 9! | 362880 | |
| 10! | 3628800 | |


### <span style="color:#2E86AB">Key Property — Recursive Definition</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">n! = n × (n−1)!</span>

</div>

Example: 7! = 7 × 6! = 7 × 720 = **5040**

### <span style="color:#2E86AB">Example — Word "SUN"</span>

- 3 distinct letters → 3! = 3 × 2 × 1 = **6 arrangements**
- All: `SUN` `SNU` `USN` `UNS` `NSU` `NUS`

> **Rule:** No. of ways to arrange **n unique objects** = n!

---

## <span style="color:#1565C0">3. Permutation</span>

> **Definition:** Permutation means **ordered selection** (arrangement). It counts the number of ways to select r items from n items and arrange them, where **order matters**.

```
n items (total) → select r items → arrange them → r items in order
```

### <span style="color:#2E86AB">Formula Derivation</span>

Selecting r items from n, one at a time:

| Position | Choices |
|:--------:|:-------:|
| 1st | n |
| 2nd | n−1 |
| 3rd | n−2 |
| … | … |
| r-th | n−r+1 |

Total = n × (n−1) × (n−2) × … × (n−r+1) &nbsp;→&nbsp; multiply & divide by (n−r)! &nbsp;→&nbsp; **n! / (n−r)!**


<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">ⁿPᵣ = n! / (n−r)!</span>

</div>

### <span style="color:#2E86AB">Examples</span>

- **Word "DATE", 3-letter words** — ⁴P₃ = 4! / 1! = 24/1 = **24 words** *(DAT ≠ TAD)*
- **Arranging all letters of "MATHS"** — ⁵P₅ = 5! / 0! = **120 ways**

### <span style="color:#2E86AB">Special Cases</span>

| Expression | Value | Explanation |
|:----------:|:-----:|-------------|
| ⁿP₀ | 1 | One way to arrange 0 items |
| ⁿP₁ | n | Selecting any one item |
| ⁿPₙ | n! | Arranging all n items |
| ⁿP₂ | n(n−1) | Selecting and arranging 2 |
| ⁿPᵣ | n × ⁽ⁿ⁻¹⁾P₍ᵣ₋₁₎ | Recursive form |

---

## <span style="color:#1565C0">4. Combination</span>

> **Definition:** Combination means **unordered selection**. It counts the number of ways to select r items from n items where **order does NOT matter** — only the group (selection) matters.

```
n items (total) → select r items → r items (as a group, no order)
```

### <span style="color:#2E86AB">Formula Derivation</span>

ⁿPᵣ counts ordered selections. Each group of r items can be arranged in r! ways — all the same combination. So we divide out the arrangements:

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">ⁿCᵣ = n! / (r! × (n−r)!)</span>

</div>

### <span style="color:#2E86AB">Examples</span>

- **Selecting books** — ⁵C₃ = 5! / (3! × 2!) = 120/12 = **10 ways**
- **Forming a committee** — ⁸C₃ = 8! / (3! × 5!) = 336/6 = **56 committees**
- **Symmetry in action** — ¹⁰C₃ = ¹⁰C₇ = **120** *(choosing 3 = leaving out 7)*

### <span style="color:#2E86AB">Special Cases</span>

| Expression | Value | Explanation |
|:----------:|:-----:|-------------|
| ⁿC₀ | 1 | One way to select nothing |
| ⁿC₁ | n | Selecting any single item |
| ⁿCₙ | 1 | Only one way to select all |
| ⁿCᵣ | ⁿC₍ₙ₋ᵣ₎ | Symmetry property |

---

## <span style="color:#1565C0">5. Relation Between Permutation & Combination</span>

| | Permutation ⁿPᵣ | Combination ⁿCᵣ |
|--|:--------------:|:--------------:|
| **Order** | <span style="color:#1565C0">Matters</span> | Does NOT matter |
| **Type** | Selection + Arrangement | Selection only |
| **Example** | <span style="color:#C0392B">ABC ≠ BAC ≠ CAB</span> *(all different)* | <span style="color:#27AE60">ABC = BAC = CAB</span> *(all same)* |

### <span style="color:#2E86AB">Key Relation</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">ⁿPᵣ = ⁿCᵣ × r!</span>

</div>

> Every combination × its r! arrangements = total permutations.

**Proof:**
- Combinations (unordered groups) = ⁵C₃ = **10**
- Each group arranged in 3! = 6 ways
- Total ordered = 10 × 6 = **60** = ⁵P₃ ✓

### <span style="color:#2E86AB">When to Use Which?</span>

**Use Permutation when:**
- Arranging letters or forming words
- Ranking (1st, 2nd, 3rd place)
- Assigning different roles (President, VP, Secretary)
- Creating passwords or PINs
- Seating arrangements

**Use Combination when:**
- Forming committees or teams (no role difference)
- Selecting items from a group
- Choosing lottery numbers
- Grouping students
- Counting handshakes or connections

### <span style="color:#2E86AB">Classic Comparison Example</span>

From 5 students — A, B, C, D, E:

| Task | Type | Formula | Result |
|------|------|:-------:|:------:|
| Select 2 for a **team** (no roles) | Combination | ⁵C₂ | **10** |
| Elect **President & VP** (roles differ) | Permutation | ⁵P₂ | **20** |

> <span style="color:#27AE60">AB = BA</span> when forming a team (same group) &nbsp;|&nbsp; <span style="color:#C0392B">AB ≠ BA</span> when assigning roles (different outcomes)

---

## <span style="color:#1565C0">6. Key Properties & Important Points</span>

### <span style="color:#2E86AB">Permutation Properties</span>

- ⁿPᵣ = n × (n−1) × … × (n−r+1) = n! / (n−r)!
- ⁿPₙ = n!
- ⁿP₀ = 1
- ⁿP₁ = n
- ⁿPᵣ = n × ⁽ⁿ⁻¹⁾P₍ᵣ₋₁₎ &nbsp;*(recursion)*

### <span style="color:#2E86AB">Combination Properties</span>

- ⁿCᵣ = ⁿC₍ₙ₋ᵣ₎ — **symmetry** *(key property!)*
- ⁿC₀ = ⁿCₙ = 1
- ⁿC₁ = n
- ⁿCᵣ + ⁿC₍ᵣ₋₁₎ = ⁽ⁿ⁺¹⁾Cᵣ — **Pascal's Rule**
- ⁿCᵣ = (n / r) × ⁽ⁿ⁻¹⁾C₍ᵣ₋₁₎

### <span style="color:#2E86AB">Factorial Properties</span>

- 0! = 1! = 1
- n! = n × (n−1)!
- (n+1)! = (n+1) × n!
- For large n: n! grows faster than any exponential function

---

### <span style="color:#2E86AB">Important Derivations</span>

#### <span style="color:#5B8DB8">Arrangements with Repeated Letters</span>

If a word has n letters where one letter repeats **p** times, another repeats **q** times, etc.:

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">Arrangements = n! / (p! × q! × …)</span>

</div>

- **"BANANA"** — 6 letters, A×3, N×2 → 6! / (3! × 2!) = 720 / 12 = **60**
- **"MISSISSIPPI"** — 11 letters: M×1, I×4, S×4, P×2 → 11! / (1! × 4! × 4! × 2!) = **34,650**

---

#### <span style="color:#5B8DB8">Circular Permutations</span>

Arranging n distinct objects **in a circle**:

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">Circular arrangements = (n−1)!</span>

</div>

> One position is fixed in a circle to remove rotational duplicates.

- **5 people at a round table** = (5−1)! = 4! = **24 ways**
- **6 beads in a necklace** (two-sided) = (6−1)! / 2 = **60 ways** *(divide by 2 — flipping gives same arrangement)*

---

#### <span style="color:#5B8DB8">Total Subsets of a Set</span>

A set with n elements has **2ⁿ subsets** in total (including empty set and full set).

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">ⁿC₀ + ⁿC₁ + ⁿC₂ + … + ⁿCₙ = 2ⁿ</span>

</div>

**Example:** Set {a, b, c} → 2³ = **8 subsets**
`{}` `{a}` `{b}` `{c}` `{a,b}` `{a,c}` `{b,c}` `{a,b,c}`

---

#### <span style="color:#5B8DB8">Handshake / Connection Problems</span>

If n people each shake hands with every other person exactly once:

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">Total handshakes = ⁿC₂ = n(n−1) / 2</span>

</div>

**Example:** 10 people → ¹⁰C₂ = 10 × 9 / 2 = **45 handshakes**

---

## <span style="color:#1565C0">7. Quick Reference Formulas</span>

| Formula | Expression |
|---------|:----------:|
| Factorial | n! = n × (n−1) × … × 1 |
| Permutation | ⁿPᵣ = n! / (n−r)! |
| Combination | ⁿCᵣ = n! / (r! × (n−r)!) |
| Relation | ⁿPᵣ = ⁿCᵣ × r! |
| Repeated letters | n! / (p! × q! × …) |
| Circular arrangement | (n−1)! |
| Total subsets | 2ⁿ |
| Handshakes | n(n−1)/2 |
| Complementary probability | P(Aᶜ) = 1 − P(A) |
| Pascal's Rule | ⁿCᵣ + ⁿC₍ᵣ₋₁₎ = ⁽ⁿ⁺¹⁾Cᵣ |

---

## <span style="color:#1565C0">8. Permutation vs Combination — Reference Table</span>

| n \ r | r = 0 | r = 1 | r = 2 | r = 3 |
|:-----:|:-----:|:-----:|:-----:|:-----:|
| n = 1 | P:1, C:1 | P:1, C:1 | — | — |
| n = 2 | P:1, C:1 | P:2, C:2 | P:2, C:1 | — |
| n = 3 | P:1, C:1 | P:3, C:3 | P:6, C:3 | P:6, C:1 |
| n = 4 | P:1, C:1 | P:4, C:4 | P:12, C:6 | P:24, C:4 |
| n = 5 | P:1, C:1 | P:5, C:5 | P:20, C:10 | P:60, C:10 |
| n = 6 | P:1, C:1 | P:6, C:6 | P:30, C:15 | P:120, C:20 |

---

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 16px 28px; margin: 16px auto; max-width: 420px;">

### <span style="color:#0A2FA8">Golden Rule</span>

**Always ask — *"Does order matter?"***

<span style="color:#27AE60">**Yes → Permutation (ⁿPᵣ)**</span>

<span style="color:#C0392B">**No → Combination (ⁿCᵣ)**</span>

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