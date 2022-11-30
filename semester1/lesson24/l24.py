class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def __str__(self):
        return f'Class info: name= {self.name} age= {self.age}'
    
    def __repr__(self) :
        return f' Class info: name= {self.name}, age={self.age}'

        
    
person=Person("BEkzod",19)
person2=Person("Ikrom",20)
print(person2,person)



class Point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    # def __str__(self):
    #     return "({0},{1})".format(self.x,self.y)
    def __add__(self,other):
        x=self.x+other.x
        y=self.y +other.y
        return Point(x,y)

p1=Point(1,2)
p2=Point(4,5)
result=p1+p2 
print(result.x,result.y)
# p2.x,p2.y