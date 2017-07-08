import numpy as np

A  = np.arange(3,15)

print(A)
'''
[ 3  4  5  6  7  8  9 10 11 12 13 14]
'''
print(A[3])
'''
6
'''

B = np.arange(3,15).reshape((3,4))
print(B)
'''
[[ 3  4  5  6]
 [ 7  8  9 10]
 [11 12 13 14]]
 '''
print(B[2])
'''
[11 12 13 14]
'''

print(B[1][1])
print(B[2,1])
'''
8
12
'''

print(B[1,:])
'''
[ 7  8  9 10]
'''

print(B[:,1])
'''
[ 4  8 12]
'''

print(B[1,1:3])
'''
[8 9]
'''

for row in B:
    print(row)
'''
[3 4 5 6]
[ 7  8  9 10]
[11 12 13 14]
'''

for col in B.T:
    print(col)
'''
[ 3  7 11]
[ 4  8 12]
[ 5  9 13]
[ 6 10 14]
'''
print(B.flatten())
'''
[ 3  4  5  6  7  8  9 10 11 12 13 14]
'''
for items in B.flat:
    print(items)
'''
3
4
5
6
7
8
9
10
11
12
13
14
'''