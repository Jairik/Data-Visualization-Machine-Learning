''' JJ McCauley '''
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, classification_report

# Collecting features and targets for testing and training sets
ftdf = pd.read_csv('FoodTypeDataset.csv')
x = ftdf.iloc[:, :-1].values
y = ftdf.iloc[:, -1].values
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.2, random_state=42)

# Creating & self testing Gradient Boosting Classifier
gbmodel = GradientBoostingClassifier()  # Default parameters for now
#gbmodel.fit(x, y)
#print("Self Test Score: ", gbmodel.score(x, y))

# Creating test parameters
learning_rate = [.1]  # Default parameter to decrease parameter tuning time
n_estimators = [200]  # [j for j in range(195, 205)]
subsample = [1.0]  # Default Value
min_samples_split = [2] #[m for m in range(2, 5)]
min_samples_leaf = [3] #[msl for msl in range(3, 5)]
max_depth = [md for md in range(37, 45)]  # Tweaked after test
max_features = [mf for mf in range(5, 15)]
max_features.append(25)
max_features.append(None)

max_depth.append(None)
params = {
    'learning_rate':learning_rate, 'n_estimators':n_estimators, 'subsample':subsample,
    'min_samples_split':min_samples_split, 'min_samples_leaf':min_samples_leaf, 
    'max_depth':max_depth, 'random_state':[42], 'max_features':max_features
}

# Creating grid gb model to test parameters
# grid = GridSearchCV(gbmodel, params, cv=4, n_jobs=-1, verbose=2)
# grid.fit(x_train, y_train)
# print(f"Best Parameters: {grid.best_params_}")
# best_gbmodel = grid.best_estimator_
# y_pred = best_gbmodel.predict(x_test)
# print("Score: ", best_gbmodel.score(x_test, y_test))

optimal_gb = GradientBoostingClassifier(learning_rate=.1, max_depth=38, max_features=13, min_samples_leaf=3,
                                        min_samples_split=2, n_estimators=200, subsample=1.0, random_state=42)
optimal_gb.fit(x_train, y_train)
y_pred = optimal_gb.predict(x_test)

# Printing Classification Report
print(classification_report(y_test, y_pred))  

# Showing heatmap of classification confusion matrix
cm = confusion_matrix(y_test, y_pred)
fancycm = ConfusionMatrixDisplay(confusion_matrix=cm)
fancycm.plot(cmap='Blues')
plt.title("Confusion Matrix for Food Type Classification Model")
plt.xlabel("Predicted Labels")
plt.ylabel("True Labels")
plt.show()

''' -- TESTING RESULTS --- 
Old Best Parameters: {'learning_rate': 0.1, 'max_depth': 37, 'min_samples_leaf': 3, 'min_samples_split': 2, 
'n_estimators': 200, 'random_state': 42, 'subsample': 0.4}
Score:  0.45714285714285713 (very low??)

NEW BEST PARAMETERS: {'learning_rate': 0.1, 'max_depth': 38, 'max_features': 13, 'min_samples_leaf': 3, 
'min_samples_split': 2, 'n_estimators': 200, 'random_state': 42, 'subsample': 1.0}
Score:  0.5508021390374331
'''