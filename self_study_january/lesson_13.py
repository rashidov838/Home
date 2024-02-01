# def shades_of_grey(num):
#     shades=[]
#     hex='123456789abcdef'
#     counter=0
#     for i in range(num):
#         if counter==15:
#             counter=0
#         gray=f'#0{hex[counter]}0{hex[counter]}0{hex[counter]}'
#         if i>=15:
#             gray=f'#1{hex[counter]}1{hex[counter]}1{hex[counter]}'
#         shades.append(gray)
#         counter+=1
#     return shades
# print(shades_of_grey(50))


# def multiplication(num1,num2):
#     list_elements=[]
#     for n in range(num1):
#         list_elements.append(n*num2)
#     return list_elements

# print(multiplication(10,4))


# def my_func(name,default=22):
#     return f'Name: {name }, id: {default}'
# print(my_func('Bekzod',1376172))



# def show_me(name,age ,default='hi',*args):
#     print(name,age,default,'args= ',args)
# show_me('Bekzod',123,'qweqweq',[{3,4, 3,4,5,6}],18239012,"AJDALKsdaksdna")




# def info(*args):
#     for i in args:
#         print(i)
# info(123,'jahdfkjadfk',{89:17238,19283:'Bekkaka'},'NADBMNSNDS')


# def my_info():
#     list_obj=['name','age']
#     result={}
#     result=result.fromkeys(list_obj)
#     result['name']='samir'
#     result['age']=43
#     return result
# print(my_info())


# def asd():
#     numbers=[1,2,3,4]
#     list_of_result=[]
#     for i in range(len(numbers)):
#         list_of_result.append([numbers]*4)
#     return list_of_result

# print(*asd(),end='\n')



# words= ['trek    ', 'qwerty', 'redline', 'BEKZOD  Sami']


# print(words[0].title())
# print(words[0].lower())
# print(words[0].upper())
# print(words[0])
# print(words[0].strip())
# print(words[3].casefold())
# print(words[3].endswith('Samir'))
cars = ['bmw', 'audi', 'toyota', 'subaru']
# print(list({id:i.capitalize()} for  id,i in enumerate(sorted(cars))))

# print(cars[0].isalnum())

cars = ['bmw', 'audi', 'toyota', 'subaru']
change_alp=str.maketrans('a','P')
print(cars[1].translate(change_alp))
