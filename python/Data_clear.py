from sre_constants import CATEGORY_SPACE
import pandas as pd
import json
import numpy as np
from numpy import nan as NA
data = pd.Series([1, 2, NA, 4, NA])
#data = data[data.notnull()]
#data = data.dropna()

dat = pd.DataFrame([[1, 6, 3], [1, NA, NA], [NA, NA, NA], [NA, 6, 3]])
#dat = dat.dropna(how='all')
dat[4] = NA
dat.fillna({1: 1, 2: 2}, inplace=True)
dat.replace(NA, 1, inplace=True)

ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]
bins = [18, 25, 35, 60, 100]
cats = pd.cut(ages, bins)
# print(pd.value_counts(cats))
dats = np.random.randn(20)
dats = pd.cut(dats, 4, precision=2)

datas = pd.DataFrame(np.random.randn(1000, 4))
print(datas.describe())
