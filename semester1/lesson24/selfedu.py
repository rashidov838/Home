# class Student:

#     def init(self, first_name, last_name, grades=[]):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.grades = list(grades) # копия списка как deep copy
    
#     def add_grade(self, grade):
#         self.grades.append(grade)
    
#     def get_average(self):
#         return sum(self.grades) / len(self.grades)

# johnDoe=Student("John", "Doe")
# janeDoe=Student("Jane", "Doe")
# jamesSmith=Student("James", "Smith")
# jennaSmith=Student("Jenna", "Smith")
# students=(johnDoe, janeDoe, jamesSmith, jennaSmith)
# firstAssesmentGrades=[63,92,82,75]


# """Вместо этого кода, напишем динамичный код с for циклом"""
# # johnDoe.add_grade(firstAssesmentGrades[0])
# # janeDoe.add_grade(firstAssesmentGrades[1])
# # jamesSmith.add_grade(firstAssesmentGrades[2])
# # jennaSmith.add_grade(firstAssesmentGrades[3])  

# # Динамичный код:

# for i, student in enumerate(students):
#     print(i, student.first_name)
#     student.add_grade(firstAssesmentGrades[i])  # 0 1 2 3

# print(johnDoe.grades)
# print(janeDoe.grades)
# print(jamesSmith.grades)
# print(jennaSmith.grades)
# 
# try:
#     f=open("myfile2.txt")
# except FileNotFoundError:
#     print("Cant be opened it")

# print("KOLA")

# try:
#     x,y=map(int,input().split())
#     res=x/y
# except ValueError:
#     print("You made mistake")
# except ZeroDivisionError:
#     print(" Division by zero")


# class Counter:
#     def __init__(self) :
#         self.__counter=0
#     def __call__(self,step=5, *args, **kwds):
#         print("__calL__  ")
#         # self.__counter=self.__counter+1
#         self.__counter=self.__counter+step
#         return self.__counter
# c=Counter()
# c(10)
# c(40)
# print(c(90))

# data=(4.5,3.4,True,4,5,6,-11,[True,False])
# S=0
# for x in data:
#     if isinstance(x,float):
#         S+=x
# print(S)


# data=(4.5,3.4,True,4,5,6,-11,[True,False])
# # s=sum(filter(lambda x: isinstance(x, float),data))
# s=sum(filter(lambda x: type(x) is int,data))
# print(s)


# a=[11, 12, 13, 14, 15]
# b=[]
# c=[]
# for i in a:
#     if i%2==0:
#         b.append(i**2)
#     else:
#         c.append(i)

# print(sum(b+c))

a=['tomato']
pur=[]
for  i in a:
    if i=='tomato':
        pur.append(i)
print(pur)