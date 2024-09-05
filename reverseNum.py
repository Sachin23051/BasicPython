def rev(n):
    rNum=0
    while n>0:
        last_digit = n%10
        rNum = rNum*10+last_digit
        n=n//10
    print(rNum)

rev(1234)