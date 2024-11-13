import numpy as np;
two_d_array = np.array([[1,2,3,4],
                       [5,6,7,8],
                       [9,10,11,12],[13,14,15,16]])
print("Original Array",two_d_array)
excluding_first_row=two_d_array[1:]
excluding_last_column=two_d_array[:,:-1]
column_in_row=two_d_array[1:3,0:2]
second_and_third_column=two_d_array[:,1:3]
second_and_third_of_1st_row=two_d_array[0, 1:3]
four_to_ten=two_d_array.ravel()[::-1][4:11]
print("Excluding first row",excluding_first_row)
print("Excluding last column",excluding_last_column)
print("First and second column in 2nd and 3rd row",column_in_row)
print("Elements of 2nd and 3rd column",second_and_third_column)
print("2nd and 3rd element of first row",second_and_third_of_1st_row)
print("Indices from 4 to 10",four_to_ten)
