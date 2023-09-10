import numpy as np

import matplotlib.pyplot as plt

data =  np.array([[2,1] ,[2,2],[3,2] ,[3,3], [4 ,1], [6,5], [7,4], [7, 5] ,[8, 5] ,[8, 6] ,[7, 7]])

mean = np.mean(data, axis=0)

data = data - mean
square_m = np.dot(data.T, data)
print("Covariance\n", square_m/len(data))
eigenvalues, eigenvectors = np.linalg.eig(square_m)

print("Eigenvalues\n",eigenvalues/len(data))
print("Eigenvectors\n",eigenvectors)
result = np.dot(data, eigenvectors[:, 0:2])

print("Projected Data\n",result)

v = np.var(result, axis=0, ddof=1)
sv = np.sum(v)
ve = np.array([v[0] / sv, v[1] / sv])
print("\nPercent variance explained computed: ")
print(ve)
plt.title("PCA1 and PCA2")
plt.plot(result)
plt.legend(["PCA 1", "PCA 2"])
plt.show()
