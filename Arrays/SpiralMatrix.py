matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
n = len(matrix)
m = len(matrix[0])

left = 0
right = m - 1
top = 0
bottom = n - 1
ans = []

while left <= right and top <= bottom:
    # Traverse from left to right
    for i in range(left, right + 1):
        ans.append(matrix[top][i])
    top += 1

    # Traverse from top to bottom
    for i in range(top, bottom + 1):
        ans.append(matrix[i][right])
    right -= 1

    # if top <= bottom:
        # Traverse from right to leftf
    for i in range(right, left - 1, -1):
                           
            ans.append(matrix[bottom][i])
    bottom -= 1

    # if left <= right:
        # Traverse from bottom to top
    for i in range(bottom, top - 1, -1):
            ans.append(matrix[i][left])
    left += 1

print("Spiral Order:", ans)
