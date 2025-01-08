class Solution:
     
    #Function to find if there exists a triplet in the 
    #array A[] which sums up to X.
    def hasTripletSum(self,A, n, X):
        # Your Code Here
        A.sort()
        for i in range(n):
            y = X - A[i]
            low = i + 1
            high = n-1
            while low < high:
                if A[low] + A[high] == y:
                    print(A[low],A[high],high)
                    return 1
                
                elif  A[low] + A[high] < y:
                    low += 1
                
                elif A[low] + A[high] > y:
                    high -= 1
        return 0   
solution=Solution()

print(solution.hasTripletSum([1, 4, 45, 6, 10, 8],6,13))
            