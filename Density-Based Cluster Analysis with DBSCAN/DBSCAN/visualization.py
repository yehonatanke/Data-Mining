import numpy as np
import matplotlib.pyplot as plt


def plot_data(data, title):
    plt.figure(figsize=(10, 8))
    plt.scatter(data[:, 0], data[:, 1], color='b', s=30, marker='o')
    plt.title(title)
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.grid(True)
    plt.gca().set_aspect('equal', adjustable='box')  # Ensure equal aspect ratio
    plt.show()


def plot_clusters(data, clusters, title):
    plt.figure(figsize=(10, 8))
    plt.scatter(data[:, 0], data[:, 1], color='gray', s=30, marker='o', label='Noise')  # Plot noise points

    for cluster_id, cluster_indices in enumerate(clusters):
        if len(cluster_indices) > 0:
            cluster_data = data[cluster_indices]
            plt.scatter(cluster_data[:, 0], cluster_data[:, 1], label=f'Cluster {cluster_id + 1}')

            # Calculate centroid of the cluster for label positioning
            centroid_x = np.mean(cluster_data[:, 0])
            centroid_y = np.mean(cluster_data[:, 1])

            # Annotate cluster label outside the x and y box
            plt.annotate(
                f'Cluster {cluster_id + 1}',
                xy=(centroid_x, centroid_y),
                xytext=(centroid_x + 0.05, centroid_y + 0.05),  # Offset for label
                textcoords='offset points',
                ha='center', va='center',
                bbox=dict(boxstyle='round,pad=0.5', fc='yellow', alpha=0.5),
                arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0')
            )

    plt.title(title)
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
    plt.grid(True)
    plt.gca().set_aspect('equal', adjustable='box')  # Ensure equal aspect ratio
    plt.show()
