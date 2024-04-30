import matplotlib.pyplot as plt


def plot_data(data, title="Before Clustering"):
    """
    Plot data points.

    Parameters:
        data (ndarray): Input data points, shape (n_samples, n_features).
        title (str): Title of the plot.
    """
    plt.figure(figsize=(10, 8))
    plt.scatter(data[:, 0], data[:, 1], c='blue', s=30, marker='.')
    plt.title(title)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()


def plot_clustered_data(clustered_data, noise_points, title="After Clustering"):
    """
    Plot clustered data with different colors for each cluster.

    Parameters:
        clustered_data (dict): Dictionary containing clustered data points.
            Keys are cluster IDs, and values are arrays of points in each cluster.
        title (str): Title of the plot.
        :param title:
        :param clustered_data: (dict) Dictionary containing clustered data points.
        :param noise_points:
    """
    plt.figure(figsize=(10, 8))

    # Plot noise points in gray
    plt.scatter(noise_points[:, 0], noise_points[:, 1], c='gray', marker='x', s=20, label='Noise')

    # Iterate through clustered_data and plot points with different colors for each cluster
    for cluster_id, cluster_points in clustered_data.items():
        plt.scatter(cluster_points[:, 0], cluster_points[:, 1], marker='.', s=30)

    plt.title(title)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.grid(True)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()
