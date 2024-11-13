import numpy as np
even_numbers=np.arange(2,31,2)
slice_result=even_numbers[2:9:2]
last_3_elements=even_numbers[-3:]
alternate_elements=even_numbers[::2]
last_3_alternate_elements=alternate_elements[-3:]
print("array",even_numbers)
print("numbers 2 to 8",slice_result)
print("Last 3 elements",last_3_elements)
print("Alternate elements",alternate_elements)
print("The last 3 alternate elements",last_3_alternate_elements)
