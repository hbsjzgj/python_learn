import numpy as np

A = np.arange(2,14).reshape(3,4)
'''print(A)
[[ 2  3  4  5]
 [ 6  7  8  9]
 [10 11 12 13]]
 '''
print(np.argmin(A))
print(np.argmax(A))
'''元素的最小值和最大值的位置
np.argmin(A):0
np.argmax(A):11
'''

print(A.mean())
print(np.mean(A))
'''矩阵平均值
7.5
7.5
'''
print(np.average(A))
'''矩阵平均值
7.5
'''

print(np.median(A))
'''中位数
7.5
'''
print(np.cumsum(A))
'''累加
[ 2  5  9 14 20 27 35 44 54 65 77 90]
'''

print(np.diff(A))
'''累差
[[1 1 1]
 [1 1 1]
 [1 1 1]]
 '''

print(np.nonzero(A))
'''非零位置
(array([0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2]),  行 
 array([0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3]))  列'''

print(np.sort(A))
'''排序 逐行进行
[[ 2  3  4  5]
 [ 6  7  8  9]
 [10 11 12 13]]
'''

print(np.transpose(A))
print(A.T)
'''反向数列
[[ 2  6 10]
 [ 3  7 11]
 [ 4  8 12]
 [ 5  9 13]]
 
[[ 2  6 10]
 [ 3  7 11]
 [ 4  8 12]
 [ 5  9 13]]
'''
print((A.T).dot(A))
'''乘法运算
[[140 158 176 194]
 [158 179 200 221]
 [176 200 224 248]
 [194 221 248 275]]
 '''

print(np.clip(A,5,9))
'''小于5得数 变成5 
   大于9的数 变成9
[[5 5 5 5]
 [6 7 8 9]
 [9 9 9 9]]
 '''

print(np.mean(A,axis = 0))
'''axis = 0 对于列计算 平均值
[ 6.  7.  8.  9.]
'''

print(np.mean(A,axis = 1))
'''axis = 0 对于行计算 平均值
[  3.5   7.5  11.5]
'''