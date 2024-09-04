# thislist=[100,65,50,88]

# def diff(n):
#     return abs(n-50)

# thislist.sort(key=diff)
# print(thislist)

# set1={1,2,3,4}
# t1=(1,2,3,4)
# l=[1,2,4,5]
# print(type(set1) ,type(t1),type(l))

# set1={1,2,3,45,60}
# set2={5,6,78,90}
# newset =set1|(set2)
# print(newset)

# def my_fun(name):
#     print("Hello " +name)
# name =input("enter your name : ")
# my_fun(name)
#  
def my_function(*childs):
    print("the young childs : " + childs[0])

my_function("sachin","ganesh","NEHA")