import numpy as np


print("\n1. Creating Arraysn")
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([[1, 2], [3, 4]])
print(arr1)
print(arr2)


print("\n2. Special Arrays")
zeros = np.zeros((2, 3))
ones = np.ones((2, 3))
identity = np.eye(3)
print("Zeros:\n", zeros)
print("Ones:\n", ones)
print("Identity:\n", identity)


print("\n3. Array Properties")
arr = np.array([[1, 2, 3], [4, 5, 6]])
print("Shape:", arr.shape)
print("Dimensions:", arr.ndim)
print("Data type:", arr.dtype)
print("Size:", arr.size)

print("\n4. Reshape")
reshaped = arr.reshape(3, 2)
print(reshaped)


print("\n5. Arithmetic Operations")
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print("Add:", a + b)
print("Subtract:", a - b)
print("Multiply:", a * b)
print("Divide:", a / b)

print("\n 6. Mathematical Functions")
arr = np.array([1, 4, 9, 16])
print("Square root:", np.sqrt(arr))
print("Log:", np.log(arr))
print("Exponential:", np.exp(arr))

print("\n7. Aggregation")
arr = np.array([1, 2, 3, 4, 5])
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Max:", np.max(arr))
print("Min:", np.min(arr))
print("Std Dev:", np.std(arr))


print("\n8. Indexing & Slicing")
arr = np.array([10, 20, 30, 40, 50])
print("Element at index 2:", arr[2])
print("Slice:", arr[1:4])

print("\ns9. 2D Indexing")
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2d[0, 1])  

print("\n10. Boolean Masking")
arr = np.array([1, 2, 3, 4, 5])
print(arr[arr > 3])

print("\n11. Random Numbers")
print("Random:", np.random.rand(3))
print("Random Int:", np.random.randint(1, 10, 5))

print("\n 12. Linear Algebra ")
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
print("Matrix Multiply:\n", np.dot(a, b))
print("Determinant:", np.linalg.det(a))
print("Inverse:\n", np.linalg.inv(a))

print("\n 13. Broadcasting")
arr = np.array([1, 2, 3])
print(arr + 5)

print("\n15. Copy vs View ")
arr = np.array([1, 2, 3])
copy = arr.copy()
view = arr.view()
arr[0] = 99
print("Original:", arr)
print("Copy:", copy)
print("View:", view)