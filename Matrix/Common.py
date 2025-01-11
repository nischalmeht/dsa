# arr = [[1, 2, 1, 9, 8], 
#        [3, 7, 8, 5, 1], 
#        [8, 7, 7, 3, 1], 
#        [8, 1, 2, 7, 9]]

# n = len(arr)
# m = len(arr[0])
# r=4
# c=5
# mp=dict()
# for i in arr[0]:
#     mp[i]=1
# print(mp.keys())
       
# for i in range(1,r):
#     for j in range(c):
#         if arr[i][j] in mp.keys() and mp[arr[i][j]]== i:  
#             mp[arr[i][j]]=i+1
#         if i==r-1:
#            print(arr[i][j])


# A Program to prints common element 
# in all rows of matrix 

# Specify number of rows and columns 
M = 4
N = 5

# prints common element in all 
# rows of matrix 
def printCommonElements(mat): 

	mp = dict() 

	# initialize 1st row elements 
	# with value 1 
	for j in range(N): 
		mp[(mat[0][j])] = 1

	# traverse the matrix 
	for i in range(1, M): 
		for j in range(N): 
			
			# If element is present in the 
			# map and is not duplicated in 
			# current row. 
			if (mat[i][j] in mp.keys() and
							mp[(mat[i][j])] == i): 
								
			# we increment count of the 
			# element in map by 1 
				mp[(mat[i][j])] = i + 1

				# If this is last row 
				if i == M - 1: 
					print(mat[i][j], end = " ") 
			
# Driver Code 
mat = [[1, 2, 1, 4, 8], 
	[3, 7, 8, 5, 1], 
	[8, 7, 7, 3, 1], 
	[8, 1, 2, 7, 9]] 

printCommonElements(mat) 

# This code is contributed 
# by mohit kumar 29 
