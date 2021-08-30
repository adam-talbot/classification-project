import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

def clean_telco(df):
   '''
   This function takes in a df, drops unnecessary columns, cleans and changes data type for total_charges column, 
   renames categories for senior_citizen column, and removes redundant categories from 7 others columns
   '''
    df.drop(columns = ['payment_type_id', 'contract_type_id', 'internet_service_type_id', 'customer_id'], inplace=True)
    df.total_charges.replace(to_replace={' ' : '0'}, inplace = True)
    df.total_charges = df.total_charges.astype('float')
    df.senior_citizen = np.where(df.senior_citizen == 1, 'Yes', 'No')
    df.replace(to_replace='No internet service', value='No', inplace=True)
    df.replace(to_replace='No phone service', value='No', inplace=True)
    return df

def split_telco(df):
    '''
    This function takes in a df and splits it into train, validate, and test dfs
    final proportions will be 60/20/20 for train/validate/test
    '''
    train_validate, test = train_test_split(df, test_size=.2, random_state=123, stratify=df.churn)
    train, validate = train_test_split(train_validate, test_size=.25, random_state=123, stratify=train_validate.churn)
    return train, validate, test

def dummy_and_split_telco(df):
    '''
    This function takes in a df, creates dummies for all categorical columns,
    concats dummies onto original df, drops original columns that have been dummied,
    and splits the new df into 60/20/20 train/validate/test
    '''
    cat_cols = df.select_dtypes(include='object').columns.tolist()
    dummy_df = pd.get_dummies(df[cat_cols], drop_first = True)
    df_w_dummies = pd.concat([df, dummy_df], axis=1)
    df_w_dummies.drop(columns=cat_cols, inplace=True)
    train, test = train_test_split(df_w_dummies, test_size=.2, random_state=123, stratify=df_w_dummies.churn_Yes)
    train, validate = train_test_split(train, test_size=.25, random_state=123, stratify=train.churn_Yes)
    return train, validate, test

def prepare_telco(df):
    '''
    This function takes in a df, cleans the df, and splits the df
    '''
    df = clean_telco(df)
    train, validate, test = dummy_and_split(df)
    return train, validate, test