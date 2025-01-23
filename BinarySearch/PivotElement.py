# def PivotElement(arr):
#     low =0
#     end=len(arr)-1
#     # print(mid)
#     while low<end:
#      print("hhii")
     
#      mid=(low + end)//2
#      if arr[mid]>=arr[0]:
#         low=mid+1
#      else:
#         end=mid
#     return low
# result =PivotElement([1,7,3,6,5,6])
# print(result,'rr')


def PivotElement(arr):
    left_total=0
    total=sum(arr)
    for i in range(len(arr)):
        right_total =total-left_total-arr[i]
        if left_total== right_total:
            return i
        left_total+=arr[i]
    return -1
        

result =PivotElement([2,1,-1])
print(result,'rr')