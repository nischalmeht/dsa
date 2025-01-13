mat=[[16, 28, 60, 64],[22, 41, 63, 91], [27, 50, 87, 93],[36, 78, 87, 94]]
def kth_smallest(matrix, k):
    n = len(matrix)
    low = matrix[0][0]
    high = matrix[-1][-1]
    
    while low < high:
        mid = low + (high - low) // 2
        count = 0
        
        # Count elements less than or equal to mid in each row
        for row in matrix:
            for val in row:
                if val <= mid:
                    count += 1
                else:
                    break  # Stop counting for this row as it's sorted
        
        if count < k:
            low = mid + 1
        else:
            high = mid
    
    return low
print(kth_smallest(mat,3))
# arr=[]
# for i in range(len(mat)):
#     for j in range(len(mat)):
#         arr.append(mat[i][j])
# arr.sort()
# k=3
# n=k-1
# print(arr[n])
