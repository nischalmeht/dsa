
class Solution:
    def increasingTriplet(self, nums):
        n = len(nums)
        if n < 3:
            return False

        # Step 1: Create and populate leftMin array
        left_min = [0] * n
        left_min[0] = nums[0]
        for i in range(1, n):
            left_min[i] = min(left_min[i - 1], nums[i])
        
        # print(left_min)

        # Step 2: Create and populate rightMax array
        right_max = [0] * n
        right_max[-1] = nums[-1]
        print(right_max)
        
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], nums[i])
        # print(right_max,'right_max')

        # Step 3: Check for the triplet condition
        for i in range(1, n - 1):
            if left_min[i] < nums[i] < right_max[i]:
                print(nums)
                return True

        return False
solution= Solution()
print(solution.increasingTriplet([3,2,1,2,1]))