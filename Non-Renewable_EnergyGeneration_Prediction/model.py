import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from xgboost.sklearn import XGBRegressor
from sklearn.svm import SVR
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

data = pd.read_csv('data/merged.csv')

X_train, X_test, y_train, y_test = train_test_split(
    data.drop('target', axis=1), 
    data['target'],
    test_size=0.2, 
    random_state=42
)

model = RandomForestRegressor()

parameters = {
    'n_estimators': [10, 50, 100],
    'max_depth': [None, 50, 100],
    'min_samples_leaf': [1, 2, 4]
}

clf = GridSearchCV(model, parameters, scoring='r2', cv=5)
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

print(f'R2 score: {r2_score(y_test, y_pred)}')