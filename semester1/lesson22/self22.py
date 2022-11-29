class Point:
    def __init__(self,x=0,y=0):
        self.__x=x
        self.__y=y
    @classmethod
    def set_cord(self,x,y): #setter
        if type(x) in (int,float) and type(y) in (int,float):
            self.__x=x
            self.__y=y
        else:
            raise ValueError("Error") 
    def get_coord(self): #GETTER
       return self.__x,self.__y
pt=Point(1,2)
# print(pt.__x,pt.__y)   
pt.set_cord(10,20)
print(pt.get_coord())


from datetime import date

first_date = date(2020, 10, 2)
second_date = date(2020, 10, 30)
delta = second_date - first_date
print(delta)
