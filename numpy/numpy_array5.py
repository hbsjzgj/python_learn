import numpy as np

a = np.arange(4.0)
b = a
c = a
d = b
a[0] = 0.3
print(a)
'''
[ 0.3  1.   2.   3. ]
'''
print( b is a)
'''
True
'''
d[1:3]=[2.2,3.3]
'''
a:[ 0.3  2.2  3.3  3. ]
d:[ 0.3  2.2  3.3  3. ]
'''

b = a.copy()
a[3] = 6.6
'''
a:[ 0.3  2.2  3.3  6.6]
b:[ 0.3  2.2  3.3  3. ]
'''
print(a)
print(b)