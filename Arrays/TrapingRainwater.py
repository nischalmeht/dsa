arr=[0,1,0,2,1,0,1,3,2,1,2,1]
left=[]
leftindex=arr[0]

right=[]
righend=arr[-1]
for i in range(len(arr)):
    if(leftindex>arr[i]):
        left.append(leftindex)
    else:
        leftindex=arr[i]
        left.append(arr[i])

for i in range(len(arr)-1,-1,-1):   
    if(righend>arr[i]):
        right.append(righend)
    else:
        righend=arr[i]
        right.append(arr[i])
right.reverse()
ans=0
for i in range(len(arr)):
    # print(left[i])
    # print(arr[i])/
    ans+=min(left[i],right[i])-arr[i]
print(ans)