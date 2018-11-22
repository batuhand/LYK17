import numpy as np

d1 = np.diag([1,2,3])
d2 = np.diag([1,2,3], k = 1)

m1 = np.zeros((5,4))
m2 = np.ones((2,3))

print(d1)
print(d2)
print(m1)
print(m2)