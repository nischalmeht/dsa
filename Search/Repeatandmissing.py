arr = [4, 3, 6, 2,2, 1, 1]
diction = dict()
arr2=[]
max_number = max(arr) + 1

# Initialize the dictionary with keys from 0 to max_number-1 and values as 0
for i in range(1,max_number):
    diction[i] = 0

# Count the frequency of each number in the array
for i in range(len(arr)):
    if arr[i] in diction:
        diction[arr[i]] += 1
for key,val in diction.items():
    if val>1 or val==0:

        print(key)   
# print(arr2)

