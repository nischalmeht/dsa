def threeSum(nums):
    st = set()  # To store unique triplets
    n = len(nums)

    for i in range(n):
        hashset = set()
        for j in range(i + 1, n):
            third = -(nums[i] + nums[j])  # The number needed to form a triplet
            
            # If 'third' is already in hashset, we found a valid triplet
            if third in hashset:
                temp = tuple(sorted([nums[i], nums[j], third]))  # Sort to avoid duplicate triplets
                st.add(temp)  # Store in set to remove duplicates
            
            hashset.add(nums[j])  # Store j-th element in hash set

    return list(map(list, st))  # Convert set of tuples to a list of lists

# Example Usage
nums = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums))
