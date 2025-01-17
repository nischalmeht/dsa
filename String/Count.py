def Count(n):
    if n == 1:
        return "1"  # Base case when n equals 1
    
    say = Count(n - 1)  # Recursively call Count with n-1
    result = ""
    i = 0
    while i < len(say):
        ch = say[i]
        count = 1
        
        # Count consecutive characters
        while i < len(say) - 1 and say[i] == say[i + 1]:
            count += 1
            i += 1
        
        result +=str(count) + str(ch)   # Append character and its count to result
        i += 1  # Move to the next character in say
    
    return result


print(Count(2))  
