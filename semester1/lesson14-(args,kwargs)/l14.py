
# Правило передачи аргумента
def order_of_args(name,default='go',*args,sep='seperator',username,end='\n',**kwargs):
    print(name,default,args,username,end, sep, kwargs)
order_of_args('Bekhruz',123,4,5,6,username='ago',end='not enter',sep='not sep',email='e@mail.com',look=[1,2,3])
 

def func(*args,**kwargs):
    return args,kwargs
print(*func(2,3,4,[5],username={'usernam':"qweq"},goal=('qwertyu')))

def func(*args,**kwargs):
    print(args,kwargs)
func(2,3,4,[5],username={'usernam':"qweq"},goal=('qwertyu'))