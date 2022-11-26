
#Exercise 1
for val in [1, 2, 3, 4, 5, [6, 7, 8, 5, 6], (4, 5, 6)]: 
    if isinstance(val,(int)):
         print(val) 
    if isinstance(val, (list, set, tuple)): 
        for i in val: 
            print(i) 


#Exercise 2
a= [1, 2, 3, 4, 5, 6, 7]
for i in range(len(a)):
    a[i] *=4
    print(a)

a=[1, 2, "hello", 4, 5, 6, 7]
del a[2]
del a[5]
for i in range(len(a)):
    a[i] *=4
    print(a)


for val in [1, 2, 3, 4, 5, [6, 7, 8, 5, 6], (4, 5, 6)]:           
    if isinstance(val, (list, set, tuple)): 
        for i in val: 
            print(i) 
    else:
        print(val)

