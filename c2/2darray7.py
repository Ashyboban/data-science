import numpy as np;
matrix1=np.array([[1,2,3],[4,5,6],[7,8,9]])
matrix2=np.array([[9,8,7],[6,5,4],[3,2,1]])
matrix_sum=matrix1+matrix2
matrix_diff=matrix1-matrix2
matrix_prod=matrix1*matrix2
matrix_div=matrix1/matrix2
matrix_multiply=np.dot(matrix1,matrix2)
matrix_trans=np.transpose(matrix1)
diagonal_sum=np.trace(matrix1)
print("matrix sum",matrix_sum)
print("Matrix diff",matrix_diff)
print("Matrix prod",matrix_prod)
print("Matrix_div",matrix_div)
print("Matrix multiply",matrix_multiply)
print("Matix Transpose",matrix_trans)
print("Matrix Diagonal Sum",diagonal_sum)

