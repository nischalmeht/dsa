arr=[0,1,0,3,12]
i,j=0,0
while j<len(arr):
    if(arr[j]!=0):
        arr[i],arr[j]=arr[j],arr[i]
        i+=1
    j+=1
print(arr)