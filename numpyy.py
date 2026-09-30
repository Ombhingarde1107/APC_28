# 1# pyrefly: ignore [missing-import]
# import numpy as np

# arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

# print("Array:", arr)
# print("Size:", arr.size)
# print("Data Type:", arr.dtype)
# print("Dimensions:", arr.ndim)

# 2pyrefly: ignore [missing-import]
# import numpy as np 

# a = np.array([10, 20, 30, 40, 50])
# b = np.array([2, 4, 5, 8, 10])

# print("Addition:", a + b)
# print("Subtraction:", a - b)
# print("Multiplication:", a * b)
# print("Division:", a / b)
# print("Modulus:", a % b)
3
# import numpy as np

# arr = np.array([10, 25, 30, 45, 50, 65, 70, 80, 90, 100])

# print("Maximum:", np.max(arr))
# print("Minimum:", np.min(arr))
# print("Sum:", np.sum(arr))
# print("Average:", np.mean(arr))
4
# import numpy as np

# arr = np.arange(1, 21)

# even = arr[arr % 2 == 0]
# odd = arr[arr % 2 != 0]

# print("Even Numbers:", even)
# print("Odd Numbers:", odd)

5

# import numpy as np

# arr = np.arange(1, 13)

# print("2 x 6 Matrix:")
# print(arr.reshape(2, 6))

# print("\n3 x 4 Matrix:")
# print(arr.reshape(3, 4))

# print("\n4 x 3 Matrix:")
# print(arr.reshape(4, 3))
# 6
# import numpy as np

# a = np.array([[1, 2, 3],
#               [4, 5, 6],
#               [7, 8, 9]])

# b = np.array([[9, 8, 7],
#               [6, 5, 4],
#               [3, 2, 1]])

# result = a + b

# print("Matrix Addition:")
# print(result)

# 7
# import numpy as np

# a = np.array([[1, 2, 3],
#               [4, 5, 6]])

# b = np.array([[7, 8],
#               [9, 10],
#               [11, 12]])

# result = np.matmul(a, b)

# print("Matrix Multiplication:")
# print(result)

#8
# import numpy as np

# arr = np.array([[1, 2, 3, 4],
#                 [5, 6, 7, 8],
#                 [9, 10, 11, 12]])

# print("Original Matrix:")
# print(arr)

# print("Transpose:")
# print(arr.T)

# 9
# import numpy as np

# arr = np.array([[1, 2, 3, 4],
#                 [5, 6, 7, 8],
#                 [9, 10, 11, 12],
#                 [13, 14, 15, 16]])

# print("First Row:", arr[0])
# print("Last Column:", arr[:, -1])
# print("Diagonal Elements:", np.diag(arr))
# print("Second and Third Rows:")
# print(arr[1:3])

#10
# import numpy as np

# arr = np.array([[1, 2, 3, 4],
#                 [5, 6, 7, 8],
#                 [9, 10, 11, 12],
#                 [13, 14, 15, 16]])

# print("Sum of Each Row:", np.sum(arr, axis=1))
# print("Sum of Each Column:", np.sum(arr, axis=0))

#11
# import numpy as np

# arr = np.arange(1, 21)

# print("First 5 Elements:", arr[:5])
# print("Last 5 Elements:", arr[-5:])
# print("Alternate Elements:", arr[::2])
# print("Reverse Order:", arr[::-1])

#12
# import numpy as np

# arr = np.array([10, 25, 55, 40, 75, 30, 90, 45, 60, 20])

# arr[arr > 50] = 0

# print("Modified Array:", arr)

#13

# import numpy as np

# arr = np.array([50, 10, 80, 30, 20, 90, 40])

# ascending = np.sort(arr)
# descending = np.sort(arr)[::-1]

# print("Ascending Order:", ascending)
# print("Descending Order:", descending)

#14
# import numpy as np

# arr = np.array([10, 20, 10, 30, 20, 40, 30, 50])

# unique = np.unique(arr)

# print("Unique Elements:", unique)

#15
# import numpy as np

# a = np.array([[1, 2],
#               [3, 4]])

# b = np.array([[5, 6],
#               [7, 8]])

# print("Horizontal Concatenation:")
# print(np.hstack((a, b)))

# print("Vertical Concatenation:")
# print(np.vstack((a, b)))

#16
# import numpy as np

# marks = np.array([75, 80, 65, 90, 85, 70, 95, 60, 88, 78])

# print("Highest Marks:", np.max(marks))
# print("Lowest Marks:", np.min(marks))
# print("Average Marks:", np.mean(marks))
# print("Median:", np.median(marks))
# print("Standard Deviation:", np.std(marks))

#17
# import numpy as np

# marks = np.array([65, 78, 55, 90, 88, 72, 60, 95, 81, 69,
#                   85, 50, 76, 92, 63, 70, 89, 58, 80, 74])

# average = np.mean(marks)

# print("Class Average:", average)
# print("Marks Above Average:", marks[marks > average])

#18
# import numpy as np

# arr = np.arange(1, 25).reshape(2, 3, 4)

# print("3D Array:")
# print(arr)

# print("Number of Dimensions:", arr.ndim)
# print("Shape:", arr.shape)
# print("Size:", arr.size)

#19
# import numpy as np

# arr = np.arange(1, 25).reshape(2, 3, 4)

# print("First Element:", arr[0, 0, 0])
# print("Last Element:", arr[-1, -1, -1])
# print("Element at [0,1,2]:", arr[0, 1, 2])
# print("Element at [1,2,3]:", arr[1, 2, 3])

#20
# import numpy as np

# arr = np.arange(1, 25).reshape(2, 3, 4)

# print("Sum of All Elements:", np.sum(arr))
# print("Sum of Each Layer:")
# print(np.sum(arr, axis=(1, 2)))

# print("Sum Along Rows:")
# print(np.sum(arr, axis=2))

# print("Sum Along Columns:")
# print(np.sum(arr, axis=1))

#21
# import numpy as np

# arr = np.random.randint(1, 101, size=(2, 3, 4))

# print("Original Array:")
# print(arr)

# arr[arr > 50] = 0

# print("Modified Array:")
# print(arr)

#22
# import numpy as np

# arr = np.random.randint(1, 101, size=(3, 4, 5))

# print("Array:")
# print(arr)

# print("Mean:", np.mean(arr))
# print("Median:", np.median(arr))
# print("Standard Deviation:", np.std(arr))
# print("Variance:", np.var(arr))
# print("Minimum:", np.min(arr))
# print("Maximum:", np.max(arr))

#23
# import numpy as np

# arr = np.arange(1, 25).reshape(2, 3, 4)

# print("Original 3D Array:")
# print(arr)

# flat = arr.flatten()

# print("Flattened Array:")
# print(flat)

#24
# import numpy as np

# arr = np.arange(1, 28).reshape(3, 3, 3)

# flat = arr.flatten()

# print("Flattened Array:", flat)
# print("Sum:", np.sum(flat))
# print("Average:", np.mean(flat))
# print("Maximum:", np.max(flat))
# print("Minimum:", np.min(flat))

#25
# import numpy as np

# arr = np.random.randint(1, 101, size=(3, 4, 5))

# flat = arr.flatten()
# average = np.mean(flat)

# print("Original 3D Array:")
# print(arr)

# print("\nElements Greater Than 50:")
# print(flat[flat > 50])

# print("\nEven Numbers:")
# print(flat[flat % 2 == 0])

# print("\nElements Less Than Average:")
# print(flat[flat < average])

# print("\nAverage:", average)