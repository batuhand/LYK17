import numpy as np

x1 = np.arange(0,10,1)
x2 = np.arange(-1,1,0.1)
print(x1)
print(x2)


l1 = np.linspace(0,10,10)
l2 = np.logspace(0,10,10,base = 2)
print(l1)
print(l2)



x,y = np.mgrid[0:5,0:5]
print(x)
print(y)