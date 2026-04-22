<div align="center">

# <span style="color:#0A2FA8">Steps of Machine Learning - The ML Pipeline</span>

<sub>Problem Definition → Data Collection → Data Cleaning & Preprocessing → EDA → Feature Engineering → Model Selection → Training → Evaluation & Tuning → Deployment → Monitoring & Maintenance</sub>

</div>

---

## <span style="color:#1565C0">Overview - What is an ML Pipeline?</span>

> **Definition:** An ML Pipeline is a structured, end-to-end sequence of steps that transforms raw, unprocessed data into a deployed, production-ready machine learning model.

Building an ML model is not just about writing a few lines of code and calling `.fit()`. It is a disciplined engineering process with multiple stages - each stage directly affects the quality of the final model.

```
Problem Definition → Data Collection → Data Cleaning & Preprocessing → EDA → Feature Engineering & Selection → Model Selection → Model Training → Model Evaluation & Tuning → Model Deployment → Model Monitoring & Maintenance
```

Every step feeds into the next. A mistake in Step 1 will corrupt every step that follows - this is why "garbage in, garbage out" is the most important principle in ML.

---

## <span style="color:#1565C0">Step 0 - Problem Definition</span>

> **Definition:** Problem Definition is the very first step where you clearly identify and articulate what you are trying to solve, before touching any data or writing any code.

Skipping this step is one of the most common mistakes beginners make. Without a well-defined problem, you cannot choose the right data, the right algorithm, or the right metric.

---

### <span style="color:#2E86AB">Questions to Answer at This Stage</span>

| Question | Why it matters |
|:---|:---|
| What is the goal? | Defines the entire direction of the project |
| What is the input and output? | Determines what data to collect and what to predict |
| Is this supervised or unsupervised? | Dictates the class of algorithms to consider |
| Is it classification or regression? | Determines which metrics to use |
| What does success look like? | Defines the evaluation criteria and threshold |
| What are the constraints? | Budget, latency, explainability, hardware limitations |

---

### <span style="color:#2E86AB">Good vs Bad Problem Definition</span>

| | <span style="color:#C0392B">Bad (Vague)</span> | <span style="color:#27AE60">Good (Specific)</span> |
|:---|:---|:---|
| Goal | "Make a model about customers" | "Predict which customers will churn in the next 30 days" |
| Output | "Something about sales" | "Forecast next month's sales revenue in INR" |
| Success | "As accurate as possible" | "Achieve F1 > 0.85 on the test set" |

---

### <span style="color:#2E86AB">ML Problem Types - Decision Map</span>

```
What are you predicting?
├── A number (price, temperature, score)       → Regression
├── A category (spam/not, dog/cat/bird)        → Classification
├── Groups in unlabeled data                   → Clustering
├── Sequence of actions to maximize reward     → Reinforcement Learning
└── Similarity / ranking (search, recommendations) → Ranking / Retrieval
```

---

## <span style="color:#1565C0">Step 1 - Data Collection</span>

> **Definition:** Data Collection is the process of identifying, gathering, and storing raw data that will be used to train the machine learning model.

The model can only ever be as good as the data it is trained on. This is the most foundational step in the entire pipeline.

---

### <span style="color:#2E86AB">Types of Data</span>

| Type | Description | Example |
|:---|:---|:---|
| Structured | Organized in rows and columns | CSV files, SQL tables, Excel sheets |
| Unstructured | No fixed format | Images, audio, video, raw text, PDFs |
| Semi-structured | Partially organized | JSON, XML, HTML, logs |
| Time-series | Data indexed by time | Stock prices, sensor readings, weather data |

---

### <span style="color:#2E86AB">Sources of Data</span>

| Source | Examples |
|:---|:---|
| Public datasets | Kaggle, UCI ML Repository, Google Dataset Search, Hugging Face |
| Web scraping | BeautifulSoup, Scrapy - extracting data from websites |
| APIs | Twitter API, OpenWeatherMap API, government open data APIs |
| Databases | Company SQL/NoSQL databases, data warehouses |
| Surveys & forms | Google Forms, manual data entry |
| Sensors & IoT | GPS, accelerometers, smart devices |
| Synthetic data | Artificially generated data when real data is scarce |

---

### <span style="color:#2E86AB">What Makes Good Data?</span>

| Property | Meaning |
|:---|:---|
| Relevant | Data must relate directly to the problem being solved |
| Sufficient | Enough samples for the model to learn generalizable patterns |
| Representative | Must cover all real-world cases - not biased toward one group |
| Accurate | Labels and values must be correct |
| Consistent | Same format and units throughout |
| Timely | Recent enough to reflect the current state of the world |

---

### <span style="color:#2E86AB">Key Concepts in Data Collection</span>

#### <span style="color:#5B8DB8">Labeled vs Unlabeled Data</span>

> **Labeled data:** Each data point has a known correct answer (used in supervised learning).
> **Unlabeled data:** No answers provided - the model finds patterns on its own (used in unsupervised learning).

#### <span style="color:#5B8DB8">Data Imbalance</span>

> **Definition:** A dataset is imbalanced when one class has significantly more samples than another.

**Example:** A fraud detection dataset may have 99% legitimate transactions and only 1% fraudulent ones. A model trained naively will simply predict "not fraud" every time and still achieve 99% accuracy - which is misleading and useless.

Solutions to class imbalance:
- Oversampling the minority class (SMOTE)
- Undersampling the majority class
- Using class-weighted loss functions

#### <span style="color:#5B8DB8">Data Privacy & Ethics</span>

- Personal data must comply with regulations (GDPR, India's DPDP Act)
- Biased training data leads to biased models - a major real-world problem
- Always obtain consent when collecting user data

---

## <span style="color:#1565C0">Step 2 - Data Preprocessing</span>

> **Definition:** Data Preprocessing is the step where raw, dirty data is cleaned, transformed, and organized into a format that ML algorithms can work with effectively.

Real-world data is almost always messy. It contains missing values, inconsistent formats, typos, outliers, and irrelevant columns. Preprocessing fixes all of this before training begins.

```
Raw Data → Clean → Transform → Format → Ready-to-train Data
```

---

### <span style="color:#2E86AB">2.1 Handling Missing Values</span>

> **Definition:** Missing values are data points where a value was not recorded or is unavailable - represented as `NaN`, `null`, or blank cells.

#### <span style="color:#5B8DB8">Strategies</span>

| Strategy | When to use | How |
|:---|:---|:---|
| Remove rows | Very few missing rows relative to total data | `dropna()` |
| Remove columns | Column has > 50-70% missing values | Drop the feature entirely |
| Mean imputation | Numerical data, roughly normal distribution | Replace with column mean |
| Median imputation | Numerical data with outliers | Replace with column median |
| Mode imputation | Categorical data | Replace with most frequent value |
| Forward/backward fill | Time-series data | Fill with previous / next value |
| Model-based imputation | Complex relationships | Use another ML model to predict missing value |

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">Rule of thumb: If missing > 50% → drop the column. If missing < 5% → drop the rows. Otherwise → impute.</span>

</div>

---

### <span style="color:#2E86AB">2.2 Handling Outliers</span>

> **Definition:** An outlier is a data point that lies far away from the majority of other data points - it is abnormally high or low.

**Example:** A dataset of human ages has one entry of `450` - that is an outlier caused by a data entry error.

#### <span style="color:#5B8DB8">Detection Methods</span>

| Method | Description |
|:---|:---|
| Z-Score | Flag values more than 3 standard deviations from the mean |
| IQR Method | Flag values below Q1 - 1.5×IQR or above Q3 + 1.5×IQR |
| Box plot | Visual detection of outliers |
| Scatter plot | Spot unusual data points visually |

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">IQR = Q3 − Q1 &nbsp;|&nbsp; Lower Bound = Q1 − 1.5 × IQR &nbsp;|&nbsp; Upper Bound = Q3 + 1.5 × IQR</span>

</div>

#### <span style="color:#5B8DB8">Handling Strategies</span>

| Strategy | When |
|:---|:---|
| Remove the outlier | Clear data entry error |
| Cap / Winsorize | Replace outlier with boundary value |
| Log transformation | Compress the scale of a skewed feature |
| Keep it | If the outlier is a real, meaningful data point |

---

### <span style="color:#2E86AB">2.3 Encoding Categorical Data</span>

> **Definition:** Encoding converts categorical (text-based) variables into numerical form so that ML algorithms can process them.

ML models are mathematical - they only understand numbers, not strings like `"Male"` or `"Red"`.

#### <span style="color:#5B8DB8">Types of Encoding</span>

| Encoding Type | When to use | Example |
|:---|:---|:---|
| Label Encoding | Ordinal data (has order) | `Low=0, Medium=1, High=2` |
| One-Hot Encoding | Nominal data (no order) | `Color: Red=[1,0,0], Blue=[0,1,0]` |
| Binary Encoding | High-cardinality nominal | Converts to binary digits |
| Target Encoding | High-cardinality with target correlation | Replace category with mean target value |

> **Warning:** Never use Label Encoding on nominal data (e.g., `Red=0, Blue=1, Green=2`) because the model will falsely assume `Green > Blue > Red`, which is meaningless.

---

### <span style="color:#2E86AB">2.4 Feature Scaling</span>

> **Definition:** Feature scaling transforms numerical features so they all exist on a comparable scale - preventing features with large magnitudes from dominating the model.

**Example:** A dataset has `Age` (range: 0–100) and `Salary` (range: 20,000–200,000). Without scaling, salary dominates distance-based calculations completely and the model ignores age.

#### <span style="color:#5B8DB8">Normalization (Min-Max Scaling)</span>

> Rescales values to a fixed range, typically [0, 1].

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">x' = (x − x_min) / (x_max − x_min)</span>

</div>

- Use when: data is not normally distributed, bounded range is needed
- Sensitive to outliers - one extreme value distorts the entire scale

#### <span style="color:#5B8DB8">Standardization (Z-Score Scaling)</span>

> Rescales values so the feature has mean = 0 and standard deviation = 1.

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">x' = (x − μ) / σ</span>

</div>

- Use when: data is approximately normally distributed
- Robust to outliers compared to normalization

#### <span style="color:#5B8DB8">When does scaling matter?</span>

| Algorithm | Scaling needed? |
|:---|:---:|
| Linear Regression | Yes |
| Logistic Regression | Yes |
| SVM | Yes |
| KNN | Yes |
| K-Means Clustering | Yes |
| Decision Tree | No |
| Random Forest | No |
| Naive Bayes | No |

---

### <span style="color:#2E86AB">2.5 Train-Test Split</span>

> **Definition:** The dataset is divided into separate subsets - one for training the model and one for evaluating how well it generalizes to unseen data.

```
Full Dataset → Train Set (70-80%) + Test Set (20-30%)
```

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">Standard Split: 80% Train | 20% Test &nbsp;|&nbsp; Or: 70% Train | 15% Val | 15% Test</span>

</div>

- **Training set:** The model learns patterns from this data
- **Validation set:** Used to tune hyperparameters during development
- **Test set:** Held out completely - only used once at the very end to measure final performance

> **Critical Rule:** Never let the model see the test set during training. If the model is evaluated on data it has seen, the results are meaningless - this is called **data leakage**.

---

### <span style="color:#2E86AB">2.6 Cross Validation</span>

> **Definition:** Cross Validation is a technique to evaluate model performance more reliably by training and testing on multiple different splits of the data.

#### <span style="color:#5B8DB8">K-Fold Cross Validation</span>

```
Data split into K equal folds (e.g., K=5)

Fold 1: [TEST] [TRAIN] [TRAIN] [TRAIN] [TRAIN] → Score 1
Fold 2: [TRAIN] [TEST] [TRAIN] [TRAIN] [TRAIN] → Score 2
Fold 3: [TRAIN] [TRAIN] [TEST] [TRAIN] [TRAIN] → Score 3
Fold 4: [TRAIN] [TRAIN] [TRAIN] [TEST] [TRAIN] → Score 4
Fold 5: [TRAIN] [TRAIN] [TRAIN] [TRAIN] [TEST] → Score 5

Final Score = Average of all 5 scores
```

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">CV Score = (Score₁ + Score₂ + ... + Scoreₖ) / K</span>

</div>

- More reliable than a single train-test split
- Every data point gets to be in the test set exactly once
- Common values: K = 5 or K = 10

---

---

## <span style="color:#1565C0">Step 3 - Exploratory Data Analysis (EDA)</span>

> **Definition:** EDA is the process of visually and statistically exploring the dataset to understand its structure, patterns, distributions, relationships, and anomalies - before building any model.

EDA is the "get to know your data" phase. You cannot engineer good features or select the right model if you do not first understand what the data looks like.

```
Cleaned Data → Summarize → Visualize → Find Patterns → Generate Hypotheses → Inform Feature Engineering
```

---

### <span style="color:#2E86AB">3.1 Univariate Analysis - One Feature at a Time</span>

> Examines the distribution and summary of each individual feature.

| Data Type | What to check | Visualization |
|:---|:---|:---|
| Numerical | Mean, median, std, min, max, skewness | Histogram, Box plot, KDE plot |
| Categorical | Frequency of each category, dominant class | Bar chart, Pie chart |
| Boolean | True/False ratio | Count plot |

#### <span style="color:#5B8DB8">Key Summary Statistics</span>

| Statistic | What it tells you |
|:---|:---|
| Mean | Average value - sensitive to outliers |
| Median | Middle value - robust to outliers |
| Standard Deviation | Spread of values around the mean |
| Skewness | Whether distribution leans left or right |
| Kurtosis | Whether distribution has heavy or light tails |

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">Skewness > 0 → Right skewed (tail on right) &nbsp;|&nbsp; Skewness < 0 → Left skewed (tail on left)</span>

</div>

---

### <span style="color:#2E86AB">3.2 Bivariate Analysis - Two Features at a Time</span>

> Examines the relationship between two variables - especially between a feature and the target.

| Pair Type | What to check | Visualization |
|:---|:---|:---|
| Numerical vs Numerical | Correlation, linear relationship | Scatter plot, Correlation heatmap |
| Categorical vs Numerical | Mean target value per category | Box plot, Violin plot, Bar chart |
| Categorical vs Categorical | Co-occurrence, dependency | Grouped bar chart, Chi-square test |

#### <span style="color:#5B8DB8">Correlation</span>

> **Definition:** Correlation measures the strength and direction of the linear relationship between two numerical variables.

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">Pearson Correlation r = Cov(X, Y) / (σ_X × σ_Y) &nbsp;|&nbsp; Range: −1 to +1</span>

</div>

| Value of r | Interpretation |
|:---:|:---|
| +1 | Perfect positive correlation |
| +0.7 to +1 | Strong positive |
| +0.4 to +0.7 | Moderate positive |
| 0 | No linear correlation |
| −0.4 to −0.7 | Moderate negative |
| −1 | Perfect negative correlation |

> **Correlation ≠ Causation.** Two variables can be correlated without one causing the other.

---

### <span style="color:#2E86AB">3.3 Multivariate Analysis - Many Features Together</span>

> Examines patterns and relationships across multiple features simultaneously.

| Technique | Description |
|:---|:---|
| Correlation heatmap | Visual matrix of all feature correlations - spot multicollinearity |
| Pair plot | Grid of scatter plots for all feature pairs |
| PCA plot | Visualize high-dimensional data in 2D |
| Grouped statistics | Group data by target class and compare feature distributions |

#### <span style="color:#5B8DB8">Multicollinearity</span>

> **Definition:** Multicollinearity occurs when two or more features are highly correlated with each other - they carry redundant information.

- Example: `height_cm` and `height_inches` in the same dataset - they are the same thing
- Problem: Causes instability in linear models
- Fix: Drop one of the correlated features, or use PCA

---

### <span style="color:#2E86AB">3.4 What to Look For During EDA</span>

| Finding | Action to take |
|:---|:---|
| Missing values | Plan imputation strategy |
| Outliers | Decide to remove, cap, or keep |
| Skewed distributions | Plan log or square-root transformation |
| Highly correlated features | Plan to drop one or apply PCA |
| Class imbalance | Plan oversampling / undersampling |
| Irrelevant features | Flag for removal in feature selection |
| Interesting patterns | Generate hypotheses for new engineered features |

---

### <span style="color:#2E86AB">3.5 EDA Tools in Python</span>

| Library | Purpose |
|:---|:---|
| `pandas` | `.describe()`, `.value_counts()`, `.corr()` |
| `matplotlib` | Base plotting - histograms, scatter plots, bar charts |
| `seaborn` | Statistical plots - heatmap, pairplot, violin, box plot |
| `plotly` | Interactive visualizations |
| `ydata-profiling` | Auto-generates full EDA report in one line |

---

## <span style="color:#1565C0">Step 4 - Feature Engineering & Selection</span>

> **Definition:** Feature Engineering is the process of using domain knowledge and data transformations to create new, more informative input variables (features) that help the model learn better.

> **Definition:** Feature Selection is the process of choosing only the most relevant features from the dataset and removing redundant, irrelevant, or harmful ones.

These two steps are often what separates a good model from a great one.

---

### <span style="color:#2E86AB">4.1 What is a Feature?</span>

> **Definition:** A feature (also called input variable, attribute, or predictor) is a measurable property of the data used as input to the model.

**Example:** In a house price prediction model:
- Features: `area`, `number of bedrooms`, `location`, `age of house`, `floor number`
- Target (label): `price`

---

### <span style="color:#2E86AB">4.2 Feature Engineering Techniques</span>

#### <span style="color:#5B8DB8">Creating New Features from Existing Ones</span>

| Technique | Example |
|:---|:---|
| Arithmetic combination | `price_per_sqft = price / area` |
| Date/time decomposition | Extract `day`, `month`, `hour`, `day_of_week` from a timestamp |
| Interaction features | `height × weight` to create BMI |
| Aggregation | Mean/max/min spend per customer over last 30 days |
| Binning | Convert continuous age into groups: `0-18`, `19-35`, `36-60`, `60+` |
| Log transformation | Apply `log(x)` to compress right-skewed distributions |
| Polynomial features | `x²`, `x³` to capture non-linear relationships |

#### <span style="color:#5B8DB8">Text Features (NLP)</span>

| Technique | Description |
|:---|:---|
| Bag of Words (BoW) | Count how many times each word appears |
| TF-IDF | Weights words by how unique they are to a document |
| Word Embeddings | Convert words to dense numerical vectors (Word2Vec, GloVe) |

---

### <span style="color:#2E86AB">4.3 Feature Selection Techniques</span>

Too many features = more noise, slower training, risk of overfitting. Feature selection removes what doesn't help.

#### <span style="color:#5B8DB8">Filter Methods</span>

> Select features independently of any ML model - based on statistical properties.

| Method | What it measures |
|:---|:---|
| Correlation coefficient | Linear relationship between feature and target |
| Chi-Square test | Dependency between categorical feature and target |
| Variance threshold | Remove features with near-zero variance (they carry no information) |
| ANOVA F-test | Difference in means across classes |

#### <span style="color:#5B8DB8">Wrapper Methods</span>

> Train the model repeatedly with different feature subsets and pick the best one.

| Method | Description |
|:---|:---|
| Forward Selection | Start with 0 features, add one at a time - keep if performance improves |
| Backward Elimination | Start with all features, remove one at a time - remove if performance stays same |
| Recursive Feature Elimination (RFE) | Iteratively removes least important features based on model weights |

#### <span style="color:#5B8DB8">Embedded Methods</span>

> Feature selection happens automatically during model training.

| Method | Description |
|:---|:---|
| LASSO (L1 Regularization) | Drives unimportant feature weights to exactly zero |
| Random Forest Importance | Ranks features by how much they reduce impurity across all trees |
| Gradient Boosting Importance | Similar to Random Forest - each feature gets an importance score |

---

### <span style="color:#2E86AB">4.4 Dimensionality Reduction</span>

> **Definition:** Dimensionality reduction compresses many features into fewer dimensions while preserving as much useful information as possible.

Used when the dataset has hundreds or thousands of features (the "curse of dimensionality").

| Technique | Type | Description |
|:---|:---|:---|
| PCA (Principal Component Analysis) | Linear | Projects data onto directions of maximum variance |
| t-SNE | Non-linear | Visualizes high-dimensional data in 2D/3D |
| LDA (Linear Discriminant Analysis) | Linear | Maximizes separation between classes |
| Autoencoders | Deep Learning | Compresses data via neural network encoding |

---

## <span style="color:#1565C0">Step 5 - Model Selection</span>

> **Definition:** Model Selection is the process of choosing the right ML algorithm for the specific problem, based on the type of data, task, and constraints.

No single algorithm works best for all problems. This step requires understanding the nature of the task.

---

### <span style="color:#2E86AB">5.1 Identify the Problem Type First</span>

```
What is your output?
├── Continuous number (e.g., price, temperature)  → Regression
├── Category / Class (e.g., spam or not, dog or cat) → Classification
├── No labels - find hidden structure → Clustering / Unsupervised
└── Sequential decisions with rewards → Reinforcement Learning
```

---

### <span style="color:#2E86AB">5.2 Algorithm Selection Guide</span>

| Task | Small data | Large data | Notes |
|:---|:---|:---|:---|
| Binary Classification | Logistic Regression, SVM | Random Forest, XGBoost | Start simple |
| Multi-class Classification | Decision Tree, KNN | Random Forest, XGBoost, Neural Net | |
| Regression | Linear Regression, Ridge | Random Forest, Gradient Boosting | |
| Clustering | K-Means, Hierarchical | DBSCAN, Mini-batch K-Means | |
| Anomaly Detection | IsolationForest, LOF | Autoencoder | |
| NLP / Text | Naive Bayes, TF-IDF + LR | Transformers (BERT) | |
| Image Classification | - | CNN, ResNet, EfficientNet | DL required |

---

### <span style="color:#2E86AB">5.3 Model Complexity Considerations</span>

| Factor | Simpler Model | Complex Model |
|:---|:---|:---|
| Data size | Small datasets | Large datasets |
| Interpretability needed | Yes (healthcare, law, finance) | Less critical |
| Training time | Fast | Slow |
| Risk of overfitting | Low | High (needs regularization) |
| Examples | Linear Regression, Logistic | XGBoost, Neural Networks |

> **Best practice:** Always start with a simple baseline model (e.g., Logistic Regression or Linear Regression). Complexity should only be added when the simple model is provably insufficient.

---

### <span style="color:#2E86AB">5.4 The No Free Lunch Theorem</span>

> **Definition:** No single ML algorithm is universally superior to all others across all possible problems. Every algorithm has assumptions, strengths, and weaknesses.

This is why model selection, experimentation, and evaluation are critical - there is no shortcut of always using one "best" algorithm.

---

## <span style="color:#1565C0">Step 6 - Model Training</span>

> **Definition:** Model Training is the process of feeding prepared data into the selected algorithm so it can adjust its internal parameters to minimize prediction error.

---

### <span style="color:#2E86AB">6.1 What Happens During Training?</span>

```
Initialize model parameters (weights)
    ↓
Feed training data (batch by batch)
    ↓
Model makes a prediction
    ↓
Calculate the error using a Loss Function
    ↓
Adjust parameters to reduce error (via Optimization)
    ↓
Repeat for all batches and epochs
    ↓
Training complete → Model has learned the pattern
```

#### <span style="color:#5B8DB8">Key Terms in Training</span>

| Term | Definition |
|:---|:---|
| Loss Function | Measures how wrong the model's prediction is |
| Optimizer | Algorithm that adjusts parameters to reduce loss (e.g., Gradient Descent) |
| Epoch | One complete pass through the entire training dataset |
| Batch size | Number of samples processed before parameters are updated |
| Learning rate | How large a step the optimizer takes when updating parameters |

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">Goal of Training: Minimize the Loss Function</span>

</div>

---

### <span style="color:#2E86AB">6.2 Overfitting and Underfitting</span>

> **Overfitting:** The model learns the training data too well - including its noise - and performs poorly on new unseen data.
> **Underfitting:** The model is too simple to capture the patterns in the data - performs poorly on both training and test data.

| | Training Performance | Test Performance |
|:---|:---:|:---:|
| Underfitting | <span style="color:#C0392B">Poor</span> | <span style="color:#C0392B">Poor</span> |
| Good Fit | <span style="color:#27AE60">Good</span> | <span style="color:#27AE60">Good</span> |
| Overfitting | <span style="color:#27AE60">Excellent</span> | <span style="color:#C0392B">Poor</span> |

```
Underfitting                 Good Fit               Overfitting
(High Bias)                 (Balanced)             (High Variance)
Too simple model          Right complexity          Too complex model
```

#### <span style="color:#5B8DB8">Fixing Overfitting</span>

- Add more training data
- Reduce model complexity
- Apply regularization (L1 / L2)
- Use dropout (neural networks)
- Early stopping during training
- Use cross-validation

#### <span style="color:#5B8DB8">Fixing Underfitting</span>

- Use a more complex model
- Add more relevant features
- Reduce regularization
- Train for more epochs

---

---

## <span style="color:#1565C0">Step 7 - Model Evaluation & Tuning</span>

> **Definition:** Model Evaluation measures how well the trained model generalizes to unseen data. Tuning then optimizes the model's hyperparameters to push performance further.

---

### <span style="color:#2E86AB">7.1 Evaluation Metrics - Classification</span>

> **Confusion Matrix:** A table that summarizes the prediction results of a classification model.

```
                    Predicted Positive    Predicted Negative
Actual Positive         TP (True Pos)         FN (False Neg)
Actual Negative         FP (False Pos)         TN (True Neg)
```

| Metric | Formula | What it measures |
|:---|:---|:---|
| Accuracy | (TP + TN) / Total | Overall correct predictions |
| Precision | TP / (TP + FP) | Of all predicted positives, how many were actually positive |
| Recall (Sensitivity) | TP / (TP + FN) | Of all actual positives, how many were correctly found |
| F1 Score | 2 × (Precision × Recall) / (Precision + Recall) | Harmonic mean of Precision and Recall |
| ROC-AUC | Area under ROC curve | Model's ability to distinguish between classes |

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">F1 = 2 × (Precision × Recall) / (Precision + Recall)</span>

</div>

#### <span style="color:#5B8DB8">When to prioritize which metric?</span>

| Scenario | Prioritize |
|:---|:---|
| Class imbalance | F1 Score or ROC-AUC (not accuracy) |
| Cost of false positive is high (e.g., spam filter) | Precision |
| Cost of false negative is high (e.g., cancer detection) | Recall |
| Balanced classes, general use | Accuracy |

---

### <span style="color:#2E86AB">7.2 Evaluation Metrics - Regression</span>

| Metric | Formula | What it measures |
|:---|:---|:---|
| MAE (Mean Absolute Error) | Mean of `|actual - predicted|` | Average magnitude of errors - easy to interpret |
| MSE (Mean Squared Error) | Mean of `(actual - predicted)²` | Heavily penalizes large errors |
| RMSE (Root MSE) | `√MSE` | Same unit as target - more interpretable than MSE |
| R² (R-Squared) | 1 - (SS_res / SS_tot) | Proportion of variance explained by the model |

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">R² = 1 − (SS_residual / SS_total) &nbsp;|&nbsp; Range: −∞ to 1 &nbsp;|&nbsp; Higher is better</span>

</div>

- R² = 1 → Perfect model
- R² = 0 → Model is no better than predicting the mean
- R² < 0 → Model is worse than predicting the mean

---

### <span style="color:#2E86AB">7.3 Hyperparameter Tuning</span>

> **Definition:** Hyperparameters are settings defined before training that control how the model learns - they are not learned from data automatically.

| Type | Examples |
|:---|:---|
| Model hyperparameters | Number of trees in Random Forest, depth of Decision Tree |
| Training hyperparameters | Learning rate, batch size, number of epochs |
| Regularization | L1/L2 lambda values, dropout rate |

#### <span style="color:#5B8DB8">Tuning Strategies</span>

| Strategy | Description | Pros | Cons |
|:---|:---|:---|:---|
| Grid Search | Try every combination of specified values | Exhaustive, finds best in grid | Very slow |
| Random Search | Try random combinations | Faster, often finds near-optimal | May miss best |
| Bayesian Optimization | Uses past results to decide what to try next | Efficient | More complex to implement |

---

## <span style="color:#1565C0">Step 8 - Model Deployment</span>

> **Definition:** Deployment is the process of integrating a trained ML model into a production environment where it can receive real-world inputs and serve predictions to end users or other systems.

Training a model on a laptop is not the end - a model only creates value when it is deployed and used in the real world.

---

### <span style="color:#2E86AB">8.1 The Deployment Pipeline</span>

```
Trained Model (saved file)
    ↓
Model Serialization (save to disk)
    ↓
Build an API / Service (REST API using Flask / FastAPI)
    ↓
Containerize (Docker)
    ↓
Deploy to Cloud / Server (AWS, GCP, Azure, Render, Railway)
    ↓
Monitor in Production
```

---

### <span style="color:#2E86AB">8.2 Model Serialization - Saving the Model</span>

> **Definition:** Serialization is converting the trained model object into a file format that can be stored on disk and loaded later without retraining.

| Format | Library | Use case |
|:---|:---|:---|
| `.pkl` (Pickle) | Python built-in | Scikit-learn models - small/medium size |
| `.joblib` | joblib library | Better for large numpy arrays |
| `.h5` / `.keras` | TensorFlow/Keras | Deep Learning models |
| `.pt` / `.pth` | PyTorch | PyTorch models |
| ONNX | Open format | Cross-framework model sharing |

```python
# Save
import joblib
joblib.dump(model, 'model.joblib')

# Load
model = joblib.load('model.joblib')
```

---

### <span style="color:#2E86AB">8.3 Serving the Model - REST API</span>

> **Definition:** A REST API wraps the ML model and exposes a URL endpoint that accepts input data and returns a prediction - allowing any app, website, or system to use the model.

```
Client sends: POST /predict  { "age": 25, "salary": 50000 }
         ↓
API loads model → runs model.predict(input) → returns result
         ↓
Client receives: { "prediction": "approved", "confidence": 0.87 }
```

Common tools for serving ML models:

| Tool | Description |
|:---|:---|
| Flask | Lightweight Python web framework - easy to build ML APIs |
| FastAPI | Modern, faster Python framework - auto-generates API docs |
| Streamlit | Build interactive ML web apps with minimal code |
| Gradio | Fast UI for ML demos - great for prototyping |
| TensorFlow Serving | Production-grade serving for TensorFlow models |
| TorchServe | Production-grade serving for PyTorch models |

---

### <span style="color:#2E86AB">8.4 Deployment Environments</span>

| Environment | Description | Tools |
|:---|:---|:---|
| Local server | Run on a laptop or on-premise server | Flask + localhost |
| Cloud platforms | Scalable, managed infrastructure | AWS SageMaker, GCP Vertex AI, Azure ML |
| Serverless | No server management - auto-scales | AWS Lambda, Google Cloud Functions |
| Edge deployment | Run directly on device (phone, sensor) | TensorFlow Lite, ONNX Runtime |
| Containerized | Portable, reproducible environments | Docker, Kubernetes |

---

---

## <span style="color:#1565C0">Step 9 - Model Monitoring & Maintenance</span>

> **Definition:** Model Monitoring is the continuous tracking of a deployed model's performance in production. Maintenance is the ongoing process of keeping the model accurate, relevant, and operational as the real world changes over time.

Deployment is not the end. A model that was accurate last year may become inaccurate today because the real world changes. Without monitoring, you have no way of knowing when your model has silently degraded.

```
Deployed Model → Track performance → Detect drift → Alert → Investigate → Retrain → Redeploy
```

---

### <span style="color:#2E86AB">9.1 Why Models Degrade Over Time</span>

| Reason | Explanation |
|:---|:---|
| Data drift | Real-world input distributions shift - model was trained on old patterns |
| Concept drift | The relationship between features and the target changes |
| Software changes | Upstream data pipelines break or change column formats |
| Business changes | Company strategy shifts - model's goal is no longer aligned |
| Label drift | The distribution of the output variable changes |

### <span style="color:#2E86AB">9.2 Types of Drift</span>

| Drift Type | Definition | Example |
|:---|:---|:---|
| Data Drift | Statistical distribution of input features changes | User demographics shift |
| Concept Drift | The relationship between input and output changes | A product that used to be popular is no longer |
| Label Drift | Distribution of the target variable changes | Fraud patterns evolve |

### <span style="color:#2E86AB">9.3 What to Monitor</span>

| Metric | What it detects |
|:---|:---|
| Prediction accuracy over time | Overall model performance degradation |
| Input feature distributions | Data drift - compare live data vs training data |
| API latency and response time | Infrastructure or bottleneck issues |
| Data schema changes | New or missing columns breaking the pipeline |
| Business-level KPIs | Whether model decisions are actually helping the business |
| Error rates and exceptions | Bugs or unexpected inputs crashing the model |

### <span style="color:#2E86AB">9.4 Retraining Strategy</span>

| Strategy | Description |
|:---|:---|
| Scheduled retraining | Retrain on a fixed schedule (weekly, monthly) |
| Trigger-based retraining | Retrain when performance drops below a threshold |
| Continuous learning | Model updates incrementally as new data arrives |

### <span style="color:#2E86AB">9.5 Maintenance Tasks</span>

| Task | Description |
|:---|:---|
| Model versioning | Track which model version is deployed and when |
| A/B testing | Gradually roll out a new model version vs the old one |
| Shadow mode testing | Run new model in parallel without serving its predictions yet |
| Rollback plan | Always keep the previous model version ready if new one fails |
| Documentation updates | Keep model cards and API docs in sync with every change |

---

## <span style="color:#1565C0">Complete ML Life Cycle - End-to-End Summary</span>

```
STEP 0 - PROBLEM DEFINITION
    Define goal → Identify input/output → Determine task type → Set success criteria
    ↓
STEP 1 - DATA COLLECTION
    Gather structured / unstructured data from relevant sources
    ↓
STEP 2 - DATA CLEANING & PREPROCESSING
    Handle missing values → Remove outliers → Encode categories
    → Scale features → Train-test split → Cross validation setup
    ↓
STEP 3 - EXPLORATORY DATA ANALYSIS (EDA)
    Univariate → Bivariate → Multivariate analysis
    → Understand distributions, correlations, and anomalies
    ↓
STEP 4 - FEATURE ENGINEERING & SELECTION
    Create new features → Select relevant ones → Reduce dimensionality
    ↓
STEP 5 - MODEL SELECTION
    Identify task type → Choose algorithm → Set baseline model
    ↓
STEP 6 - MODEL TRAINING
    Fit model to training data → Minimize loss → Tune epochs & batch size
    ↓
STEP 7 - MODEL EVALUATION & TUNING
    Evaluate metrics (Accuracy / F1 / RMSE / R²)
    → Tune hyperparameters → Fix overfitting / underfitting → Finalize model
    ↓
STEP 8 - MODEL DEPLOYMENT
    Serialize model → Build REST API → Containerize → Deploy to cloud
    ↓
STEP 9 - MODEL MONITORING & MAINTENANCE
    Track performance → Detect drift → Retrain → Version & maintain
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