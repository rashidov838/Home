USERS=[{'name': 'Behruz',
        'email': '234asd@gmail.com',
        'password': '12313123',
        'purchases': [],
        'card': {'code' :'1234567890098765','money':500}
}]
PRODUCTS=[{
    'tomato':120,
    'pop':250,
    'apple':350,
    'koko':400
}]
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
        for user in USERS:
            if user['email']==email or user['password']==password:
                return 'Wrong email or password'
            else:
                break

        if not (name and email and password and card_code and card_balance):
            return "Empty values were given"

        if name.isalpha() and "@" in email and len(password)>=6 and len(card_code)==16:
            USERS.append({'name': name,
        'email': email,
        'password': password,
        'purchases': [],
        'card': {'code' :card_code,'money':card_balance}
}

            )
            return cls(name,email,password,card_code,card_balance)
        else:
            return 'Wrong credentials'
    @classmethod
    def login(cls,email,password):
        for i in USERS:
            if i['email']==email and i['password']==password:
                return 'Welcome'
            else:
                return 'Wrong email or password'
    def selll_buy(self):
        self.choose=input('Product: ')
        for p in PRODUCTS:
            if self.choose in p:
                for u in USERS:
                    if 100<=p['tomato']<=200:
                        return u['card']['money']-p['tomato']
                    elif  100<p['pop']<=200  :
                         return  u['card']['money']-p['pop'] 
                    elif 100<p['apple']<=200:
                        return u['card']['money']-p['apple']
                    elif 201<=p['tomato']<=300:
                        return u['card']['money']-p['pop']
                    elif  201<p['pop']<=300:
                        return u['card']['money']-p['tomato']
                    elif 201<=p['apple']<=300:
                        return u['card']['money']-p['apple']                        
                    elif 301<=p['tomato']<=500:
                        return u['card']['money']-p['tomato']
                    elif 301<=p['pop']<=500:
                        return u['card']['money']-p['pop']
                    elif 301<=p['apple']<=500 :
                        return u['card']['money']-p['apple']


enter_method=input('Choose method: register or login: ')
if enter_method=='register':
    user_1=Store.register('behruz','behruz@gmail.com','21fghghs','4562456245624562',1000)
    print(user_1)
elif enter_method=='login':
    user_1=Store.login('234asd@gmail.com','12313123')
    print(user_1)  
user_1=Store(2,2,2,2,2)
print(user_1.selll_buy())
# print(user_1.name,user_1.email,user_1.email)
# for user in USERS:
#     print(user)

# print(user_1.purchase)











"""Черновик"""
# ???????????????????????????????????????????
   