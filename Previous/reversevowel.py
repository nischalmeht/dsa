
def reverseVowels(s):  
        s = list(s)  
        i,j = 0,len(s)-1  
        while i<j:  
            if s[i] in ['a','e','i','o','u', 'A','E','I','O','U'] and s[j] in ['A','E','I','O','U']:  
                s[i],s[j]=s[j],s[i]  
                i = i+1  
                j = j-1  
            elif s[i]  not in ['a','e','i','o','u', 'A','E','I','O','U'] and s[j] in ['a','e','i','o','u', 'A','E','I','O','U']:  
                i = i+1  
            elif s[i] in ['a','e','i','o','u', 'A','E','I','O','U'] and s[j] not in ['a','e','i','o','u', 'A','E','I','O','U']:  
                j = j-1  
            else:  
                i=i+1  
                j = j-1  
        return "".join(s)  
print(reverseVowels('JavaTpoint'))