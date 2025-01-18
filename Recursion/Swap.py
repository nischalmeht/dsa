def Swap(l, r, arr):
    # Base case: Stop recursion when left index exceeds the right index
    if l > r:
        return
    
    # Swap elements at indices l and r
    arr[l], arr[r] = arr[r], arr[l]
    
    # Recursive call, moving towards the middle
    Swap(l + 1, r - 1, arr)

# Example usage
arr = [1, 3, 4, 5, 8]
Swap(0, len(arr) - 1, arr)

# Output the reversed array
print(arr)  # Output: [8, 5, 4, 3, 1]
