<div align="center">

# <span style="color:#0A2FA8">Bayes' Theorem : Probability</span>

<sub>Complete notes covering Bayes' Theorem, Naive Bayes Classifier, derivations, examples, and applications</sub>

</div>

---

## <span style="color:#1565C0">1. What is Bayes' Theorem?</span>

> **Definition:** Bayes' Theorem is a fundamental rule in probability used for updating the belief in a hypothesis when new evidence comes in. It connects prior knowledge with new observed evidence to compute a revised (posterior) probability.

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">P(H|D) = [ P(H) · P(D|H) ] / P(D)</span>

</div>


---

## <span style="color:#1565C0">2. Key Terminology</span>

| Term | Symbol | Meaning |
|:---:|:---:|:---|
| **Prior** | `P(H)` | Initial belief in an event before new evidence |
| **Posterior** | `P(H\|D)` | Updated belief after incorporating evidence |
| **Likelihood** | `P(D\|H)` | How probable the evidence is, given the hypothesis |
| **Marginal Likelihood** | `P(D)` | Acts as a normalizing constant |

---

## <span style="color:#1565C0">3. Derivation of Bayes' Theorem</span>

### <span style="color:#2E86AB">3.1 Starting Point - Conditional Probability</span>

> **Definition:** Conditional probability is the probability of event A occurring, given that event B has already occurred.

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">P(A|B) = P(A ∩ B) / P(B)  · · · (i)</span>

</div>

Since the intersection can be expanded using the **multiplication rule**:

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">P(A ∩ B) = P(A) · P(B|A)</span>

</div>

### <span style="color:#2E86AB">3.2 Law of Total Probability</span>

> **Definition:** The total probability of event B across all mutually exclusive cases of A.

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">P(B) = P(A ∩ B) + P(Ā ∩ B)</span>
### <span style="color:#D4A017">= P(A)·P(B|A) + P(Ā)·P(B|Ā)</span>

</div>

### <span style="color:#2E86AB">3.3 Full / Expanded Form of Bayes' Theorem</span>

Substituting the Law of Total Probability into equation (i):

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 560px;">

### <span style="color:#D4A017">P(A|B) = P(A)·P(B|A) / [ P(A)·P(B|A) + P(Ā)·P(B|Ā) ]</span>

</div>

This is the **complete expanded form** of Bayes' Theorem - equivalent to the compact form but with the denominator fully written out.

---

## <span style="color:#1565C0">4. Classic Example - Medical Diagnosis Problem</span>

### <span style="color:#2E86AB">4.1 Problem Statement</span>

A lab has proposed a test for a rare disease which is **99% accurate**. Given:
1. The disease affects **1 in 10,000** people → 100 in 1,000,000
2. The population of the country is **1 million people**

**Find:** If a person tests positive, what is the actual probability they are sick?

### <span style="color:#2E86AB">4.2 Simulated Confusion Matrix (on 1,000,000 people)</span>

|  | <span style="color:#C0392B">Diagnosed Sick</span> | <span style="color:#27AE60">Diagnosed Healthy</span> |
|:---|:---:|:---:|
| **Actual Healthy** (999,900 people) | <span style="color:#C0392B">9,999</span> - 1% false positive | <span style="color:#27AE60">989,901</span> - 99% correct |
| **Actual Unhealthy** (100 people) | <span style="color:#27AE60">99</span> - 99% correct | <span style="color:#C0392B">1</span> - 1% false negative |

### <span style="color:#2E86AB">4.3 Solving with Bayes' Theorem</span>

**Given values:**

```
P(Sick)                    = 0.01%  = 0.0001
P(Not Sick)                = 99.99% = 0.9999
P(Diagnosed Sick | Sick)   = 99%    = 0.99
P(Diagnosed Sick | Not Sick) = 1%   = 0.01
```

Let `A = Sick`, `B = Diagnosed Sick`

**Step 1 - Compute P(A ∩ B):**

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">P(A ∩ B) = P(A) · P(B|A) = (0.01/100) × (99/100)</span>

</div>

**Step 2 - Compute P(B) using Law of Total Probability:**

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 560px;">

### <span style="color:#D4A017">P(B) = (0.01/100 × 99/100) + (99.99/100 × 1/100)</span>

</div>

**Step 3 - Apply Bayes' Theorem:**

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">P(Sick | Diagnosed Sick) = 99 / (99 + 9999) ≈ 0.0098</span>

### <span style="color:#D4A017">≈ 0.98% - less than 1%</span>

</div>

### <span style="color:#2E86AB">4.4 Key Insight - Base Rate Neglect</span>

> Even though the test is 99% accurate, a person who tests positive has only **~1% chance of actually being sick**. This is because the disease is extremely rare. Ignoring this base rate leads to a dangerously wrong conclusion - this is known as **base rate neglect**, and Bayes' Theorem is the correct way to account for it.

---

## <span style="color:#1565C0">5. Naive Bayes Classifier</span>

### <span style="color:#2E86AB">5.1 Definition</span>

> **Definition:** Naive Bayes is a Machine Learning classification algorithm based on Bayes' Theorem. It is called "Naive" because it assumes all features are **conditionally independent** of each other given the class - which is rarely true in practice, but the algorithm still works well in many real-world tasks.

### <span style="color:#2E86AB">5.2 General Formula</span>

For a class `C` and features `x₁, x₂, ..., xₙ`:

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 620px;">

### <span style="color:#D4A017">P(C | x₁, x₂, ..., xₙ) ∝ P(C) · P(x₁|C) · P(x₂|C) · ... · P(xₙ|C)</span>

</div>

Due to the independence assumption, the joint likelihood simplifies to a product of individual likelihoods - making computation very efficient.

### <span style="color:#2E86AB">5.3 Types of Naive Bayes</span>

| Type | Feature Distribution | Common Use Case |
|:---|:---:|:---|
| **Gaussian NB** | Continuous (normal distribution) | Medical data, scientific measurements |
| **Multinomial NB** | Discrete counts | Text classification, NLP |
| **Bernoulli NB** | Binary (0 or 1) | Spam detection, document classification |

### <span style="color:#2E86AB">5.4 Advantages</span>

- Easy to implement and computationally very fast
- Effective when the number of features is large
- Requires relatively little training data
- Scales well with high-dimensional data (e.g., text corpora)
- Handles multi-class problems naturally

### <span style="color:#2E86AB">5.5 Limitations</span>

- **Strong independence assumption** - features are rarely truly independent in real-world data
- **Zero probability problem** - if a feature value never appeared during training, it assigns zero probability to that class (fix: **Laplace smoothing**)
- Probability estimates (confidence scores) are often unreliable, even when classification is correct
- Not suitable when feature correlations are significant

---

## <span style="color:#1565C0">6. Important Related Concepts</span>

### <span style="color:#2E86AB">6.1 Conditional Probability</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">P(A|B) = P(A ∩ B) / P(B)</span>

</div>

### <span style="color:#2E86AB">6.2 Law of Total Probability</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">P(B) = Σᵢ P(Aᵢ) · P(B | Aᵢ)</span>

</div>

### <span style="color:#2E86AB">6.3 Complementary Rule</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">P(Ā) = 1 − P(A)</span>

</div>

### <span style="color:#2E86AB">6.4 Multiplication Rule</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">P(A ∩ B) = P(A) · P(B|A)</span>

</div>

---

## <span style="color:#1565C0">7. Applications of Bayes' Theorem</span>

| Domain | Application |
|:---|:---|
| **Medicine** | Disease diagnosis, drug efficacy testing |
| **Spam Filtering** | Classifying emails as spam / not spam |
| **NLP** | Sentiment analysis, text categorization |
| **Finance** | Credit risk scoring, fraud detection |
| **Search Engines** | Relevance ranking of results |
| **Robotics / AI** | Sensor fusion, object recognition |
| **Weather Forecasting** | Updating probability given new sensor observations |

---

## <span style="color:#1565C0">8. Bayesian vs. Frequentist Approach</span>

| Aspect | <span style="color:#C0392B">Frequentist</span> | <span style="color:#27AE60">Bayesian</span> |
|:---|:---:|:---:|
| Definition of Probability | Long-run frequency of events | Degree of belief |
| Uses Prior Knowledge | No | Yes - explicitly incorporated |
| Updates with New Data | No | Yes - posterior updates prior |
| Interpretation | Objective | Principled and subjective |
| Best For | Large repeated experiments | Small data, sequential updating |

---

## <span style="color:#1565C0">9. Conceptual Flow Summary</span>

```
Prior Belief  →  P(H)
      +
New Evidence  →  P(D|H)
      |
      ↓  [Bayes' Theorem]
      |
Updated Belief → P(H|D)  =  Posterior
```

> **Prior** = what you believed before seeing any evidence
> **Likelihood** = how well the evidence fits the hypothesis
> **Posterior** = your updated, rational belief after incorporating evidence

Bayes' Theorem is the mathematically correct framework for **reasoning under uncertainty** - it ensures belief updates are consistent, principled, and proportional to evidence strength.

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

