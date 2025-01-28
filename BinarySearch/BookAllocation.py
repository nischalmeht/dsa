def isPossible(arr, n, m, mid):
    pageCount = 1
    totalSum = 0

    for i in range(n):
        if arr[i] > mid:  # If a single book exceeds `mid`, allocation is not possible
            return False

        if totalSum + arr[i] <= mid:
            totalSum += arr[i]
        else:
            pageCount += 1
            if pageCount > m:  # More students are required than allowed
                return False
            totalSum = arr[i]  # Allocate current book to the next student

    return True


def BookAllocation(arr, n, m):
    if m > n:  # Edge case: More students than books
        return -1

    s = 0  # Start of binary search
    e = sum(arr)  # Maximum possible allocation (all books to one student)
    ans = -1

    while s <= e:
        mid = (s + e) // 2  # Calculate the middle value
        if isPossible(arr, n, m, mid):
            ans = mid  # Update the answer with the current valid allocation
            e = mid - 1  # Try for a smaller maximum allocation
        else:
            s = mid + 1  # Try for a larger maximum allocation

    return ans


# Example usage
result = BookAllocation([7,2,5,10,8], 5, 2)
print(result)  # Output: 60
