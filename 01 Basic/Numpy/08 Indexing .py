import numpy as np

x = np.array([
    [25, 5000, 1],
    [32, 8000, 0],
    [40, 12000, 1],
    [28, 6000, 0],
])
# x[row,column]
print(x[1,0]) 
print(x[2,2]) 
print(x[:2,1]) 
print(x[:2,:2]) 

