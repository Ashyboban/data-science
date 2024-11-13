print("\nGeorge Scaria SJC23MCA030")
print("MCA 2023-2025\n")
import numpy as np
array_2d=np.array( [ [1+2j, 3+4j, 5+6j], [7+8j, 9+10j, 11+12j] ],dtype=complex)
print("2d array")
print(array_2d)
row, column=array_2d.shape
print("Rows= ", row)
print("Column= ", column)
dimention=array_2d.ndim
print("Dimension of array : ", dimention)
reshape_array=array_2d.reshape(3,2)
print("reshaped array 3x2")
print(reshape_array)