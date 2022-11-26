 # Exercise1
# num=int(input("Write 6: "))
# for i in range(1,num+1):
#     print(' '*(num-i)+'* '*i)
# print(' '*4+' *'*1+' '*2)
# print(' '*4+' *'*1+' '*2)
# print(' '*4+' *'*1+' '*2)
# print(' '*4+' *'*1+' '*2)

# Exercise2 
 
b=[2,3,4,5,6]
for i in range(len(b)):
    if i%2==0:
        print('Четное')
    else:
        print('Нечетное')
   
# Дополнительно сам сделал
# a=int(input('Write number: '))
# while True:
#     if a%2==0:
#         print('Четное')
#         break
#     else:
#         print('Нечетное')    
#         break


# Exercise3
# faranheits = [200, 190, 240, 45] 
# celsius1= (faranheits[0] - 32) * 5 / 9
# celsius2 = (faranheits[1] - 32) * 5 / 9
# celsius3 = (faranheits[2] - 32) * 5 / 9
# celsius4= (faranheits[3] - 32) * 5 / 9
# print(celsius1,celsius2,celsius3,celsius4)
# val=[celsius1,celsius2,celsius3,celsius4]
# while True:
#     for i in val:
#         if i<50.0:
#             print(f"Слишком горячо{i}" )
#             break
#         else:
#             print(f'Жить можно{i}')            





   

# num=int(input("rows: "))
# for i in range(1,num+1): 
#     print(' '*(num-i)+'* '*i)
# print(' '*4+' *'*1+' '*2)
# print(' '*4+' *'*1+' '*2)
# print(' '*4+' *'*1+' '*2)
# print(' '*4+' *'*1+' '*2)

# OYBEK AKA 
faranheits = [20, 19, 24, 45, 140]
i = 0
while i < len(faranheits):
    celsius = ((faranheits[i]) - 32) * 5 / 9
    i += 1
    if celsius >= 50:        
        print(f"Слишком горячо: {celsius}")
        break  
    elif celsius <= 5:
        print(f"Жить можно: {celsius}")

