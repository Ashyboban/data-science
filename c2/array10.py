import numpy as np;
matrix_size=3
matrix=np.random.randint(10,20,size=(matrix_size,matrix_size))
print("Original Matrix")
print(matrix)
if np.linalg.matrix_rank(matrix)==matrix_size:
    inverse_matrix=np.linalg.inv(matrix)
    print("\nInverse Matrix:")
    print(inverse_matrix)
else:
    print("\nThe matrix is not invertible(rank is less than size)")
rank=np.linalg.matrix_rank(matrix)
print("\nRank of the Matrix:",rank)
determinant=np.linalg.det(matrix)
print("\nDeterminant of the matrix:",determinant)
matrix_1d=matrix.flatten()
print("\nMatrix as 1d array:")
print(matrix_1d)
eigenvalues,eigenvectors=np.linalg.eig(matrix)
print("\neigenvalues",eigenvalues)
print("\neigenvectors",eigenvectors)