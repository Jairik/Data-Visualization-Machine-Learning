''' Classification Based Wireless Indoor Locatization '''

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score  # Preparing data & cross validating
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
print("KNN Self Test Accuracy:", knn_selftest.score(x, y), "\nClassification Report: ", classification_report(y_pred, y_test))

# Self-testing and printing classification report for Decision Tree
dt_selftest = DecisionTreeClassifier(criterion='entropy')
dt_selftest.fit(x, y)
y_pred = dt_selftest.predict(x_test)
print("Decision Tree Self Test Accuracy:", dt_selftest.score(x, y), "\nClassification Report: ", classification_report(y_pred, y_test))

''' Independent-tests '''
# Re-training and testing KNN
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(x_train, y_train)
y_pred = knn.predict(x_test)
print("KNN Independent Test Accuracy: ", knn.score(x_test, y_test), "\nClassification Report: ", classification_report(y_pred, y_test), "\n", confusion_matrix(y_pred, y_test))

# Re-training and testing DT
dt = DecisionTreeClassifier(criterion='entropy')
dt.fit(x_train, y_train)
y_pred = dt.predict(x_test)
print("Decision Tree Independent Test: ", dt.score(x_test, y_test), "\nClassification Report: ", classification_report(y_pred, y_test), "\n", confusion_matrix(y_pred, y_test))


''' Optimizing Models '''
# Testing KNN with different n_neighbors and weights using cross-validation
# for i in range(1, 50):
#     knn_test_n = KNeighborsClassifier(n_neighbors=i, weights = 'uniform', n_jobs=-1)
#     knn_test_w = KNeighborsClassifier(n_neighbors=i, weights = 'distance', n_jobs=-1)
#     knn_test_n.fit(x_train, y_train)
#     knn_test_w.fit(x_train, y_train)
#     print(f"KNN {i} uniform weights: ", (cross_val_score(knn_test_n, x_test, y_test)).mean()) # folds default to 5 
#     print(f"KNN {i} distance weights: ", (cross_val_score(knn_test_w, x_test, y_test)).mean(), "\n") 
# Best results were accomplished at k=3 and distance weights (.98333334) 

knn_final = KNeighborsClassifier(n_neighbors=3, weights='distance', n_jobs=-1)

# Testing Decision Tree with various different parameters using cross-validation
# dt_test_cg = DecisionTreeClassifier(criterion='gini')
# dt_test_ce = DecisionTreeClassifier(criterion='entropy')
# print(f"DT Gini default: {cross_val_score(dt_test_cg, x, y).mean()} \n \
#     DT Entrophy Default: {cross_val_score(dt_test_ce, x, y)}\n")
# for i in range(5, 30, 5):  # Testing max depth to prevent overly-complex trees
#     dt_test_cg_md = DecisionTreeClassifier(criterion='gini', max_depth=i)
#     dt_test_ce_md = DecisionTreeClassifier(criterion='entropy', max_depth=i)
#     print(f"DT Gini Max Depth {i}: {cross_val_score(dt_test_cg_md, x, y).mean()} \n \
#     DT Entrophy Max Depth {i}: {cross_val_score(dt_test_ce_md, x, y).mean()}\n")
#     for j in range(3, 10): # Testing minimum sample split to potentially prevent overfitting
#         dt_test_cg_ss = DecisionTreeClassifier(criterion='gini', max_depth=i, min_samples_split=j)
#         dt_test_ce_ss = DecisionTreeClassifier(criterion='entropy', max_depth=i, min_samples_split=j)
#         print(f"DT Gini Max Depth {i} Sample Split {j}: {cross_val_score(dt_test_cg_ss, x, y).mean()} \n \
#         DT Entrophy Max Depth {i} Sample Split {j}: {cross_val_score(dt_test_ce_ss, x, y).mean()}\n")
# Interestingly, best fit is around max depth 10 sample split 8-9 for Gini (around .97)

dt_final = DecisionTreeClassifier(criterion='gini', max_depth=10, min_samples_split=8)

print(f"KNN accuracy of {cross_val_score(knn_final, x, y).mean()} vs Decision Tree accuracy of {cross_val_score(dt_final, x, y).mean()}")  # KNN Wins!

''' Showing independent test results of final knn '''
knn_final.fit(x_train, y_train)
y_pred = knn_final.predict(x_test)
print(f"Final KNN Accuracy: {knn_final.score(x_test, y_test)}")
print(f"Final KNN Classification Report: {classification_report(y_pred, y_test)}")
print("Final KNN Confusion Matrix: ")
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

print("Final KNN Test Size Bar Figure: ")    
plt.bar(x=test_sizes, height=knn_models_scores, color=['blue'], edgecolor='black')
plt.ylim(94, 100)
plt.title("KNN Test Size Accuracies")
plt.xlabel("Test Size (%)")
plt.ylabel("Accuracy (%)")
plt
plt.show()