import pandas as pd
import boto3
import numpy as np
from multiprocessing import Pool
import matplotlib.pyplot as plt
from sklearn import metrics


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

def get_size(df):
    '''
    Get a the pd.dataframe size in Gigabytes.
    '''
    return str(round(sum(df.memory_usage()/10**6), 2)) + ' Mb'

def print_info(df, name_string):
    print('{} pd.DataFrame shape: {}'.format(name_string, df.shape))
    print('{} pd.DataFrame size: {}'.format(name_string, get_size(df)))
    
def get_intersection_by_npi(LEIE, PartD):
    npi_excl = set(LEIE['NPI'])
    npi = set(PartD['npi'])
    common_npi = npi_excl.intersection(npi)
    NPI_df = LEIE[['NPI','EXCLTYPE','EXCLDATE','REINDATE']][LEIE['NPI']\
                                                          .isin(common_npi)]\
                                                          .drop_duplicates()\
                                                          .reset_index(drop=True)
    return NPI_df

def get_NPI_counts(PartD, LEIE):
    PartD_npi = set(PartD['npi'])
    LEIE_npi = set(LEIE['NPI'][(LEIE['NPI'] != 0) & (pd.to_datetime(LEIE["EXCLDATE"], format="%Y%m%d").dt.year > 2013)])
    match_by_npi = PartD_npi.intersection(LEIE_npi)

    npi_dict = {'Participating healthcare providers in Medicare Part D': len(PartD_npi),
                'Excluded healthcare providers since 2014 with an NPI': len(LEIE_npi),
                'Total matches by NPI': len(match_by_npi)}

    NPI_counts = pd.DataFrame.from_dict(npi_dict, orient='index')
    NPI_counts.rename(columns={0:'Count'}, inplace=True)

    return NPI_counts

def bar_plot_NPI_count(NPI_counts):
    NPI_counts.plot.barh(logx=True, grid=True, figsize=(8,5), fontsize=14, legend=None, title='Count')
    
def run_random_forest(X,y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2, stratify=y)
    
    clf = RandomForestClassifier(n_jobs=-1)
    
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    return y_test, y_pred

def plot_roc(y_test, y_pred, title):
    fpr, tpr, threshold = metrics.roc_curve(y_test, y_pred)
    roc_auc = metrics.auc(fpr, tpr)

    # method I: plt
    plt.title(title)
    plt.plot(fpr, tpr, 'b', label = 'AUC = %0.2f' % roc_auc)
    plt.legend(loc = 'lower right')
    plt.plot([0, 1], [0, 1],'r--')
    plt.xlim([0, 1])
    plt.ylim([0, 1])
    plt.ylabel('True Positive Rate')
    plt.xlabel('False Positive Rate')
    plt.show()
    
def random_sample(X, y, size=1000000, minority_ratio=0.05):
    # add y to X
    X['label'] = y
    
    # Isolate minority & majority class
    X_minority = X[y].reset_index(drop=True)
    X_majority = X[~y].reset_index(drop=True)

    minority_idx = np.random.randint(low=0,high=X_minority.shape[0], size=round(size*minority_ratio))
    majority_idx = np.random.randint(low=0,high=X_majority.shape[0], size=round(size*(1-minority_ratio)))
    
    over_samp = X_minority.iloc[minority_idx]
    under_samp = X_majority.iloc[majority_idx]
    
    X_adj = pd.concat([over_samp, under_samp], axis=0).reset_index(drop=True)
    y_adj = X_adj.pop('label')
    
    return X_adj, y_adj

def grid_search_wrapper(refit_score='precision_score'):
    """
    fits a GridSearchCV classifier using refit_score for optimization
    prints classifier performance metrics
    """
    skf = StratifiedKFold(n_splits=10)
    grid_search = GridSearchCV(clf, param_grid, scoring=scorers, refit=refit_score,
                           cv=skf, return_train_score=True, n_jobs=-1)
    grid_search.fit(X_train.values, y_train.values)

    # make the predictions
    y_pred = grid_search.predict(X_test.values)

    print('Best params for {}'.format(refit_score))
    print(grid_search.best_params_)

    # confusion matrix on the test data.
    print('\nConfusion matrix of Random Forest optimized for {} on the test data:'.format(refit_score))
    print(pd.DataFrame(confusion_matrix(y_test, y_pred),
                 columns=['pred_neg', 'pred_pos'], index=['neg', 'pos']))
    return grid_search

def conf_mat(y_test, y_pred):
    y_test = pd.Series(y_test, name='Actual')
    y_pred = pd.Series(y_pred, name='Predicted')
    return pd.crosstab(y_test, y_pred, ).T