import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

# Step 1: Load Data
data = pd.read_csv("restaurant.csv")

  # assume dataset in CSV
X = data.drop("Wait", axis=1)
y = data["Wait"]

# Convert categorical variables to numeric
X = pd.get_dummies(X)

# Step 2: Train Decision Tree
tree_clf = DecisionTreeClassifier(criterion="entropy", max_depth=4, random_state=42)
tree_clf.fit(X, y)

# Step 3: Visualize the Decision Tree
plt.figure(figsize=(20,10))
plot_tree(tree_clf, feature_names=X.columns, class_names=["No","Yes"], filled=True)
plt.show()

# Step 6: Evaluation
from sklearn.metrics import accuracy_score
y_pred = tree_clf.predict(X)
print("Training Accuracy:", accuracy_score(y, y_pred))


# Exercise 1: Use Gini index instead of Entropy
tree_gini = DecisionTreeClassifier(criterion="gini", max_depth=4, random_state=42)
tree_gini.fit(X, y)

plt.figure(figsize=(20,10))
plot_tree(tree_gini, feature_names=X.columns, class_names=["No","Yes"], filled=True)
plt.title("Decision Tree (criterion = gini, depth = 4)")
plt.show()

y_pred_gini = tree_gini.predict(X)
print("Training Accuracy (gini, depth=4):", accuracy_score(y, y_pred_gini))


# Exercise 2: Limit depth = 2 (Entropy)
tree_entropy_depth2 = DecisionTreeClassifier(criterion="entropy", max_depth=2, random_state=42)
tree_entropy_depth2.fit(X, y)

plt.figure(figsize=(20,10))
plot_tree(tree_entropy_depth2, feature_names=X.columns, class_names=["No","Yes"], filled=True)
plt.title("Decision Tree (criterion = entropy, depth = 2)")
plt.show()

y_pred_entropy2 = tree_entropy_depth2.predict(X)
print("Training Accuracy (entropy, depth=2):", accuracy_score(y, y_pred_entropy2))


# -----------------------------------
# 5. Experiment
# -----------------------------------
# Remove "Reservation" attribute and retrain
X_exp = data.drop(["Wait", "Reservation"], axis=1)
X_exp = pd.get_dummies(X_exp)

tree_exp = DecisionTreeClassifier(criterion="entropy", max_depth=4, random_state=42)
tree_exp.fit(X_exp, y)

plt.figure(figsize=(20,10))
plot_tree(tree_exp, feature_names=X_exp.columns, class_names=["No","Yes"], filled=True)
plt.title("Decision Tree (without Reservation)")
plt.show()

y_pred_exp = tree_exp.predict(X_exp)
print("Training Accuracy (without Reservation):", accuracy_score(y, y_pred_exp))