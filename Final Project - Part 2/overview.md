## Thyroid Prediction Models Analysis

### Overview
This project analyzes various prediction models for thyroid conditions using different clustering and classification algorithms. The primary focus is on distinguishing between healthy individuals and those with hyperthyroid or hypothyroid conditions.

### Clustering Algorithms
- **K-Means Clustering**: Groups the data into three clusters representing healthy, hyperthyroid, and hypothyroid individuals. The number of clusters (K) is set to 3. Key attributes such as TSH, TT4, T4U, and FTI are used for clustering.
- **DBSCAN Clustering**: Density-Based Spatial Clustering of Applications with Noise (DBSCAN) identifies clusters based on the density of data points, helping in distinguishing outliers and forming clusters without specifying the number of clusters in advance【5:0†source】.

### Artificial Neural Network (ANN)
- **Multilayer Perceptron (MLP)**: An MLP with three hidden layers was used to classify thyroid conditions. The network includes 21 neurons in the input layer, 10 neurons in each hidden layer, and 3 neurons in the output layer representing hypothyroid, hyperthyroid, and healthy conditions【5:2†source】.
- **Activation Function**: Sigmoid activation function is used in the hidden layers to introduce non-linearity【5:7†source】.
- **Training**: The network was trained using backpropagation and gradient descent, optimizing the Mean Squared Error (MSE) loss function over 500 epochs【5:9†source】【5:12†source】.

### Data and Methodology
- **Data**: The dataset contains 9,172 records with features including TSH, TT4, T3, T4U, and FTI levels.
- **Preprocessing**: The data is normalized, and missing values are handled appropriately to ensure the clustering algorithms perform optimally.
- **Feature Selection**: Key features are selected based on their relevance to thyroid conditions, and their distribution is analyzed to understand their impact on clustering.

### Results
- **K-Means Clustering**: Successfully grouped the data into three clusters with a clear distinction between healthy, hyperthyroid, and hypothyroid individuals【5:6†source】.
- **DBSCAN Clustering**: Identified clusters based on the density of the data points, effectively handling noise and outliers【5:4†source】.
- **ANN Classification**: The MLP achieved an accuracy of 95.45% on the test set, outperforming other methods such as CART and C4.5【5:3†source】【5:9†source】.

### Evaluation
- **Cluster Evaluation**: The clusters are evaluated based on their coherence and separation, ensuring that the identified clusters accurately represent different thyroid conditions.
- **Performance Metrics**: Metrics such as accuracy, precision, recall, and Kappa statistic are used to evaluate the performance of the clustering and classification algorithms【5:6†source】【5:9†source】.

### Conclusion
The analysis demonstrates the effectiveness of clustering and classification algorithms in predicting thyroid conditions. K-Means provides clear cluster separation, while DBSCAN offers robust handling of outliers and noise. The MLP classifier shows high accuracy and robustness in classifying thyroid conditions【5:10†source】.

