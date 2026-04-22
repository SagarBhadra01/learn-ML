<div align="center">

# <span style="color:#0A2FA8">Types of Machine Learning</span>

<sub>Supervised · Unsupervised · Semi-Supervised · Reinforcement · Self-Supervised Learning</sub>

</div>

---

## <span style="color:#1565C0">Overview - Why Are There Different Types?</span>

> **Definition:** The "type" of Machine Learning refers to the learning paradigm - the fundamental way a model learns from data based on what kind of data is available and what kind of feedback the model receives during training.

Different real-world problems come with different kinds of data. Sometimes you have millions of labeled examples. Sometimes you have no labels at all. Sometimes you have an agent that must learn by trial and error. Each of these scenarios requires a completely different approach to learning.

```
Is your data labeled?
├── Yes, fully labeled                  → Supervised Learning
├── No labels at all                    → Unsupervised Learning
├── Small labeled + large unlabeled     → Semi-Supervised Learning
├── Labels from interaction/reward      → Reinforcement Learning
└── Labels generated from the data itself → Self-Supervised Learning
```

---

## <span style="color:#1565C0">1. Supervised Learning</span>

> **Definition:** Supervised Learning is a type of ML where the model is trained on a labeled dataset - meaning every input example has a corresponding correct output (label). The model learns the mapping from input to output by minimizing the difference between its predictions and the known correct answers.

The word "supervised" comes from the idea that the training process is supervised by the correct answers - the model is constantly told whether it was right or wrong.

```
Input (X) + Correct Label (Y)  →  Model learns f(X) ≈ Y  →  Predict Y for new X
```

---

### <span style="color:#2E86AB">1.1 How Supervised Learning Works</span>

```
Step 1: Collect labeled data   → { (X₁,Y₁), (X₂,Y₂), ..., (Xₙ,Yₙ) }
Step 2: Feed data to model     → Model makes prediction Ŷ
Step 3: Calculate loss         → Error = difference between Ŷ and Y
Step 4: Update model           → Adjust parameters to reduce error
Step 5: Repeat                 → Until model converges on the best parameters
Step 6: Predict on new data    → f(X_new) → Ŷ_new
```

---

### <span style="color:#2E86AB">1.2 Two Sub-types of Supervised Learning</span>

#### <span style="color:#5B8DB8">Classification</span>

> **Definition:** The output is a discrete category (class label). The model learns to assign each input to one of a fixed set of categories.

| Type | Description | Example |
|:---|:---|:---|
| Binary Classification | Only 2 possible output classes | Spam or Not Spam, Disease or No Disease |
| Multi-class Classification | 3 or more possible output classes | Digit recognition (0–9), Flower species |
| Multi-label Classification | Each input can belong to multiple classes at once | A news article tagged as both "Sports" and "Finance" |

**Common Classification Algorithms:**

| Algorithm | Best for |
|:---|:---|
| Logistic Regression | Linear decision boundaries, interpretable output |
| Decision Tree | Non-linear, interpretable, small datasets |
| Random Forest | General purpose, robust, handles missing data |
| SVM (Support Vector Machine) | High-dimensional data, clear margin separation |
| K-Nearest Neighbors (KNN) | Small datasets, non-linear boundaries |
| Naive Bayes | Text classification, fast training |
| Gradient Boosting / XGBoost | Tabular data, competitions, high accuracy |
| Neural Networks | Complex patterns, image/text/audio |

**Evaluation Metrics for Classification:** Accuracy, Precision, Recall, F1 Score, ROC-AUC, Confusion Matrix

---

#### <span style="color:#5B8DB8">Regression</span>

> **Definition:** The output is a continuous numerical value. The model learns to predict a quantity rather than a category.

| Type | Description | Example |
|:---|:---|:---|
| Simple Regression | One input feature predicts one output | Height predicts weight |
| Multiple Regression | Many input features predict one output | Area + location + age predicts house price |
| Polynomial Regression | Non-linear relationship between input and output | Growth curves, physical simulations |
| Time-Series Regression | Output depends on past values over time | Stock price forecasting, weather prediction |

**Common Regression Algorithms:**

| Algorithm | Best for |
|:---|:---|
| Linear Regression | Linear relationships, interpretable |
| Ridge / Lasso Regression | When regularization is needed |
| Decision Tree Regressor | Non-linear relationships |
| Random Forest Regressor | General purpose regression |
| SVR (Support Vector Regression) | Non-linear, small to medium datasets |
| Gradient Boosting Regressor | High accuracy on tabular data |
| Neural Networks | Complex non-linear regression |

**Evaluation Metrics for Regression:** MAE, MSE, RMSE, R²

---

### <span style="color:#2E86AB">1.3 Key Characteristics of Supervised Learning</span>

| Property | Detail |
|:---|:---|
| Data requirement | Labeled data required - expensive and time-consuming to obtain |
| Output | A specific prediction (class or number) |
| Learning signal | Direct - model is explicitly told the correct answer |
| Use case | When you know exactly what you want to predict |
| Risk | Requires high-quality labels - noisy labels hurt performance |

---

### <span style="color:#2E86AB">1.4 Real-World Examples</span>

| Application | Input (X) | Output (Y) | Type |
|:---|:---|:---|:---|
| Email spam filter | Email text, metadata | Spam / Not Spam | Classification |
| House price prediction | Area, location, rooms | Price in INR | Regression |
| Medical diagnosis | Patient symptoms, test results | Disease / No Disease | Classification |
| Credit scoring | Transaction history, income | Default risk score | Regression |
| Sentiment analysis | Review text | Positive / Negative / Neutral | Classification |
| Sales forecasting | Past sales, seasonality | Next month's sales | Regression |

---

### <span style="color:#2E86AB">1.5 Advantages and Disadvantages</span>

| <span style="color:#27AE60">Advantages</span> | <span style="color:#C0392B">Disadvantages</span> |
|:---|:---|
| Clear objective - well-defined loss to minimize | Requires large amounts of labeled data |
| High accuracy when labels are good | Labeling data is expensive and time-consuming |
| Easy to evaluate performance objectively | Cannot learn beyond what is in the training labels |
| Well-understood algorithms and theory | Sensitive to noisy, incorrect, or biased labels |
| Widely applicable across industries | May not generalize to data very different from training data |

---

## <span style="color:#1565C0">2. Unsupervised Learning</span>

> **Definition:** Unsupervised Learning is a type of ML where the model is trained on data that has no labels. The model must discover hidden patterns, structures, or groupings in the data entirely on its own - with no guidance on what the correct output should be.

There is no "supervisor" telling the model if it is right or wrong. The model finds structure by itself.

```
Input (X) only - no Y labels  →  Model finds hidden patterns  →  Groups / Structures / Representations
```

---

### <span style="color:#2E86AB">2.1 Sub-types of Unsupervised Learning</span>

#### <span style="color:#5B8DB8">Clustering</span>

> **Definition:** Clustering is the task of grouping similar data points together into clusters, where points within a cluster are more similar to each other than to points in other clusters.

```
Unlabeled data points  →  Algorithm groups similar ones  →  Clusters with no pre-defined labels
```

| Algorithm | How it works | Best for |
|:---|:---|:---|
| K-Means | Assigns points to K centroids, iteratively updates centroids | Large datasets, spherical clusters |
| Hierarchical Clustering | Builds a tree (dendrogram) by merging/splitting clusters | When you don't know K, small datasets |
| DBSCAN | Groups densely packed points, marks sparse points as noise | Irregular shapes, handling outliers |
| Gaussian Mixture Models | Probabilistic - assumes data comes from K Gaussian distributions | Soft/overlapping clusters |
| Mean Shift | Finds dense regions by shifting points toward high-density areas | Unknown number of clusters |

**Real-world examples of clustering:**
- Customer segmentation (group customers by buying behavior)
- Document grouping (organize news articles by topic)
- Gene expression analysis (group genes with similar behavior)
- Anomaly detection (points that don't fit any cluster are anomalies)

---

#### <span style="color:#5B8DB8">Dimensionality Reduction</span>

> **Definition:** Dimensionality reduction compresses data from a high-dimensional space into a lower-dimensional representation while retaining as much useful information as possible.

Used when datasets have hundreds or thousands of features - known as the **curse of dimensionality**.

| Algorithm | Type | Description |
|:---|:---|:---|
| PCA (Principal Component Analysis) | Linear | Projects onto directions of maximum variance |
| t-SNE | Non-linear | Preserves local structure - used for 2D/3D visualization |
| UMAP | Non-linear | Faster than t-SNE, preserves both local and global structure |
| LDA (Linear Discriminant Analysis) | Linear | Maximizes class separation (also used in supervised settings) |
| Autoencoders | Deep Learning | Encoder-decoder neural network that learns compressed representations |
| ICA (Independent Component Analysis) | Linear | Separates a signal into independent components |

**Real-world examples:**
- Visualizing high-dimensional image data in 2D
- Compressing features before feeding into another model
- Face recognition (reduce 1000-pixel image to 50 key features)
- Noise removal in signals

---

#### <span style="color:#5B8DB8">Association Rule Learning</span>

> **Definition:** Association rule learning finds interesting relationships or co-occurrence patterns between variables in large datasets.

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">Rule format: If {A} → Then {B} &nbsp;|&nbsp; e.g. If {bread, butter} → {milk}</span>

</div>

| Metric | Definition | Formula |
|:---|:---|:---|
| Support | How often the items appear together | P(A ∩ B) |
| Confidence | How often the rule is correct | P(B \| A) = P(A ∩ B) / P(A) |
| Lift | How much better the rule is vs random chance | Confidence / P(B) |

**Algorithms:** Apriori, FP-Growth, Eclat

**Real-world examples:**
- Market basket analysis ("Customers who bought X also bought Y")
- Recommendation engines
- Medical co-diagnosis (patients with condition A often also have B)
- Web clickstream analysis

---

#### <span style="color:#5B8DB8">Anomaly Detection (Unsupervised)</span>

> **Definition:** Anomaly detection identifies data points that are significantly different from the rest of the data - without any labeled examples of what an anomaly looks like.

| Algorithm | How it works |
|:---|:---|
| Isolation Forest | Anomalies are easier to isolate with random splits - shorter path = anomaly |
| Local Outlier Factor (LOF) | Compares local density of a point to its neighbors |
| One-Class SVM | Learns a boundary around normal data - anything outside is anomaly |
| DBSCAN | Points not assigned to any cluster are treated as anomalies |
| Autoencoder | High reconstruction error = anomaly |

**Real-world examples:** Network intrusion detection, fraud detection, manufacturing defect detection

---

#### <span style="color:#5B8DB8">Density Estimation</span>

> **Definition:** Density estimation models the underlying probability distribution of the data - understanding where data points are likely to come from.

**Algorithms:** Kernel Density Estimation (KDE), Gaussian Mixture Models (GMM)

**Real-world examples:** Generating synthetic data, anomaly detection, understanding data distributions

---

### <span style="color:#2E86AB">2.2 Key Characteristics of Unsupervised Learning</span>

| Property | Detail |
|:---|:---|
| Data requirement | No labels needed - works on raw data |
| Output | Clusters, reduced representations, rules, or distributions |
| Learning signal | None - model finds its own structure |
| Use case | Exploring unknown data, finding hidden patterns |
| Challenge | Hard to evaluate - no ground truth to measure against |

---

### <span style="color:#2E86AB">2.3 Advantages and Disadvantages</span>

| <span style="color:#27AE60">Advantages</span> | <span style="color:#C0392B">Disadvantages</span> |
|:---|:---|
| No labeling cost - works on raw data | No objective measure of success |
| Discovers unexpected hidden patterns | Results can be ambiguous or hard to interpret |
| Can process massive unlabeled datasets | Algorithms are sensitive to data scaling and parameters |
| Foundation for exploratory data analysis | Difficult to validate - no ground truth |
| Useful as preprocessing for supervised learning | Clustering results can vary run to run (e.g., K-Means) |

---

## <span style="color:#1565C0">3. Semi-Supervised Learning</span>

> **Definition:** Semi-Supervised Learning is a hybrid approach that uses a small amount of labeled data combined with a large amount of unlabeled data during training. The model leverages the structure in the unlabeled data to improve its performance beyond what the labeled data alone could achieve.

This is the most practical paradigm for many real-world applications because labeled data is expensive while unlabeled data is abundant.

```
Small labeled set (L) + Large unlabeled set (U)  →  Model learns from both  →  Better generalization
```

---

### <span style="color:#2E86AB">3.1 The Core Problem It Solves</span>

| Scenario | Problem |
|:---|:---|
| Fully Supervised | Need thousands of expensive human-labeled examples |
| Fully Unsupervised | No guidance - results may not align with the task |
| Semi-Supervised | Use a small labeled set for direction + vast unlabeled data for structure |

**Analogy:** Imagine learning to identify birds. You have 50 labeled photos (bird species identified) and 50,000 unlabeled photos. Semi-supervised learning uses all 50,050 photos - the 50 give it the concept of bird species, and the 50,000 help it learn what birds look like in general.

---

### <span style="color:#2E86AB">3.2 Core Assumptions</span>

Semi-supervised learning works because of three key assumptions about the data:

| Assumption | Meaning |
|:---|:---|
| Smoothness Assumption | If two points are close in input space, their labels should be the same |
| Cluster Assumption | Data naturally clusters, and points in the same cluster share a label |
| Manifold Assumption | High-dimensional data lies on a lower-dimensional manifold - unlabeled data helps find that manifold |

---

### <span style="color:#2E86AB">3.3 Techniques in Semi-Supervised Learning</span>

#### <span style="color:#5B8DB8">Self-Training (Pseudo-Labeling)</span>

```
Train on labeled data (L)
    ↓
Predict on unlabeled data (U)
    ↓
Add high-confidence predictions as new labels (pseudo-labels)
    ↓
Retrain on L + pseudo-labeled U
    ↓
Repeat until convergence
```

> **Risk:** If the model makes wrong pseudo-labels with high confidence, errors can propagate and compound - called confirmation bias.

---

#### <span style="color:#5B8DB8">Label Propagation</span>

> Spreads labels from labeled points to unlabeled points through a similarity graph - nearby points receive similar labels.

```
Build a graph where edges connect similar data points
    ↓
Labeled nodes "propagate" their labels to unlabeled neighbors
    ↓
Unlabeled points receive soft label scores from their neighbors
```

---

#### <span style="color:#5B8DB8">Co-Training</span>

> Trains two separate models on two different "views" of the data. Each model labels examples for the other.

**Example:** A web page classifier - one model uses the page content, another uses the hyperlinks pointing to it. Each labels unlabeled examples for the other.

---

#### <span style="color:#5B8DB8">Consistency Regularization</span>

> The model should produce the same prediction for a data point regardless of small perturbations or augmentations applied to it.

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">Loss = Supervised Loss (on L) + λ × Consistency Loss (on U)</span>

</div>

**Methods using this:** MixMatch, FixMatch, UDA (Unsupervised Data Augmentation)

---

#### <span style="color:#5B8DB8">Generative Models</span>

> Generative models (like VAEs and GANs) learn the distribution of the data. They can then generate new labeled examples or use the learned distribution to improve classification.

---

### <span style="color:#2E86AB">3.4 Real-World Examples</span>

| Domain | Labeled data | Unlabeled data | Application |
|:---|:---|:---|:---|
| Medical imaging | Few labeled scans (expensive to annotate) | Millions of unlabeled scans | Disease detection |
| NLP / Text | Few labeled documents | Billions of sentences on the internet | Text classification |
| Speech recognition | Some transcribed audio | Huge raw audio recordings | Voice assistant training |
| Web content | Few labeled pages | Millions of unlabeled web pages | Topic classification |

---

### <span style="color:#2E86AB">3.5 Advantages and Disadvantages</span>

| <span style="color:#27AE60">Advantages</span> | <span style="color:#C0392B">Disadvantages</span> |
|:---|:---|
| Reduces labeling cost dramatically | If labeled data has noise, errors amplify during training |
| Better performance than supervised with tiny labeled set | More complex to implement than pure supervised |
| Leverages the abundance of real-world unlabeled data | Requires careful assumption validation |
| Foundation of modern large-scale ML systems | Pseudo-label errors can cascade (confirmation bias) |

---

## <span style="color:#1565C0">4. Reinforcement Learning</span>

> **Definition:** Reinforcement Learning (RL) is a type of ML where an agent learns to make sequential decisions by interacting with an environment. The agent receives feedback in the form of rewards or penalties based on its actions, and its goal is to learn a policy that maximizes cumulative reward over time.

RL is fundamentally different from supervised and unsupervised learning - there is no fixed dataset. The data is generated through the agent's own interactions with the environment.

```
Agent observes State (S)  →  Takes Action (A)  →  Receives Reward (R) + New State (S')  →  Learns better policy  →  Repeat
```

---

### <span style="color:#2E86AB">4.1 Core Components of Reinforcement Learning</span>

> **Agent:** The learner or decision-maker. The entity that takes actions.

> **Environment:** Everything the agent interacts with. It responds to the agent's actions and provides new states and rewards.

> **State (S):** The current situation or observation that the agent perceives from the environment at a given time step.

> **Action (A):** A decision or move the agent can take in a given state.

> **Reward (R):** A scalar feedback signal from the environment after the agent takes an action. Positive reward = good action, Negative reward = bad action.

> **Policy (π):** The agent's strategy - a mapping from states to actions. This is what the agent is trying to learn.

> **Value Function (V):** Estimates the long-term expected reward from a given state - how good it is to be in that state.

> **Q-Function (Q):** Estimates the expected reward for taking a specific action in a specific state - Q(s, a).

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">Goal: Learn policy π* that maximizes: G = R₁ + γR₂ + γ²R₃ + ... (discounted cumulative reward)</span>

</div>

where γ (gamma) is the **discount factor** - a value between 0 and 1 that controls how much the agent values future rewards vs immediate rewards.

| γ value | Behavior |
|:---:|:---|
| γ = 0 | Agent is completely short-sighted - only cares about immediate reward |
| γ = 1 | Agent values all future rewards equally - fully far-sighted |
| γ ≈ 0.9 | Typical setting - balances short-term and long-term rewards |

---

### <span style="color:#2E86AB">4.2 The RL Loop</span>

```
┌─────────────────────────────────────────────────┐
│                                                 │
│   Agent  ──── Action (A) ────►  Environment     │
│     ▲                               │           │
│     │                               │           │
│   State (S) + Reward (R)  ◄─────────┘           │
│                                                 │
└─────────────────────────────────────────────────┘

At each time step:
1. Agent observes current state S
2. Agent selects action A using its policy π
3. Environment transitions to new state S'
4. Environment returns reward R
5. Agent updates its policy based on (S, A, R, S')
6. Repeat
```

---

### <span style="color:#2E86AB">4.3 Exploration vs Exploitation</span>

> One of the most fundamental challenges in RL - the agent must balance:

| Strategy | Description |
|:---|:---|
| Exploration | Try new, unknown actions to discover better strategies |
| Exploitation | Use the best known action to maximize immediate reward |

> **Too much exploitation** → Agent gets stuck in a local optimum (never finds better strategies)
> **Too much exploration** → Agent wastes time on bad actions and never performs well

**ε-greedy strategy:** With probability ε, take a random action (explore). With probability 1−ε, take the best known action (exploit). ε is gradually reduced over time.

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">ε-greedy: Action = random with prob ε &nbsp;|&nbsp; best known action with prob (1 − ε)</span>

</div>

---

### <span style="color:#2E86AB">4.4 Types of RL Algorithms</span>

#### <span style="color:#5B8DB8">Model-Free vs Model-Based</span>

| Type | Description | Example |
|:---|:---|:---|
| Model-Free | Agent learns from direct experience - no model of the environment | Q-Learning, PPO |
| Model-Based | Agent builds an internal model of the environment to plan ahead | AlphaZero, Dyna-Q |

#### <span style="color:#5B8DB8">Value-Based Methods</span>

> Learn the value function V(s) or Q(s,a) and derive policy from it.

| Algorithm | Description |
|:---|:---|
| Q-Learning | Off-policy - learns Q-values using the Bellman equation |
| SARSA | On-policy - updates Q-values based on the action actually taken |
| DQN (Deep Q-Network) | Q-Learning with a neural network as the Q-function approximator |

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">Bellman Equation: Q(s,a) = R + γ × max Q(s', a')</span>

</div>

#### <span style="color:#5B8DB8">Policy-Based Methods</span>

> Directly optimize the policy π without computing value functions.

| Algorithm | Description |
|:---|:---|
| REINFORCE | Monte Carlo policy gradient - updates after complete episode |
| PPO (Proximal Policy Optimization) | Stable, widely used - clips updates to prevent large policy changes |
| A3C / A2C | Asynchronous / Advantage Actor-Critic - parallel training |

#### <span style="color:#5B8DB8">Actor-Critic Methods</span>

> Combine value-based (Critic evaluates) and policy-based (Actor decides action).

| Algorithm | Description |
|:---|:---|
| A2C / A3C | Advantage Actor-Critic - stable and fast |
| SAC (Soft Actor-Critic) | Maximizes reward + entropy - encourages exploration |
| TD3 | Twin Delayed DDPG - reduces overestimation in continuous action spaces |

---

### <span style="color:#2E86AB">4.5 Real-World Applications of RL</span>

| Domain | Application |
|:---|:---|
| Games | AlphaGo, AlphaZero, OpenAI Five (Dota 2), Atari game playing |
| Robotics | Robot arm control, locomotion, manipulation tasks |
| Autonomous vehicles | Lane keeping, collision avoidance, parking |
| Finance | Algorithmic trading, portfolio optimization |
| Healthcare | Personalized drug dosing, clinical trial design |
| NLP | RLHF - training ChatGPT/Claude using human feedback |
| Data center optimization | Google used RL to reduce cooling energy by 40% |
| Recommendation systems | Optimizing long-term user engagement |

---

### <span style="color:#2E86AB">4.6 Advantages and Disadvantages</span>

| <span style="color:#27AE60">Advantages</span> | <span style="color:#C0392B">Disadvantages</span> |
|:---|:---|
| Can solve sequential decision-making problems | Extremely data-hungry - requires millions of interactions |
| Learns from interaction - no labeled dataset needed | Training is unstable and hard to reproduce |
| Can discover superhuman strategies (AlphaGo) | Reward function design is difficult and critical |
| Works in dynamic, changing environments | Very slow training - computationally expensive |
| Foundation of modern AI systems (LLM alignment via RLHF) | Exploration in real world is dangerous (robotics, autonomous vehicles) |

---

## <span style="color:#1565C0">5. Self-Supervised Learning</span>

> **Definition:** Self-Supervised Learning (SSL) is a learning paradigm where the model generates its own supervisory signal from the raw, unlabeled data itself - by creating a pretext task whose labels are derived automatically from the data structure.

Self-supervised learning sits at the intersection of supervised and unsupervised learning. It is technically supervised (uses labeled training pairs) but the labels are not human-annotated - they come from the data itself.

```
Unlabeled raw data  →  Automatically generate (Input, Label) pairs from data structure  →  Train supervised  →  Rich representations
```

---

### <span style="color:#2E86AB">5.1 The Core Idea - Pretext Tasks</span>

> **Definition:** A pretext task is a self-defined supervised task created from unlabeled data where the "labels" are generated automatically from the data itself. Solving the pretext task forces the model to learn useful, general representations of the data.

The pretext task is not the final goal - it is a training vehicle. After training on the pretext task, the learned representations are transferred to the actual downstream task (fine-tuning).

```
Pretext Task (self-generated labels)
    ↓
Model learns rich representations of data
    ↓
Transfer representations to Downstream Task (fine-tune with small labeled set)
```

---

### <span style="color:#2E86AB">5.2 Examples of Pretext Tasks</span>

#### <span style="color:#5B8DB8">For Text (NLP)</span>

| Pretext Task | How labels are created | Model trained |
|:---|:---|:---|
| Masked Language Modeling (MLM) | Randomly mask 15% of words - predict masked words | BERT |
| Next Sentence Prediction (NSP) | Predict whether two sentences are consecutive | BERT |
| Causal Language Modeling (CLM) | Predict the next word given all previous words | GPT series |
| Sentence order prediction | Predict if two sentences are in the correct order | ALBERT |

#### <span style="color:#5B8DB8">For Images (Computer Vision)</span>

| Pretext Task | How labels are created | Model |
|:---|:---|:---|
| Image rotation prediction | Rotate image by 0°, 90°, 180°, 270° - predict the rotation angle | RotNet |
| Jigsaw puzzle solving | Shuffle image patches - predict correct arrangement | Jigsaw CNN |
| Colorization | Convert to grayscale - predict original colors | Colorization Net |
| Image inpainting | Mask a region of image - predict the missing region | Context Encoders |
| Contrastive learning | Two augmented views of the same image should have similar embeddings | SimCLR, MoCo |

#### <span style="color:#5B8DB8">For Audio / Video</span>

| Pretext Task | Description |
|:---|:---|
| Temporal order prediction | Predict whether video frames are in the correct time order |
| Audio-visual correspondence | Predict whether an audio clip matches a video frame |
| Masked spectrogram prediction | Mask parts of audio spectrogram and predict them (Audio MAE) |

---

### <span style="color:#2E86AB">5.3 Contrastive Learning - The Most Important SSL Technique</span>

> **Definition:** Contrastive learning trains the model to produce similar representations for different views (augmentations) of the same data point, and dissimilar representations for different data points.

```
Image X  →  Augmentation 1 (crop, flip, color jitter)  →  View 1
Image X  →  Augmentation 2 (different crop, blur)       →  View 2

Goal: Embedding of View 1 ≈ Embedding of View 2  (positive pair - same image)
      Embedding of View 1 ≠ Embedding of View 3  (negative pair - different image)
```

<div align="center" style="border: 2px solid #D4A017; border-radius: 8px; padding: 14px 24px; margin: 12px auto; max-width: 480px;">

### <span style="color:#D4A017">Contrastive Loss: L = − log [ exp(sim(z₁,z₂)/τ) / Σ exp(sim(z₁,zₖ)/τ) ]</span>

</div>

where `sim` is cosine similarity and `τ` (tau) is a temperature hyperparameter.

**Key Contrastive Learning frameworks:**

| Framework | Key contribution |
|:---|:---|
| SimCLR | Simple contrastive learning - two augmentations + projection head + NT-Xent loss |
| MoCo (Momentum Contrast) | Maintains a queue of negative samples - memory efficient |
| BYOL | No negative pairs needed - uses a momentum encoder |
| SimSiam | No negative pairs, no momentum encoder - simpler architecture |
| CLIP | Contrastive learning between image and text pairs |

---

### <span style="color:#2E86AB">5.4 Foundation Models and SSL</span>

> Self-supervised learning is the engine behind every major foundation model in AI today.

| Model | Modality | SSL Technique |
|:---|:---|:---|
| BERT | Text | Masked Language Modeling |
| GPT-2 / GPT-3 / GPT-4 | Text | Causal Language Modeling |
| RoBERTa | Text | Improved MLM training |
| MAE (Masked Autoencoder) | Images | Mask 75% of image patches, reconstruct them |
| DINO / DINOv2 | Images | Self-distillation with no labels |
| wav2vec 2.0 | Audio | Masked speech prediction |
| CLIP | Image + Text | Contrastive image-text matching |

The standard workflow for modern AI:

```
Self-Supervised Pretraining (on massive unlabeled data)
    ↓
Fine-tuning on downstream task (with small labeled dataset)
    ↓
High performance with minimal labeled data
```

---

### <span style="color:#2E86AB">5.5 SSL vs Semi-Supervised Learning</span>

These two are often confused. The distinction is important:

| Aspect | Semi-Supervised Learning | Self-Supervised Learning |
|:---|:---|:---|
| Labeled data used? | Yes - a small labeled set guides learning | No - labels are auto-generated from data |
| Human annotation needed? | Yes - for the small labeled set | No - zero human labels at pretraining |
| Goal | Improve a specific task using unlabeled data | Learn general representations for transfer |
| Typical workflow | Labeled + unlabeled → train together | Pretrain on pretext task → fine-tune downstream |
| Examples | FixMatch, Label Propagation | BERT, GPT, SimCLR, MAE |

---

### <span style="color:#2E86AB">5.6 Advantages and Disadvantages</span>

| <span style="color:#27AE60">Advantages</span> | <span style="color:#C0392B">Disadvantages</span> |
|:---|:---|
| No human labeling needed at pretraining | Pretext task design requires expertise |
| Scales to billions of unlabeled data points | Training is computationally very expensive |
| Learns rich, transferable representations | Quality depends heavily on augmentation/pretext task choice |
| Powers the most capable AI models today | Fine-tuning still requires some labeled data |
| Generalizes well to many downstream tasks | Representations may capture pretext-task-specific features, not task-relevant ones |

---

## <span style="color:#1565C0">Complete Comparison - All 5 Types of ML</span>

| Aspect | Supervised | Unsupervised | Semi-Supervised | Reinforcement | Self-Supervised |
|:---|:---:|:---:|:---:|:---:|:---:|
| Labeled data | Required (all) | None | Small amount | None (rewards) | Auto-generated |
| Human annotation | Yes | No | Minimal | No | No |
| Output | Prediction | Structure | Prediction | Policy | Representations |
| Feedback type | Direct label | None | Partial label | Reward signal | Reconstruction error |
| Data efficiency | Low | High | Medium-High | Very Low | High |
| Typical use | Classification, Regression | Clustering, Compression | Low-label scenarios | Sequential decisions | Pretraining |
| Complexity | Low-Medium | Medium | Medium-High | Very High | High |
| Example algorithms | Random Forest, SVM, XGBoost | K-Means, PCA, DBSCAN | FixMatch, Label Propagation | DQN, PPO, SAC | BERT, GPT, SimCLR |
| Real-world example | Spam filter, Price prediction | Customer segmentation | Medical imaging | AlphaGo, ChatGPT RLHF | BERT, GPT models |

---

## <span style="color:#1565C0">Choosing the Right Paradigm - Decision Guide</span>

```
Do you have labeled data?
├── Yes, fully labeled
│     ├── Predict a number?     → Supervised Regression
│     └── Predict a category?   → Supervised Classification
│
├── No labels at all
│     ├── Find groups?          → Unsupervised Clustering
│     ├── Reduce features?      → Unsupervised Dimensionality Reduction
│     ├── Find rules/patterns?  → Association Rule Learning
│     └── Pretrain for later?   → Self-Supervised Learning
│
├── Small labeled + large unlabeled
│     └── Improve with unlabeled data?  → Semi-Supervised Learning
│
└── No labels, but can define a reward
      └── Sequential decisions?        → Reinforcement Learning
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

