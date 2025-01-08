arr=[1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
steps=arr[0]
maxReach=arr[0]
jump=1

for i in range(1,len(arr)):
    if i==len(arr)-1:
        print(jump)
        exit()
    maxReach=max(maxReach,i + arr[i])
    steps=steps-1

    if steps==0:
        jump+=1
        if i>=maxReach:
            print(-1)
            exit()
        steps =maxReach-i
print(-1)
    
    
   
    