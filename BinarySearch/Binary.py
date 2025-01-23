def Binary(arr, k):
    low = 0
    high = len(arr) - 1
    if high>=low:
        mid=(high+low)//2
        if arr[mid]<k:
            return Binary(arr,low,mid-1,k)
    # while low <= high:
    #     mid = (low + high) // 2
    #     if arr[mid] > k:
    #         high = mid - 1
    #     elif arr[mid] < k:
    #         low = mid + 1
    #     else:
    #         return mid
    # return -1

# list1 = [12, 24, 32, 39, 45, 50, 54]
# n = 25
# bin = Binary(list1, n)
# if bin != -1:
#     print(str(bin))
# else:
#     print("no number found")
