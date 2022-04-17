"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.18.0
"""

import numpy as np
import pandas as pd

def maintenance_initial_transformation(
    data_2020:pd.DataFrame
    , data_pre_2020:pd.DataFrame
):
    """Node to initialize maintenance dataset and bringing 2020 and pre 2020 data together.
    """

    data_2020['2020'] = '1'
    data_pre_2020['2020'] = '0'
    data = pd.concat([data_pre_2020, data_2020])
    return data
    
def remove_nan_rows_and_columns(
    data
    , NAN_COLUMN_THRESHOLD
    , NAN_ROW_THRESHOLD
):
    """This node removes rows and columns with more than a specific threshold
    percentual of NaN values.
    """

    column_thresh = data.shape[0]*NAN_COLUMN_THRESHOLD
    data = data.dropna(thresh=column_thresh, axis = 1)
    row_thresh = data.shape[1]*NAN_ROW_THRESHOLD
    data = data.dropna(thresh=row_thresh, axis = 0)
    return data

def correcting_nan(
    data:pd.DataFrame
):
    """Node to fix NaN values that are originally a 'na' string.
    """

    data = data.replace("na", np.nan)
    data = data.replace("neg", 0)
    data = data.replace("pos", 1)
    data = data.apply(pd.to_numeric)
    return data

def fill_na_with_median(
    data:pd.DataFrame
):
    """Filling NaN data with median of the column.
    """

    data = data.fillna(data.median())
    return data

def calculating_corr_matrix(
    data:pd.DataFrame
):
    """Node to calculate the corr() matrix.
    """

    corr = data.corr()
    return corr

def deleting_high_correlation_columns(
    data:pd.DataFrame
    , corr:pd.DataFrame
    , CORR_THRESHOLD
):
    """Node to eliminate one of the columns with higher than a specified correlation
    threshold percentual between them.
    """

    columns = np.full((corr.shape[0],), True, dtype=bool)
    for i in range(corr.shape[0]):
        for j in range(i+1, corr.shape[0]):
            if corr.iloc[i,j] >= CORR_THRESHOLD:
                if columns[j]:
                    columns[j] = False
    selected_columns = data.columns[columns]
    data = data[selected_columns]
    return data, selected_columns

def train_test_for_this_dataset(
    data:pd.DataFrame
    , flag_column
    , label
):
    """This node separates train and test in a speficic way for maintenance dataset, since
    we want to have pre_2020 data as a train set and 2020 data as test set. This is an
    alternative to train_test_split from scikit-learn.
    """

    train = data.loc[data['2020'] == 0].loc[:, data.columns != flag_column]
    test = data.loc[data['2020'] == 1].loc[:, data.columns != flag_column]
    x_train = train.loc[:, train.columns != label]
    x_test = test.loc[:, test.columns != label]
    y_train = train[label]
    y_test = test[label]
    return x_train, x_test, y_train, y_test

def maintenance_dataset_preparation(
    data:pd.DataFrame
    , CORR_THRESHOLD
    , NAN_COLUMN_THRESHOLD
    , NAN_ROW_THRESHOLD
    , flag_column
    , label
):
    """This will join all the functions for dataset preparation, since we won't
    need to run specific functions during exploration and modelling.
    """

    data = correcting_nan(data)
    data = remove_nan_rows_and_columns(data, NAN_COLUMN_THRESHOLD, NAN_ROW_THRESHOLD)
    data = fill_na_with_median(data)
    corr = calculating_corr_matrix(data)
    data, _ = deleting_high_correlation_columns(data, corr, CORR_THRESHOLD)
    x_train, x_test, y_train, y_test = train_test_for_this_dataset(data, flag_column, label)
    return data, corr, x_train, x_test, y_train, y_test