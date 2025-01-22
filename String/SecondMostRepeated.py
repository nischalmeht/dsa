# arr=["aaa", "bbb", "ccc", "bbb", "aaa", "aaa"]
# dicts=dict()
# for i in range(len(arr)):    
#     if arr[i] not in dicts:        
#         dicts[arr[i]]=1
#     else:
#         dicts[arr[i]] +=len(arr[i])


arr = ["aaa", "bbb", "ccc", "bbb", "aaa", "aaa"]
dicts = dict()

for i in range(len(arr)):
    if arr[i] not in dicts:
        dicts[arr[i]] = 1  # Set the initial value as the length of the string
    else:
        dicts[arr[i]] += 1  # Increment by the length of the string


f_max = -float("inf")  # Initialize to negative infinity
second_max = -float("inf")  # Initialize second largest to negative infinity
ans=""
second_maxkey=None
# First, find the largest value (f_max)
for key, value in dicts.items():
    f_max = max(f_max, value)

# Then, find the second largest value (second_max)
for key, value in dicts.items():
    if value < f_max and value>second_max:  # Check for values less than the largest
        second_max = max(second_max, value)
        second_maxkey=key
        # ans=second_max[ans]


# Output the second largest value
print("Second Largest Value:", second_maxkey)

