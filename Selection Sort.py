arr = [5, 3, 8, 4, 2]
n = len(arr)
for i in range(n):
    min = i
    for j in range(i + 1, n):
        if arr[j] < arr[min]:
            min = j
    temp = arr[i]
    arr[i] = arr[min]
    arr[min] = temp
print("Sorted Array:", arr)
