import pandas as pd
import boto3
import numpy as np
from multiprocessing import Pool





def read_from_efs(f_name, **kwargs):
    '''
    Input: file name in the efs `DrFraud/data` directory (ex: LEIE.csv)
    Output: pd.DataFrame
    '''
    f_path = '~/SageMaker/efs/DrFraud/data/{}'.format(f_name)
    df = pd.read_csv(f_path, index_col=0, low_memory=False, **kwargs)
    return df

def save_to_efs(df, f_name, **kwargs):
    '''
    Input: pd.DataFrame, file name in the efs `DrFraud/data` directory
    Output: None
    '''
    efs_path = '~/SageMaker/efs/DrFraud/data/{}'.format(f_name)
    return df.to_csv(efs_path, sep=',', **kwargs)

def read_s3(f_name, **kwargs):
    '''
    Input: file name in the `dast1healthcare` s3 bucket (ex: 06-2018 LEIE.csv)
    Output: pd.DataFrame
    '''
    s3 = boto3.client('s3')
    f_path = 's3://dast1healthcare/{}'.format(f_name)
    df = pd.read_csv(f_path, low_memory=False, **kwargs)
    return df

def add_year(df, year):
    '''
    Input: pd.DataFrame, year as `int` type
    Output: pd.DatafFrame with added `year` column
    '''
    df['year'] = pd.Series([year] * len(df))
    return df

    
def parallelize_dataframe(df, func):
    '''
    def multiply_columns(data):
    data['length_of_word'] = data['species'].apply(lambda x: len(x))
    return data
    
    iris = parallelize_dataframe(iris, multiply_columns)
    '''
    df_split = np.array_split(df, num_partitions)
    pool = Pool(num_cores)
    df = pd.concat(pool.map(func, df_split))
    pool.close()
    pool.join()
    return df