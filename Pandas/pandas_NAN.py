import pandas as pd
import numpy as np

dates = pd.date_range('20160101',periods=6)
df = pd.DataFrame(np.arange(24).reshape(6,4),index = dates,columns=['A','B','C','D'])
df.iloc[0,1] = np.nan
df.iloc[1,2] = np.nan
'''
             A     B     C   D
2016-01-01   0   NaN   2.0   3
2016-01-02   4   5.0   NaN   7
2016-01-03   8   9.0  10.0  11
2016-01-04  12  13.0  14.0  15
2016-01-05  16  17.0  18.0  19
2016-01-06  20  21.0  22.0  23
'''
df.dropna(axis = 0 , how = 'any')#how = {'any',all}
'''
             A     B     C   D
2016-01-03   8   9.0  10.0  11
2016-01-04  12  13.0  14.0  15
2016-01-05  16  17.0  18.0  19
2016-01-06  20  21.0  22.0  23
'''
df.dropna(axis = 1 , how = 'any')
'''
             A   D
2016-01-01   0   3
2016-01-02   4   7
2016-01-03   8  11
2016-01-04  12  15
2016-01-05  16  19
2016-01-06  20  23
'''

#print(df.fillna(value = 0))
'''NAN -> 0
             A     B     C   D
2016-01-01   0   0.0   2.0   3
2016-01-02   4   5.0   0.0   7
2016-01-03   8   9.0  10.0  11
2016-01-04  12  13.0  14.0  15
2016-01-05  16  17.0  18.0  19
2016-01-06  20  21.0  22.0  23
'''

print(df.isnull())
'''check NAN  T or F
                A      B      C      D
2016-01-01  False   True  False  False
2016-01-02  False  False   True  False
2016-01-03  False  False  False  False
2016-01-04  False  False  False  False
2016-01-05  False  False  False  False
2016-01-06  False  False  False  False
'''

print(np.any(df.isnull())== True)
''' check all of matrix
True
'''



