import matplotlib.pyplot as plt



x1 = [1, 2, 3, 4, 5]
y1 = [2, 4, 3, 6, 5]

x2 = [2, 3, 4, 5, 6]
y2 = [3, 4, 5, 6, 7]

plt.scatter(x1, y1, color='red', marker='o', label='Data Points1')
plt.scatter(x2, y2, color='blue', marker='x', label='Data Points2')
plt.legend()
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Scatter Plot")
plt.show()
