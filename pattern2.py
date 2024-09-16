#   1  2  3  4  5
#   *  *  *  *  *
#   11  12  13  14  15
#   *  *  *  *  *
#   21  22  23  24  25
#   *  *  *  *  *

n = 6
num =1
for i in range(1,n+1):
    for j in range(1,6):
        if i%2==0:
            print("  *" , end="")
            num+=1
        else:
            print(" ",num,end="")
            num+=1
    # num+=1
    print()