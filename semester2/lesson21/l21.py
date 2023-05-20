# Decorator  it expand opport function 
# d 
# hello()


# def hello_2(func):
#     func()
#     return 2
# print(hello_2(hello))



# def wrapper():
#     def Hello_World():
#         return 'hi bro'
#     return Hello_World()
# print(wrapper())



# Decorator
# def my_dec(func):
#     def wrapper():
#         print("Расшряем функц")
#         func()
#         print("Расшряем функц")
#     return wrapper

# answer=my_dec(hello)
# # print(my_dec(hello))
# print(answer())


# # def like():
# #     print('gretting')
# # like()

# def authorize(func):
#     def wrapper():
#         print("Расшряем функц")
#         func()
#         print("Расшряем функц")
#     return wrapper

# answer=authorize(like)
# # print(answer)
# print(answer())

# @authorize
# def like():
#     print('gretting')
# like()


# -----------------------------------------------------------------
# def authorize(func):
#     def wrapper(x,y):
#         print("Расширяем функцию")
#         print("Расширяем функцию")
#         return func(x,y)
#     return wrapper

# # answer=authorize(like)
# # # print(answer)
# # print(answer())

# @authorize
# def multiplication(item,price):
#     return item*price
# print(multiplication(123,567))
# --------------------------------------------------------------------------------------------------------------





def authorize(func):
    def wrapper(*args,**kwargs):
        print("Расширяем функцию")
        print("Расширяем функцию")
        return func(*args,**kwargs)
    return wrapper

# answer=authorize(like)
# print(answer)
# print(answer())
@authorize
def like(username):
    print(f"{username} liked post ")
like('bekzod')

@authorize
def buy(item,price):
    return item*price

print(buy(32,45))


# -------------------------------------------
# def repeat(num_items):
#     def decorator_repeat(func):
#         def wrapper_repeat(*args,**kwargs):
#             for i in range(num_items):
#                 value=func(*args,**kwargs)
#             return value
#         return wrapper_repeat
#     return decorator_repeat

# @repeat(num_items=3)
# def hello():
#     print("hi baby")

# hello()



