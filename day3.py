from abc import ABC,abstractmethod

# # abstraction in python

# class Person:
#     def show(self):
#         pass
# class Child1:
#     def show(self):
#         print("message from Child 1")


# child1 =Child1()
# child1.show()

# #Polymorhism 
# class A:
#     @staticmethod
#     def add(a,b):
#         print("Addition from First Function")
#         print(a+b)
# class B(A):  
#     @staticmethod
#     def add(a,b,c=0):
#         print("Addition from Second Function")
#         print(a+b+c)
        
#     @staticmethod   
#     def parent_add(a,b):
#         A.add(a,b)
        
# b=B()

    
# b.add(2,5)
# b.add(3,4,5)
# b.parent_add(3,8)

# Polymorphism in Class 

# class Bird :
#     def intro(self):
#         print("There are differnt types of Birds")
#     def flight(self):
#         print("Some Birds can Fly but Some Can't fly ")
# class Sparrow(Bird):
#     def flight(self):
#         print("Sparrow can fly ")
# class Ostrich(Bird):
#     def flight(self):
#         print("Ostrich Can't fly ")

# obj_bird =Bird()
# obj_spr=Sparrow()
# obj_ost=Ostrich()

# obj_bird.intro()
# obj_bird.flight()
# obj_ost.intro()
# obj_ost.flight()
# obj_spr.intro()
# obj_spr.flight()      

# Abstract class

# class Polygon(ABC) :
#     @abstractmethod
#     def noOfside(self):
#         pass
# class Triangle(Polygon):
    
#     def noOfside(self):
#         print("I have 3 sides")
# class Pentagon(Polygon):
    
#     def noOfside(self):
#         print("I have 5 sides")
# class Hexagon(Polygon):
    
#     def noOfside(self):
#         print("I have 6 sides ")
# T=Triangle()
# P=Pentagon()
# H=Hexagon()

# T.noOfside()
# P.noOfside()
# H.noOfside()

# User input for List

# user_input =[]
# num_input=int(input("Numbers of Input you enters : "))
# for _ in range(num_input):
#     item =input("Enter the Items : ")
#     user_input.append(item)

# print(user_input)

# for Dictionary

# decorator

def percentage(func):
    def inner_func(n):
        result =func(n)
        return [result ,{result*100/50}]
    return inner_func
    
@percentage 
def square(n):
    return n**2
    
a = square(4)
print(a)