from typing import List

# Kids With the Greatest Number of Candies
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:        
        ans=[]
        for i in range (len(candies)):
            if candies[i]+ extraCandies >= max(candies):
                ans.append(True)
            else:
                ans.append(False)        
        return ans
solution = Solution()

print(solution.kidsWithCandies([2,3,5,1,3],2))