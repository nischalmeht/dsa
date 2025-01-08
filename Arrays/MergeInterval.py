intervals =[[1,3],[2,6],[8,10],[15,18]]
intervals = sorted(intervals, key=lambda x: x[0])
# print(intervals[0])
curent= intervals[0]
arr=[]
# for i in range(1,len(intervals)):
#     if curent[1] >= intervals[i][0]:
#         print(curent[1],'arrr')
#         curent=[curent[0], intervals[i][1]]
#         arr.append([curent[0], intervals[i][1]])
#     else:
#         arr.append(intervals[i])
# print(arr)
for i in range(1,len(intervals)):
    if curent[1]<intervals[i][0]:
        arr.append(curent)
        curent = intervals[i]
    else:
        curent[1]= max(curent[1],intervals[i][1])
    
arr.append(curent)
print(arr)
    