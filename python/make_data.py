import pandas as pd
import numpy as np
import json
dat = pd.Series(np.random.randn(6), index=[
                ['a', 'a', 'c', 'b', 'b', 'd'], [1, 2, 3, 5, 4, 2]])
# print(dat['b'])
# print(dat.unstack())
dat.index.names = ['key1', 'key2']
# print(dat.swaplevel('key1', 'key2'))  # 交换层级索引
dat1 = pd.DataFrame({'a': range(7),
                     'b': range(7, 0, -1),
                     'c': ['one', 'one', 'one', 'two', 'two', 'two', 'two'],
                     'd': [0, 1, 2, 0, 1, 2, 3]})
dat2 = dat1.set_index(['c', 'd'])
dat3 = np.arange(12).reshape((3, 4))
print(dat3)
