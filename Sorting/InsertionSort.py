arr=[1,2,4,5,9,3,8]


for i in range(1,len(arr)):
    temp=arr[i]
    # j=i-1
    for j in range(i-1,0):
        if arr[j]>temp:
            arr[j+1]=arr[j]
            
        else:
            break
       

print(arr)            



        
