# data={
#     "users":[{"username":"Bekzod",'password':1002030}]
# }


# def authorize(username,password):
#     def decorator_authorize(func):
#         def wrapper(*args,**kwargs):
#             for item in data['users']:
#                 if item['username']==username and item['password']==password:
#                     return func(*args,**kwargs)
#                 else:
#                     return "wrong credentials!\n\n PLease check ypur data"

#             return wrapper
#         return decorator_authorize
# @authorize(username="user_1",password=1002030)
# def like():
#     print("liked")
# like()

# import time
# def main_test(func):
#     def wrapper(*args,**kwargs):
#         start=time.time()
#         result=func(*args,**kwargs)
#         end=time.time()
#         print(f'Result {start-end}')
#         return result
#     return wrapper

 
# @main_test
# def sub_test(a,b):
#     if a<b:
#         print(a)
#     else:
#         print(b)
# sub_test(5,6)

# Написать @wrapper

# Exception
# raise
# asset
# assert 1!=1,'Not correct'

# raise ZeroDivisionError
# print('wqew')

# try:
#     x=10
#     y=0
#     assert  x/y
# except:
#     print("error")

try:
    x=10
    y=0
    x/0
    
except ZeroDivisionError:
    print("error")


