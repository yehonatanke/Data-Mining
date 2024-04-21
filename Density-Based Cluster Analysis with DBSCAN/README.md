# Density-Based Cluster Analysis with DBSCAN

This Python program performs density-based cluster analysis using the DBSCAN algorithm. It allows users to input their own data or use sample data provided within the program. The program provides visualizations of the original data and the clustered data using scatter plots.


## Features

- Performs density-based clustering using the DBSCAN algorithm.
- Provides options for inputting user data or using sample data.
- Visualizes original data and clustered data with scatter plots.
- Handles noisy or outlier data points.

## DBSCAN

DBSCAN is based on the concept of density. It defines clusters as dense regions in the data space, separated by regions of lower density. The algorithm uses two parameters:
- Epsilon $(ε)$: The maximum radius of the neighborhood around a data point.
- Minimum Points $(MinPts)$: The minimum number of data points required to form a dense region.

The algorithm proceeds as follows:
1. For each data point, it identifies its ε-neighborhood, which includes all points within a distance of ε from the data point.
2. If a data point has at least MinPts neighbors within its ε-neighborhood (including itself), it is considered a core point.
3. Core points that are reachable from each other form a cluster. This is achieved by recursively expanding the cluster from each core point to its neighbors.
4. Any data point that is not a core point and does not belong to any cluster is classified as noise or an outlier.

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/yehonatanke/Data-Mining/tree/main/Density-Based%20Cluster%20Analysis%20with%20DBSCAN
    ```
2. Navigate to the project directory:

   ```bash
   cd Density-Based Cluster Analysis with DBSCAN/DBSCAN
   ```
3. Run the `main.py` script:

   ```bash
   python main.py

4. Choose your data input preference:
    - Select option 1 to use sample data.
    - Select option 2 to provide your own data.

5. Follow the prompts to input data if you choose option 2.

6. View the scatter plot visualizations of the original data and clustered data.


## Output Example

![Original Data](https://github.com/yehonatanke/Data-Mining/blob/main/Density-Based%20Cluster%20Analysis%20with%20DBSCAN/output/before.jpeg)
*Figure 1: Scatter plot of original data*

![Clustered Data](https://github.com/yehonatanke/Data-Mining/blob/main/Density-Based%20Cluster%20Analysis%20with%20DBSCAN/output/after.jpeg)
*Figure 2: Scatter plot of clustered data*


## License

This project is licensed under the MIT License.
