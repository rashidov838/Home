# class Cat:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def info(self):
#         print(f'I am cat. My name is {self.name}. i am {self.age} years old')
    
#     def make_sound(self):
#         print('Meow')

# class Dog:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def info(self):
#         print(f'I am do. My name is {self.name}. i am {self.age} years old')
    
#     def make_sound(self):
#         print('BArk')

# cat1=Cat("Kitty",2.5)
# dog1=Cat("Flluy",4)
"""Полиморфизим"""
# for animal in (cat1,dog1):
#     animal.info()
#     animal.make_sound()
    # animal.info()
users=[{'name': 'Behruz',
        'email': '234asd@gmail.com',
        'password': '123456789',
        'purchases': [],
        'card': {'code' :'1234567890098765','money':1000}
}]


class Store:
    
    def __init__(self,name,email,password,card,amount,purchases=['tomato','orange']):
        self.name=name
        self.email=email
        self.password=password
        self.purchases=list(purchases)
        self.card=card
        self.amount=amount
        
    def log(self):
        
        self.check_email=input('Lets check your email: ')
        self.check_password=input('Lets check your password: ')
        for i in users:
            if i['password']==self.check_password and i['email']==self.check_email:
                return f'Welcome my darling'
            elif i['password']==self.check_password or i['email']==self.check_email:
                return f'Wrong email or password'
            else:
                return f' Please register'
      
    def register(self):
            self.name=input('Write your name: ')
            if self.name.isalpha():
                pass
            else:
                raise SystemExit
            self.email=input("Write your email: ")
            a='@'
            if a in self.email:
                pass
            else:
                raise SystemExit
            self.password=input("Write your password ")
            if  len(self.password)>=6:
                pass               
            else:
                raise SystemExit
            self.card=input("Write your number of card: ")
            if  len(self.card)==16:
                pass
            else:
                raise SystemExit
            self.amount=int(input("Your amount: "))
    
   
            self.registers=[{'name': self.name,
                            'email': self.email,
                            'password': self.password,
                            'card': {'code' :self.card,'money':self.amount}
                                     }]
            return self.registers
  
      
    
    def purchase(self):
        self.buy_product=input('Write your product: ')
        if self.buy_product in self.purchases and self.amount>=100:
            self.balance=self.amount-100
            return f'Остаток: {self.balance}'
        elif self.buy_product in self.purchases and self.amount<=100:
            return f'Not money' 
        else:
            return f"Not product"

    def add_product(self):
        if self.buy_product in self.purchases and self.amount>=100:
            self.balance=self.amount-100
            return f'Было купленно {self.buy_product}, Баланс на счету {self.balance}, Было потраченно {self.amount-self.balance}'
        elif self.buy_product in self.purchases and self.amount<=100:
            return f'Не достаточно денег  {100-self.amount}'
        else:
            return f"Нет продукта {self.buy_product}"
    def all_users(self):
            self.registers.extend([{'purchases':self.buy_product}])
            return users+self.registers
enter_method=input('Choose method: register or login: ')
st1=Store(1,2,2,2,2)
if enter_method=='register':
    print(st1.register())
elif enter_method=='login':
    print(st1.log())

print(st1.purchase())
print(st1.add_product())
print(st1.all_users())