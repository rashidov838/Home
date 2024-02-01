# from itertools import permutations
# word="cpderwars"
# letter=[w for w in word]
# print(letter)
# for p in list(permutations(letter)):
#     print(''.join(p))
# name='Bekzod'


# def show_info():
#     global name
#     print(name)
#     name='Sherzod'
#     return name

# print(show_info())




# def main_funct():
#     name='Samir'
#     def my_sub_function():
#         return name
#     return my_sub_function()
# print(main_funct())




# def my_function_root():
#     age=12
#     def my_func_parent():
#         nonlocal age
#         age=34
#         return age
#     return my_func_parent()
# print(my_function_root())



# def fact(n):
#     if n==0:
#         return 1
#     return fact(n-1)*n
# print(fact(5))



# num=int(input('Write number: '))
# count=0
# for i in range(1,num+1):
#     for j in range(1,i+1):
#         print(count+j,end='')
#     count+=1
#     print()


def message(numbers):
    def show_message():
        return 'my number: '+ str(numbers)
    return show_message()

print(message(123)) 



def fibonacci(num):
    cur=1
    if num>2:
        cur=fibonacci(num-1)+fibonacci(num-2)
    return cur
number=int(input('Write your number: '))
print(fibonacci(number))