import pandas as pd

left1 = pd.DataFrame({'Key':['K0','K1','K2','K3'],
                       'A':['A0','A1','A2','A3'],
                       'B':['B0','B1','B2','B3']})
right1= pd.DataFrame({'Key':['K0','K1','K2','K3'],
                       'C':['C0','C1','C2','C3'],
                       'D':['D0','D1','D2','D3']})
'''
    A   B Key
0  A0  B0  K0
1  A1  B1  K1
2  A2  B2  K2
3  A3  B3  K3
    C   D Key
0  C0  D0  K0
1  C1  D1  K1
2  C2  D2  K2
3  C3  D3  K3
'''

res = pd.merge(left1,right1,on='Key')
'''
    A   B Key   C   D
0  A0  B0  K0  C0  D0
1  A1  B1  K1  C1  D1
2  A2  B2  K2  C2  D2
3  A3  B3  K3  C3  D3
'''
left2 = pd.DataFrame({'Key1':['K0','K0','K1','K2'],
                      'Key2':['K0','K1','K0','K1'],
                       'A':['A0','A1','A2','A3'],
                       'B':['B0','B1','B2','B3']})
right2= pd.DataFrame({'Key1':['K0','K1','K1','K2'],
                    'Key2':['K0','K0','K0','K0'],
                       'C':['C0','C1','C2','C3'],
                       'D':['D0','D1','D2','D3']})

'''
    A   B Key1 Key2
0  A0  B0   K0   K0
1  A1  B1   K0   K1
2  A2  B2   K1   K0
3  A3  B3   K2   K1
    C   D Key1 Key2
0  C0  D0   K0   K0
1  C1  D1   K1   K0
2  C2  D2   K1   K0
3  C3  D3   K2   K0
'''
#how = ['left','right','outer','inner']
res = pd.merge(left2,right2,on=['Key1','Key2'],how='inner')
'''基于左右共同的Key合并
    A   B Key1 Key2   C   D
0  A0  B0   K0   K0  C0  D0
1  A2  B2   K1   K0  C1  D1
2  A2  B2   K1   K0  C2  D2
'''

res = pd.merge(left2,right2,on=['Key1','Key2'],how='outer')
'''基于左右所有的Key合并
     A    B Key1 Key2    C    D
0   A0   B0   K0   K0   C0   D0
1   A1   B1   K0   K1  NaN  NaN
2   A2   B2   K1   K0   C1   D1
3   A2   B2   K1   K0   C2   D2
4   A3   B3   K2   K1  NaN  NaN
5  NaN  NaN   K2   K0   C3   D3
'''
res = pd.merge(left2,right2,on=['Key1','Key2'],how='right')
'''基于右侧的Key合并
     A    B Key1 Key2   C   D
0   A0   B0   K0   K0  C0  D0
1   A2   B2   K1   K0  C1  D1
2   A2   B2   K1   K0  C2  D2
3  NaN  NaN   K2   K0  C3  D3
'''

#indicator
df1=pd.DataFrame({'col1':[0,1],'col_left':['a','b']})
df2=pd.DataFrame({'col1':[1,2,2],'col_right':[2,2,2]})
'''
   col1 col_left
0     0        a
1     1        b
   col1  col_right
0     1          2
1     2          2
2     2          2
'''

res = pd.merge(df1,df2,on='col1',how='outer',indicator=True)
'''
   col1 col_left  col_right      _merge
0     0        a        NaN   left_only
1     1        b        2.0        both
2     2      NaN        2.0  right_only
3     2      NaN        2.0  right_only
'''
res = pd.merge(df1,df2,on='col1',how='outer',indicator='indicator_column')
'''
   col1 col_left  col_right indicator_column
0     0        a        NaN        left_only
1     1        b        2.0             both
2     2      NaN        2.0       right_only
3     2      NaN        2.0       right_only

'''

#merged by index
left3 = pd.DataFrame({ 'A':['A0','A1','A2'],
                       'B':['B0','B1','B2']},
                       index=['K0','K1','K2'])
right3= pd.DataFrame({ 'C':['C0','C2','C3'],
                       'D':['D0','D2','D3']},
                     index=['K0','K2','K3'])
'''
     A   B
K0  A0  B0
K1  A1  B1
K2  A2  B2
     C   D
K0  C0  D0
K2  C2  D2
K3  C3  D3
'''
res = pd.merge(left3,right3,left_index=True,right_index=True,how='outer')
'''
      A    B    C    D
K0   A0   B0   C0   D0
K1   A1   B1  NaN  NaN
K2   A2   B2   C2   D2
K3  NaN  NaN   C3   D3
'''
res = pd.merge(left3,right3,left_index=True,right_index=True,how='inner')
'''
     A   B   C   D
K0  A0  B0  C0  D0
K2  A2  B2  C2  D2
'''

print(res)


