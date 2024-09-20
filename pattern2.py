n=18
num=1
while num<=n:
    for i in range(1,11):
        if i<6 and num <=n:
            print( ' ', num,end='')
            num+=1
        elif i > 5 and num <=n:
            print("*" ,end ='')
            num+=1
            
    print()

        
        