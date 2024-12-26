from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if(n==0):
            return True
        for i in range(len(flowerbed)):
            left_khali = flowerbed[i-1] or i==0
            right_khali = flowerbed[i+1]==0 or i == len(flowerbed)-1

            if(left_khali and right_khali):
                flowerbed[i]=1
                n=n-1
            if(n==0):
                return True
solution = Solution()
print(solution.canPlaceFlowers([1,0,0,0,1], 1))

# from typing import List

# class Solution:
#     def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
#         if n == 0:
#             return True
        
#         for i in range(len(flowerbed)):
#             if flowerbed[i] == 0:
#                 left_empty = (i == 0 or flowerbed[i-1] == 0)
#                 right_empty = (i == len(flowerbed)-1 or flowerbed[i+1] == 0)
                
#                 if left_empty and right_empty:
#                     flowerbed[i] = 1
#                     n -= 1
                
#                 if n == 0:
#                     return True
        
#         return False

# solution = Solution()
# print(solution.canPlaceFlowers([1, 0, 0, 0, 1], 1))  # Example usage
