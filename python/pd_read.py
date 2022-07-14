import numpy as np
import pandas as pd
import json
dat = pd.read_csv('data.csv', nrows=10)
print(dat.to_json())
dat.to_csv('data_out.csv')

date = pd.date_range('1/1/2000', periods=7)
ts = pd.Series(np.arange(7), index=date)
ts.to_csv('dates.csv')
