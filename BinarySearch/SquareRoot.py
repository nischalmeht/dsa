def Square(n):
    low = 0
    high = n
    ans = 0

    # Integer part of the square root
    while low <= high:
        mid = (low + high) // 2
        if mid * mid <= n:
            ans = mid  # Store the closest integer square root
            low = mid + 1
        else:
            high = mid - 1

    # Precision for the fractional part
    increment = 0.1
    for _ in range(1):  # Adjust `range` for more decimal places
        while ans * ans <= n:
            ans += increment
        ans -= increment  # Step back to the closest valid value

    return round(ans, 1)  # Round to 1 decimal place

# Example usage
result = Square(8)
print(result)  # Output: 2.8 (approximation to one decimal place)
