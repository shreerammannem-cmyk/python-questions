# create the below matrix A and B with python
# A = 1 2 3
#     4 5 6
#     7 8 9 
# 
# B = 1 2 1
#     6 2 3
#     4 2 1 
# 
# Add these two matrices and store it in C 
# Create matrix A
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Create matrix B
B = [
    [1, 2, 1],
    [6, 2, 3],
    [4, 2, 1]
]

# Create matrix C with zeros
C = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

# Add matrices A and B
for i in range(3):
    for j in range(3):
        C[i][j] = A[i][j] + B[i][j]

# Print Matrix A
print("Matrix A:")
for row in A:
    print(row)

# Print Matrix B
print("\nMatrix B:")
for row in B:
    print(row)

# Print Matrix C
print("\nMatrix C (A + B):")
for row in C:
    print(row)