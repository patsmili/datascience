## Create A DataFrame from dictionary

import pandas as pd

## creating dataframe by reading from a datz dictionary

data = [{'name': 'vikash', 'age': 27}, {'name': 'Satyam', 'age': 14}]
df = pd.DataFrame.from_dict(data, orient='columns')
df

## If the Dictionary is nested you first need to normalize it

from pandas.io.json import json_normalize

data = [
  {
    'name': {
      'first': 'vikash',
      'last': 'singh'
    },
    'age': 27
  },
  {
    'name': {
      'first': 'satyam',
      'last': 'singh'
    },
    'age': 14
  }
]

df = pd.DataFrame.from_dict(json_normalize(data), orient='columns')

df

##  creating dataframe by reading from a csv file

df = pd.read_csv('./data/sample_data.csv', index_col=False)
df

df_2 = pd.read_csv('./data/sample_data_2.csv', index_col=False, header=None)
df_2.columns = ['col_1', 'col_2', 'taget']
df_2

##Create A DataFrame with randomly generated data
import numpy as np

df = pd.DataFrame(np.random.randint(0,10,size=(10, 4)), columns=list('ABCD'))
df

## Merge dataframe by joining on a column

df = pd.DataFrame([[1, 3], [2, 4]], columns=['A', 'B'])
df

df2 = pd.DataFrame([[1, 5], [1, 6]], columns=['A', 'C'])
df2

df.merge(df2, how='left', on='A')  # merges on columns A
df

df2.drop_duplicates(subset=['A'], inplace=True)
df2

## merge dataframe by columns using index

df = pd.DataFrame([[1, 3], [2, 4]], columns=['A', 'B'])
df

df2 = pd.DataFrame([[1, 5], [1, 6]], columns=['A', 'D'])
df2

pd.concat([df, df2], axis=1)

## merge dataframe and split again.

ts1 = [1,2,3,4]
ts2 = [6,7,8,9]

dt = {'col_1': ts1, 'col_2': ts2}
dt

df_1 = pd.DataFrame(data=dt)
df_1

df_2 = pd.DataFrame(np.random.randn(3, 2), columns=['col_1', 'col_2'])
df_2

df_all = pd.concat((df_1, df_2), axis=0, ignore_index=True)
df_all

print(df_1.shape)
print(df_2.shape)
print(df_all.shape)

df_train = df_all[:df_1.shape[0]]
df_test = df_all[df_1.shape[0]:]

print(df_train.shape)
print(df_test.shape)
print(df_all.shape)