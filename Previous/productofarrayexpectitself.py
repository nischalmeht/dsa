# Function to calculate the product of all 
# elements except the current element
def productExceptSelf(arr):
    n = len(arr)

    # If only one element, return a list with 1
    if n == 1:
        return [1]

    left = [1] * n
    right = [1] * n
    prod = [1] * n

    # Construct the left array
    for i in range(1, n):
        left[i] = arr[i - 1] * left[i - 1]

    # Construct the right array
    for j in range(n - 2, -1, -1):
        right[j] = arr[j + 1] * right[j + 1]

    # Construct the product array using left[] and right[]
    for i in range(n):
        prod[i] = left[i] * right[i]

    return prod

# Driver code
arr = [1,2,3,4]
res = productExceptSelf(arr)

print(" ".join(map(str, res)))