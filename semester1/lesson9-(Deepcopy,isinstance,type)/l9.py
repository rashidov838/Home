import copy
# from platform import python_branch
a=[2,3,4]
b=a.copy()
print('a= ', a, 'b= ', b)

a=[2,3,4]
b=a.copy()
b.append(6787)
print('a= ', a, 'b= ', b)

a=a=[2,3,4,[2,3]]
b=a.copy()
b[2]=400
b[3][1]=12
print('a= ', a, 'b= ', b)

#Copy.deepcopy  оно помогает без тзменения скопировать все значение и оно независимое и можно внести изменение
a=[2,3,4,[2,3]]
b=copy.deepcopy(a)
b[2]=400
b[3][1]=12
print('a= ', a, 'b= ', b)
# a is b , b is a
a=[2,3,4]
b=a
a.append(78)
print('a= ', a, 'b= ', b)

 
# print(type('qwerty'), str, 'qwerty'==str)
# val=['12']
# if type(val)== int or type(val)==str:
#     print(True)
# else:
#     print('False')


# val=input('')
# if type(val)== int or type(val)==str:
#     print(True)
# else:
#     print('False')

# byte of python
# Lytce about python
# mark lutz 

# print('list')
# numbers=[1,2,3,4,5,6,7]
# for num in numbers:
#     print(num+2)

# print('Tuple')
# numbers=[1,2,3,4,5,6,7]
# for num in numbers:
#     print(num+2)

# # print('Set')
# # numbers=[1,2,3,4,5,6,7]
# # for num in numbers:
# #     print(num+2)

# print('Dict')
user={
    'name':'Gearge',
    'age':23,
    'skill':'swim',
}
for key in user:
    print(key)

print('Duct val')
for val in user.values():
    print(val)

print('\ndict val')
for key,val in user.items():
    print('key= ',key,'val=',val)

# for val in [1, 2, 3, 4, 5, [6, 7, 8, 5, 6], (4, 5, 6)]: 
#     print(val[:6]) 
#     if isinstance(val, (list, set, tuple)): 
#         for i in val: 
#             print(i)