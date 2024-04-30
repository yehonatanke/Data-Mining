import grid_cluster as g_cluster
import data_generation
import visualization as vis


def main():
    # Option for user to choose data source or data generation
    # Read data from file or generate data
    data = data_generation.generate_data()

    # Plot data before clustering
    vis.plot_data(data, title="Before Clustering")

    # Perform grid-based clustering
    clustered_data = g_cluster.grid_based_clustering(data)

    # Plot clustered data
    vis.plot_clustered_data(clustered_data=clustered_data, noise_points=data, title="After Clustering")


if __name__ == "__main__":
    main()
