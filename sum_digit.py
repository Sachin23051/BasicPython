num=12399999999999

def sum_digit(num):
    sum=0
    count=1
    while num >0:
        
        digit =num%10
        sum=sum+digit
        count+=1
        num=num//10
        
    if sum>9:
        sum =sum_digit(sum)
  
    
    return sum
    
print(sum_digit(num))