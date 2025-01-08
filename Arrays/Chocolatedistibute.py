arr = [3, 4, 1, 9, 56, 7, 9, 12]
m = 5
n=len(arr)
arr.sort()
minDiff=float("inf")
for i in range(n-m+1):
    diff= arr[i+m-1] - arr[i]
    minDiff= min(diff,minDiff)
print(minDiff)


    