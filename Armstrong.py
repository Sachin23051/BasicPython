# n =153
# Is Armstrong number
#reason 1*1*1+5*5*5+3*3*3=153


def armstrong(n):
    new_n =n
    Sum=0
    while n>0:
        digit =n%10
        Sum =digit*digit*digit+Sum
        n=n//10

    if Sum ==new_n:
        print(f"{new_n} Is Armstrong Number")
    else:
        print(f"{new_n} Is not Armstrong Number")
        
        
armstrong(153)
armstrong(347)
        