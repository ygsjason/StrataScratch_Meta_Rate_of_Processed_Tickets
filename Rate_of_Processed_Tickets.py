# Import your libraries
import pandas as pd
from functools import reduce

# Start writing code
df1 = facebook_complaints.drop_duplicates()

# the n of proccessed tickets for each type
df2 = df1.groupby('type')['processed'].apply(lambda x: x[x == True].count()).reset_index(name = 'n_prcd')
df2 = df1.groupby('type')['processed'].apply(lambda x: (x == True).sum()).reset_index(name = 'n_prcd')

# the n of total tickets for each type
df3 = df1.groupby('type')['processed'].count().reset_index(name = 'n_total')

dflist = [df2, df3]
df4 = reduce(lambda l,r: pd.merge(l, r, how = 'left', on = 'type'), dflist)
df5 = df4.assign(rate = lambda df: df.n_prcd/df.n_total)
