class Solution:
    def reverseWords(self, s: str) -> str:
        word = s.split(" ")
        words = word[-1::-1]        
        return str(words)
solution= Solution()
print(solution.reverseWords("the sky is blue"))
# Original list
words = ["example", "", "", "good", "a"]

# Filter out empty strings
filtered_words = filter(None, words)

# Join the list into a single string with spaces
result = ' '.join(filtered_words)

print(result)  # Output: "example good a"


