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
n_estimators = [j for j in range(50, 250, 50)]  # Refine After Initial Test
subsample = [s for s in np.arange(0.1, .5, .1)]  # Refine After Initial Test
min_samples_split = [m for m in range(2, 15)]
min_samples_leaf = [msl for msl in range(1, 15)]
max_depth = [md for md in range(25, 100, 15)]
max_depth.append(None)
params = {
    'learning_rate':learning_rate, 'n_estimators':n_estimators, 'subsample':subsample,
    'min_samples_split':min_samples_split, 'min_samples_leaf':min_samples_leaf, 
    'max_depth':max_depth, 'random_state':[42]
}

# Creating grid gb model to test parameters
grid = GridSearchCV(gbmodel, params, cv=4, n_jobs=-1, verbose=1)
grid.fit(x_train, y_train)
print(f"Best Parameters: {grid.best_params_}")
best_gbmodel = grid.best_estimator_
y_pred = best_gbmodel.predict()
