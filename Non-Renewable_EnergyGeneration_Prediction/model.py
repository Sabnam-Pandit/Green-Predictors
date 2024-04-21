import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from xgboost.sklearn import XGBRegressor
from sklearn.svm import SVR
from sklearn.metrics import r2_score

data = pd.read_csv('data/merged.csv')

X_train, X_test, y_train, y_test = train_test_split(
    data.drop('target', axis=1), 
    data['target'],
    test_size=0.2, 
    random_state=42
)

model = XGBRegressor()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

r2 = r2_score(y_test, y_pred)

print(f'R2 Score: {r2}')