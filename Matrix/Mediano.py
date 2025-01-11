import math


arr=[[1, 3, 5], [2, 6, 9], [3, 6, 9]]
n=len(arr)
m=len(arr[0])
# print(arr[0])
arr1=[]

for i in range(n):
    for j in range(m):
        # print(arr[i][j])
        arr1.append(arr[i][j])
arr1.sort()
ceil=math.ceil((n*m)/2)
# print(math.ceil((n*m)/2))
print(arr1[ceil])