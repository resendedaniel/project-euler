from __future__ import division
import pandas as pd
import numpy as np

i, j = 0, 0
n = 2

def try_path(i, j, n = 2):
    x = 0
    if i == n or j == n:
        return 1
    else:
        x += try_path(i + 1, j, n)
        x += try_path(i, j + 1, n)
    return x

print(try_path(0,0,14))

x = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
y = [6, 20, 70, 252, 924, 3423, 12870, 48620, 184756, 705432, 2704156, 10400600, 40116600]

df = pd.DataFrame({'x':x, 'y':y})
df['ratio'] = np.concatenate([[np.nan], df['y'][1:len(y)].values/df['y'][0:(len(y)-1)].values])
df.plot(kind = 'scatter', x = 'x', y = 'ratio')