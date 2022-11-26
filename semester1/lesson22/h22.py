# # 1
class Point():
    color='red'
    circle=2
    def set_coords(self,x,y):
        self.x=x
        self.y=y

pt=Point()
pt2=Point()
pt.set_coords(1,3)
pt2.set_coords(111,300)
print(pt.__dict__)
print(pt2.__dict__)
# # 2
# class Point():
#     color='red'
#     circle=2
#     def set_coords(self,x,y):
#         self.x=x
#         self.y=y

#     def get_coords(self):
#         return (self.x,self.y)

# pt=Point()
# pt.set_coords(1,2)
# a=getattr(pt,'get_coords')
# print(a())

# # 3
# class Point():
#     color='red'
#     circle=2
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def __del__(self):
#         print(" Удаление   " +str(self))
#     def set_coords(self,x,y):
#         self.x=x
#         self.y=y

#     def get_coords(self):
#         return self.x,self.y
# h=Point(30,50)
# print(h.__dict__)
# print(h.__dict__)

# class Point():
#     def __new__(cls,*args,**kwargs):
#         print(" New " +str(cls))
#     def __init__(self,x=0,y=0):
#         print(" init : "+str(self))
#         self.x=x
#         self.y=y

# pt=Point(80,80)
# print(pt)

    
class Person:
    def __init__(self, name):
        self.name = name
    def greet(self, name):
        return "Hello {}, my name is {}".format(name, self.name)
joe = Person('Joe')
print(joe.greet('Kate'))


class Point:
    def set_coords(self,A,B,C):
        self.A=A-15
        self.B=B-15
        self.C=C-15
       
    def set_coords1(self,A,B,X):
        self.A=A-25
        self.B=B-25
        self.X=X-25   
    
pt=Point()
pt2=Point()
pt.set_coords(20,15,10)
pt2.set_coords1(40,25,10)
print(pt.__dict__)
print(pt2.__dict__)

# # https://www.codewars.com/kata/5641275f07335295f10000d0/train/python
# def count_by(x, n):
#     a=[]
#     for i in range(n):
#         a.append(x*(i+1))
#     return a
# print(count_by(1,10))
# "This website is for losers LOL!"

def disemvowel(string_):
    # b=string_[:2]+string_[3:4] + string_[5:6] +string_[7:9]+string_[10:11]+string_[14:15]+string_[16:17]+string_[19:21]+string_[22:23]+string_[24:26]+string_[27:28]+string_[30:31]+string_[32:]
    # t=b.split("_")
    a=string_.replace('i','')
    t=a.replace('e','')
    s=t.replace('o','')
    s1=s.replace('O','')
    return s1
print(disemvowel("This website is for losers LOL!"))