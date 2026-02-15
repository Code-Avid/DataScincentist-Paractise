import numpy as np

X = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print(X.mean(axis=0))

print(X.mean(axis=1))