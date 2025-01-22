def fibonnaci(n):
    if n<=1:
        return n
    return fibonnaci(n-1) + fibonnaci(n-2)

def fibonnaciSeries(num):
    series=[fibonnaci(i) for i in range(num)]
    return series
result=fibonnaciSeries(5)
print(result)