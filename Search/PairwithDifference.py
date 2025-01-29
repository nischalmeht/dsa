arr= [5, 20, 3, 2, 5, 80]
ans=-1
x=78
# for i in range(0,len(arr)):
#     y=arr[i] + x
#     for j in range(0,len(arr)):       
#         if arr[j]==y:
#             print(arr[i])
#             ans=1
#             break
# print(ans)
    
arr = [5, 20, 3, 2, 5, 80]
arr.sort()  # Sorting the array (O(N log N))

for i in range(len(arr) - 1):
    target = arr[i] + 78  # Look for arr[j] such that arr[j] = arr[i] + 78
    # Binary search for the target value
    low, high = i + 1, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            print(arr[mid], arr[i])
            break
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
