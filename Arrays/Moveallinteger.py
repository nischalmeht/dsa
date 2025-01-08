arr = [-1, 2, -3, 4, 5, 6, -7, 8, 9]
# i=0
# j=len(arr)-1
# while i < j:
#     if arr[i]<0:
#         i=i+1
#     elif arr[j]>0:
#         j=j-1
#     else:
#         arr[i],arr[j]=arr[j],arr[i]
#         i=i+1
#         j=j-1
# print(arr)
i=0
j=len(arr)-1
while i < j:
    if arr[i]>0:
        i=i+1
    elif arr[j]<0:
        j=j-1
    else:
        arr[i],arr[j]=arr[j],arr[i]
        i=i+1
        j=j-1

k=0
while k< len(arr) and i < len(arr):
    arr[i],arr[k]=arr[k],arr[i]
    i=i+1
    k=k+2
print(arr)
    
