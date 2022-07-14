import pandas as pd
import numpy as np
from sqlalchemy import column
import matplotlib.pyplot as plt
obj = pd.Series([1, 2, 3, 4])
# print(obj.values)
# print(obj.index)
obj2 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
# print(obj2[['a']])
dat = {'d': 10, 'c': 20, 'e': 30}
states = ['a', 'd', 'c']
dara = pd.Series(dat, states)  # 生成Series序列
dara.name = 'zimu'
dara.index.name = 'values'  # 索引标记
# print(dara)
dara = dara.reindex(['a', 'g', 'c'])
# print(dara)
id = ['a', 'b', 'c', 'd']
cl = ['as', 'bs', 'cs', 'ds']
padata = pd.DataFrame(np.arange(16).reshape((4, 4)), index=id, columns=cl)
#padata.drop('as', axis=1, inplace=True)
# newdata = padata.loc['b', ['bs', 'cs']]  # loc为轴标签，iloc为整数标签
padata.plot()
plt.show()
