def traiangle_pattern(n):
    for i in range(1,n+1):
        print("*" *i)

traiangle_pattern(5)
print(" ")

def square(n):
    for i in range(n):
        print("*"*n)

square(3)

def pyramid(n):
    for i in range(n):
        print(" "*(n-i-1),"*"*(2*i+1))

pyramid(4)