def SumofNo(i,n):
    if i<1:
        print(n)
        return     
    SumofNo(i-1,n+i)
    # return sum
# print(SumofNo(5))
SumofNo(3,0)