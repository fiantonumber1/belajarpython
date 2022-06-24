import numpy as np

# three dimensional arrays
m1 = ([1, 0],[0,1])
m2 = ([1,2],[0,1])
m2_inverse = np.linalg.inv(np.array(m2))


print("result")
m3 = np.dot(m2,m1)
m4 = np.dot(m3,m2_inverse)

print(m4)
