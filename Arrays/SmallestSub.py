class Solution:
    def sb(self, nums, x):
        # Your code goes here 
        left=0
        current=0
        length=float("inf")
        for i in range(len(nums)):
            print(i)
            current+=nums[i]
            while current>x:
                length=min(length, i+1-left)
                
                current-=nums[left]
                left+=1
        if length==float("inf"):
            return 0
        return length
solution = Solution()
print(solution.sb([1, 4, 45, 6, 0, 19],51))