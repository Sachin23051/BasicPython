def fact(n):
    if n<=1:
        return 1
    else :
        return n*fact(n-1)

print(fact(5))

def fact1(n):
    fact =1
    if n<=1:
        return 1
    else:
        for i in range(1,n+1):
            fact =fact*i
    return fact
    
print(fact(6))