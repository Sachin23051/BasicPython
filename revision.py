# # Neated Dictionary

# thisdict ={
#     "dict1":{
#         'name':'sachin',
#         'id': 49,
#         'city':"mumbai"
#     },
#     "dict2":{
#         'name':'shiva',
#         'id': 38,
#         'city':"ddn"
#     },
#     "dict3":{
#         'name':'pak',
#         'id': 50,
#         'city':"mum"
#     },
#     "dict4":{
#         'name':'nadeem',
#         'id': 50,
#         'city':"delhi"
#     }
    
# }

# for x ,obj in thisdict.items():
#     print()
#     print(x)
#     for y in obj:
#         print(y + ' : ' ,obj[y])

# arbitrary function 

# names =['sachin','gupta','shivam']

# def display(*arr):
#     print(f"your name is {arr[0]}")

# display(*names)
    
# thisdic ={
#     'name':'sachin',
#     'id':49,
#     'city':"Mumbai"
    
# }

# def my_func(**thisdict):
#     print(f"Your name is {thisdict['name']}")
#     print(f"Your city name is {thisdict['city']}")
    

# my_func(**thisdic)

# x= lambda a,b,c:a+b+c
# print(x(2,3,4))

# Python oops

# class A:
#     name ="sachin"
#     id=49
#     def display(self):
#         print(self.name,self.id)
        
# a=A()
# a.display()


# class Student:
#     school="XYZ"
    
#     def __init__(self,div):
#         self.div =div
        
# class Student1(Student):
#     def __init__(self,name,id,div):
#         self.name =name
#         self.id=id
#         super().__init__(div)
        
    
# s1=Student1("Sachin",49,'A')
# print(s1.name,s1.id,s1.div,s1.school)
# # s2=Student("shivam",39)

# multiple inheritance

# class Father:
#     def skill(self):
#         print("Father Skill")
# class Mother:
#     def hobbies(self):
#         print("Hobbies from Mother")
# class Child(Mother,Father):
#     def talent(self):
#         print("Talent from Child")
        
# child=Child()
# child.skill()
# child.hobbies()
# child.talent()

# Multilevel inheritance
# class Grandparents:
#     def displayG(self):
#         print("Grandparent Message")
# class Parent(Grandparents):
#     def displayP(self):
#         print("Parent Message")
# class Child(Parent):
#     def displayC(self):
#         print("Child Message")
        
# child =Child()
# child.displayC()
# child.displayP()
# child.displayG()

# Hierachical Inheritance

# class Parent :
#     def dispalyP(self):
#         print("Message From Parent")
# class Child1(Parent):
#     def dispalyC1(self):
#         print("Message from Child1")
# class Child2(Parent):
#     def  displayC2(self):
#         print("Message from Child2 ")
        
# c1=Child1()
# c1.dispalyC1()
# c1.dispalyP()
# c2=Child2()
# c2.displayC2()
# c2.dispalyP()

# Ploymorphism
# class Pentagon:
#     def display(self):
#         print("I  have Five Side")
# class Triangle:
#     def display(self):
#         print("I have Three side")
# class Sqaure:
#     def display(self):
#         print("I have four Side")
# p=Pentagon()
# p.display()
# t=Triangle()
# t.display()
# s=Sqaure()
# s.display() 
from abc import ABC, abstractmethod

class Polygon(ABC):
    @abstractmethod
    def noOfSide(self):
        pass
class Triangle(Polygon):
    def noOfSide(self):
        print("I have three sides")
        
class  Square(Polygon):
    def noOfSide(self):
        print("I have four Side")
        
t=Triangle()
t.noOfSide()
s=Square()
s.noOfSide()