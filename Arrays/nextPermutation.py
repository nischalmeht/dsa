# arr=[1,2,3]
# idx,idx2=-1,-1
# for i in range(len(arr)-2,-1,-1):
#     if arr[i]<arr[i+1]:        
#         idx=i
#         break

# for i in range(len(arr)-2,-1,-1):
#     if(arr[idx]<arr[i]):
#         idx2=i
#         break
# arr[idx],arr[idx2]=arr[idx2],arr[idx]
# print(arr,'arrrr')


arr = [1, 3,4,2 ]

# Step 1: Find the first decreasing element from the end
idx = -1
for i in range(len(arr) - 2, -1, -1):
    if arr[i] < arr[i + 1]:
        idx = i
        break

if idx == -1:  # If no such element, reverse the array (last permutation)
    arr.reverse()
else:
    print(idx)
    # Step 2: Find the element just larger than arr[idx]
    for i in range(len(arr) - 1, idx, -1):
        if arr[i] > arr[idx]:
            # Step 3: Swap
            arr[idx], arr[i] = arr[i], arr[idx]
            break
    # Step 4: Reverse the part after idx
    # arr[idx + 1:] = reversed(arr[idx + 1:])

print(arr)
