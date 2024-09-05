def swap(a,b):
    a,b=b,a
    print(a,b)

def swap_arth(a,b):
    a=a+b
    b=a-b
    a=a-b
    print(a,b)

swap(20,40)
swap_arth(40,50)
