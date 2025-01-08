arr=[2,3,1,-1,-4,4,-5]
ps,ns=0,1
nums= [0] * len(arr)
for i in range(0,len(arr)):
    if arr[i]>0:
        nums[ps]=arr[i]
        ps+=2
    else:
        nums[ns]=arr[i]
        ns+=2
print(nums)