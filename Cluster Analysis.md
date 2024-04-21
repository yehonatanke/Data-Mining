### Concepts:
- **Cluster Analysis**: A technique used to group similar objects into clusters, where objects in the same cluster are more similar to each other than to those in other clusters.
- **Cluster**: A group of data points that are similar to each other within the group and dissimilar to points in other clusters.
- **Centroid**: The center point of a cluster, often represented by the mean or median of the data points in the cluster.
- **Distance Metric**: A measure used to quantify the dissimilarity between data points, such as Euclidean distance, Manhattan distance, or cosine similarity.
- **Clustering Algorithm**: A method used to partition a dataset into clusters based on certain criteria, such as K-means, hierarchical clustering, or DBSCAN.

### Algorithms:
- **K-means**: A partitioning clustering algorithm that aims to divide data points into K clusters by iteratively assigning each point to the nearest centroid and updating centroids based on the mean of points in each cluster.
- **Hierarchical Clustering**: A method that creates a tree of clusters by recursively merging or dividing clusters based on their proximity until all points belong to a single cluster.
- **DBSCAN (Density-Based Spatial Clustering of Applications with Noise)**: A density-based clustering algorithm that groups together closely packed points while marking outliers as noise.

### Evaluation Metrics:
- **Silhouette Score**: Measures the cohesion and separation of clusters by comparing the average distance between data points within a cluster to the average distance between points in different clusters.
- **Davies–Bouldin Index**: Evaluates the compactness and separation of clusters by comparing the average distance between each cluster's centroid to the average distance between points within the cluster and other clusters.
- **Elbow Method**: A heuristic technique used to determine the optimal number of clusters in a dataset by plotting the within-cluster sum of squares (WCSS) against the number of clusters and identifying the "elbow" point where the rate of decrease slows down.

### Steps:
1. **Data Preprocessing**: Normalize or scale features to ensure equal importance.
2. **Choose Algorithm**: Select an appropriate clustering algorithm based on data characteristics and requirements.
3. **Choose Number of Clusters**: Determine the optimal number of clusters using domain knowledge, visualization, or evaluation metrics.
4. **Run Algorithm**: Apply the chosen clustering algorithm to the dataset.
5. **Evaluate Clusters**: Assess the quality of clusters using evaluation metrics or domain-specific criteria.
6. **Interpret Results**: Analyze and interpret the clusters to gain insights into the underlying patterns in the data.

### Distance Functions:

- **Euclidean Distance**:
  - Description: Measures the straight-line distance between two points in Euclidean space.
  - Formula: $\sqrt{\sum (x_i - y_i)^2}$

- **Manhattan Distance (City Block Distance)**:
  - Description: Measures the distance between two points by summing the absolute differences of their coordinates.
  - Formula: $\sum |x_i - y_i| \$

- **Cosine Similarity**:
  - Description: Measures the cosine of the angle between two vectors in multidimensional space, indicating their similarity.
  - Formula: $\frac{\sum x_i \cdot y_i}{\sqrt{\sum x_i^2} \cdot \sqrt{\sum y_i^2}} \$

- **Jaccard Distance**:
  - Description: Measures the dissimilarity between two sets by comparing their intersection to their union.
  - Formula: $1 - \frac{|X \cap Y|}{|X \cup Y|} \$

- **Hamming Distance** (for binary data):
   - Description: Measures the number of positions at which corresponding symbols differ in two equal-length sequences.
   - Formula: <br>
 
<br> $$\sum_{i=1}^{n} \delta(x_i, y_i) \ , \  where \ \delta(x_i, y_i) = \begin{cases} 0 & \text{if } x_i = y_i \\\\\\\\ 1 & \text{if } x_i \neq y_i \end{cases}  <br> $$  


- **Mahalanobis Distance**:
  - Description: Measures the distance between a point and a distribution, taking into account the covariance between variables.
  - Formula: $\sqrt{(x - \mu)^T \Sigma^{-1} (x - \mu)}$



### Applications:
- Customer Segmentation
- Document Clustering
- Image Segmentation
- Anomaly Detection
- Market Segmentation
