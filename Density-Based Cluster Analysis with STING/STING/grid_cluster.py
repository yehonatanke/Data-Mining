import numpy as np


def grid_based_clustering(data, grid_size=0.1, min_points=5):
    """
    Perform grid-based clustering on the given data.

    Parameters:
        data (ndarray): Input data points, shape (n_samples, n_features).
        grid_size (float): Size of the grid cells.
        min_points (int): Minimum number of points required in a cluster.

    Returns:
        clustered_data (dict): Dictionary containing clustered data points.
            Keys are cluster IDs, and values are arrays of points in each cluster.
    """
    # Initialize empty dictionary to store clusters
    clustered_data = {}

    # Convert data to numpy array if it's not already
    data = np.array(data)

    # Create a grid covering the data
    x_min, x_max = np.min(data[:, 0]), np.max(data[:, 0])
    y_min, y_max = np.min(data[:, 1]), np.max(data[:, 1])
    x_grid = np.arange(x_min, x_max, grid_size)
    y_grid = np.arange(y_min, y_max, grid_size)

    # Assign points to grid cells
    grid_assignment = np.zeros((len(x_grid), len(y_grid)), dtype=np.int32)
    for i, x in enumerate(x_grid):
        for j, y in enumerate(y_grid):
            points_in_cell = np.where((data[:, 0] >= x) & (data[:, 0] < x + grid_size) &
                                      (data[:, 1] >= y) & (data[:, 1] < y + grid_size))[0]
            grid_assignment[i, j] = len(points_in_cell)

    # Initialize cluster ID
    cluster_id = 0

    # Iterate over each grid cell
    for i in range(len(x_grid)):
        for j in range(len(y_grid)):
            # Check if the cell has enough points to be considered a cluster
            if grid_assignment[i, j] >= min_points:
                # Mark all points in this cell as belonging to the same cluster
                points_in_cell = np.where((data[:, 0] >= x_grid[i]) & (data[:, 0] < x_grid[i] + grid_size) &
                                          (data[:, 1] >= y_grid[j]) & (data[:, 1] < y_grid[j] + grid_size))[0]
                clustered_data[cluster_id] = data[points_in_cell]
                cluster_id += 1

    return clustered_data
