def prime(n):
    if n<=1:
        return False
    elif n==2 or n==3:
        return True
    else:
        m=n//2
        for x in range(2,m):
            if n%x==0:
                return False
                break
        
    return True

n= 100
while n>0:
    if prime(n):
        print(n)
    n-=1