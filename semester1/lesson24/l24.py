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



# class Point:     
#     def __init__(self,x=0,y=0):
#         self.x=x
#         self.y=y
#     # def __str__(self):
#     #     return "({0},{1})".format(self.x,self.y)
#     def __add__(self,other):
#         x=self.x+other.x
#         y=self.y +other.y
#         return Point(x,y)

# p1=Point(1,2)
# p2=Point(4,5)
# result=p1+p2 
# print(result.x,result.y)
# p2.x,p2.y

class BaseCharacter:
    experience=0
    lvl=1
    def __init__(self,health,mana,damage,type,skills):
        self.health=health
        self.mana=mana
        self.damage=damage
        self.type=type
        self.skills=skills
    
    def attack(self,enemy_health):
        return enemy_health -self.damage

    def heal(self):
        if 'heal' in self.skills:
            self.health+=10

    def enemy_killed(self,enemy_lvl):
        if enemy_lvl==1:
            self.experience+=5
            self.level_up()
            print(f'Your leveled up! Curent level is {self.lvl}')
    def level_up(self):
        """ Максимальный уровень - 5 """
        if 10 <=self.experience<=20:
            self.lvl+=1
        elif 21 <=self.experience<=31:
            self.lvl+=1
        elif 31 <=self.experience<=41:
            self.lvl+=1   
        elif 41 <=self.experience<=51:
            self.lvl+=1 
        elif 51 <=self.experience:
            self.lvl+=1
class Archer(BaseCharacter):
    pass

class Paladin(BaseCharacter):
    pass

class Wizard(BaseCharacter):
    pass 

player1=BaseCharacter(15,50,15,'base',['heal'])
player2=BaseCharacter(15,50,15,'base',['heal'])

print(player2.health)

player2.health=player1.attack(player2.health)
print(player2.health)

print(player1.lvl)
if player2.health<=0:
    player1.enemy_killed(player2.lvl)