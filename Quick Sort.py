arr = [50, 20, 80, 10, 40, 60, 30]
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = []
    right = []
    for i in range(1, len(arr)):
        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])
    return quick_sort(left) + [pivot] + quick_sort(right)
sorted_arr = quick_sort(arr)
print("Original Array:", arr)
print("Sorted Array:", sorted_arr)
