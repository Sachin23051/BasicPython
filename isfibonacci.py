# check the number is exist in Fibonaci Series

def isPerfectSquare(x):
    s=int(x**0.5)
    return s*s==x

def isFibonacci(n):
    return isPerfectSquare(5*n*n+4) or isPerfectSquare(5*n*n-4)

print(isFibonacci(3))
print(isFibonacci(4))