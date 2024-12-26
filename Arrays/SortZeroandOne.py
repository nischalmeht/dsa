arr=[0,1,1,0,0,0,1,0,1,1]
i=0
j=len(arr)-1
while i <=j:
    if arr[i]==0:
        i=i+1
    if arr[j]==1:
        j=j-1
    else:
        arr[i],arr[j]=arr[j],arr[i]
        i=i+1
        j=j+1
print(arr)