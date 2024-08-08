import numpy as np
import math



x= np.array([1,2,3])
y = np.array([2,2,-5])
x_transpose = np.transpose(x)
y_transpose = np.transpose(y)
m = np.dot(x,y)
x_length = (np.dot(x,x_transpose))**(0.5)
y_length = (np.dot(y,y_transpose))**(0.5)
cos_theta = m/(x_length*y_length)
print(math.acos(cos_theta))