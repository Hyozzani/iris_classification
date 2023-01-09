import pandas as pd

df = pd.read_csv('Iris.csv', index_col=0)
print(df)

df_sort = df.to_csv('Iris_.csv')