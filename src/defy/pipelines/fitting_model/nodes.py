"""
This is a boilerplate pipeline 'fitting_model'
generated using Kedro 0.18.0
"""

import pickle
from sklearn.linear_model import RidgeClassifier
# import xgboost as xgb
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

def fitting_model(x_train, y_train):
    model = RidgeClassifier()
    model.fit(x_train, y_train)
    return model