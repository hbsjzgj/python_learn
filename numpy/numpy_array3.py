import numpy as np

A = np.ones(3)
B = np.array([2,2,2])
C = np.vstack((A,B))

D = np.hstack((A,B))
print(C)
'''上下合并
[[ 1.  1.  1.]
 [ 2.  2.  2.]]
 '''

print(D)
'''左右合并
[ 1.  1.  1.  2.  2.  2.]
'''

print(A[np.newaxis,:])
'''
[[ 1.  1.  1.]]
'''
print(A[np.newaxis,:].shape)
'''(1, 3)
'''
print(A[:,np.newaxis])
'''
[[ 1.]
 [ 1.]
 [ 1.]]
 '''
print(A[:,np.newaxis].shape)
'''
(3, 1)
'''
print(np.hstack((A[:,np.newaxis],B[:,np.newaxis])))
'''
[[ 1.  2.]
 [ 1.  2.]
 [ 1.  2.]]
 '''

E = np.concatenate((A,B,B,A),axis=0)
print(E)
'''
[ 1.  1.  1.  2.  2.  2.  2.  2.  2.  1.  1.  1.]
'''