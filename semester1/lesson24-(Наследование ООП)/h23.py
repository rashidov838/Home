# class Math: 
#     def __init__(self,multiplication,square,ploshad,circle):
#         self.multiplication=multiplication
#         self.square=square
#         self.ploshad=ploshad
#         self.circle=circle
    
#     def Multiplication(self):
#         self.a=int(input("a= "))
#         self.b=int(input("b= "))
#         self.multiplication=(self.a*self.b)
#         return f" Multiplication = {self.multiplication}"
#     def Square(self):
#         self.c=int(input("c= "))
#         self.d=int(input("d= "))
#         self.l=self.c**self.d
#         return f" Square = {self.l}"
#     @staticmethod
#     def ploshad_kvadrata(o=int(input('O= ')),h=int(input('h= '))):
#         return f"kvadrata ={o*h}"
#     @staticmethod
#     def ploshad_circle(P=3.14,R=int(input('R= '))):
#         L= P*(R**2)
#         return f"ploshad_circle ={L}"
#     @staticmethod    
#     def ploshad_triangle(F=int(input('F= ')),G=int(input('G= ')),Y=int(input('Y= '))):
#             p=(F+G+Y)/2
#             s=pow((p*(p-F)*(p-G)*(p-Y)),1/2)
#             return f"ploshad_triangle = {s}"


# maths=Math(1,2,3,4)
# print(maths.Multiplication())
# print(maths.Square())
# print(maths.ploshad_kvadrata())
# print(maths .ploshad_circle())
# print(maths.ploshad_triangle())






class Personage():
    def __init__(self,health,mana,damage,type,skill,name):
        self.health=health
        self.mana=mana
        self.type=type
        self.skill=skill
        self.damage=damage
        self.name=name
    def attack(self):
        self.attacks=self.health-self.damage
        return self.attacks

    def heals(self):
        self.heal=self.health-self.attacks
        return self.heal

    def level_up(self):
        self.levelup=0
        if self.attacks<1000:
            return self.levelup-10
        else:
            return self.levelup+10

class Archer(Personage):
    def __init__(self,health,mana,damage,type,skill,name):
        super().__init__(health,mana,damage,type,skill,name)

    def attack(self):
        return super().attack()
    def level_up(self):
        return super().level_up()
    def heals(self):
        return super().heals()

class PAladin(Personage):
    def __init__(self,health,mana,damage,type,skill,name):
        super().__init__(health,mana,damage,type,skill,name)

    def attack(self):
        return super().attack()

    def level_up(self):
        return super().level_up()
    def heals(self):
        return super().heals()

class Wizard(Personage):
    def __init__(self,health,mana,damage,type,skill,name):
        super().__init__(health,mana,damage,type,skill,name)

    def attack(self):
        return super().attack()

    def level_up(self):
        return super().level_up()
    def heals(self):
        return super().heals()    

personages=Personage(1000,100,150,"Protagonist","Shoot","Persogage")
personages_1=Archer(1000,200,150,'Warrior','Beat',"Archer")
personages_2=PAladin(9000,300,150,'Ranger','Kill',"PAladin")
personages_3=Wizard(800,400,150,'Mage','Destroy',"Wizard")
# print(personages.health)

print(personages_3.attack(),personages_3.level_up(),personages_3.heals())
print(personages_2.attack(),personages_2.level_up(),personages_2.heals())
print(personages_1.attack(),personages_1.level_up(),personages_1.heals())



 
# # Codewars
# class Block:
#     def __init__(self,a,b,c):
#         self.a=a
#         self.b=b
#         self.c=c
#     def get_width(self):
#         if self.a==2:
#             return 2
#     def get_length(self):
#         if self.b==4:
#             return 2
#     def get_height(self):
#         if self.c==6:
#             return 6
#     def get_volume(self):
#         if (self.a*self.b*self.c)==48:
#             return 48
#     def get_surface_area(self):
#         if 2*((self.a*self.b)+(self.a*self.c)+(self.c*self.b)):
#             return 88
        
# b = Block([2,4,6])
# print(b.get_height())
# print(b.get_surface_area())
# class object:
#     def __init__(self,radius,mass):
#         self.radius=radius
#         self.mass=mass
        
# class Sphere(object):
#     def __init__(self, radius, mass):
#         super().__init__(radius, mass)
#         self.p=3.14          
#     def get_radius(self):
#         if self.radius==2:
#             return f"Check radius {self.radius}"

#     def get_mass(self):
#         if self.mass==50:
#             return f"Check mass {self.mass}"

#     def get_volume(self):
#         self.volume=4/3*self.p*(self.radius**3)
#         if self.volume:
#             return f"Check volume{self.volume}"
            
#     def get_surface_area(self):      
#         self.surface_area=4*self.p*self.radius*2
#         if self.surface_area:
#             return f"Check area {self.surface_area}"
#     def get_density(self):
#         self.density=(self.mass/self.volume)
#         if self.density:
#             return f"Check density{self.density}"       


# ball = Sphere(2,50)
# print(ball.get_mass())
# print(ball.get_radius())
# print(ball.get_volume())
# print(ball.get_density())
# print(ball.get_surface_area())
# https://www.codewars.com/kata/55c1d030da313ed05100005d/train/python
# test.assert_equals(ball.get_radius(),2, "Check radius")
# test.assert_equals(ball.get_mass(),50, "Check mass")
# test.assert_equals(ball.get_volume(), 33.51032, "Check volume")
# test.assert_equals(ball.get_surface_area(),50.26548, "Check area")
# test.assert_equals(ball.get_density(),1.49208, "Check density")