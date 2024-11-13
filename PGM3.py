print("\nGeorge Scaria SJC23MCA030")
print("MCA 2023-2025\n")
def bubble_sort(arr):
    for n in range(len(arr) -1,0,-1):
        swapped=False
        for i in range(n):
            if arr[i] > arr[i+1]:
                swapped=True
                arr[i],arr[i+1] = arr[i+1],arr[i]
        if not swapped:
            return

n=int(input("Enter the number of elements:"))
arr=[]
for i in range(n):
    value=int(input(f"Enter the value{i+1}"))
    arr.append(value)
print("unsorted list is:")
print(arr)

bubble_sort(arr)
print("sorted list is:")
print(arr)