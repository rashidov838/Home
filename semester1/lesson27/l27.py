# """Comprehention
# """
# numbers=[]
# for i in range(100):
#     numbers.append(i)
# print(numbers)

# numbers=[i for i in range(10)]
# print(numbers)


# def multiply(i):
#     return i*5
# print(multiply(90))


# numbers=[i*5 for i in range(10)]
# print(numbers)

# numbers=[i*5 if i<5 else False for i in range(10)]
# print(numbers)

# text=(('Hi','Steve'),('Whats ','Up'))
# print([word for sentences in text for word in sentences])



USERS=[{'name': 'Behruz',
        'email': '234asd@gmail.com',
        'password': '12313123',
        'purchases': [],
        'card': {'code' :'1234567890098765','balance':500}
}]
PRODUCTS={
    'key':3,
    'wear':200
}
PRODUCTS2={
    'key':3,
    'wear':200
}

class Store:
    purchases=[]
    # buy_product=input('Write your product: ')
    def __init__(self,name,email,password,card_code,card_balance):
        self.name=name
        self.email=email
        self.password=password
        self.card_code=card_code
        self.card_balance=card_balance
        
    @classmethod
    def register(cls,name,email,password,card_code,card_balance):
        """Регистрация и создание пользования
            Args:
                name(str):name
                email(str):email
                password(str):password
                card_code(str):card_code
                card_balance(int):card_balance
        """
        for user in USERS:
            if user['email']==email or user['password']==password:
                return 'Пользователь с такими данными уже есть.'
            else:
                break
        """Обязательные поля что они не пустые"""
        if not (name and email and password and card_code and card_balance):
            return "Empty values were given"

        if name.isalpha() and "@" in email and len(password)>=6 and len(card_code)==16 and card_balance>=0:
            USERS.append({  'name': name,
                            'email': email,
                            'password': password,
                            'purchases': [],
                            'card': {'code' :card_code,'balance':card_balance}
})
            return cls(name,email,password,card_code,card_balance)
        else:
            return 'Wrong credentials'

    @classmethod
    def login(cls,email,password):
        if not (email and password):
            return 'Empty values were given'
        for i in USERS:
            if i['email']==email and i['password']==password:
                return cls(i["name"],email,password,i['card']["code"],i['card']['balance'])
            
        return 'Wrong email or password'

    def purchase(self,product):
        if product not in PRODUCTS.keys():
            return 'Not available'
        if self.card_balance<=0:
            return 'Not enough money'
        for key,val in PRODUCTS.items():
            if key==product and self.card_balance-val >= 0:
                self.card_balance -=val
                self.purchases.append(product)
                for id,user in enumerate(USERS):
                    if user['email']==self.email:
                        USERS[id]['purchases'].append(product)
                PRODUCTS.pop(key)
                return f'\n Succesfully bought {product} and added into purchases!\n Balance:{self.card_balance}\n Your purchases {self.purchases}'
        return f'{self.name}  / {self.card_balance}: Not enough money.'

class StoreOwner:
    def __init__(self,add,delete,changes):
        self.add=add
        self.delete=delete
        self.changes=changes
    def adds(self):
        self.product=input('Adds product: ')
        self.price=int(input('Adds price : '))
        if  self.product not in PRODUCTS2.keys():
            PRODUCTS2.update({
                self.product:self.price
            })
            return PRODUCTS2
        else:
            return 'Not'
    def deletes(self):
        self.product=[input('Delete product: ')]
        for key in self.product:
            if key in PRODUCTS2:
                del PRODUCTS2[key]
                return PRODUCTS2
            else:
                return 'Dont have this product'
    def changes_product(self):
        self.product=input('Choose product: ')
        for key in PRODUCTS2:
            if key==self.product:
                PRODUCTS2[key]=int(input('Change price: '))
                return PRODUCTS2
        else:
            return f'Not'

user_3=StoreOwner(1,2,3)
print(user_3.adds())
print(user_3.deletes())
print(user_3.changes_product())

# enter_method=input('Choose method: register or login: ')
# if enter_method=='login':
#     user_1=Store.login('234asd@gmail.com','12313123')
#     if isinstance(user_1,Store):
#         print(user_1.purchase('wear'))
#     else:
#         print('Wrong email or password')
# elif enter_method=='register':
#     user_1=Store.register('behruz','behruz@gmail.com',
#                          '21fghghs','4562456245624562',1000)
#     user_2=Store.register('QWERTY','QWERTY@gmail.com',
#                          '21fghghs','4562956245624562',500)
#     if isinstance(user_1,Store):
#         print(user_1.purchase('wear'))
#     if isinstance(user_1,Store):
#         print(user_1.purchase('key'))
#     else:
#         print('Wrong email or password')
# for user in USERS:
#     print(user)
# print(PRODUCTS)
