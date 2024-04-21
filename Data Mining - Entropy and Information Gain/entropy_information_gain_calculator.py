import math


# Function to calculate entropy
def entropy(probabilities):
    return -sum(p * math.log2(p) for p in probabilities if p)


# Function to calculate information gain
def information_gain(parent_entropy, child_entropies, child_weights):
    weighted_sum = sum(weight * entropy for weight, entropy in zip(child_weights, child_entropies))
    return parent_entropy - weighted_sum


# Function to calculate probabilities for a given feature
# Function to calculate probabilities for a given feature
def calculate_probabilities(data, feature):
    total_count = len(data[feature])
    probabilities = {}
    for value in set(data[feature]):
        value_count = sum(1 for item in data[feature] if item == value)
        probabilities[value] = value_count / total_count
    return probabilities


# Example dataset
data = {
    'Age_range': ['51-60', '70+', '31-40', '70+', '51-60', '61-70', '51-60', '61-70', '41-50', '61-70', '30-'],
    'Smoke': ['No', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'No', 'No', 'Yes', 'Yes'],
    'Dyspnea_on_exertion': ['Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'No', 'No', 'Yes', 'No'],
    'Wheezing': ['Yes', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'No', 'Yes', 'No', None],
    'Phlegm': ['No', 'Yes', 'Yes', 'Yes', 'No', 'No', 'No', 'No', 'Yes', 'No', 'Yes'],
    'Inhaler_use': ['Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'No', 'No', 'No', 'Yes', 'No'],
    'COPD': ['No', 'Yes', 'No', 'Yes', 'No', 'Yes', 'No', 'No', 'No', 'Yes', 'No']
}

# Calculate probabilities and entropy for the target variable (COPD)
target_probabilities = calculate_probabilities(data, 'COPD')
target_entropy = entropy(target_probabilities.values())
print("Entropy of COPD:", target_entropy)

# Calculate information gain for each feature
features = ['Age_range', 'Smoke', 'Dyspnea_on_exertion', 'Wheezing', 'Phlegm', 'Inhaler_use']
for feature in features:
    probabilities = calculate_probabilities(data, feature)
    weighted_entropies = []
    for value, prob in probabilities.items():
        subset = [data['COPD'][i] for i in range(len(data[feature])) if data[feature][i] == value]
        subset_probabilities = calculate_probabilities({'COPD': subset}, 'COPD')
        subset_entropy = entropy(subset_probabilities.values())
        weighted_entropies.append(prob * subset_entropy)
    gain = information_gain(target_entropy, weighted_entropies, probabilities.values())
    print(f"Information Gain for {feature}: {gain}")
