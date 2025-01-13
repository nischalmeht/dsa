arr= [[0,1,1,1], [0,0,1,1], [1,1,1,1], [0,0,0,0]]
def MaxOne(arr):
    maxRow=0
    current_row=-1
    for i in range(len(arr)):
        if arr[i]==1:
            # print(i,'index')
            maxRow+=1

    # print(max(maxRow))
            # break
# print(MaxOne())            
        
for i in range(len(arr)):
    MaxOne(arr[i])