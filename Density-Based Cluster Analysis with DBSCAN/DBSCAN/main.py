import numpy as np
from cluster import DBSCAN
from visualization import plot_data, plot_clusters


def get_user_preference():
    """
    Prompt the user for their preference regarding data input.

    Returns:
    - choice: int
              User's choice (1 for using sample data, 2 for providing own data).
    """
    print("How would you like to input data?")
    print("1. Use sample data")
    print("2. Provide your own data")
    choice = int(input("Enter your choice (1 or 2): "))
    return choice


def get_user_data():
    """
    Prompt the user to input their own data.

    Returns:
    - data: numpy array of shape (n_samples, n_features)
            User-provided data.
    """
    n_samples = int(input("Enter the number of data points: "))
    n_features = int(input("Enter the number of features: "))
    print("Enter data points (one row at a time):")
    data = []
    for i in range(n_samples):
        data_row = [float(x) for x in input().split()]
        if len(data_row) != n_features:
            print(f"Invalid number of features. Expected {n_features}. Please try again.")
            return None
        data.append(data_row)
    return np.array(data)


def main():
    choice = get_user_preference()

    if choice == 1:
        # Sample data
        data = np.random.rand(130, 2)  # 100 data points with 2 features
    elif choice == 2:
        # User-provided data
        data = get_user_data()
        if data is None:
            return  # Exit if user-provided data is invalid
    else:
        print("Invalid choice. Please enter 1 or 2.")
        return

    # Hyperparameters
    eps = 0.1  # Epsilon
    min_samples = 5  # Minimum number of samples required to form a dense region

    # Perform clustering using DBSCAN
    dbscan = DBSCAN(eps=eps, min_samples=min_samples)
    clusters = dbscan.fit(data)

    # Plot original data
    plot_data(data, title="Original Data")

    # Plot clustered data
    plot_clusters(data, clusters, title="Clustered Data")


if __name__ == "__main__":
    main()
