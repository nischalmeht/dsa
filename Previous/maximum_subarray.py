arr=[1,12,-5,-6,50,3]
k=4
sum=0
for i in range(k):
    sum=arr[i]
    
start=0
end=k
maxsum=sum
while end<len(arr):
    sum-=arr[start]
    start+=1

    sum+=arr[end]
    end+=1
    maxsum = max(maxsum,sum)
    print(maxsum/k)



#     def findMaxAverage(nums, k):
#     # Get the sum for the starting window
#     window_sum = sum(nums[:k])
#     max_sum = window_sum

#     # Start sliding the window
#     start_index = 0
#     end_index = k
#     while end_index < len(nums):
#         # Remove the first element of the previous window
#         window_sum -= nums[start_index]
#         start_index += 1

#         # Add the next element to the window
#         window_sum += nums[end_index]
#         end_index += 1

#         # Update the maximum sum
#         max_sum = max(max_sum, window_sum)

#     # Return the average
#     return max_sum / k

# # Example usage
# nums = [1, 12, -5, -6, 50, 3]
# k = 4
# print(findMaxAverage(nums, k))  # Output: 12.75
