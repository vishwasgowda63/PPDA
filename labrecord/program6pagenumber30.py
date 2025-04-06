import numpy as np

# Create two 3x3 matrices with random integers between 1 and 10
matrix1 = np.random.randint(1, 11, size=(3, 3))
matrix2 = np.random.randint(1, 11, size=(3, 3))

# Matrix subtraction
subtraction_result = matrix1 - matrix2

# Element-wise division (with float output)
division_result = matrix1 / matrix2

# Display the results
print("Matrix 1:")
print(matrix1)

print("\nMatrix 2:")
print(matrix2)

print("\nMatrix Subtraction (Matrix1 - Matrix2):")
print(subtraction_result)

print("\nElement-wise Division (Matrix1 / Matrix2):")
print(division_result)

