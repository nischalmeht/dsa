# from typing import List


# class Solution:
#     def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         arr=[]
#         for i in range(0,len(nums1)):
#             el= nums1[i]
#             for j in range(0,len(nums2)):
#                 if (el== nums2[j]) and el not in arr:
#                     arr.append(nums1[i])
#         return arr

# nums1 = [1, 2, 2, 1]
# nums2 = [2, 2]
# solution= Solution()
# print(solution.intersection(nums1,nums2))



from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        arr = []
        i, j = 0, 0

        # Ensure both arrays are sorted
        nums1.sort()
        nums2.sort()

        # Use two pointers to find the intersection
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                if not arr or arr[-1] != nums1[i]:  
                    arr.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1

        return arr

# Example Usage
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
solution = Solution()
print(solution.intersection(nums1, nums2))  # Output: [2, 3]
