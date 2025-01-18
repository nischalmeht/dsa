def sumofNNumbers(n):
    if n==1:
        return 1
    return n * sumofNNumbers(n-1)
result=sumofNNumbers(3)
print(result,'rs')