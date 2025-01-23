def Peak(arr):
    low=0
    end=len(arr)-1
    mid=(low + end)//2
    while low < end:
        if arr[mid]<arr[mid+1]:
            low=mid +1
        else:
            end=mid
        mid=(low + end)//2
    return low
result= Peak([0,10,5,2])
print(result)