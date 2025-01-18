def PrintNTimes(i,n):
    if i>n:
        return
    print(i)
    PrintNTimes(i+1,n)
PrintNTimes(1,30)
    