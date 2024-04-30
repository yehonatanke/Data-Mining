<div align="center">
  <img src="https://img.shields.io/badge/language-Python-%233776AB.svg?logo=python">
  <img src="https://img.shields.io/badge/uses-Grid%20Based%20Clustering-%232A2F3D.svg">
  <img src="https://custom-icon-badges.demolab.com/github/license/denvercoder1/custom-icon-badges?logo=law">
</div>

# Grid-Based Clustering Program

## Overview
This project implements a grid-based clustering algorithm in Python to categorize data points into clusters based on their proximity. The program provides options for both generating synthetic data and clustering user-provided data. It then visualizes the data before and after clustering to facilitate analysis.

# Grid-Based Clustering

Grid-based clustering is a method used to partition data points into clusters by dividing the data space into a grid of cells and assigning points to clusters based on their location within these cells. This approach is particularly useful for spatial data analysis and is commonly applied in fields such as geographic information systems (GIS), image processing, and data mining.

### Objective
The main objective of grid-based clustering is to group data points that are spatially close together into the same cluster, while keeping clusters well-separated from each other. By dividing the data space into a grid, grid-based clustering methods can efficiently handle large datasets and identify clusters of varying shapes and densities.

### Techniques
Grid-based clustering can be performed using various techniques, including:

1. **Density-Based Grid Clustering**: Identify dense regions of data points in the grid cells and group them into clusters. Techniques such as DBSCAN (Density-Based Spatial Clustering of Applications with Noise) can be adapted to work with grid-based data structures, allowing for the automatic detection of clusters with varying densities.

2. **Cell-Based Clustering**: Assign each data point to the grid cell it belongs to and then merge adjacent cells with a sufficient number of points into clusters. This approach is straightforward and efficient for datasets with a uniform distribution of points.

3. **Hierarchical Grid Clustering**: Build a hierarchical tree of grid cells by recursively merging or splitting cells based on their content. This allows for exploring the data at different levels of granularity and can handle datasets with varying densities.

4. **Grid-Based Partitioning**: Partition the data space into a fixed number of grid cells and then apply traditional clustering algorithms such as K-means or hierarchical clustering to the points within each cell. This approach combines the benefits of grid-based and traditional clustering methods.

### Applications
Grid-based clustering has various applications in spatial data analysis and beyond, including:

- Geographic data analysis and visualization.
- Image segmentation and object detection.
- Network traffic analysis and anomaly detection.
- Customer segmentation and market analysis.
- Environmental monitoring and resource management.

### Advantages
- Scalability: Grid-based clustering methods are highly scalable and can efficiently handle large datasets by partitioning the data space into manageable chunks.
- Flexibility: Grid-based clustering can accommodate datasets with varying shapes, densities, and dimensions, making it suitable for a wide range of applications.
- Interpretability: The grid structure provides a natural way to interpret and visualize the clustering results, making it easier to understand the spatial distribution of clusters.

### Limitations
- Grid Size Sensitivity: The choice of grid size can impact the clustering results, and selecting an appropriate grid size may require domain knowledge or experimentation.
- Boundary Effects: Clusters near the boundary of grid cells may be split across multiple cells, leading to suboptimal clustering results.
- Curse of Dimensionality: Grid-based clustering may struggle with high-dimensional data, as the number of grid cells increases exponentially with the number of dimensions.

Overall, grid-based clustering is a powerful technique for partitioning spatial data into meaningful clusters, offering scalability, flexibility, and interpretability for a wide range of applications.


## Features
- **Grid-based Clustering**: Utilizes a grid-based approach to cluster data points, grouping them based on their proximity within predefined grid cells.
- **Data Generation**: Supports the generation of synthetic data with customizable parameters, including the number of points, number of clusters, and cluster standard deviation.
- **Data Visualization**: Provides visualizations of the data both before and after clustering, allowing users to observe the effectiveness of the clustering algorithm.
- **Modular Structure**: Organizes the codebase into separate modules for data generation, clustering, plotting, and the main execution script, enhancing readability and maintainability.

## Usage
1. **Setup**: Ensure that Python (version 3.x) is installed on your system along with the necessary dependencies (NumPy and Matplotlib).
2. **Execution**: Run the `main.py` script to execute the program. This will generate or load data, perform grid-based clustering, and visualize the results.
3. **Customization**: Modify the parameters in the `main.py` file to customize data generation or clustering settings according to your requirements.

## Files
- **main.py**: Entry point of the program. Orchestrates data generation, clustering, and visualization.
- **clustering.py**: Implements the grid-based clustering algorithm.
- **data_generation.py**: Generates synthetic data for clustering.
- **plotting.py**: Contains functions for visualizing data before and after clustering.
- **utils.py**: Contains utility functions and constants used across the project.

## Output Example

![Original Data](https://github.com/yehonatanke/Data-Mining/blob/main/Density-Based%20Cluster%20Analysis%20with%20STING/output/before.png)
*Figure 1: Scatter plot of original data*

![Clustered Data](https://github.com/yehonatanke/Data-Mining/blob/main/Density-Based%20Cluster%20Analysis%20with%20STING/output/after.png)
*Figure 2: Scatter plot of clustered data*

## Dependencies
- Python (3.x)
- NumPy
- Matplotlib

## License

This project is licensed under the MIT License.
