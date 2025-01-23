def FirstOccurance(arr,n):
    low=0
    high=len(arr)-1
    ans=-float("inf")
    while low < high:
        mid=(low+high)//2
        if arr[mid]>n:
            high=mid-1
        elif arr[mid]<n:
            low=mid+1
        else:
            ans=mid
            high=mid-1
    return ans

def lasttOccurance(arr,n):
    low=0
    high=len(arr)-1
    ans=-float("inf")
    while low < high:
        mid=(low+high)//2
        if arr[mid]>n:
            high=mid-1
        elif arr[mid]<n:
            low=mid+1
        else:
            ans=mid
            low=mid+1
    return ans

result=FirstOccurance([5,7,7,8,8,10],8)
result2=lasttOccurance([5,7,7,8,8,8,8,8,8,8,8,8,8,10],8)
print(result)
print(result2)
        