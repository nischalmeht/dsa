arr = [1,10, 20, 13, 12, 15, 3, 4, 5]
i=0
j=len(arr)-1
while i < j:
    if arr[i]>arr[i+1]:
        arr[i],arr[i+1]=arr[i+1],arr[i]
    i=i+1
    if i==j:
        i=0
        j-=1
     
print(arr)
    
