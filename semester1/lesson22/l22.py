class PlayerCharacter:
    membership=True
    def __init__(self,name='Bekzod',age=19) :
        self.name=name
        self.age=age
    
    def shout(self):
        return f"My name is {self.name}"
    
    @classmethod
    def adding_things_2(cls,num1,num2,num3,num4):
        return cls(num1+num2,num3*num4)
     
    @staticmethod
    def multiply(a,b): # Оно используется без self
        return a*b

players_1=PlayerCharacter('Sher',30)
print(players_1.name,players_1.age)# Перезаписать

players_3=PlayerCharacter.adding_things_2(2,20,90,90)
print(players_3.age,players_3.name) 

print(players_1.multiply(20,80)) 


class PlayerCharacter:
    membership=True
    def __init__(self,hobby,name='Bekzod',age=19) :
        self.name=name
        self.age=age
        self._hobby=hobby  # Оно помогает использовать внутри класса 
    
    def _welcome(self):
        return "HEEEEEEEEEEEEEY"
    
    def shout(self):
        return f"{self._welcome()}, My name is {self.name} and my hobby is {self._hobby}"

players_1=PlayerCharacter("PLaying football ",'Sher',30)
print(players_1.shout())



# class Ship:
#     def __init__(self, draft, crew):
#         self.draft = draft
#         self.crew = crew
#     def  is_worth_it(self):
#         if (self.crew+1.5)>20:
#             return False
#         elif self.draft==self.crew:
#             return True