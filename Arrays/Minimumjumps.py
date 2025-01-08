arr= [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
arr1=[2,3,1,0,4]

# def minimumJumps(arr1):
#     jumps=0
#     for i in range(0,len(arr1)-1):
#         if i > jumps:
#             return False
#         jumps = max(jumps,i+ arr[i])
#     return jumps

# print(minimumJumps(arr1))

def min_jumps(arr):
    n = len(arr)
    if n <= 1:
        return 0  # No jump needed if the array has only one element
    
    if arr[0] == 0:
        return -1  # Cannot move forward if the first element is 0
    
    # Initialize variables
    maxReach = arr[0]
    steps = arr[0]
    jumps = 1  # Start with the first jump
    
    for i in range(1, n):
        # If we have reached the last index
        if i == n - 1:
            return jumps
        
        # Update maxReach
        maxReach = max(maxReach, i + arr[i])
        
        # Use a step to move to the next index
        steps -= 1
        
        # If no steps are left
        if steps == 0:
            jumps += 1  # Increment the jump count
            
            # If the current index is greater than or equal to maxReach, we cannot move further
            if i >= maxReach:
                return -1
            
            # Reinitialize steps
            steps = maxReach - i
    
    return -1  # If the end is not reachable



    
