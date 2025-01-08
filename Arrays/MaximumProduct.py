arr=[2,3,-2,4]
maxp=float("-inf")
prod=1
for i in range(len(arr)):
            
            
            prod*=arr[i]
            maxp=max(prod, maxp)
            if prod==0:
                prod=1
prod=1            
for i in range(len(arr)-1,-1,-1):            
            prod*=arr[i]
            maxp=max(prod, maxp)
            if prod==0:
                prod=1

print(maxp,'Max')