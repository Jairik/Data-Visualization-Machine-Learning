''' JJ McCauley '''
import pandas as pd
import numpy as np  # Potentially not needed
import matplotlib as plt
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import xgboost as xgb

# Collecting features and targets for testing and training sets
ftdf = pd.read_csv('FoodTypeDataset.csv')
x = ftdf.iloc[:, :-1].values
y = ftdf.iloc[:, -1].values
# All Features
# print(x.shape)
# print(y.shape)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.3, random_state=42)

# Creating & self testing Gradient Boosting Classifier
gbmodel = GradientBoostingClassifier()  # Default parameters for now
gbmodel.fit(x, y)
print("Self Test Score: ", gbmodel.score(x, y))

# Creating test parameters
learning_rate = [.1]  # Default parameter to decrease parameter tuning time
n_estimators = [200] #[j for j in range(195, 205)]
subsample = [s for s in np.arange(.4, .7, .1)]  # Refined after initial test
subsample.append(1.0)
min_samples_split = [2] #[m for m in range(2, 5)]
min_samples_leaf = [3] #[msl for msl in range(3, 5)]
max_depth = [md for md in range(37, 40)]  # Tweaked after test
max_depth.append(None)
params = {
    'learning_rate':learning_rate, 'n_estimators':n_estimators, 'subsample':subsample,
    'min_samples_split':min_samples_split, 'min_samples_leaf':min_samples_leaf, 
    'max_depth':max_depth, 'random_state':[42]
}

# Creating grid gb model to test parameters
grid = GridSearchCV(gbmodel, params, cv=4, n_jobs=-1, verbose=2)
grid.fit(x_train, y_train)
print(f"Best Parameters: {grid.best_params_}")
best_gbmodel = grid.best_estimator_
y_pred = best_gbmodel.predict(x_test)
print("Score: ", best_gbmodel.score(x_test, y_test))

# Best Parameters: {'learning_rate': 0.1, 'max_depth': 37, 'min_samples_leaf': 3, 'min_samples_split': 2, 'n_estimators': 200, 'random_state': 42, 'subsample': 0.4}
# Score:  0.45714285714285713 (very low??)