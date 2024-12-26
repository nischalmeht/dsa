# Python3 program for the above approach

# Function to count the maximum number
# of pairs from given array with sum K
def maxPairs(nums, k):
	
	# Sort array in increasing order
	nums = sorted(nums)

	# Stores the final result
	result = 0

	# Initialize the left and right pointers
	start, end = 0, len(nums) - 1
	
	# Traverse array until start < end
	while (start < end):
		if (nums[start] + nums[end] > k):

			# Decrement right by 1
			end -= 1

		elif (nums[start] + nums[end] < k):

			# Increment left by 1
			start += 1
			
		# Increment result and left
		# pointer by 1 and decrement
		# right pointer by 1
		else:
			start += 1
			end -= 1
			result += 1

	# Print the result
	print(result)

# Driver Code
if __name__ == '__main__':
	
	arr = [ 1, 3,2 , 4 ]
	K = 5

	# Function Call
	maxPairs(arr, K)
	
# This code is contributed by mohit kumar 29
