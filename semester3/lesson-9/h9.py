import sqlite3


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

class Store:
    purchases=[]
    

    
    def __init__(self,name,email,password,card_code,card_balance):
        self.name=name
        self.email=email
        self.password=password
        self.card_code=card_code
        self.card_balance=card_balance
        self.connection=sqlite3.connect('store_database.db')
        self.cursor=self.connection.cursor()
        # self.cursor.execute("""
        #     CREATE TABLE IF NOT EXISTS information(
        #         name varchar(200),
        #         email varchar(50),
        #         password varchar(100),
        #         card_code varchar(100),
        #         card_balance decimal
        #     )
        # """)
        
        # self.cursor.execute("""
        #     INSERT INTO information(name,email,password,card_code,card_balance) VALUES('Behruz','234asd@gmail.com','12313123','1234567890098765',500)
        #     """)

        # self.cursor.execute("""
        #     CREATE TABLE IF NOT EXISTS products(
        #         name varchar(200),
        #         price integer
        #     )
        # """)
        # self.cursor.execute("""
        #     INSERT INTO products VALUES('баклажан',999)
        #     """)
        # self.connection.commit()
        
        
    @classmethod
    def register(cls,name,email,password,card_code,card_balance):
        connection=sqlite3.connect('store_database.db')
        cursor=connection.cursor()
        for user in cursor.execute('select * from information').fetchall():
            # print(user)
            if user[1]==email or user[2]==password:
                return 'Пользователь с такими данными уже есть.'
            else:
                break
        """Обязательные поля что они не пустые"""
        if not (name and email and password and card_code and card_balance):
            return "Empty values were given"
        information_for_reg=[]
        if name.isalpha() and "@" in email and len(password)>=6 and len(card_code)==16 and card_balance>=0:
            
            information_for_reg.append({  "name": name,"email": email,"password": password,"card_code":card_code,"card_balance":card_balance
})
            # cursor.executemany("INSERT INTO information VALUES(:name,:email,:password,:card_code,:card_balance)",tuple(information_for_reg))
            # connection.commit()
            return cls(name,email,password,card_code,card_balance)
        else:
            return 'Wrong credentials'

    @classmethod
    def login(cls,email,password):
        connection=sqlite3.connect('store_database.db')
        cursor=connection.cursor()
        if not (email and password):
            return 'Empty values were given'
        for i in cursor.execute('select * from information').fetchall():
            if i[1]==email and i[2]==password:
                return cls(i[0],email,password,i[3],i[4])
        return 'Wrong email or password'
    purchases=[]
    def purchase(self,product):
        connection=sqlite3.connect('store_database.db')
        cursor=connection.cursor()
        for pr in cursor.execute('select * from products').fetchall():
            if product == pr[0]:
                return 'Not available'
            if self.card_balance<=0:
                return 'Not enough money'
            
            if pr[0]==product and self.card_balance-pr[1] >= 0:
                price=self.card_balance -pr[1]
                
                self.purchases.append(
                    {'name':product,
                    'price': price}
                )
            cursor.executemany("INSERT INTO products VALUES(:name,:price)",tuple(self.purchases))
            connection.commit()



enter_method='login'
if enter_method=='login':
    user_1=Store.login('234asd@gmail.com','12313123')
    if isinstance(user_1,Store):
        print(user_1.purchase('wear'))
    else:
        print('Wrong email or password')
elif enter_method=='register':
    user_1=Store.register('Bekzod','behruz@gmail.com','21fghghs','4562456245624562',1000)
    user_2=Store.register('QWERTY','QWERTY@gmail.com','21fghghs','4562956245624562',500)
    if isinstance(user_1,Store):
        print(user_1.purchase('wear'))
    if isinstance(user_1,Store):
        print(user_1.purchase('key'))
    else:
        print('Wrong email or password')
for user in USERS:
    print(user)
print(PRODUCTS)

