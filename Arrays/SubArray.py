arr1=[11, 7, 1, 13, 21, 3, 7, 3]
arr2= [11, 3, 7, 1, 7]

# def subset(arr1,arr2):
#     for i in arr2:
#         if i in arr1:
#             continue
#         else:
#             return False
#     return True

# print(subset(arr1,arr2))

def subset(arr1,arr2):
    d1=dict()
    for  i in arr1:
        if i not in d1:
            d1[i]=1
        else:
            d1[i]+=1
    for i in arr2:
        if i not in d1:
            return "No"
        if i in d1 and d1[i]<1:
            return "NO"
        else:
            d1[i]-=1
    return True

print(subset(arr1,arr2))


# arr=["a","b","c"]
# i=0 
# j=len(arr)-1
# while i<=j:
#     if arr[i]=="b":
#         arr[i],arr[j]=arr[j],arr[i]
#         i=i+1
#         j=j-1
# print(arr)

