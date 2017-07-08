import pandas as pd
import numpy  as np

s = pd.Series([1,2,6,np.nan,44,1])
'''
0     1.0
1     2.0
2     6.0
3     NaN
4    44.0
5     1.0
dtype: float64
'''
dates = pd.date_range('20160101',periods=6)
'''
DatetimeIndex(['2016-01-01', '2016-01-02', '2016-01-03', '2016-01-04',
               '2016-01-05', '2016-01-06'],
              dtype='datetime64[ns]', freq='D')
'''
df = pd.DataFrame(np.random.randn(6,4),index = dates,columns=['a','b','c','d'])
'''
                   a         b         c         d
2016-01-01 -1.356093  1.547215  2.078924  0.195829
2016-01-02 -1.582019  1.031998 -0.145557  1.358493
2016-01-03 -1.498136 -1.696422 -0.606822 -0.311891
2016-01-04  0.681333 -0.595401  1.646859  0.332776
2016-01-05 -0.038429 -0.390254  0.501133  0.198530
2016-01-06 -0.856171 -0.942062  0.123941 -0.719315
'''

df1 = pd.DataFrame(np.arange(12).reshape(3,4))
'''
   0  1   2   3
0  0  1   2   3
1  4  5   6   7
2  8  9  10  11
'''
df2 = pd.DataFrame({'A':1.,
                    'B':pd.Timestamp('20130102'),
                    'C':pd.Series(1,index=list(range(4)),dtype='float32'),
                    'D':np.array([3]*4,dtype='int32'),
                    'E':pd.Categorical(["test","train","test","train"]),
                    'F':'foo'})
'''
     A          B    C  D      E    F
0  1.0 2013-01-02  1.0  3   test  foo
1  1.0 2013-01-02  1.0  3  train  foo
2  1.0 2013-01-02  1.0  3   test  foo
3  1.0 2013-01-02  1.0  3  train  foo
'''

print(df2.dtypes)
'''
A           float64
B    datetime64[ns]
C           float32
D             int32
E          category
F            object
dtype: object
'''

print(df2.index)
'''
Int64Index([0, 1, 2, 3], dtype='int64')
'''

print(df2.columns)
'''
Index(['A', 'B', 'C', 'D', 'E', 'F'], dtype='object')
'''

print(df2.values)
'''
[[1.0 Timestamp('2013-01-02 00:00:00') 1.0 3 'test' 'foo']
 [1.0 Timestamp('2013-01-02 00:00:00') 1.0 3 'train' 'foo']
 [1.0 Timestamp('2013-01-02 00:00:00') 1.0 3 'test' 'foo']
 [1.0 Timestamp('2013-01-02 00:00:00') 1.0 3 'train' 'foo']]
 '''

print(df2.describe())
'''只显示数字形式
         A    C    D
count  4.0  4.0  4.0
mean   1.0  1.0  3.0
std    0.0  0.0  0.0
min    1.0  1.0  3.0
25%    1.0  1.0  3.0
50%    1.0  1.0  3.0
75%    1.0  1.0  3.0
max    1.0  1.0  3.0
'''

print(df2.T)
'''行列颠倒
                     0                    1                    2  \
A                    1                    1                    1   
B  2013-01-02 00:00:00  2013-01-02 00:00:00  2013-01-02 00:00:00   
C                    1                    1                    1   
D                    3                    3                    3   
E                 test                train                 test   
F                  foo                  foo                  foo   

                     3  
A                    1  
B  2013-01-02 00:00:00  
C                    1  
D                    3  
E                train  
F                  foo 
'''

print(df2.sort_index(axis = 1,ascending= False))
'''对 列进行排序   倒序 
     F      E  D    C          B    A
0  foo   test  3  1.0 2013-01-02  1.0
1  foo  train  3  1.0 2013-01-02  1.0
2  foo   test  3  1.0 2013-01-02  1.0
3  foo  train  3  1.0 2013-01-02  1.0
'''
print(df2.sort_index(axis = 0,ascending= False))
'''
     A          B    C  D      E    F
3  1.0 2013-01-02  1.0  3  train  foo
2  1.0 2013-01-02  1.0  3   test  foo
1  1.0 2013-01-02  1.0  3  train  foo
0  1.0 2013-01-02  1.0  3   test  foo
'''

print(df2.sort_values(by='E'))
''' 对E列 进行排序
     A          B    C  D      E    F
0  1.0 2013-01-02  1.0  3   test  foo
2  1.0 2013-01-02  1.0  3   test  foo
1  1.0 2013-01-02  1.0  3  train  foo
3  1.0 2013-01-02  1.0  3  train  foo

'''












