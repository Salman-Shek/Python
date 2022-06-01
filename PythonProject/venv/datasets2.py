import pandas as pd
from pandas.core.arrays import categorical
from pandas.core.indexes.numeric import Int64Index

data = {'age': [39, 50, 38, 53, 28, 37, 49, 52, 31, 42],
        'education-num': [13, 13,  9,  7, 13, 14,  5,  9, 14, 13],
        'workclass': ['State-gov', 'Self-emp-not-inc', 'Private', 'Private', 'Private', 'Private', 'Private', 'Self-emp-not-inc', 'Private', 'Private'],
        'income': ['<=50K', '<=50K', '<=50K', '<=50K', '<=50K', '<=50K', '<=50K', '>50K', '>50K', '>50K']
        }
df = pd.DataFrame(data)
finished_partitions = []

feature_columns = ['age', 'education-num', 'workclass']
finished_partitions = [Int64Index([2, 3, 6, 7], dtype='int64'),
                       Int64Index([4, 5, 8], dtype='int64'),
                       Int64Index([0, 1, 9], dtype='int64')]
feature_columns = ['age', 'education-num', 'workclass']


def agg_categorical_column(series):
    return [','.join(set(series))]

def agg_numerical_column(series):
    return [series.mean()]

## my code:

def Convert(a):
    it = iter(a)
    res_dct = dict(zip(it, it))
    return res_dct

aggregations = {}
for column in feature_columns:
    if column in categorical:
        aggregations[column] = agg_categorical_column # class 'function'. ex. output: {'age': <function agg_numerical_column at 0x7f314231c9e0>, 'education-num': <function agg_numerical_column at 0x7f314231c9e0>, 'workclass': <function agg_categorical_column at 0x7f314231c830>}
    else:
        aggregations[column] = agg_numerical_column   # class 'function'. ex. output: {'age': <function agg_numerical_column at 0x7f314231c9e0>, 'education-num': <function agg_numerical_column at 0x7f314231c9e0>, 'workclass': <function agg_categorical_column at 0x7f314231c830>}

partition = finished_partitions[0]
tmp = df.loc[partition] # Pandas DataFrame for partition, i, in partitions I
grouped_columns = tmp.agg(aggregations, squeeze=False) # Pandas Series