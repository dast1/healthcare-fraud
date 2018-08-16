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

import re, math
from collections import Counter

WORD = re.compile(r'\w+')

def get_cosine(vec1, vec2):
    # print vec1, vec2
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x]**2 for x in vec1.keys()])
    sum2 = sum([vec2[x]**2 for x in vec2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator

def text_to_vector(text):
    return Counter(WORD.findall(text))

def get_similarity(pair):
    a = text_to_vector(pair[0].strip().lower())
    b = text_to_vector(pair[1].strip().lower())

    return get_cosine(a, b)


def plot_multi(data, threshold_value, xlabel, cols=None, spacing=.1, **kwargs):

    from pandas import plotting

    # Get default color style from pandas - can be changed to any other color list
    if cols is None: cols = data.columns
    if len(cols) == 0: return
    colors = getattr(getattr(plotting, '_style'), '_get_standard_colors')(num_colors=len(cols))

    # First axis
    ax = data.loc[:, cols[0]].plot(label=cols[0], color=colors[0], **kwargs)
    ax.set_ylabel(ylabel=cols[0])
    lines, labels = ax.get_legend_handles_labels()

    for n in range(1, len(cols)):
        # Multiple y-axes
        ax_new = ax.twinx()
        ax_new.spines['right'].set_position(('axes', 1 + spacing * (n - 1)))
        data.loc[:, cols[n]].plot(ax=ax_new, label=cols[n], color=colors[n % len(colors)])
        ax_new.set_ylabel(ylabel=cols[n])

        # Proper legend position
        line, label = ax_new.get_legend_handles_labels()
        lines += line
        labels += label
    
    # add State threshold
    threshold_value = threshold_value
    ax.axvline(threshold_value, color='r', linestyle='-', linewidth=.5)
    
    ax.legend(lines, labels, loc=0)
    ax.grid(color='k', linestyle='--', linewidth=1)
    ax.set_xlabel(xlabel=xlabel)
    return ax

def plot_multi_log(data, threshold_value, xlabel, cols=None, spacing=.1, **kwargs):

    from pandas import plotting

    # Get default color style from pandas - can be changed to any other color list
    if cols is None: cols = data.columns
    if len(cols) == 0: return
    colors = getattr(getattr(plotting, '_style'), '_get_standard_colors')(num_colors=len(cols))

    # First axis
    ax = data.loc[:, cols[0]].plot(label=cols[0], color=colors[0], **kwargs)
    ax.set_ylabel(ylabel=cols[0])
    lines, labels = ax.get_legend_handles_labels()

    for n in range(1, len(cols)):
        # Multiple y-axes
        ax_new = ax.twinx()
        ax_new.spines['right'].set_position(('axes', 1 + spacing * (n - 1)))
        data.loc[:, cols[n]].plot(ax=ax_new, label=cols[n], color=colors[n % len(colors)])
        ax_new.set_ylabel(ylabel=cols[n])

        # Proper legend position
        line, label = ax_new.get_legend_handles_labels()
        lines += line
        labels += label
    
    # add State threshold
    threshold_value = threshold_value
    ax.axvline(threshold_value, color='r', linestyle='-', linewidth=.5)
    
    ax.legend(lines, labels, loc=0)
    ax.grid(color='k', linestyle='--', linewidth=1)
    ax.set_xlabel(xlabel=xlabel)
    return ax

def log_plot(data, threshold, title, ylabel, xlabel, **kwargs):
    ax = data.plot(**kwargs)
    ax.axvline(threshold, color='r', linestyle='-', linewidth=1)
    ax.grid(color='k', linestyle='--', linewidth=1)
    ax.legend([ylabel, 'Threshold at {} position'.format(threshold)])
    ax.set_ylabel(ylabel=ylabel)
    ax.set_xlabel(xlabel=xlabel)
    return ax