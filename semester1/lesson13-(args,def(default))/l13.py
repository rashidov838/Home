def shades_of_grey(n):
    shades=[]
    hex='123456789abcdef'
    counter=0
    for i in range(n):
        if counter ==15:
            counter=0
        gray=f'#0{hex[counter]}0{hex[counter]}0{hex[counter]}'
        if i>=15:
            gray=f'#1{hex[counter]}1{hex[counter]}1{hex[counter]}'
        shades.append(gray)
        counter+=1
    return shades
print(shades_of_grey(50))
# n=[]
# def qwer(num=10):
#     for i in range(5,10):
#         a=num*i
#         n.append(a)
#     return n
# print(qwer())

# def create_list(n,num):
#     numbers=[]
#     for i in range(n):
#         numbers.append(i*num)
#     return numbers
# print(create_list(10,6))      


# def func(a,default='hi'):
#     print('a= ',a)
# func(12)
# func(12,'not hi')

# def func(a,b,default='hi'):
#     print('a= ',a,'b= ',b, default)
# func(12,5)
# func(a=12,b=4)
# func(12,4,'not hi')

# #арги
# def func(a,b,default='hi',*args):
#     print(a,b,default,'args= ',args)
# func(12,4,'wqeqwq',[{3,4, 3,4,5,6}])

# def any(*args):
#     """ Функция которая принимает любое количество аргументов и выводит тх на экран """
#     print('args= ',args)
#     for arg in args:
#         print(arg)
# any(2,3,4,'goooooo','biiiiiiii',{3,2,2,},(4,4,4),[1,2,3])

