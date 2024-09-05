# Lambda Experssion 
 
# x= lambda a,b,c:a+b+c

# print(x(2,4,5))

# python oops

# class Student:
#     name ="Sachin"

# class Student1(Student):
#     rollno =49



# s1=Student1()
# print(s1.name)
# print(s1.rollno)


#constructor 

# class Students:
#     name= "Sachin"
#     def __init__(self) :
#         print("Message from constructor")

# s1=Students()

# class Students:
#     college_name ="VPP"  #class attribute

#     def __init__(self,name,marks):
#         self.name = name   #object attribute
#         self.marks=marks

#     def display(self):
#         return self.college_name 



# s1=Students("Sachin" ,49)
# print(s1.name,s1.marks,s1.college_name)

# print(s1.display())

# s2=Students("Vipin" ,26)
# print(s2.name,s2.marks,s2.college_name)


# practise

# class Students:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     @staticmethod             #decorator
#     def wel():
#         print("Welcome to College")

#     def Avg(self):
#         total_marks = sum(self.marks)  
#         num_subjects = len(self.marks)  
#         avg = total_marks / num_subjects  
#         print(f"Your name is {self.name} and your average marks are {avg:.2f}")


# s1 = Students("Sachin", [30, 50, 40])
# s1.name="Vipin"
# s1.wel()
# s1.Avg()  

#Practise question for abstraction and encapsulation

# class Account :
#     def __init__(self,bal,acc):
#         self.bal=bal
#         self.acc=acc
#     def credit(self,amount):
#         self.bal-=amount
#         print(f"Your credit amount is {amount}")
#         print(f"Total balance is {self.bal}")

#     def debit(self,amount):
#         self.bal+=amount
#         print(f"Your debit amount is {amount}")
#         print(f"Total balance is {self.bal}")

# Acc1=Account(10000,1233)
# del Acc1.acc
# Acc1.acc
# Acc1.credit(500)
# Acc1.debit(600)


#multiple inheritance
# class A:
    
#     var1="message from A"
    

# class B:
#     var2="message from B"

# class C(A,B):
#    var3="message from C"

# c=C()
# print(c.var1)
# print(c.var2)
# print(c.var3)

# class carP:
#     def __init__(self,type):
#         self.type=type
    
#     def display(self):
#         print("message fom parent")

# class BMW(carP):
#     def __init__(self,color,type):
#         self.color=color
#         super().__init__(type)
#         super().display()

# b=BMW("latest","white")
# print(b.color)
# print(b.type)

# classmethod

# class Students:
#     name ="Vipin"

#     @classmethod
#     def display(cls,name):
#         cls.name=name

# s1=Students()
# s1.display("Neha")

# print(s1.name)
# print(Students.name)



# class Parent :
#     def __init__(self,name):
#         self.name=name
        
#     def show(self):
#         print("Hello" ,self.name)
# class Address(Parent):
#     def __init__(self,name,Area):
#         super().__init__(name)
#         self.Area=Area
        
#     def display(self):
#         print("Your Area ",self.Area)
    

# obj =Address("Sachin","Wadala")
# obj.show()
# obj.display()
