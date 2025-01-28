def pivot(arr, n):
    low = 0
    high = n - 1
    while low < high:
        mid = (low + high) // 2
        if arr[mid] > arr[high]:
            low = mid + 1
        else:
            high = mid
    return low

def binarySearch(arr, low, high, target):
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1

def SearchEl(arr, target):
    n = len(arr)
    pivot_index = pivot(arr, n)
    
    # Determine which part of the array to search
    if target >= arr[pivot_index] and target <= arr[n - 1]:
        return binarySearch(arr, pivot_index, n - 1, target)
    else:
        return binarySearch(arr, 0, pivot_index - 1, target)

# Test the function
result = SearchEl([4,5,6,7,0,1,2], 3)
print(result)  # Output: 4 (index of 0)
