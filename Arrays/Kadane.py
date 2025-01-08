arr= [5, 4, 1, 7, 8]
cur_sum = 0
max_sum=0
for i in  range(0,len(arr)):
    cur_sum= cur_sum + arr[i]
    if cur_sum>max_sum:
        max_sum= cur_sum
    if cur_sum<0:
        cur_sum=0
print(max_sum,'max')