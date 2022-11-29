from datetime import date
class Father:
    house=True
    def __init__(self,name,job,hoby,bank_account) :
        self.name=name
        self.job=job
        self.hoby=hoby
        self.bank_account=bank_account

    def spend(self,amount):
        self.bank_account-=amount
    
    def income(self,amount):
        self.bank_account+=amount



class Mother:
    cooked_food=""
    def cook(self,products):
        if "carrot" in products and "meat" in products and "rice" in products:
            self.cooked_food=" mother plow"
        else:
            print("We cant cook with these products.")


class Child(Father,Mother):
    def __init__(self,name,job,hoby,bank_account,age) :
        self.age=age
        super().__init__(name,job,hoby,bank_account)


    def cook(self, products):
        super().cook(products)
        if "oil" in products and "eggplant" in products and "tomato" in products:
            self.cooked_food='fired-eggplant'




child=Child("Bek","IT","Jump",100100,24)

print(child.bank_account,child.hoby)

child.spend(10)
print(child.bank_account)

child.income(400)
print(child.bank_account)


child.cook(["carrot",'meat','rice'])
print(child.cooked_food)

child.cook(['oil','eggplant','tomato'])
print(child.cooked_food)



# child.date_birth(date(2003, 1, 10),date(2022, 11, 26))
# print(child.delta)
