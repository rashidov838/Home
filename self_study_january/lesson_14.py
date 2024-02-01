def order_Of_info(name,default='go',*args,sep='separator',username,end='\n',**kwargs):
    print(f'Name: {name},\n default: {default},\n args: {args},\n Username: {username},\n end: {end},\n sep: {sep},\n kwargs: {kwargs}',end='\n')

order_Of_info('Bekzod','bye',4,5,6,username='Niga',end='not sep',email='bekz@123.com',password='8134791384')



def my_function(*args,**kwargs):
    return f'Args: {args}, kwargs: {kwargs}'

print(my_function(1,2,3,4,[4,5,5],{1:"id"},username='Bekzod',password=12376273621))

def funct(*args,**kwargs):
    print(args,kwargs)

funct(2,3,4,5,[6],username={'id':7123612},password='qhwekjwenqwkle')
