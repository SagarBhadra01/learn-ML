<div align="center">

# <span style="color:#0A2FA8">Introduction to Probability</span>

<sub>Fundamental concepts of probability - definitions, sample spaces, events, and key formulas</sub>

</div>

---

## <span style="color:#1565C0">1. Probability</span>

> **Definition:** Probability is a numerical measure of the **likelihood or chance** of a particular event occurring. It quantifies uncertainty on a scale from 0 to 1.

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">P(E) = Number of favourable outcomes / Total number of possible outcomes</span>

</div>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">0 ≤ P(E) ≤ 1</span>

</div>

| Value | Meaning | Example |
|:---:|:---|:---|
| `P(E) = 0` | Event is **impossible** | Rolling a 7 on a standard die |
| `P(E) = 1` | Event is **certain** | Getting a number ≤ 6 on a die |
| `P(E) = 0.5` | Event has **equal chance** of occurring or not | Tossing a fair coin |

---

## <span style="color:#1565C0">2. Experiment</span>

> **Definition:** An Experiment is any process or activity that is performed to **observe and record outcomes**.

### <span style="color:#2E86AB">Examples</span>

- Flipping a coin and observing which side lands up
- Rolling a die and noting the number
- Drawing a card from a deck and seeing its value

---

## <span style="color:#1565C0">3. Random Experiment</span>

> **Definition:** A Random Experiment is a special type of experiment in which the outcome **cannot be predicted in advance**, but all **possible outcomes are known beforehand**.

### <span style="color:#2E86AB">Examples</span>

| Experiment | Possible Outcomes |
|:---|:---|
| Tossing a coin | Head (H), Tail (T) |
| Rolling a die | 1, 2, 3, 4, 5, 6 |
| Drawing a card from a deck | Any of 52 cards |
| Tossing 2 coins | HH, HT, TH, TT |

---

## <span style="color:#1565C0">4. Sample Space (S)</span>

> **Definition:** The Sample Space is the set of **all possible outcomes** of a random experiment. It is also called the **Domain Set**. Denoted by **S**; each element in S is called a **sample point**.

### <span style="color:#2E86AB">Examples</span>

| Experiment | Sample Space | n(S) |
|:---|:---|:---:|
| Tossing 1 coin | `S = {H, T}` | 2 |
| Tossing 2 coins | `S = {HH, HT, TH, TT}` | 4 |
| Rolling 1 die | `S = {1, 2, 3, 4, 5, 6}` | 6 |
| Rolling 2 dice | All ordered pairs (1,1) to (6,6) | 36 |

---

## <span style="color:#1565C0">5. Event (E)</span>

> **Definition:** An Event is any **subset of the Sample Space**. It is a collection of one or more outcomes from the sample space that we are interested in. Denoted by **E**; n(E) = number of outcomes in the event.

### <span style="color:#2E86AB">Types of Events</span>

| Type | Description | Example |
|:---|:---|:---|
| **Simple Event** | Only one outcome | Getting exactly H on a coin |
| **Compound Event** | More than one outcome | Getting an even number on a die |
| **Sure / Certain Event** | Always occurs, E = S | Getting a number ≤ 6 on a die |
| **Impossible Event** | Never occurs, E = ∅ | Getting 8 on a die |
| **Complementary Event** | All outcomes NOT in E | If E = {H}, then E' = {T} |

### <span style="color:#2E86AB">Example</span>

Rolling a die, collecting only **even numbers**:

```
S = {1, 2, 3, 4, 5, 6}   →   E = {2, 4, 6}   →   n(E) = 3
```

---

## <span style="color:#1565C0">6. Probability Formula — Detailed</span>

Let **S** be the Sample Space and **E** be an Event. Then:

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">P(E) = n(E) / n(S)</span>

</div>

| Symbol | Meaning |
|:---:|:---|
| `n(E)` | Number of favourable outcomes in event E |
| `n(S)` | Total number of outcomes in sample space S |

---

## <span style="color:#1565C0">7. Worked Example</span>

**Random Experiment:** Tossing **2 fair coins**

```
Sample Space:   S = {HH, HT, TH, TT}   →   n(S) = 4
Event (E):      Getting exactly 1 head
                E = {HT, TH}            →   n(E) = 2
```

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">P(E) = n(E) / n(S) = 2 / 4 = 0.5</span>

</div>

---

## <span style="color:#1565C0">8. Equally Likely Outcomes</span>

> **Definition:** Outcomes are said to be **equally likely** when each outcome has the **same chance** of occurring — no outcome is more probable than another.

### <span style="color:#2E86AB">Example</span>

Tossing a fair coin — both H and T have equal probability:

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">P(H) = P(T) = 1/2</span>

</div>

---

## <span style="color:#1565C0">9. Favourable Outcomes</span>

> **Definition:** Favourable outcomes are the outcomes from the sample space that **satisfy the condition** of the given event.

### <span style="color:#2E86AB">Example</span>

Rolling a die, Event = getting a number > 4:

```
S = {1, 2, 3, 4, 5, 6}
Favourable outcomes = {5, 6}   →   n(E) = 2
```

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">P(E) = 2/6 = 1/3</span>

</div>

---

## <span style="color:#1565C0">10. Complementary Event</span>

> **Definition:** The Complement of an Event E (written as **E'** or **E-bar**) is the set of all outcomes in the sample space that are **not** in E.

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">P(E') = 1 - P(E)</span>

</div>

### <span style="color:#2E86AB">Examples</span>

**Example 1:** Tossing a coin, `E = {H}`
```
P(E)  = 1/2
P(E') = 1 - 1/2 = 1/2
```

**Example 2:** Drawing a red card from a standard deck
```
P(red)     = 26/52 = 1/2
P(not red) = 1 - 1/2 = 1/2
```

---

## <span style="color:#1565C0">11. Quick Reference Summary</span>

| Term | Meaning |
|:---|:---|
| **Experiment** | A process performed to observe outcomes |
| **Random Experiment** | Unpredictable outcome, known range of outcomes |
| **Sample Space (S)** | Set of ALL possible outcomes |
| **Event (E)** | A subset of the sample space |
| **Equally Likely Outcomes** | Each outcome has equal chance |
| **Favourable Outcomes** | Outcomes satisfying the event condition |
| **Complementary Event (E')** | Outcomes NOT in E |
| **P(E)** | n(E) / n(S) |
| **Range of P(E)** | 0 ≤ P(E) ≤ 1 |
| **P(E')** | 1 - P(E) |

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