# 1 
# def factorial(n,fact):
#     return (fact*i for i  in range(1,n+1)) 

# generator=factorial(3,11)
# for gen in generator:
#     print(gen)

# 2
# def cs_generator():
#     return ("Computer Science"+str(i) for i in range(1,5))


# generator=cs_generator()
# for gen in generator:
#     print(gen)


# 3
# def student_standing_generator():
#     student_standing=['Freshman','Senior','Junior','Freshman']
#     for student in student_standing:
#         if student=='Freshman':
#             yield student+str(500)
#         elif student=='Senior':
#             yield student+str(300)
#         elif student=='Junior':
#             yield student+str(100)

# students=student_standing_generator()
# for st in students:
#     print(st)

def factorial_generator(n):
    term=1
    for i in range(1,n+1):
        c=term*i
        yield c
        term=c


fact=factorial_generator(10)
for i in fact:
    print(i)


# Read information about method:
# 1,send
# 2,trow
# 3,close
