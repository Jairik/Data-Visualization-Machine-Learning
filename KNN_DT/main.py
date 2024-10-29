''' Classification Based Wireless Indoor Locatization '''

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV  # Preparing data, cross validating, parameter optimization
from sklearn.tree import DecisionTreeClassifier  # DT
from sklearn.neighbors import KNeighborsClassifier  # KNN
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, classification_report  # Confusion Matrix for analyzing results
from matplotlib import pyplot as plt
import matplotlib as mpl

# Load the data into pandas and split into testing & training data (70/30 split)
df = pd.read_csv('wifi_localization.txt', delimiter='\t', header=None) 
x = df.iloc[:, :7] # Features
y = df.iloc[:, -1] # Classifier
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.3, random_state=42)

''' Self-tests using all data '''
x_test = x
y_test = y
# Self-testing and printing classification report for KNN
knn_selftest = KNeighborsClassifier(n_neighbors=5)
knn_selftest.fit(x, y)
y_pred = knn_selftest.predict(x_test)
print("KNN Self Test Accuracy:", knn_selftest.score(x, y), "\nClassification Report:\n", classification_report(y_pred, y_test))

# Self-testing and printing classification report for Decision Tree
dt_selftest = DecisionTreeClassifier(criterion='entropy')
dt_selftest.fit(x, y)
y_pred = dt_selftest.predict(x_test)
print("Decision Tree Self Test Accuracy:", dt_selftest.score(x, y), "\nClassification Report:\n", classification_report(y_pred, y_test))

''' Independent-tests '''
# Re-training and testing KNN
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(x_train, y_train)
y_pred = knn.predict(x_test)
print("KNN Independent Test Accuracy: ", knn.score(x_test, y_test), "\nClassification Report:\n", classification_report(y_pred, y_test), "\n", confusion_matrix(y_pred, y_test))
''' Utilizing scikit-learn's grid search to test different KNN model parameters '''
n_neighbors_counts = [i for i in range(1, 50)]
param_grid = [{
    'n_neighbors': n_neighbors_counts, 'weights': ['uniform', 'distance'], 'metric': ['euclidean', 'manhattan']
}]
grid_search = GridSearchCV(estimator=knn, param_grid=param_grid, cv=10, scoring='accuracy')
grid_search.fit(x_train, y_train)
print(f"\tBest Parameters: {grid_search.best_params_}")
print(f"\tBest Cross-Validation Score: {grid_search.best_score_}")
knn_final = grid_search.best_estimator_
print(f"\tScore with testing data: {knn_final.score(x_test, y_test)}\n\
    {classification_report(knn_final.predict(x_test), y_test)}")

# Re-training and testing DT
dt = DecisionTreeClassifier(criterion='entropy')
dt.fit(x_train, y_train)
y_pred = dt.predict(x_test)
print("Decision Tree Independent Test: ", dt.score(x_test, y_test), "\nClassification Report:\n", classification_report(y_pred, y_test), "\n", confusion_matrix(y_pred, y_test))
''' Utilizing scikit-learn's grid search to test different Decision Tree model parameters '''
max_depth_counts = [i for i in range(1, 20)]
max_depth_counts.append(None)  # No max depth
min_sample_split_counts = [i for i in range(2, 10)]
param_grid = [{
    'criterion':['entropy', 'gini'], 
     'max_depth': max_depth_counts, 
     'min_samples_split': min_sample_split_counts
}]
grid_search = GridSearchCV(estimator=DecisionTreeClassifier(), param_grid=param_grid, cv=10, scoring='accuracy')
grid_search.fit(x_train, y_train)
print(f"\tBest Parameters: {grid_search.best_params_}")
print(f"\tBest Cross-Validation Score: {grid_search.best_score_}")
dt_final = grid_search.best_estimator_
print(f"\tScore with testing data: {dt_final.score(x_test, y_test)}\n\
    {classification_report(dt_final.predict(x_test), y_test)}")

''' Showing Confusion Matrix for Optimal Model '''
# print("Final KNN Confusion Matrix: ")
cm = ConfusionMatrixDisplay.from_estimator(knn_final, x_test, y_test)  
plt.show()

''' Drawing figure for accuracy of 10%-50% testing data '''
mpl.rcParams['figure.facecolor'] = 'gray'  # Set default background color
knn_models_scores = []
test_sizes = ['10%', '20%', '30%', '40%', '50%']
for i in test_sizes:
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=(int(i.strip('%')))*.01, random_state=14)
    knn_final.fit(x_train, y_train)
    knn_models_scores.append((knn_final.score(x_test, y_test))*100)

# print("Final KNN Test Size Bar Figure: ")    
plt.bar(x=test_sizes, height=knn_models_scores, color=['blue'], edgecolor='black')
plt.ylim(94, 100)
plt.title("KNN Test Size Accuracies")
plt.xlabel("Test Size (%)")
plt.ylabel("Accuracy (%)")
plt.show()