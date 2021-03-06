import numpy as np

#定义array类型
#a = np.array([2,23,4],dtype = np.int)
#a = np.array([2,23,4],dtype = np.int32)
#a = np.array([2,23,4],dtype = np.float32)
#print(a.dtype)

#a = np.array([[2,23,4],
#              [3,34,5]])

#定义全部为0的矩阵
a = np.zeros((3,4))
'''print
[[ 0.  0.  0.  0.]
 [ 0.  0.  0.  0.]
 [ 0.  0.  0.  0.]]
'''

a = np.ones((3,4))
'''print
[[ 1.  1.  1.  1.]
 [ 1.  1.  1.  1.]
 [ 1.  1.  1.  1.]]'''


a= np.arange(10,20,2)
'''print
[10 12 14 16 18]
'''
a= np.arange(12).reshape(3,4)
'''
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]'''

a = np.linspace(1, 10, 20).reshape(4,5)
'''
[[  1.           1.47368421   1.94736842   2.42105263   2.89473684]
 [  3.36842105   3.84210526   4.31578947   4.78947368   5.26315789]
 [  5.73684211   6.21052632   6.68421053   7.15789474   7.63157895]
 [  8.10526316   8.57894737   9.05263158   9.52631579  10.        ]]
 '''
print(a)