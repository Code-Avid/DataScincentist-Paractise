import numpy as np

data = np.array([48, 49, 50, 51, 52, 500])

q1 = np.percentile(data, 25)
q3 = np.percentile(data, 75)
iqr = q3 - q1

lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr

outliers_iqr = data[(data < lower) | (data > upper)]
print(len(outliers_iqr),outliers_iqr)

