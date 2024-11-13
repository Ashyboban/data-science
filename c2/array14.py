print("23MCA030--GEORGE SCARIA")
import numpy as np
A=np.array([[1,2,3],
            [4,5,6],
            [7,8,9]])
B=np.array([[2,3,4],
            [5,6,7],
            [8,9,10]])
C=np.array([[3,4,5],
            [6,7,8],
            [9,10,11]])
result=np.dot(np.dot(A,B),C)
print("matrix A",A)
print("matrix B",B)
print("matrix C",C)
print("After multiplication",result)
