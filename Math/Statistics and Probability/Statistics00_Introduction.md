<div align="center">

# <span style="color:#0A2FA8">Introduction to Statistics</span>


</div>

## <span style="color:#1565C0">1. What is Statistics?</span>


> **Statistics** is the science of collecting, analyzing, interpreting, and presenting data. It provides a systematic framework for making sense of numerical information and drawing meaningful conclusions from it.

**Purpose:** To identify patterns in real-world data and make valid inferences about a population based on a sample.

---

## <span style="color:#1565C0">2. Key Distinction: Probability vs. Statistics</span>

These two fields are inverses of each other:

| Aspect | Direction | Given | Goal |
|--------|-----------|-------|------|
| **Probability** | Forward Reasoning | A known model | Predict data/outcomes |
| **Statistics** | Reverse Reasoning | Observed data | Infer/build the model |

### <span style="color:#2E86AB">Example</span>
A fair die is rolled 1000 times and outcomes are recorded.

- **Probability asks:** If the die is fair, how often should we expect a 6?
- **Statistics asks:** Given these 1000 outcomes, is the die actually fair?

---

## <span style="color:#1565C0">3. Role of Statistics in Machine Learning</span>

Statistics forms the backbone of ML across the entire pipeline:

- **Data Understanding** - Summarizing distributions, detecting outliers, understanding variable relationships
- **Feature Engineering** - Selecting, transforming, and creating variables that improve model performance
- **Dimensionality Reduction** - Techniques like PCA use variance to reduce feature space (e.g., from 500 features → 20)
- **Modeling** - Regression, classification, clustering - all grounded in statistical theory
- **Model Evaluation** - Metrics like accuracy, precision, AUC, p-values, confidence intervals

---

## <span style="color:#1565C0">4. Two Branches of Statistics</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 600px;">

### <span style="color:#D4A017">Statistics Framework</span>

```
  STATISTICS
 /       \
Descriptive              Inferential
Statistics               Statistics
 |                        |
Summarizing                Making predictions
      data                    about population
                              from sample
```

</div>

### <span style="color:#2E86AB">4.1 Descriptive Statistics</span>


> **Purpose:** Summarizing and describing data

Descriptive statistics help us understand patterns in our dataset through three main approaches:

#### <span style="color:#5B8DB8">A. Measure of Central Tendency</span>
- **Mean** - Average value of the dataset
- **Mode** - Most frequently occurring value
- **Median** - Middle value when data is ordered

#### <span style="color:#5B8DB8">B. Measure of Variability</span>
- **Range** - Difference between maximum and minimum values
- **Variance** - Average squared deviation from the mean
- **Standard Deviation** - Square root of variance (same units as data)
- **Interquartile Range (IQR)** - Range of the middle 50% of data

#### <span style="color:#5B8DB8">C. Graphical Representation</span>
- **Histogram** - Shows frequency distribution of continuous data
- **Boxplot** - Displays data distribution using quartiles
- **Pie chart** - Shows proportions of categorical data

---

### <span style="color:#2E86AB">4.2 Inferential Statistics</span>


> **Purpose:** Making predictions about a population from a sample

Inferential statistics enable us to draw conclusions beyond our immediate data:

#### <span style="color:#5B8DB8">Key Components:</span>

1. **Probability Distributions**
   - Understanding the likelihood of different outcomes
   - Common distributions: Normal, Binomial, Poisson, etc.

2. **Hypothesis Testing**
   - Testing claims about population parameters
   - Involves null hypothesis (H₀) and alternative hypothesis (H₁)
   - Uses p-values to determine statistical significance

3. **Regression Analysis**
   - Modeling relationships between variables
   - Predicting dependent variables from independent variables
   - Linear, logistic, polynomial regression, etc.

4. **Confidence Intervals**
   - Range of values likely to contain the true population parameter
   - Expressed with a confidence level (e.g., 95% confidence interval)

---

## <span style="color:#1565C0">5. Statistics Workflow</span>

### <span style="color:#2E86AB">Forward Reasoning (Probability)</span>
```
Given Model → Predict Data
```

### <span style="color:#2E86AB">Reverse Reasoning (Statistics)</span>
```
Given Data → Predict Model
```

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">Probability ⇄ Statistics</span>

**Model → Data** (Probability)  
**Data → Model** (Statistics)

</div>

This bidirectional relationship forms the foundation of statistical inference and machine learning.

---

## <span style="color:#1565C0">Key Takeaways</span>

✓ Statistics provides tools for understanding and interpreting data systematically

✓ Descriptive statistics summarize what we observe in our data

✓ Inferential statistics help us make predictions about larger populations

✓ The relationship between probability and statistics is fundamental - they work in opposite directions

✓ Machine learning heavily relies on statistical concepts at every stage of the pipeline

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
