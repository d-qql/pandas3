import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import openpyxl

df = pd.read_excel(io='students_info.xlsx', engine='openpyxl')
dh = pd.read_html('results_ejudge.html')
averagesolved1 = []
for i in range(1, 9):
    count1 = 0
    totalsolved1 = 0
    for j in df[df.group_faculty == i][['login']][df.login != 'NaN'][['login']].index:
        idE = str(df.at[j, 'login'])
        for k in range(len(dh[0].User)):
            if dh[0].User[k] == idE:
                idH = k
                break
        count1 = count1 + 1
        totalsolved1 = totalsolved1 + int(dh[0].loc[[k], 'Solved'])
    try:
        averagesolved1.append(totalsolved1 / count1)
    except:
        averagesolved1.append(0)
index1 = [1, 2, 3, 4, 5, 6, 7, 8]
plt.title('Faculty group rating')
plt.bar(index1, averagesolved1)
plt.show()
index2 = []

for i in range(len(df)):
    try:
        index2.index(int(df.at[i, 'group_out']))
        pass
    except:
        index2.append(int(df.at[i, 'group_out']))

print(index2)
averagesolved2 = []
for i in index2:
    count2 = 0
    totalsolved2 = 0
    for j in df[df.group_out == i][['login']][df.login != 'NaN'][['login']].index:
        idE = str(df.at[j, 'login'])
        for k in range(len(dh[0].User)):
            if dh[0].User[k] == idE:
                idH = k
                break
        count2 = count2 + 1
        totalsolved2 = totalsolved2 + int(dh[0].loc[[k], 'Solved'])
    try:
        averagesolved2.append(totalsolved2 / count2)
    except:
        averagesolved2.append(0)

plt.title('Out group rating')
plt.bar(index2, averagesolved2)
plt.show()








