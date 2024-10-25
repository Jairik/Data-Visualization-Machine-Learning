''' Classification Based Wireless Indoor Locatization '''

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split  # Preparing data
from sklearn.tree import DecisionTreeClassifier  # DT
from sklearn.neighbors import KNeighborsClassifier  # KNN
from sklearn.metrics import confusion_matrix  # Confusion Matrix for analyzing results

# Load the data into pandas and split into testing & training data (70/30 split)
df = pd.read_csv('wifi_localization.txt', delimiter='\t', header=None) 
x = df.iloc[:, :7] # Features
y = df.iloc[:, -1] # Classifier
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.3, random_state=42)

''' Self-tests using all data '''
# Self-testing and printing classification report for KNN
knn_selftest = KNeighborsClassifier(n_neighbors=5)
knn_selftest.fit(x, y)
print("KNN Self Test:", knn_selftest.score(x, y))

# Self-testing and printing classification report for Decision Tree
dt_selftest = DecisionTreeClassifier(criterion='entropy')
dt_selftest.fit(x, y)
print("Decision Tree Self Test:", dt_selftest.score(x, y))


''' Independent-tests '''
# Re-training and testing KNN
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(x_train, y_train)
y_pred = knn.predict(x_test)
print("KNN Independent Test: ", knn.score(x_test, y_test), "\n", confusion_matrix(y_pred, y_test))

# Re-training and testing DT
dt = DecisionTreeClassifier(criterion='entropy')
dt.fit(x_train, y_train)
y_pred = dt.predict(x_test)
print("Decision Tree Independent Test: ", dt.score(x_test, y_test), "\n", confusion_matrix(y_pred, y_test))


''' Optimizing Models '''
# Testing KNN with different n_neighbors and weights
# for i in range(1, 100):
#     knn_test_n = KNeighborsClassifier(n_neighbors=i, weights = 'uniform', n_jobs=-1)
#     knn_test_w = KNeighborsClassifier(n_neighbors=i, weights = 'distance', n_jobs=-1)
#     knn_test_n.fit(x_train, y_train)
#     knn_test_w.fit(x_train, y_train)
#     print(f"KNN {i} uniform weights: ", knn_test_n.score(x_test, y_test))
#     print(f"KNN {i} distance weights: ", knn_test_w.score(x_test, y_test)) 
# Best results were accomplished at k=6 and uniform weight (.986667)(k=7 at distance weight 
# should similar results, however may be more computationally expensive)
knn_final = KNeighborsClassifier(n_neighbors=6, weights='uniform', njobs=-1)

