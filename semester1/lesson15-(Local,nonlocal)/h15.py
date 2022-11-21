# def fac(n):
#     if n==0:
#         return 1
#     return fac(n-1)*n
# print(fac(5))


# from cgi import print_arguments


# n=int(input())
# c=0
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(c + j,end=' ')
#     c=c+1
#     print()

# from itertools import permutations
# inp="codewars"
# letter=[x.lower() for x in inp]

# for y in list(permutations(letter)):
#     print("".join(y)) 
 
#  /////////////////////////////////////////
# self study
# def message(numbers):
#     def prnt_message():
#         return 'Число' + str(numbers)
#     return prnt_message
# print(message(90))

def fibonacci(n):
    cur = 1
    if n > 2:
        cur = fibonacci(n-1) + fibonacci(n-2)
    return cur

element = input('Введите номер искомого элемента : ')
element = int(element)
value = fibonacci(element)
print(str(element)+' элемент последовательности равен ' + str(value))