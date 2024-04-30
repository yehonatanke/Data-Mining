import numpy as np


def generate_data(num_points=1000, num_clusters=5, cluster_std=0.5):
    """
    Generate synthetic data for clustering.

    Parameters:
        num_points (int): Number of data points to generate.
        num_clusters (int): Number of clusters to generate.
        cluster_std (float): Standard deviation of clusters.

    Returns:
        data (ndarray): Generated data points, shape (num_points, 2).
    """
    # Generate random cluster centers
    cluster_centers = np.random.rand(num_clusters, 2)

    # Generate data points around cluster centers
    data = np.zeros((num_points, 2))
    for i in range(num_points):
        cluster_id = np.random.randint(num_clusters)
        data[i, 0] = np.random.normal(cluster_centers[cluster_id, 0], cluster_std)
        data[i, 1] = np.random.normal(cluster_centers[cluster_id, 1], cluster_std)

    return data
