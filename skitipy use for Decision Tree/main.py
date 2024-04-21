# import pandas as pd
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score
#
# # Step 1: Load your own dataset
# data = pd.read_csv('/Users/yehonatankeypur/Downloads/data for mmn11.csv')
#
# # Step 2: Separate features (X) and target variable (y)
# X = data.drop('COPD', axis=1)  # Adjust 'target_column_name' to your target variable's name
# y = data['target_column_name']
#
# # Step 3: Split the dataset into training and testing sets
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
#
# # Step 4: Initialize the DecisionTreeClassifier and train the model
# clf = DecisionTreeClassifier(criterion='entropy')
# clf.fit(X_train, y_train)
#
# # Step 5: Make predictions on the testing data
# y_pred = clf.predict(X_test)
#
# # Step 6: Evaluate the model's accuracy
# accuracy = accuracy_score(y_test, y_pred)
# print("Accuracy:", accuracy)


import matplotlib.pyplot as plt
import numpy as np
import math

from sklearn.tree import plot_tree

from sklearn.datasets import load_iris
from sklearn.inspection import DecisionBoundaryDisplay
from sklearn.tree import DecisionTreeClassifier

import matplotlib.pyplot as plt
import numpy as np

from sklearn.tree import plot_tree

from sklearn.inspection import DecisionBoundaryDisplay
from sklearn.tree import DecisionTreeClassifier

import pandas as pd  # Import pandas for data loading


def func1():
    iris = load_iris()
    # Parameters
    n_classes = 3
    plot_colors = "ryb"
    plot_step = 0.02

    for pairidx, pair in enumerate([[0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [2, 3]]):
        # We only take the two corresponding features
        X = iris.data[:, pair]
        y = iris.target

        # Train
        clf = DecisionTreeClassifier().fit(X, y)

        # Plot the decision boundary
        ax = plt.subplot(2, 3, pairidx + 1)
        plt.tight_layout(h_pad=0.5, w_pad=0.5, pad=2.5)
        DecisionBoundaryDisplay.from_estimator(
            clf,
            X,
            cmap=plt.cm.RdYlBu,
            response_method="predict",
            ax=ax,
            xlabel=iris.feature_names[pair[0]],
            ylabel=iris.feature_names[pair[1]],
        )

        # Plot the training points
        for i, color in zip(range(n_classes), plot_colors):
            idx = np.where(y == i)
            plt.scatter(
                X[idx, 0],
                X[idx, 1],
                c=color,
                label=iris.target_names[i],
                cmap=plt.cm.RdYlBu,
                edgecolor="black",
                s=15,
            )

    plt.suptitle("Decision surface of decision trees trained on pairs of features")
    plt.legend(loc="lower right", borderpad=0, handletextpad=0)
    _ = plt.axis("tight")

    plt.figure()
    clf = DecisionTreeClassifier().fit(iris.data, iris.target)
    plot_tree(clf, filled=True)
    plt.title("Decision tree trained on all the iris features")
    plt.show()


def func2():
    # Load your own data
    # Replace 'your_data.csv' with the path to your CSV file
    data = pd.read_csv('/Users/yehonatankeypur/Downloads/data for mmn11.csv')

    # Extract features and target labels
    X = data.drop(columns=['COPD'])  # Replace 'target_column_name' with the name of your target column
    y = data['COPD']

    # Parameters
    n_classes = len(np.unique(y))  # Calculate the number of classes dynamically
    plot_colors = "ryb"
    plot_step = 0.02

    # Plot decision boundary and data points
    fig, axes = plt.subplots(2, 3, figsize=(10, 7))

    for pairidx, pair in enumerate([[0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [2, 3]]):
        # Train your classifier
        clf = DecisionTreeClassifier().fit(X.iloc[:, pair], y)

        # Plot the decision boundary
        DecisionBoundaryDisplay.from_estimator(
            clf,
            X.iloc[:, pair],
            cmap=plt.cm.RdYlBu,
            response_method="predict",
            ax=axes[pairidx // 3, pairidx % 3],
            xlabel="Feature {}".format(pair[0]),
            ylabel="Feature {}".format(pair[1]),
        )

        # Plot the training points
        for i, color in zip(np.unique(y), plot_colors):
            idx = np.where(y == i)
            axes[pairidx // 3, pairidx % 3].scatter(
                X.iloc[idx, pair[0]],
                X.iloc[idx, pair[1]],
                c=color,
                label=i,
                cmap=plt.cm.RdYlBu,
                edgecolor="black",
                s=15,
            )

    plt.suptitle("Decision surface of decision trees trained on pairs of features")
    plt.legend(loc="lower right", borderpad=0, handletextpad=0)
    plt.tight_layout()
    plt.show()

    # Visualize the decision tree trained on all features
    plt.figure()
    clf = DecisionTreeClassifier().fit(X, y)
    plot_tree(clf, filled=True)
    plt.title("Decision tree trained on all features")
    plt.show()


def calculate_expression(x, a, b, y, c, d):
    p1 = x / (x + y)
    p2 = y / (x + y)
    result = p1 * I(a, b) + p2 * I(c, d)
    return result


def I(c1, c2):
    if c1 == 0 or c2 == 0:
        return 0
    else:
        p1 = c1 / (c1 + c2)
        p2 = c2 / (c1 + c2)
        return -1 * (p1 * math.log2(p1) + p2 * math.log2(p2))


# Example usage:
x = 4
y = 1

a = 4
b = 0

c = 1
d = 0

result = calculate_expression(x, a, b, y, c, d)
print("Result:", result)

result2 = (1 / 11) * I(1, 0) + (1 / 11) * I(1, 0) + (1 / 11) * I(1, 0) + (3 / 11) * I(3, 0) + (2 / 11) * I(2, 0) + (
            3 / 11) * I(2, 1)
print("Result2:", result2)
