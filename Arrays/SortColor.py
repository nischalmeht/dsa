from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        red = 0  # Pointer for the position of the next 0
        white = 0  # Pointer for the current element
        blue = len(nums) - 1  # Pointer for the position of the next 2
        
        while white <= blue:
            if nums[white] == 0:  # Found a 0
                nums[red], nums[white] = nums[white], nums[red]
                red += 1
                white += 1
            elif nums[white] == 1:  # Found a 1
                white += 1
            else:  # Found a 2
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1

# Test case
nums = [0, 1, 1, 0, 2, 2]
solution = Solution()
solution.sortColors(nums)  # The function modifies nums in place
print(nums)  # Print the modified nums list
