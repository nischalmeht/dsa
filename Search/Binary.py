arr = [2, 3, 4, 10, 40]

start=0
end=len(arr)-1
mid=(start+end)//2
# print(arr[mid])
key=10
print(end)
while start<=end:
    if arr[mid]<key:
        start=mid+1
    elif arr[mid]>key:
        end=mid-1
    else:
        print(arr[mid])

