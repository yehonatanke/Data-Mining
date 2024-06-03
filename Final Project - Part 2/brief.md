# Thyroid Function Classification using Machine Learning

This project explores the application of various machine learning techniques for classifying thyroid function based on medical data. The main objective is to predict and categorize patients into three groups: healthy, hyperthyroid, and hypothyroid.

## Project Overview

The project consists of three main parts:

1. **Thyroid Function Classification using Data Mining Techniques (MM"N 21)**
   - Data preprocessing and handling of problematic values
   - Application of CART and C4.5 algorithms for classification
   - Analysis of results and comparison of algorithm performance

2. **Thyroid Function Classification using Cluster Analysis (MM"N 22)**
   - Use of K-Means algorithm for cluster analysis
   - Identification of patient groups with similar symptoms and characteristics
   - Evaluation of clustering results and model accuracy

3. **Thyroid Function Classification using Artificial Neural Network (ANN)**
   - Design and architecture of a Multilayer Perceptron (MLP) network
   - Training and optimization of the neural network
   - Performance evaluation and analysis of misclassified cases

## Results and Comparison

- **Classification Accuracy:**
  - CART: 89.86%
  - C4.5: 90.27%
  - K-Means: 74.07%
  - MLP: 95.45%

- **Kappa Statistic:**
  - CART: 0.5455
  - C4.5: 0.5801
  - MLP: 0.5931

- **Model Complexity:**
  - CART and C4.5: Less complex decision trees
  - K-Means: Requires predetermining the number of clusters
  - MLP: Most complex model with two hidden layers

The MLP achieved the highest classification accuracy and Kappa statistic, outperforming the decision tree algorithms and cluster analysis. However, it was also the most complex model and required more computational resources.

## Conclusions and Future Work

The project demonstrates the potential of machine learning techniques, particularly artificial neural networks, in classifying thyroid function based on medical data. The MLP achieved the best performance, but all models struggled with classifying minority classes, highlighting the need for improved feature representation and class balancing.

Future work could include:
- Collecting more data samples from minority classes for better representation
- Exploring techniques for class balancing, such as oversampling or undersampling
- Investigating additional features or feature engineering methods
- Experimenting with alternative network architectures or algorithms

The project provides valuable insights into the application of machine learning in medical diagnosis and lays the foundation for further research and development in this domain.

