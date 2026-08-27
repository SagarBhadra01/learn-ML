<div align="center">

# <span style="color:#0A2FA8">Model Training, Evaluation & Tuning</span>

<sub>Complete A-Z notes on how ML models learn, how they are measured, and how they are optimized</sub>

</div>

---

## <span style="color:#1565C0">1. Model Training</span>

### <span style="color:#2E86AB">1.1 What is Model Training?</span>

> **Definition:** Model training is the process of feeding labeled data into a machine learning algorithm so it can learn the underlying patterns by adjusting its internal parameters to minimize prediction error.

During training, the model sees input features (X) and tries to predict the output (y). It compares its prediction to the true label, measures the error, and updates itself to do better next time. This process repeats over many iterations until the model performs well.

```
Input Data (X) → Model Prediction (ŷ) → Loss Calculation → Weight Update → Repeat
```

---

### <span style="color:#2E86AB">1.2 The Training Loop — Step by Step</span>

The core of all supervised learning is the **training loop**, which runs repeatedly until convergence or a stopping condition.

| Step | Name | What Happens |
|:---:|:---|:---|
| 1 | Forward Pass | Input flows through the model to produce a prediction |
| 2 | Loss Calculation | Difference between prediction and true label is computed |
| 3 | Backward Pass | Gradients of loss w.r.t. each parameter are computed (backpropagation) |
| 4 | Weight Update | Parameters are adjusted in the direction that reduces loss |
| 5 | Repeat | Steps 1–4 repeat for the next batch or epoch |

---

### <span style="color:#2E86AB">1.3 Loss Functions</span>

> **Definition:** A loss function (also called cost function or objective function) measures how far the model's predictions are from the true values. The goal of training is to minimize this function.

#### <span style="color:#5B8DB8">For Regression</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">MSE = (1/n) * Σ(yᵢ - ŷᵢ)²</span>

</div>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">MAE = (1/n) * Σ|yᵢ - ŷᵢ|</span>

</div>

| Loss Function | Sensitive to Outliers | Use When |
|:---|:---:|:---|
| Mean Squared Error (MSE) | Yes | You want to heavily penalize large errors |
| Mean Absolute Error (MAE) | No | Data has many outliers |
| Huber Loss | Moderate | Combines MSE + MAE robustness |
| Log-Cosh | No | Smooth, differentiable alternative to MAE |

#### <span style="color:#5B8DB8">For Classification</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">Binary Cross-Entropy = -[y·log(ŷ) + (1-y)·log(1-ŷ)]</span>

</div>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">Categorical Cross-Entropy = -Σ yᵢ · log(ŷᵢ)</span>

</div>

| Loss Function | Use Case |
|:---|:---|
| Binary Cross-Entropy | Binary classification (0 or 1) |
| Categorical Cross-Entropy | Multi-class (softmax output) |
| Sparse Categorical Cross-Entropy | Multi-class with integer labels |
| Hinge Loss | Support Vector Machines |
| KL Divergence | Comparing probability distributions |

---

### <span style="color:#2E86AB">1.4 Gradient Descent</span>

> **Definition:** Gradient descent is the optimization algorithm used to minimize the loss function by iteratively moving the model's parameters in the direction of the steepest descent (negative gradient).

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">w = w - α · (∂L / ∂w)</span>

</div>

Where:
- `w` = weight (parameter)
- `α` = learning rate
- `∂L / ∂w` = gradient of loss with respect to weight

#### <span style="color:#5B8DB8">Types of Gradient Descent</span>

| Type | Description | Pros | Cons |
|:---|:---|:---|:---|
| Batch GD | Uses entire dataset per update | Stable convergence | Slow, memory-heavy |
| Stochastic GD (SGD) | Uses 1 sample per update | Fast, online learning | Noisy updates, unstable |
| Mini-Batch GD | Uses small batches (32, 64, 128) | Balance of speed + stability | Batch size is a hyperparameter |

Mini-Batch GD is the standard in practice.

---

### <span style="color:#2E86AB">1.5 Optimizers</span>

> **Definition:** Optimizers are enhanced versions of gradient descent that use techniques like momentum or adaptive learning rates to converge faster and more reliably.

#### <span style="color:#5B8DB8">SGD with Momentum</span>

Momentum prevents oscillations by accumulating a velocity in the direction of the gradient.

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">v = β·v - α·∇L,  w = w + v</span>

</div>

#### <span style="color:#5B8DB8">RMSProp</span>

Adapts the learning rate for each parameter based on the magnitude of recent gradients.

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">w = w - (α / √(E[g²] + ε)) · g</span>

</div>

#### <span style="color:#5B8DB8">Adam (Adaptive Moment Estimation)</span>

Combines Momentum + RMSProp. Most widely used optimizer in deep learning.

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">w = w - (α · m̂) / (√v̂ + ε)</span>

</div>

Where `m̂` = bias-corrected first moment, `v̂` = bias-corrected second moment.

| Optimizer | Adaptive LR | Momentum | Best For |
|:---|:---:|:---:|:---|
| SGD | No | No | Simple models, linear |
| SGD + Momentum | No | Yes | Image classification |
| RMSProp | Yes | No | RNNs, noisy data |
| Adam | Yes | Yes | Deep learning (default) |
| AdaGrad | Yes | No | Sparse data (NLP) |
| AdamW | Yes | Yes | NLP, Transformers |

---

### <span style="color:#2E86AB">1.6 Learning Rate</span>

> **Definition:** The learning rate (α) controls the step size taken in each gradient descent update. It is the most critical hyperparameter in training.

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">Too High → Overshoots minimum (diverges)  |  Too Low → Slow convergence</span>

</div>

#### <span style="color:#5B8DB8">Learning Rate Schedules</span>

| Schedule | Description |
|:---|:---|
| Constant | Fixed LR throughout training |
| Step Decay | Reduce LR by a factor every N epochs |
| Exponential Decay | LR decays exponentially over time |
| Cosine Annealing | LR follows cosine curve, gradually reduces |
| Warm-up + Decay | Start low, increase, then decrease (used in Transformers) |
| Cyclical LR | Oscillates between min and max LR |

---

### <span style="color:#2E86AB">1.7 Epochs, Batch Size & Iterations</span>

> **Definition:** An epoch is one complete pass through the entire training dataset.

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">Iterations per epoch = Total Samples / Batch Size</span>

</div>

| Term | Meaning | Example |
|:---|:---|:---|
| Epoch | 1 full pass over all training data | 50 epochs = 50 full passes |
| Batch Size | Samples used in one weight update | 32, 64, 128, 256 |
| Iteration | One forward + backward pass on a batch | 1000 samples / 100 batch = 10 iterations |

**Effect of Batch Size:**
- Large batch → Stable gradients, faster per epoch, but may converge to sharp minima
- Small batch → Noisy gradients, slower, but often converges to better generalizing minima

---

### <span style="color:#2E86AB">1.8 Weight Initialization</span>

> **Definition:** Weight initialization sets the starting values for model parameters before training begins. Poor initialization can cause vanishing/exploding gradients.

| Method | Formula | Best For |
|:---|:---|:---|
| Zero Init | w = 0 | Never use — breaks symmetry |
| Random Normal | w ~ N(0, 0.01) | Small networks |
| Xavier / Glorot | w ~ N(0, 2/(nᵢₙ+nₒᵤₜ)) | Sigmoid, Tanh activations |
| He / Kaiming | w ~ N(0, 2/nᵢₙ) | ReLU and variants |
| LeCun | w ~ N(0, 1/nᵢₙ) | SELU activations |

---

### <span style="color:#2E86AB">1.9 Activation Functions</span>

> **Definition:** Activation functions introduce non-linearity into the network, allowing it to learn complex patterns beyond simple linear relationships.

| Activation | Formula | Range | Use Case |
|:---|:---|:---:|:---|
| Sigmoid | 1 / (1 + e⁻ˣ) | (0, 1) | Binary output layer |
| Tanh | (eˣ - e⁻ˣ) / (eˣ + e⁻ˣ) | (-1, 1) | Hidden layers (older) |
| ReLU | max(0, x) | [0, ∞) | Hidden layers (default) |
| Leaky ReLU | max(0.01x, x) | (-∞, ∞) | Avoids dying ReLU |
| ELU | x if x>0, α(eˣ-1) if x≤0 | (-α, ∞) | Smooth negative values |
| Softmax | eˣᵢ / Σeˣⱼ | (0, 1) | Multi-class output layer |

**Vanishing Gradient Problem:** Sigmoid and Tanh squash values to a tiny range, causing gradients to become near zero in deep networks. ReLU solves this.

---

### <span style="color:#2E86AB">1.10 Overfitting & Underfitting</span>

> **Definition:** Overfitting occurs when a model learns the training data too well — including noise — and fails to generalize to new data. Underfitting occurs when the model is too simple to capture the underlying patterns.

| Condition | Training Error | Test Error | Solution |
|:---|:---:|:---:|:---|
| <span style="color:#27AE60">Good Fit</span> | Low | Low | — |
| <span style="color:#C0392B">Underfitting</span> | High | High | More complex model, more features |
| <span style="color:#C0392B">Overfitting</span> | Low | High | Regularization, more data, dropout |

---

### <span style="color:#2E86AB">1.11 Bias-Variance Tradeoff</span>

> **Definition:** Bias is error from wrong assumptions (underfitting). Variance is error from sensitivity to fluctuations in training data (overfitting). The total error is the sum of both.

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">Total Error = Bias² + Variance + Irreducible Noise</span>

</div>

| | High Bias | Low Bias |
|:---|:---|:---|
| **High Variance** | Underfits AND overfits | Overfits (complex, memorizes) |
| **Low Variance** | Underfits (simple, rigid) | Ideal model |

---

### <span style="color:#2E86AB">1.12 Regularization Techniques</span>

> **Definition:** Regularization techniques constrain model complexity to prevent overfitting by adding a penalty to the loss function or by modifying the training process.

#### <span style="color:#5B8DB8">L1 Regularization (Lasso)</span>

Adds the absolute sum of weights to the loss. Drives some weights to exactly zero, producing sparse models (automatic feature selection).

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">L_total = L_original + λ · Σ|wᵢ|</span>

</div>

#### <span style="color:#5B8DB8">L2 Regularization (Ridge)</span>

Adds the squared sum of weights to the loss. Keeps all weights small but non-zero, preferred in most neural networks (weight decay).

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">L_total = L_original + λ · Σwᵢ²</span>

</div>

#### <span style="color:#5B8DB8">Dropout</span>

During each training step, randomly sets a fraction `p` of neurons to zero. Forces the network to not rely on any single neuron, acting like an ensemble of networks.

```
Training:  some neurons randomly deactivated → forces redundant learning
Inference: all neurons active, outputs scaled by (1 - p)
```

#### <span style="color:#5B8DB8">Early Stopping</span>

Monitors validation loss during training. Stops training when validation loss starts increasing, even if training loss continues to decrease.

```
Training loss still decreasing → but Validation loss rising → STOP here (save that checkpoint)
```

| Regularization | Mechanism | Best For |
|:---|:---|:---|
| L1 (Lasso) | Sparsity via weight zeroing | Feature selection |
| L2 (Ridge) | Weight decay | Most neural networks |
| Dropout | Random neuron deactivation | Deep learning |
| Early Stopping | Halt at validation minimum | All iterative models |
| Data Augmentation | Expand training set artificially | Images, text, audio |
| Batch Normalization | Normalize layer inputs | Deep networks |

---

### <span style="color:#2E86AB">1.13 Batch Normalization</span>

> **Definition:** Batch normalization normalizes the inputs to each layer so that they have a mean of zero and a standard deviation of one. This stabilizes and accelerates training.

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">x̂ = (x - μ_B) / √(σ²_B + ε),  y = γ·x̂ + β</span>

</div>

- `μ_B` = batch mean, `σ²_B` = batch variance
- `γ` and `β` are learnable scale and shift parameters

**Benefits:** Allows higher learning rates, reduces sensitivity to initialization, provides slight regularization.

---

## <span style="color:#1565C0">2. Model Evaluation</span>

### <span style="color:#2E86AB">2.1 What is Model Evaluation?</span>

> **Definition:** Model evaluation is the process of measuring how well a trained model performs on unseen data using objective metrics. It helps detect overfitting, underfitting, and guides model selection.

---

### <span style="color:#2E86AB">2.2 Train / Validation / Test Split</span>

> **Definition:** The dataset is divided into three non-overlapping subsets to ensure fair, unbiased evaluation.

| Split | Purpose | Typical Size |
|:---|:---|:---:|
| Training Set | Teach the model | 60–70% |
| Validation Set | Tune hyperparameters, monitor overfitting | 15–20% |
| Test Set | Final unbiased performance estimate | 15–20% |

```
Raw Data → [Training Set] → Model Learns
         → [Validation Set] → Hyperparameter Tuning
         → [Test Set] → Final Evaluation (touch only once!)
```

**Key Rule:** The test set must never be used during training or tuning. It is only touched once for the final report.

---

### <span style="color:#2E86AB">2.3 Cross-Validation</span>

> **Definition:** Cross-validation is a resampling technique that trains and evaluates the model on different subsets of data multiple times to get a more reliable performance estimate, especially when data is limited.

#### <span style="color:#5B8DB8">K-Fold Cross-Validation</span>

```
Data split into K equal folds:
Fold 1: [Test] [Train] [Train] [Train] [Train]
Fold 2: [Train] [Test] [Train] [Train] [Train]
Fold 3: [Train] [Train] [Test] [Train] [Train]
...
Final Score = Average of all K scores
```

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">CV Score = (1/K) · Σᵢ Score(foldᵢ)</span>

</div>

#### <span style="color:#5B8DB8">Types of Cross-Validation</span>

| Type | Description | Use When |
|:---|:---|:---|
| K-Fold (K=5 or 10) | Standard, equal folds | General use |
| Stratified K-Fold | Preserves class distribution in each fold | Imbalanced datasets |
| Leave-One-Out (LOO) | K = total samples, one sample as test | Very small datasets |
| Time Series Split | Respects temporal order | Time series data |
| Group K-Fold | Keeps groups intact (no data leakage) | Patient/user data |

---

### <span style="color:#2E86AB">2.4 Evaluation Metrics for Classification</span>

#### <span style="color:#5B8DB8">The Confusion Matrix</span>

> **Definition:** A confusion matrix is a table that shows the counts of True Positives (TP), True Negatives (TN), False Positives (FP), and False Negatives (FN) for a classification model.

```
                  Predicted Positive    Predicted Negative
Actual Positive   True Positive (TP)    False Negative (FN)
Actual Negative   False Positive (FP)   True Negative (TN)
```

#### <span style="color:#5B8DB8">Core Metrics Derived from Confusion Matrix</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">Accuracy = (TP + TN) / (TP + TN + FP + FN)</span>

</div>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">Precision = TP / (TP + FP)</span>

</div>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">Recall (Sensitivity) = TP / (TP + FN)</span>

</div>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">F1 Score = 2 · (Precision · Recall) / (Precision + Recall)</span>

</div>

| Metric | What it Measures | High Value Means |
|:---|:---|:---|
| Accuracy | Overall correctness | Most predictions are correct |
| Precision | Quality of positive predictions | Few false alarms |
| Recall | Coverage of actual positives | Few missed positives |
| F1 Score | Harmonic mean of Precision & Recall | Balance between both |
| Specificity | True Negative Rate | Good at identifying negatives |

**When to use which:**
- Use **Precision** when false positives are costly (e.g., spam filter, fraud alert)
- Use **Recall** when false negatives are costly (e.g., cancer detection, disaster prediction)
- Use **F1** when classes are imbalanced and both matter equally

#### <span style="color:#5B8DB8">ROC Curve & AUC</span>

> **Definition:** The ROC (Receiver Operating Characteristic) curve plots True Positive Rate (Recall) vs False Positive Rate at various classification thresholds. AUC is the Area Under the Curve.

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">FPR = FP / (FP + TN)  |  TPR = TP / (TP + FN)</span>

</div>

| AUC Value | Model Quality |
|:---:|:---|
| 1.0 | Perfect model |
| 0.9 – 1.0 | Excellent |
| 0.8 – 0.9 | Good |
| 0.7 – 0.8 | Fair |
| 0.5 – 0.7 | Poor |
| 0.5 | Random guessing |

#### <span style="color:#5B8DB8">Precision-Recall Curve</span>

Plots Precision vs Recall across all thresholds. More informative than ROC for heavily imbalanced datasets where the negative class dominates.

#### <span style="color:#5B8DB8">Multi-Class Metrics</span>

| Strategy | Description |
|:---|:---|
| Macro Average | Compute metric per class, take unweighted mean |
| Weighted Average | Compute metric per class, weight by support (class frequency) |
| Micro Average | Aggregate TP/FP/FN across all classes, then compute |

---

### <span style="color:#2E86AB">2.5 Evaluation Metrics for Regression</span>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">MAE = (1/n) · Σ|yᵢ - ŷᵢ|</span>

</div>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">MSE = (1/n) · Σ(yᵢ - ŷᵢ)²</span>

</div>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">RMSE = √[(1/n) · Σ(yᵢ - ŷᵢ)²]</span>

</div>

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">R² = 1 - [Σ(yᵢ - ŷᵢ)²] / [Σ(yᵢ - ȳ)²]</span>

</div>

| Metric | Unit | Penalizes Outliers | Best Value |
|:---|:---:|:---:|:---:|
| MAE | Same as y | No | 0 |
| MSE | y² (squared) | Yes (heavily) | 0 |
| RMSE | Same as y | Yes | 0 |
| R² (R-squared) | Dimensionless | Moderate | 1 |
| MAPE | % | No | 0% |

- **R² = 1.0** → Model explains all variance (perfect fit)
- **R² = 0.0** → Model is no better than predicting the mean
- **R² < 0** → Model is worse than a horizontal mean line

---

### <span style="color:#2E86AB">2.6 Learning Curves</span>

> **Definition:** Learning curves plot training and validation performance (loss or accuracy) as a function of training set size or number of epochs. They are used to diagnose bias and variance problems.

| Curve Shape | Diagnosis | Action |
|:---|:---|:---|
| Both curves converge at high error | <span style="color:#C0392B">High Bias (Underfitting)</span> | More complex model, add features |
| Large gap between train and val | <span style="color:#C0392B">High Variance (Overfitting)</span> | More data, regularization |
| Both converge at low error | <span style="color:#27AE60">Good Fit</span> | Deploy |
| Val loss increases while train decreases | <span style="color:#C0392B">Overfitting developing</span> | Use early stopping |

---

## <span style="color:#1565C0">3. Hyperparameter Tuning</span>

### <span style="color:#2E86AB">3.1 Parameters vs Hyperparameters</span>

> **Definition:** Parameters are learned by the model during training (e.g., weights, biases). Hyperparameters are set by the user before training begins and control the learning process itself.

| Type | Examples | Who Sets It |
|:---|:---|:---|
| Model Parameters | Weights (w), Biases (b) | Learned during training |
| Hyperparameters | Learning rate, batch size, epochs, regularization strength (λ) | Set manually or by search |

---

### <span style="color:#2E86AB">3.2 Grid Search</span>

> **Definition:** Grid search exhaustively evaluates all possible combinations of a predefined set of hyperparameter values using cross-validation.

```
LR = [0.001, 0.01, 0.1]
Batch Size = [32, 64]
→ Evaluate all 3 × 2 = 6 combinations
→ Pick the combination with best validation score
```

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">Total Runs = |P₁| × |P₂| × ... × |Pₙ|</span>

</div>

- **Pros:** Thorough, reproducible, finds the global best within the grid
- **Cons:** Exponentially slow as number of hyperparameters grows (curse of dimensionality)

---

### <span style="color:#2E86AB">3.3 Random Search</span>

> **Definition:** Random search samples hyperparameter combinations randomly from specified distributions rather than a fixed grid. Often more efficient than grid search.

```
LR ~ Uniform(0.0001, 0.1)
Batch Size ~ Choice([16, 32, 64, 128])
→ Sample N random combinations
→ Evaluate each with cross-validation
→ Pick best
```

**Why it often beats Grid Search:** Not all hyperparameters matter equally. Random search explores more of the important dimensions in the same number of trials.

| Method | Coverage | Efficiency | Best For |
|:---|:---:|:---:|:---|
| Grid Search | Exhaustive | Low | ≤ 3 hyperparameters |
| Random Search | Random sampling | High | Many hyperparameters |

---

### <span style="color:#2E86AB">3.4 Bayesian Optimization</span>

> **Definition:** Bayesian optimization builds a probabilistic surrogate model (usually a Gaussian Process) of the objective function and uses it to intelligently choose the next hyperparameters to evaluate — balancing exploration and exploitation.

```
Step 1: Try a few random hyperparameter sets
Step 2: Build a surrogate model of performance landscape
Step 3: Use acquisition function to pick the most promising next point
Step 4: Evaluate, update surrogate model
Step 5: Repeat until budget exhausted
```

| Method | Uses Past Results | Sample Efficiency | Scales to High Dimensions |
|:---|:---:|:---:|:---:|
| Grid Search | No | Low | No |
| Random Search | No | Medium | Yes |
| Bayesian Optimization | Yes | High | Moderate |

Popular libraries: `Optuna`, `Hyperopt`, `scikit-optimize`, `Ray Tune`.

---

### <span style="color:#2E86AB">3.5 Common Hyperparameters by Model Type</span>

#### <span style="color:#5B8DB8">Neural Networks</span>

| Hyperparameter | Typical Range | Effect |
|:---|:---|:---|
| Learning rate | 1e-4 to 1e-1 | Speed and stability of convergence |
| Batch size | 16 – 512 | Gradient noise, memory use |
| Epochs | 10 – 1000 | Training duration |
| Number of layers | 1 – 100+ | Model capacity |
| Neurons per layer | 32 – 4096 | Layer representation power |
| Dropout rate | 0.1 – 0.5 | Regularization strength |
| L2 weight decay | 1e-5 to 1e-2 | Regularization |

#### <span style="color:#5B8DB8">Decision Trees & Ensembles</span>

| Hyperparameter | Effect |
|:---|:---|
| max_depth | Controls tree depth; deeper = more complex |
| n_estimators | Number of trees (Random Forest, XGBoost) |
| min_samples_split | Minimum samples to split a node |
| max_features | Features considered at each split |
| learning_rate (boosting) | Contribution of each tree |
| subsample | Fraction of data used per tree (boosting) |

#### <span style="color:#5B8DB8">SVM</span>

| Hyperparameter | Effect |
|:---|:---|
| C | Regularization; higher = less margin, more fit |
| gamma | Kernel coefficient; higher = closer points matter more |
| kernel | Linear, RBF, polynomial — affects decision boundary shape |

---

### <span style="color:#2E86AB">3.6 Early Stopping as Tuning</span>

> **Definition:** Early stopping monitors a validation metric during training and halts when it stops improving for a set number of epochs (patience). This is both a regularization technique and a tuning method for the `epochs` hyperparameter.

```
epoch 1:  val_loss = 0.85
epoch 10: val_loss = 0.42  (improving)
epoch 20: val_loss = 0.38  (improving)
epoch 30: val_loss = 0.39  (plateau begins)
epoch 35: val_loss = 0.41  (worsening - patience=5 hit)
→ STOP, restore weights from epoch 30
```

---

### <span style="color:#2E86AB">3.7 Model Checkpointing</span>

> **Definition:** Checkpointing saves the model's weights whenever a monitored metric improves. This ensures the best version of the model is always preserved, even if training continues or is interrupted.

```
if val_accuracy > best_val_accuracy:
    best_val_accuracy = val_accuracy
    save_model_weights(checkpoint_path)
```

---

### <span style="color:#2E86AB">3.8 Nested Cross-Validation</span>

> **Definition:** Nested cross-validation uses an outer loop for performance estimation and an inner loop for hyperparameter tuning, preventing information leakage from tuning into the evaluation.

```
Outer Loop (performance estimate): K-Fold
  └─ Inner Loop (hyperparameter search): K-Fold or RandomSearch
       └─ Best hyperparams on inner val
  └─ Evaluate on outer test fold with those hyperparams
Final Score = Mean of outer fold scores
```

---

## <span style="color:#1565C0">4. Advanced Training Concepts</span>

### <span style="color:#2E86AB">4.1 Transfer Learning</span>

> **Definition:** Transfer learning uses a model pre-trained on a large dataset as the starting point for a new task, rather than training from random initialization.

```
Pre-trained Model (on ImageNet)
→ Freeze early layers (learned general features)
→ Replace final layers
→ Fine-tune on your specific dataset
```

| Strategy | When to Use |
|:---|:---|
| Feature Extraction | Small dataset, similar domain |
| Full Fine-Tuning | Large dataset, different domain |
| Partial Fine-Tuning | Medium dataset, unfreeze last N layers |

---

### <span style="color:#2E86AB">4.2 Ensemble Methods</span>

> **Definition:** Ensemble methods combine multiple models to produce better predictions than any single model alone, leveraging diversity to reduce variance and/or bias.

#### <span style="color:#5B8DB8">Bagging (Bootstrap Aggregating)</span>

Train multiple models on different random subsamples of data (with replacement). Average (regression) or majority vote (classification) final predictions. Random Forest is the most famous bagging algorithm.

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">Final Prediction = (1/M) · Σ Model_m(x)</span>

</div>

#### <span style="color:#5B8DB8">Boosting</span>

Train models sequentially, each focusing on examples the previous model got wrong. Errors guide the next learner. Examples: AdaBoost, Gradient Boosting, XGBoost, LightGBM, CatBoost.

```
Model 1 → identifies errors → Model 2 focuses on those errors → Model 3 focuses further → ...
Final = weighted sum of all models
```

#### <span style="color:#5B8DB8">Stacking</span>

Train multiple base learners on the training data. Then train a meta-learner on their predictions as inputs.

```
[Base Model 1]    
[Base Model 2] → Predictions → [Meta-Learner] → Final Prediction
[Base Model 3]    
```

| Method | Reduces | How |
|:---|:---|:---|
| Bagging | Variance | Parallel diverse models |
| Boosting | Bias (and some variance) | Sequential error correction |
| Stacking | Both | Meta-learning from base models |

---

### <span style="color:#2E86AB">4.3 Class Imbalance Handling</span>

> **Definition:** Class imbalance occurs when one class has far more samples than another, causing models to be biased toward the majority class.

| Technique | Description |
|:---|:---|
| Oversampling (SMOTE) | Synthesize new minority class samples |
| Undersampling | Remove majority class samples |
| Class Weights | Penalize misclassifying the minority class more |
| Threshold Tuning | Adjust decision threshold from 0.5 to optimize recall |
| Ensemble Methods | Balanced Random Forest, EasyEnsemble |

---

### <span style="color:#2E86AB">4.4 Gradient Problems in Deep Networks</span>

#### <span style="color:#5B8DB8">Vanishing Gradient</span>

> **Definition:** In deep networks with sigmoid/tanh activations, gradients shrink exponentially during backpropagation through many layers, causing early layers to learn very slowly.

**Solutions:** ReLU activations, Batch Normalization, Residual connections (skip connections), LSTM/GRU for RNNs.

#### <span style="color:#5B8DB8">Exploding Gradient</span>

> **Definition:** Gradients grow exponentially, causing parameter updates to become extremely large, leading to numerical instability (NaN values).

**Solutions:** Gradient clipping (clip gradients by norm or value), careful weight initialization, Batch Normalization.

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">Gradient Clipping: g = g · (threshold / max(||g||, threshold))</span>

</div>

---

## <span style="color:#1565C0">5. Full Pipeline Summary</span>

### <span style="color:#2E86AB">5.1 Training → Evaluation → Tuning Workflow</span>

```
1. Split data → train / val / test
2. Choose initial hyperparameters
3. Train model on training set
4. Evaluate on validation set → compute metrics
5. Plot learning curves → diagnose bias/variance
6. Apply regularization if overfitting
7. Run hyperparameter search (Grid / Random / Bayesian)
8. Select best hyperparameters from validation performance
9. Retrain final model on train + val with best hyperparams
10. Evaluate ONCE on test set → report final performance
```

---

### <span style="color:#2E86AB">5.2 Cheat Sheet — Metric Selection</span>

| Problem Type | Primary Metric | Secondary Metric |
|:---|:---|:---|
| Binary Classification (balanced) | Accuracy, F1 | AUC-ROC |
| Binary Classification (imbalanced) | F1, AUC-PR | Recall or Precision |
| Multi-Class Classification | Weighted F1 | Confusion Matrix |
| Regression | RMSE | R², MAE |
| Ranking / Retrieval | AUC-ROC | Precision@K |
| Anomaly Detection | Recall, AUC-ROC | Precision |

---

### <span style="color:#2E86AB">5.3 Cheat Sheet — Overfitting Toolkit</span>

| Symptom | Root Cause | Fix |
|:---|:---|:---|
| High train acc, low val acc | Overfitting | Dropout, L1/L2, more data |
| Both train and val acc low | Underfitting | Larger model, more features, tune LR |
| Val loss spikes suddenly | LR too high | Reduce learning rate or use scheduler |
| Training is slow | LR too low | Increase LR or use warm-up |
| Loss goes to NaN | Exploding gradients | Gradient clipping, lower LR |
| Early layers not learning | Vanishing gradients | ReLU, BatchNorm, skip connections |

---

<div align="center">

<sub>Part of the complete ML Pipeline study series</sub>

`Problem Definition` → `Data Collection` → `Data Cleaning` → `EDA` → `Feature Engineering` → `Model Selection` → **`Training → Evaluation → Tuning`** → `Deployment` → `Monitoring`

</div>