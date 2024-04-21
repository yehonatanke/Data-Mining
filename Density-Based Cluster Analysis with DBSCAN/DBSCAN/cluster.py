import numpy as np


class DBSCAN:
    def __init__(self, eps, min_samples):
        self.eps = eps
        self.min_samples = min_samples

    def fit(self, data):
        clusters = self._dbscan(data)
        return clusters

    def _dbscan(self, data):
        """
        Perform density-based clustering using the DBSCAN algorithm.

        Parameters:
        - data: numpy array of shape (n_samples, n_features)
                The input data to be clustered.

        Returns:
        - clusters: list of arrays
                    List containing the indices of data points in each cluster.
        """

        # Initialize variables
        n_samples = data.shape[0]
        labels = np.full(n_samples, -1)  # Initialize labels as unclassified (-1)
        cluster_id = 0

        # Iterate through each data point
        for i in range(n_samples):
            # If the point is already classified, skip it
            if labels[i] != -1:
                continue

            # Find neighbors of the current point
            neighbors = self._get_neighbors(data, i)

            # If the number of neighbors is less than min_samples, mark as noise
            if len(neighbors) < self.min_samples:
                labels[i] = 0  # Mark as noise
            else:
                cluster_id += 1
                self._expand_cluster(data, labels, i, neighbors, cluster_id)

        # Collect points belonging to each cluster
        clusters = [np.where(labels == i)[0] for i in range(1, cluster_id + 1)]

        return clusters

    def _get_neighbors(self, data, index):
        """
        Find neighbors of a data point within epsilon distance.

        Parameters:
        - data: numpy array of shape (n_samples, n_features)
                The input data.
        - index: int
                 Index of the data point for which neighbors need to be found.

        Returns:
        - neighbors: list
                     List of indices of neighboring data points.
        """
        distances = np.linalg.norm(data - data[index], axis=1)
        neighbors = np.where(distances <= self.eps)[0]
        return neighbors

    def _expand_cluster(self, data, labels, index, neighbors, cluster_id):
        """
        Expand a cluster by recursively adding reachable points.

        Parameters:
        - data: numpy array of shape (n_samples, n_features)
                The input data.
        - labels: numpy array of shape (n_samples,)
                  Array containing cluster labels for each data point.
        - index: int
                 Index of the data point being expanded.
        - neighbors: list
                     List of indices of neighboring data points.
        - cluster_id: int
                      Current cluster id.
        """
        labels[index] = cluster_id

        # Iterate through neighbors
        for neighbor_index in neighbors:
            # If neighbor is noise, mark as part of the current cluster
            if labels[neighbor_index] == 0:
                labels[neighbor_index] = cluster_id
            # If a neighbor is unclassified, check if it's a core point or border point
            elif labels[neighbor_index] == -1:
                labels[neighbor_index] = cluster_id
                neighbor_neighbors = self._get_neighbors(data, neighbor_index)
                if len(neighbor_neighbors) >= self.min_samples:
                    self._expand_cluster(data, labels, neighbor_index, neighbor_neighbors, cluster_id)
