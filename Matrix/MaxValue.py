mat = [[ 1, 2, -1, -4, -20 ],
       [ -8, -3, 4, 2, 1 ],
       [ 3, 8, 6, 1, 3 ],
       [ -4, -1, 1, 7, -6 ],
       [ 0, -4, 10, -5, 1 ]]
n=len(mat)
# ans=0
# for i in range(0,len(mat)):
#     for j in range(0,len(mat)):
#         for k in range(i+1,n):
#             for m in range(j+1,n):
#                 # if k >i and m>j:
#                 ans=max(mat[m][k]-mat[i][j],ans)
# print(ans)

# Matrix
mat = [[1, 2, -1, -4, -20],
       [-8, -3, 4, 2, 1],
       [3, 8, 6, 1, 3],
       [-4, -1, 1, 7, -6],
       [0, -4, 10, -5, 1]]

# Initialize variables
max1 = float('-inf')  # Maximum value
max2 = float('-inf')  # Second maximum value
max1_pos = None       # Position of the maximum value
max2_pos = None       # Position of the second maximum value

# Traverse the matrix to find max1 and max2
for i in range(len(mat)):
    for j in range(len(mat[0])):
        if mat[i][j] > max1:       # Update maximum
            max2 = max1            # Previous max becomes second max
            # print(max2,'max',max1)
            # max2_pos = max1_pos
            max1 = mat[i][j]
            # max1_pos = (i, j)
        elif mat[i][j] > max2:     # Update second maximum
            max2 = mat[i][j]
            # max2_pos = (i, j)

# Compute the result
max_sum = max1 + max2

# Output
print(f"Maximum sum: {max_sum}")
print(max1,max2)
# print(f"Pair: {max1_pos} and {max2_pos} (Values: {mat[max1_pos[0]][max1_pos[1]]}, {mat[max2_pos[0]][max2_pos[1]]})")

    
