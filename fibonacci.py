
#without Recursion
def fab_series(n):
    series =[]
    a,b=0,1
    while len(series)<n:
        series.append(a)
        a,b=b,a+b
    return series
    
print(fab_series(5))

#With Recursion
def fib(n):
    if n<=0:
        return []
    elif n==1:
        return [0]
    elif n==2:
        return [0,1]
    series =fib(n-1)
    series.append(series[-1]+series[-2])
    return series
    
print(fib(10))
        