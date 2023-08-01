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
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS information(
                id integer primary key autoincrement,
                name varchar(200),
                email varchar(50) unique,
                password varchar(100),
                card_code varchar(100),
                card_balance decimal
            )
        """)
        
        self.cursor.execute("""
            INSERT INTO information(name,email,password,card_code,card_balance) VALUES('Behruz','234asd@gmail.com','12313123','1234567890098765',500)
            """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS products(
                id integer primary key autoincrement,
                name varchar(200) UNIQUE,
                price integer
            )
        """)

        lst_products=[
            ('wear',200),
            ('tomato',400),
            ('kola',300),
            ('pepsi',500),
            ('баклажан',800),
            ('key',783),
        ]
        
        self.cursor.executemany("""INSERT INTO products(name,price) VALUES(?,?)""",lst_products)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS purchase(
                id integer primary key autoincrement,
                product varchar(100) ,
                price integer references products(price),
                name varchar(200) references  information(name)
            )
        """)
        self.connection.commit()
        
        
    @classmethod
    def register(cls,name,email,password,card_code,card_balance):
        connection=sqlite3.connect('store_database.db')
        cursor=connection.cursor()
        for user in cursor.execute('select * from information').fetchall():
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
            cursor.executemany("""
                INSERT INTO information(name,email,password,card_code,card_balance) VALUES(:name,:email,:password,:card_code,:card_balance)
            """,tuple(information_for_reg))
            connection.commit()
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
            if i[2]==email and i[3]==password:
                return cls(i[1],email,password,i[4],i[5])
        return 'Wrong email or password'
    def purchase(self, product):
        products={}
        connection=sqlite3.connect('store_database.db')
        cursor=connection.cursor()
        for pr in cursor.execute('select * from products').fetchall():
            products.update({pr[1]:pr[2]})
        # print(products)

        if product not in products.keys():
            return "Not available!"            
        if self.card_balance <= 0:
            return "Not enough money!"
        for key, val in products.items():
            if key == product and self.card_balance - val >= 0:
                self.card_balance -= val
                self.purchases.append(
                    {'product':key,
                    'price':val,
                    'name':self.name}
                )

        bucket=[]
        bucket.append(self.purchases[-1])
        cursor.executemany("""INSERT INTO purchase(product,price,name) VALUES(:product,:price,:name)""",tuple(bucket))
        connection.commit()

enter_method='register'
if enter_method=='login':
    user_1=Store.login('shax@gmail.com','12fghghs')
    if isinstance(user_1,Store):
        buy_product=['pepsi','tomato','баклажан','key']
        for i in buy_product:
            print(user_1.purchase(i))
    else:
        print('Wrong email or password')
elif enter_method=='register':
    user_1=Store.register('komila','komila@gmail.com','44313123','1234567890098765',99500)
    if isinstance(user_1,Store):
        buy_product=['pepsi','tomato','баклажан','key']
        for i in buy_product:
            print(user_1.purchase(i))
    if isinstance(user_1,Store):
        print(user_1.purchase('pepsi'))
    else:  
        print('Wrong email or password')