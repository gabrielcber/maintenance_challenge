"""
This is a boilerplate pipeline 'data_transforming'
generated using Kedro 0.18.0
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import PowerTransformer
from sklearn.preprocessing import LabelEncoder
from imblearn.over_sampling import SMOTE


def yeo_johnson(x_train, x_test):
    power = PowerTransformer(method='yeo-johnson', standardize=True)
    x_train = pd.DataFrame(power.fit_transform(x_train), columns = x_train.columns)
    x_test = pd.DataFrame(power.fit_transform(x_test), columns = x_test.columns)
    return x_train, x_test

def removing_bad_columns(x_train, x_test, list_of_columns):
    x_train.drop(list_of_columns, inplace=True, axis=1)
    x_test.drop(list_of_columns, inplace=True, axis=1)
    return x_train, x_test

def oversampling_with_smote(x_train, y_train):
    oversample = SMOTE()
    x_train, y_train = oversample.fit_resample(x_train, y_train)
    return x_train, y_train

def pre_training_transformation(x_train, x_test, y_train, y_test, list_of_columns):
    x_train, x_test = yeo_johnson(x_train, x_test)
    x_train, x_test = removing_bad_columns(x_train, x_test, list_of_columns)
    x_train, y_train = oversampling_with_smote(x_train, y_train)
    return x_train, y_train, x_test, y_test