class Solution:
    def lengthofSubstring(s:list):
        left = max_length=0
        char_set=set()
        for i in range(len(s)):
            while s[i] in char_set:
                left+=1
            char_set.append(s[i])
            max_length=max(max_length,i-left+1)
        return max_length
solution = Solution()
print(solution.lengthofSubstring('abca'))
        