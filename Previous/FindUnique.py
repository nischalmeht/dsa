arr = [6, 2, 5, 2, 2, 6, 6]
ans = 0

print("Input array:", arr)

for num in arr:
    ans ^= num
    print(f"XOR so far: {ans}")

print("The unique element is:", ans)
