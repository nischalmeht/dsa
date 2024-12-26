arr= [1, 2, 3, 4,6,2,9]
target=8
for i in range (0,len(arr)):
    for j in range (i+1,len(arr)):
        for k in range(j+1,len(arr)):
            if(arr[i]+ arr[j]+ arr[k]==target):
                print(arr[i],arr[j],arr[k])