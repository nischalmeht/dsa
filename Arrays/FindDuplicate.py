def findDuplicate(nums):
    for i in range(len(nums)):
        # Get the absolute value of the current element
        index = abs(nums[i]) - 1
        print(index,'innnn')
        # If the value at the index is negative, we've found our duplicate
        if nums[index] < 0:
            return index + 1
        # Mark the value at the index as visited (negative)
        nums[index] = -nums[index]
    
    # If no duplicate is found (though there should always be one)
    return -1

# Test case
nums = [3, 1, 3, 4, 2]
print("Duplicate number is:", findDuplicate(nums))
