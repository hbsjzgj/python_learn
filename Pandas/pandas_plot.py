import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#plot data

#Series

data = pd.Series(np.random.randn(1000),index= np.arange(1000))
data = data.cumsum()


#DataFrame

data = pd.DataFrame(np.random.randn(1000,4),index=np.arange(1000),columns=list("ABCD"))
data = data.cumsum()
'''
          A         B         C         D
0 -0.586466  0.965355 -0.362573  0.179765
1 -2.356683  0.610555 -0.383524  1.834141
2 -2.668768 -1.358930 -1.813230  0.920994
3 -0.360695 -3.097826 -1.628483  3.050044
4  0.154818 -4.054771 -1.947719  3.540866
'''
#data.plot()
#plot methods:
#'bar','hist','box','kde','area','scatter','hexbin','pie'
ax=data.plot.scatter(x='A',y='B',color='DarkBlue',label='Class 1')
data.plot.scatter(x='A',y='C',color='DarkGreen',label='Class 2',ax=ax)
plt.show()