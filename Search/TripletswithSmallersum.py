arr=[5, 1, 3, 4, 7]
ans=0
arr.sort()
totalsum=12
i=0
j=0
for k in range(0,len(arr)-2):
    i=i+1
    j=len(arr)-1
    while i<j:
        s=arr[i]+ arr[k]+ arr[j]
        if s<totalsum:
            ans+=j-i
            i+=1
        else:
            j-=1
(print(ans))
        
    
