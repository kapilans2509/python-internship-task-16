# Task 16: Numerical Computing Using NumPy

import numpy as np

# 1. Create arrays of different dimensions

# 1D array
arr1 = np.array([1, 2, 3, 4, 5])
print("1D Array:", arr1)
print("Shape:", arr1.shape)

# 2D array
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("\n2D Array:\n", arr2)
print("Shape:", arr2.shape)

# 3D array
arr3 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("\n3D Array:\n", arr3)
print("Shape:", arr3.shape)

# 2. Perform mathematical operations (vectorized)
print("\nMathematical Operations:")
print("Addition:", arr1 + 5)
print("Multiplication:", arr1 * 2)
print("Square:", arr1 ** 2)

# 3. Broadcasting example
print("\nBroadcasting Example:")
matrix = np.array([[1, 2, 3], [4, 5, 6]])
vector = np.array([1, 1, 1])
print("Matrix + Vector:\n", matrix + vector)

# 4. Statistical functions
print("\nStatistical Functions:")
print("Mean:", np.mean(arr1))
print("Sum:", np.sum(arr1))
print("Max:", np.max(arr1))
print("Standard Deviation:", np.std(arr1))

# 5. Generate random data
random_array = np.random.rand(3, 3)
print("\nRandom 3x3 Array:\n", random_array)

# 6. Compare NumPy vs Python list

python_list = [1, 2, 3, 4, 5]

# Python list multiplication (not element-wise)
print("\nPython list * 2:", python_list * 2)

# NumPy element-wise multiplication
print("NumPy array * 2:", arr1 * 2)

# 7. Optimized calculation (vectorized sum)
large_array = np.arange(1, 1000001)
print("\nOptimized sum using NumPy:", np.sum(large_array))
