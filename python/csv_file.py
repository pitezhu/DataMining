import csv
import pandas as pd
filename = 'data.csv'
data1 = []
header = []
with open(filename, 'r') as csvf:
    dat = csv.reader(csvf)
    header = next(dat)
    for ra in dat:
        data1.append(ra[:10])
data2 = pd.DataFrame(data1, columns=[
    'year', 'date', 'year', 'date', 'year', 'date', 'year', 'date', 'year', 'date'])
data3 = data2.loc[1]
# print(data2['year'])
data4 = {'a': {'as': 1, 'bs': 2},
         'b': {'cs': 3, 'as': 3}}
data5 = pd.DataFrame(data4)
data5.index.name = 'shux'
data5.columns.name = 'state'
print(data5.values)
