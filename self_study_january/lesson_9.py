# age=123
# if type(age) == int:
#     print("It is integer")
# else:
#     print('it is false')


# val=['12']
# if not type(val)==int or type(val)==str:
#     print(True)
# else:
#     print(False)

# val=input('')
# if type(val)==int or type(val)==str:
#     print(True)
# else:
#     print(False)


# numbers=[1,2,3,4]
# for num in numbers:
#     print(num+2)


# for info in [1, 2, 3, 4, 5, [6, 7, 8, 5, 6], (4, 5, 6)]:
#     if isinstance(info,int):
#         print(info)

#     if isinstance(info,(list,tuple,set)):
#         for i in info:
#             print('It is from '+f'{i}')


numbers=[1,7,9,15,4,5]
count=0
for num in numbers:
    count+=num
print(count)


# for num in range(len(numbers)):
#     numbers[num]*=2
# print(numbers)



# for num in range(100,200,10):
#     print(num)