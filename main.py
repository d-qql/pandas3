import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel(io='students_info.xlsx')
print(df)

dh = pd.read_html('results_ejudge.html')[0]
print(dh)
df1 = pd.merge(df, dh, left_on="login", right_on="User")
print(df1)
df2 = df1.groupby('group_faculty').sum()
df2["Average"] = df2["Solved"]/df1.groupby('group_faculty')['login'].count()
print(df2)
fig, ax = plt.subplots(1, 2)
df2['Average'].plot(kind='bar', ax=ax[0],
legend=False)
df2 = df1.groupby('group_out').sum()
df2["Average"] = df2["Solved"]/df1.groupby('group_out')['login'].count()
df2['Average'].plot(kind='bar', ax=ax[1],
legend=False)
plt.show()
groups = pd.merge(df1.loc[df1['G'] > 10],  df1.loc[df1['H'] > 10], on=['login', 'group_faculty', 'group_out', 'G', 'H'], how='outer').loc[:, ['login', 'group_faculty', 'group_out', 'G', 'H']]
print(groups)