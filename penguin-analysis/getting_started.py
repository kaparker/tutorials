import pandas as pd

"""
Data Analysis in python: Getting started with pandas
Exploring Palmer Penguins
Walk through of code in article: https://medium.com/@_kaparker/data-analysis-in-python-getting-started-with-pandas
"""

df = pd.read_csv('https://raw.githubusercontent.com/allisonhorst/palmerpenguins/47a3476d2147080e7ceccef4cf70105c808f2cbf/data-raw/penguins_raw.csv')

# Alternatvie IO
# import pymysql
# con = pymysql.connect(host='localhost', user='root', password='', db='test')
# read_sql(f'''SELECT * FROM table''', con)

if len(df) > 0:
    print(f'Length of df {len(df)}, number of columns {len(df.columns)}, dimensions {df.shape}, number of elements {df.size}.')
else:
    print(f'Problem loading df, df is empty.')

df.info()
df.info(memory_usage='deep')
print(df.memory_usage(deep=True))
print(df.memory_usage(deep=True).sum())

print(df.head())
pd.set_option('display.max_columns', None)
print(df.head())

keep_cols = ['Species', 'Region', 'Island', 'Culmen Length (mm)', 'Culmen Depth (mm)', 'Flipper Length (mm)', 'Body Mass (g)', 'Sex']
df = df.loc[:, keep_cols]	
print(df.columns)

df.info(memory_usage='deep')

print(df.isna().sum())

df['Sex'].fillna('Unknown', inplace=True)
print(df.isna().sum())

df.dropna(inplace=True)
print(df.isna().sum())

print(df['Species'].head())
print(df['Species'].nunique())
print(df['Species'].unique())

print(df.memory_usage(deep=True))
df['Species'] = df['Species'].astype('category')
print(df.memory_usage(deep=True))

for col in ['Region','Island','Sex']:
    print(f'Column: {col}, number of unique values, {df[col].nunique()}, unique values: {df[col].unique()}')

df.drop(columns=['Region'], inplace=True)
print(df.columns)

print((df['Sex']=='.').value_counts())
df['Sex'].replace('.','Unknown', inplace=True)
print((df['Sex']=='.').value_counts())

df['Sex'] = df['Sex'].astype('category')
df['Island'] = df['Island'].astype('category')

print(df.memory_usage(deep=True))
print(df.memory_usage(deep=True).sum())

df.info(memory_usage='deep')


