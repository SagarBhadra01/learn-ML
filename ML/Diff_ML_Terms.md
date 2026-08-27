<div align="center">

# <span style="color:#0A2FA8">Model Evaluation : The Complete Reference</span>

<sub>Every term, metric, and diagnostic used across training, evaluation, tuning, and comparison - what it means, when it matters, and how to read it. Applies to any machine learning project.</sub>

</div>

---

## <span style="color:#1565C0">1. The Confusion Matrix - Where Everything Starts</span>

Almost every classification metric is built from four numbers. Understand these first and the rest follows logically.

> **Definition:** A confusion matrix is a table comparing what a model predicted against what was actually true, broken into four outcomes.

| | Predicted Positive | Predicted Negative |
|:---|:---:|:---:|
| **Actual Positive** | True Positive (TP) | False Negative (FN) |
| **Actual Negative** | False Positive (FP) | True Negative (TN) |

| Term | Meaning |
|:---|:---|
| **TP** (True Positive) | Correctly predicted positive |
| **TN** (True Negative) | Correctly predicted negative |
| **FP** (False Positive) | Wrongly predicted positive - also called a **Type I error** |
| **FN** (False Negative) | Wrongly predicted negative - also called a **Type II error** |

> **Important:** Neither error type is universally "worse." Which one matters more is decided by the domain, not by any formula.

| Domain | Costlier error | Why |
|:---|:---:|:---|
| Medical screening | <span style="color:#C0392B">False Negative</span> | A missed real condition can cost a life |
| Fraud detection | <span style="color:#C0392B">False Negative</span> | Missed fraud means real financial loss |
| Spam/content filtering | <span style="color:#C0392B">False Positive</span> | Blocking something legitimate is often worse than one bad item slipping through |
| Manufacturing defect detection | <span style="color:#C0392B">False Negative</span> | A faulty product reaching customers is costlier than extra inspection |

### <span style="color:#2E86AB">Normalized Confusion Matrix</span>

> **Definition:** Same matrix, but each row or column is converted to a percentage instead of a raw count. Makes it easier to compare models across datasets of different sizes, and easier to spot class-level weaknesses at a glance.

---

## <span style="color:#1565C0">2. Core Classification Metrics</span>

### <span style="color:#2E86AB">Accuracy</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">Accuracy = (TP + TN) / (TP + TN + FP + FN)</span>

</div>

> **Definition:** Proportion of all predictions that were correct.

**Misleading on imbalanced data.** If 95% of cases belong to one class, predicting that class every time scores 95% accuracy while being useless. Never trust accuracy alone without checking class balance first.

### <span style="color:#2E86AB">Precision</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">Precision = TP / (TP + FP)</span>

</div>

> **Definition:** Of everything predicted positive, how much actually was. Answers: "When the model says positive, how often is it right?"

Matters most when **false positives are expensive**.

### <span style="color:#2E86AB">Recall (Sensitivity / True Positive Rate)</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">Recall = TP / (TP + FN)</span>

</div>

> **Definition:** Of everything actually positive, how much the model caught. Answers: "Of all the real positives, how many did the model find?"

Matters most when **false negatives are expensive**.

### <span style="color:#2E86AB">Specificity (True Negative Rate)</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">Specificity = TN / (TN + FP)</span>

</div>

> **Definition:** Of everything actually negative, how much the model correctly identified as negative. The negative-class mirror of recall - commonly paired with recall/sensitivity in medical and diagnostic ML.

### <span style="color:#2E86AB">F1 Score</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">F1 = 2 × (Precision × Recall) / (Precision + Recall)</span>

</div>

> **Definition:** Harmonic mean of precision and recall. Punishes extreme imbalance between the two - a model with 0.99 precision but 0.10 recall does not score an average, it scores poorly.

### <span style="color:#2E86AB">F-beta Score (Generalized F1)</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">F-β = (1 + β²) × (P × R) / (β² × P + R)</span>

</div>

> **Definition:** F1 is actually a special case of F-beta where β = 1, weighing precision and recall equally. Setting β > 1 (e.g. F2) weighs recall more heavily; β < 1 (e.g. F0.5) weighs precision more heavily. Use this when one of the two genuinely matters more for the problem, instead of forcing an equal-weight F1.

### <span style="color:#2E86AB">Balanced Accuracy</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">Balanced Accuracy = (Recall + Specificity) / 2</span>

</div>

> **Definition:** Average of recall on each class. Behaves like accuracy but doesn't get inflated by a dominant majority class - a useful imbalanced-data alternative to plain accuracy when you want one simple number.

### <span style="color:#2E86AB">Precision vs Recall - The Tradeoff</span>

Raising the decision threshold increases precision but lowers recall, and vice versa. There's no universally correct balance - it depends entirely on the cost of each error type in context.

---

## <span style="color:#1565C0">3. Advanced Single-Number Metrics</span>

### <span style="color:#2E86AB">Matthews Correlation Coefficient (MCC)</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">MCC = (TP×TN − FP×FN) / √((TP+FP)(TP+FN)(TN+FP)(TN+FN))</span>

</div>

> **Definition:** A single correlation-style score between −1 and +1 that uses all four confusion matrix cells at once. +1 = perfect prediction, 0 = random guessing, −1 = total disagreement. Considered one of the most reliable single metrics for imbalanced binary classification because, unlike F1, it accounts for true negatives too.

### <span style="color:#2E86AB">Cohen's Kappa</span>

> **Definition:** Measures agreement between predicted and actual labels, adjusted for the agreement expected purely by chance. Useful when comparing a model's predictions against another labeler (human or model), not just against ground truth.

### <span style="color:#2E86AB">Log Loss (Cross-Entropy Loss)</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">Log Loss = −(1/N) Σ [y·log(p) + (1−y)·log(1−p)]</span>

</div>

> **Definition:** Penalizes confident wrong predictions far more heavily than cautious wrong ones. Unlike accuracy/F1, it uses the predicted *probability*, not just the final class label - so it rewards well-calibrated confidence, not just correct guesses. Lower is better; 0 is a perfect score.

### <span style="color:#2E86AB">Support</span>

> **Definition:** The number of actual occurrences of each class in the dataset being evaluated. Always check support before trusting per-class metrics - a metric calculated on 5 examples is far less reliable than one calculated on 5,000.

---

## <span style="color:#1565C0">4. Averaging Strategies for Multi-Class / Imbalanced Data</span>

| Averaging type | How it's computed | When to use |
|:---|:---|:---|
| **Binary / `pos_label`** | Computed only for the class of interest | Best when one class is the actual target |
| **Macro avg** | Simple unweighted average across classes | All classes matter equally regardless of size |
| **Weighted avg** | Average weighted by class size (support) | Reflects overall performance but can hide poor minority-class results |
| **Micro avg** | Globally sums all TP/FP/FN across classes first, then computes | Multi-class problems where instance-level totals matter most |

> **Caution:** On imbalanced binary data, the weighted average can look strong purely because the majority class is easy, while the minority class - usually the one you actually care about - performs poorly underneath it. Always check the class-specific metric directly, not just the weighted summary.

---

## <span style="color:#1565C0">5. Threshold-Independent Metrics</span>

Precision, recall, and F1 all depend on a single decision threshold (commonly 0.5). These metrics evaluate the model **across every possible threshold** at once.

### <span style="color:#2E86AB">ROC Curve (Receiver Operating Characteristic)</span>

> **Definition:** A plot of True Positive Rate (Recall) against False Positive Rate, traced across all classification thresholds.

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">FPR = FP / (FP + TN)</span>

</div>

### <span style="color:#2E86AB">AUC-ROC (Area Under the ROC Curve)</span>

> **Definition:** The probability that the model ranks a random positive example higher than a random negative one. A single number summarizing the entire ROC curve.

| AUC value | Interpretation |
|:---:|:---|
| 0.50 | No better than random guessing |
| 0.70 – 0.80 | Acceptable |
| 0.80 – 0.90 | Good |
| 0.90 – 1.00 | Excellent |
| 1.00 | Perfect separation - often a red flag for data leakage on real-world data |

### <span style="color:#2E86AB">Precision-Recall (PR) Curve & Average Precision (AP)</span>

> **Definition:** A plot of Precision against Recall across all thresholds. Average Precision (AP) condenses this curve into a single number, the PR equivalent of AUC.

### <span style="color:#2E86AB">ROC vs PR - Which to Trust</span>

| Scenario | Preferred curve | Why |
|:---|:---:|:---|
| Roughly balanced classes | ROC / AUC | Both axes stay meaningful |
| Heavily imbalanced classes | PR / AP | A large true-negative count can make ROC look overly optimistic; PR focuses purely on positive-class performance |

### <span style="color:#2E86AB">Calibration Curve</span>

> **Definition:** Plots predicted probability against actual observed frequency. A well-calibrated model that says "80% confident" should be right about 80% of the time it says that - not just rank-order correctly, but be numerically trustworthy. Matters whenever the predicted probability itself is used downstream (e.g. risk scoring), not just the final class label.

---

## <span style="color:#1565C0">6. Train, Validation, and Test - Reading the Gaps</span>

> **Definition:** The **train set** is what the model learns from. The **validation set** is used during development to tune choices without touching the test set. The **test set** is touched only once, at the very end, to report final unbiased performance.

```
Train set → fit the model
Validation set → tune hyperparameters, compare models
Test set → final, one-time, honest performance check
```

### <span style="color:#2E86AB">Train vs Test Gap</span>

| Pattern | Train score | Test score | Diagnosis |
|:---|:---:|:---:|:---|
| <span style="color:#27AE60">Good fit</span> | High | High, close to train | Generalizes well |
| <span style="color:#C0392B">Overfitting</span> | Very high | Noticeably lower | Memorized training data, won't generalize |
| <span style="color:#C0392B">Underfitting</span> | Low | Low | Model too simple or undertrained |

**Rule of thumb:** a gap beyond roughly 3–5 percentage points between train and test score is worth investigating - consider stronger regularization, a simpler model, more training data, or fewer/cleaner features.

### <span style="color:#2E86AB">Learning Curve</span>

> **Definition:** A plot of training and validation score as a function of training set size. Reveals whether more data would actually help:
- Both curves converge to a low score → underfitting; more data alone won't fix it, the model needs more capacity or better features
- Curves stay far apart even with lots of data → overfitting; more data, regularization, or a simpler model would help

### <span style="color:#2E86AB">Validation Curve</span>

> **Definition:** A plot of training and validation score as a function of a single hyperparameter's value (e.g. tree depth, regularization strength). Shows exactly where a model transitions from underfitting to a good fit to overfitting as that parameter changes.

### <span style="color:#2E86AB">Bias-Variance Tradeoff</span>

> **Definition:** The conceptual root of overfitting/underfitting. **High bias** means the model makes overly simplistic assumptions and underfits. **High variance** means the model is overly sensitive to the specific training data and overfits. Total error is the sum of both - reducing one often increases the other, and the goal is the best balance, not eliminating either entirely.

---

## <span style="color:#1565C0">7. Cross-Validation</span>

> **Definition:** Rather than trusting a single train/test split (which can be a lucky or unlucky shuffle), cross-validation splits the training data into multiple folds, trains multiple times - each time holding out a different fold for validation - and averages the results into a more reliable estimate.

### <span style="color:#2E86AB">K-Fold Cross-Validation</span>

> **Definition:** Data is split into K equal parts. The model trains on K−1 parts and validates on the remaining one, repeated K times so every part is used for validation exactly once.

### <span style="color:#2E86AB">Stratified K-Fold</span>

> **Definition:** Same as K-Fold, but each fold preserves the original class proportions. Essential for imbalanced data - without it, some folds could end up with very few or zero minority-class examples, producing unstable, misleading scores.

### <span style="color:#2E86AB">Leave-One-Out Cross-Validation (LOOCV)</span>

> **Definition:** The extreme case of K-Fold where K equals the number of samples - each fold validates on a single example. Very thorough but computationally expensive; mainly used on small datasets.

### <span style="color:#2E86AB">Time Series Split</span>

> **Definition:** A cross-validation variant for sequential/time-dependent data, where folds always train on past data and validate on future data, never the reverse. Standard K-Fold would leak future information into training and produce falsely optimistic scores on time series problems.

### <span style="color:#2E86AB">Reading CV Mean ± Std</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">CV Score = Mean ± Standard Deviation</span>

</div>

| Component | What it tells you |
|:---|:---|
| **Mean** | Expected performance across different data subsets - more trustworthy than one test score |
| **Std (standard deviation)** | Model stability. Low std = consistent performance regardless of which data it sees. High std = performance swings a lot fold to fold - less reliable even if the mean looks good |

A model with a slightly lower mean but much lower std can be the more trustworthy real-world choice over one with a higher mean but high variance.

---

## <span style="color:#1565C0">8. Hyperparameter Tuning</span>

### <span style="color:#2E86AB">Search Strategies</span>

| Method | How it works | When to use |
|:---|:---|:---|
| **Grid Search** | Tries every combination in a defined parameter grid | Small search space, exhaustive certainty desired |
| **Random Search** | Samples a fixed number of random combinations | Large search space; usually finds near-optimal results far faster than grid search |
| **Bayesian Optimization** | Uses prior results to intelligently choose the next combination to try | Expensive-to-train models where minimizing total search trials matters |

### <span style="color:#2E86AB">`best_params_` and `best_score_`</span>

> **Definition:** `best_params_` is the hyperparameter combination that scored highest during cross-validation. `best_score_` is that combination's mean CV score - **not** the test score. Always re-evaluate the tuned model on the actual held-out test set before trusting it; CV and test performance can diverge.

> **Important:** If tuning returns a model's existing defaults as "best," that isn't a failed search - it confirms the default was already optimal within the explored range. Validating a default is a legitimate, useful outcome.

---

## <span style="color:#1565C0">9. Statistical Comparison Between Models</span>

Raw score differences (e.g. 0.976 vs 0.975) can simply be noise. These tools check whether a difference is actually meaningful.

### <span style="color:#2E86AB">Paired t-test on CV folds</span>

> **Definition:** Compares two models' scores across the same CV folds to test whether one is statistically significantly better, rather than just numerically higher by chance.

### <span style="color:#2E86AB">McNemar's Test</span>

> **Definition:** A statistical test specifically for comparing two classifiers on the same test set, based on the cases where the two models disagreed. Useful for confirming that one model is genuinely better rather than the difference being within random variation.

---

## <span style="color:#1565C0">10. Operational Metrics</span>

These don't measure correctness - they measure whether a model is actually usable in the real world.

| Metric | What it tells you | Matters most when |
|:---|:---|:---|
| **Training Time** | How long fitting the model takes | Frequent retraining, large datasets |
| **Inference / Predict Time** | How long a single prediction takes | Real-time systems, high request volume |
| **Model Size** | Memory/disk footprint of the saved model | Deployment on constrained devices, mobile, edge |
| **Throughput** | Predictions per second the model can serve | High-traffic production systems |

> A model with marginally lower accuracy but far faster inference and a smaller footprint can be the better real-world choice - correctness is not the only axis that matters once a model leaves the notebook.

---

## <span style="color:#1565C0">11. Feature Importance & Interpretability</span>

### <span style="color:#2E86AB">Feature Importances (Tree-based Models)</span>

> **Definition:** A score per feature reflecting how much it reduced impurity (e.g. Gini, entropy) across all splits in the model. Higher = more influential in the model's decisions. Useful for sanity-checking that the model is learning genuine signal rather than dataset artifacts.

### <span style="color:#2E86AB">Coefficients (Linear Models)</span>

> **Definition:** In linear/logistic models, each feature has a coefficient indicating both the direction (positive/negative class) and strength of its influence, holding other features constant. Requires features to be on comparable scales to compare coefficient magnitudes fairly.

### <span style="color:#2E86AB">SHAP Values</span>

> **Definition:** A model-agnostic method that explains each individual prediction by attributing the model's output to each input feature's specific contribution for that one prediction - more granular and reliable than global feature importance alone, especially for explaining one specific case.

### <span style="color:#2E86AB">Out-of-Bag (OOB) Score</span>

> **Definition:** Specific to bagging ensembles like Random Forest. Since each tree is trained on a random bootstrap sample, the data points left out of that sample ("out-of-bag") can be used as a free internal validation set - giving a performance estimate without needing a separate held-out split.

---

## <span style="color:#1565C0">12. Error Analysis</span>

> **Definition:** Manually inspecting *which specific examples* a model got wrong, looking for patterns - rather than treating every error as random, unexplainable noise.

| Pattern found in errors | What it usually means |
|:---|:---|
| Errors cluster around sparse/low-information inputs | Features become unstable with too little signal per sample |
| Errors look genuinely ambiguous even to a human reviewer | Possible label noise in the dataset, not a model flaw |
| A specific error type shares a consistent pattern model features don't capture | A real, fixable feature gap |
| Errors are evenly spread with no common thread | Likely near the practical ceiling for the current feature set |

Error analysis often reveals issues that aggregate metrics hide entirely - two models can post identical F1 scores while failing on completely different kinds of examples.

---

## <span style="color:#1565C0">13. Regression Metrics (For Non-Classification Models)</span>

The metrics above apply to classification. When the target is a continuous number instead of a class label, a different set applies.

### <span style="color:#2E86AB">Mean Absolute Error (MAE)</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">MAE = (1/N) Σ |yᵢ − ŷᵢ|</span>

</div>

> **Definition:** Average absolute difference between predicted and actual values. Easy to interpret directly in the target's own units; treats all errors proportionally.

### <span style="color:#2E86AB">Mean Squared Error (MSE) & Root Mean Squared Error (RMSE)</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">RMSE = √[(1/N) Σ (yᵢ − ŷᵢ)²]</span>

</div>

> **Definition:** Squares errors before averaging, so larger errors are penalized disproportionately more than small ones. RMSE converts back to the original units by taking the square root, making it more interpretable than raw MSE while keeping the same large-error sensitivity.

### <span style="color:#2E86AB">R² (Coefficient of Determination)</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">R² = 1 − (Sum of Squared Residuals / Total Sum of Squares)</span>

</div>

> **Definition:** Proportion of variance in the target that the model explains. 1.0 = perfect fit, 0 = no better than predicting the mean every time, negative = worse than predicting the mean.

### <span style="color:#2E86AB">Adjusted R²</span>

> **Definition:** R² adjusted to penalize adding features that don't genuinely improve the model. Plain R² can only go up as more features are added, even useless ones - Adjusted R² corrects for that, making it fairer when comparing models with different numbers of features.

### <span style="color:#2E86AB">Mean Absolute Percentage Error (MAPE)</span>

> **Definition:** Average absolute error expressed as a percentage of the actual value. Intuitive for business reporting ("predictions are off by 8% on average") but unstable when actual values are at or near zero.

---

## <span style="color:#1565C0">14. Comparing Models Holistically - Decision Framework</span>

No single metric should make the final call alone. A reliable order of operations:

```
1. Check the train/test gap for every candidate → discard unstable or clearly overfit ones
2. Compare CV mean ± std → prefer high mean AND low std
3. Compare the test-set metric that matches the real priority (F1, recall, precision, RMSE, etc.)
4. Check practical constraints → train/predict time, model size, throughput
5. Run error analysis on the top 1–2 candidates → confirm the failure modes are acceptable
6. Run a statistical comparison if scores are close → confirm the difference is real, not noise
7. Pick the model whose tradeoffs match the actual real-world cost of getting it wrong
```

| What's being compared | Metric to check |
|:---|:---|
| Overall correctness balance | F1 (or class-specific F1 on imbalanced data) |
| Ranking quality across thresholds | ROC-AUC (balanced) or PR-AUC / AP (imbalanced) |
| Stability across data samples | CV standard deviation |
| Generalization vs memorization | Train vs Test gap |
| Real-world cost tradeoff | Precision vs Recall, weighed by domain |
| Probability trustworthiness | Calibration curve, Log Loss |
| Production feasibility | Train/Predict time, model size, throughput |
| Whether a difference is real | Paired t-test, McNemar's test |

---

## <span style="color:#1565C0">15. Master Cheat Sheet</span>

| Term | Formula / Definition | Ideal Value | Primarily Used To Judge |
|:---|:---|:---|:---|
| Accuracy | (TP+TN)/Total | High, only on balanced data | Overall correctness |
| Precision | TP/(TP+FP) | High = few false alarms | Cost of false positives |
| Recall | TP/(TP+FN) | High = few misses | Cost of false negatives |
| Specificity | TN/(TN+FP) | High | Negative-class detection |
| F1 | Harmonic mean of P & R | Close to 1.0 | Balanced single-number summary |
| F-beta | Weighted P/R harmonic mean | Close to 1.0 | Custom precision/recall priority |
| Balanced Accuracy | (Recall+Specificity)/2 | High | Imbalanced-data accuracy alternative |
| MCC | Correlation of all 4 matrix cells | Close to +1 | Robust imbalanced-data summary |
| Log Loss | Penalized probability error | Close to 0 | Probability calibration quality |
| ROC-AUC | Area under TPR vs FPR | Close to 1.0 | Threshold-independent ranking |
| PR-AUC / AP | Area under Precision vs Recall | Close to 1.0 | Ranking quality on imbalanced data |
| CV Mean | Average score across folds | High | True expected performance |
| CV Std | Spread across folds | Low (e.g. <0.01) | Model stability |
| Train vs Test Gap | Difference in train/test score | Small (<0.05) | Overfitting check |
| Train/Predict Time | Wall-clock seconds | Lower, in context | Deployment feasibility |
| MAE / RMSE | Average (squared) error | Low | Regression accuracy |
| R² | Variance explained | Close to 1.0 | Regression fit quality |