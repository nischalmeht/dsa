arr = [1,10, 20, 13, 12, 15, 3, 4, 5]
for i in range(len(arr) - 1):  
    minIndex = i
    for j in range(i + 1, len(arr)):  
        if arr[j] > arr[minIndex]:  
            minIndex = j
    arr[minIndex], arr[i] = arr[i], arr[minIndex]  
print(arr)
