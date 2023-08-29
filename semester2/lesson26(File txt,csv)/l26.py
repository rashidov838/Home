"""
    Character Meaning:
    'r'-it is for reading
    'w'-it is used to write text
    'x'-create new file and open it for writting
    'a'-open for writing,appending to the end of file
    'b'-binary mode
    't'-text mode(default)
    '+'-open a disk file for updating(reading and writting)
    'U'-universal newlinne mode(depreciated)

"""


# my_file=open('test.txt ','r')
# print(my_file.read())
# print(my_file.readline())
# print(repr(my_file.readline()))



# # my_file.close()


# my_file=open('write.txt','w')
# age=33
# my_file.write(f'My name is Bekzod Age is {age}')
# my_file.write(f'\nMy name is Samina Age is {age}')
# my_file.close()


# Context manager: __enter__ __exit__
# with open('write.txt',mode='r') as file:
#     for i in file.readlines():
#         print(i.strip())
 
try:
    my_file=open('write.txt','a')
    #  code
except Exception as err:
    print(err)
finally:
    my_file.close()



# with open('test.txt',mode='w') as file:
#     file.write(f'Some information about us')


# with open('test.txt',mode='w') as file:
#     for i in range(10):
#         file.write(f'\nNumber is {i}')


big_list=[
    {'name':'Bekzod Rashidov',"userid":6712359021,'is_admin':False},
    {'name':'Salih Rashidov',"userid":7546821397,'is_admin':False},
    {'name':'Bobi Rashidov',"userid":3698521475,'is_admin':False},
    {'name':'Komila Rashidov',"userid":1597532486,'is_admin':True},
]

import csv

with open('output.csv','w',newline='',encoding='utf-8') as output_csv:
    fields=['name','userid','is_admin']
    output_writer=csv.DictWriter(output_csv,fieldnames=fields)
    output_writer.writeheader()
    for item in big_list:
        output_writer.writerow(item)

