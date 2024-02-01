def great():
    return 'Hello'
print('Вызов функции',great())



def information_about_me(Name):
    print(f'Name is {Name}')



information_about_me('Bekzod')



# def info(id:int,name:str,age: int):
#     return f'id: {id}, name: {name}, age: {age}'

# print(info(1,'Bekzod',89999))


# def make_upper_case():
#     word=input('Write your word: ')
#     return word.upper()

# print(make_upper_case())




# def num_pow():
#     num=int(input('Write your number: '))
#     result=pow(num,3)
#     return result
# print(num_pow())



def factorial(n):
    previous_num=1
    a=[]
    for i in range(2,n+1):
        previous_num*=i
        # a.append(previous_num)
    # return a[-1]

print(factorial(5))
