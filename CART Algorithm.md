## Classification and Regression Tree (CART) Algorithm 

The Classification and Regression Tree (CART) algorithm is a versatile machine learning technique used for both classification and regression tasks. Developed by Breiman et al., it's a tree-building algorithm that constructs binary trees using the feature and threshold that yield the largest information gain at each node.

### Key Concepts

- **Binary Trees**: CART constructs binary trees, meaning each parent node splits into exactly two child nodes.
- **Splitting Criteria**: For classification tasks, splits are typically made by maximizing the Gini impurity decrease. For regression, the reduction in mean squared error (MSE) is often used.
- **Pruning**: To avoid overfitting, CART uses pruning techniques, which involve cutting back the tree after it has been created to improve its generalization to new data.

### Mathematical Formulation

#### Gini Impurity

Gini impurity is a measure of how often a randomly chosen element from the set would be incorrectly labeled if it was randomly labeled according to the distribution of labels in the subset. 
<br> The Gini impurity for a set of items is calculated as:

```math
\left( Gini = 1 - \sum_{i=1}^{J} p_i^2 \right)
```
where $p_i$ is the proportion of class $i$ elements in the set.

#### Mean Squared Error (MSE) for Regression

The mean squared error for a node is calculated as:

$$\ MSE = \frac{1}{N} \sum_{i=1}^{N} (y_i - \hat{y})^2 \$$

where $y_i$ is the actual value, $\hat{y}$ is the predicted value (mean of the node's values), and  $N$ is the number of observations in the node.


### How It Works

1. **Starting at the root**, the algorithm selects the split that results in the most homogeneous sub-nodes according to the target variable, using measures like Gini impurity for classification or variance reduction for regression.
2. **Recursively splitting**: This process continues for each derived sub-node until a stopping criterion is met (e.g., when no further information gain is possible or when the node reaches a minimum size).
3. **Pruning the tree**: After the tree is fully grown, it might be pruned back to prevent overfitting, typically using a cost-complexity pruning method where a smaller tree is sought that achieves similar performance.

### Example

Consider a dataset with two features (X1 and X2) and a binary target. The steps might be:

- The root node examines all possible splits and selects the split at `X1 < 2.5` as it maximally reduces impurity.
- The left child node (where `X1 < 2.5` is true) might split again, say on `X2 < 3.0`.
- This process continues until the stopping criteria are met.

In practice, this might look like:

```
Root Node
├── (X1 < 2.5)
│   ├── (X2 < 3.0) -> Class 0
│   └── (X2 >= 3.0) -> Class 1
└── (X1 >= 2.5)
    └── Class 1
```

### Advantages and Limitations

**Advantages**:
- **Simple to understand and interpret**.
- **Can handle both numerical and categorical data**.
- **Non-parametric**, meaning it does not assume a particular distribution of the data.

**Limitations**:
- Prone to overfitting, especially with very deep trees.
- Sensitive to small changes in the data, which can lead to vastly different tree structures.


