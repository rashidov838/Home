
# Теория
# 1.
# Переменная хранит данные одного из типов данных. В Python существует множество различных типов данных. В данном случае рассмотрим только самые базовые типы: bool, int, float и str.
# Логические значения
# Тип bool представляет два логических значения: True или False. Значение True служит для того, чтобы показать, что что-то истинно. Тогда как значение False, наоборот, показывает, что что-то ложно.
# Целые числа
# Тип int представляет целое число, например, 1, 4, 8, 50.
# Дробные числа
# Тип float представляет число с плавающей точкой, например, 1.2 или 34.76. В качесте разделителя целой и дробной частей используется точка.
# Строки
# Тип str представляет строки. Строка представляет последовательность символов, заключенную в одинарные или двойные кавычки.
# 2.
# user_data={
#     'key':'znacheniya',
#     1:None,
#     2:21,
#     3:6.7,
#     4:[2,3,4],
#     5:(3,4,5),
#     6:{'key':"Другой словарь"}
#     #[1]:23 #error
#     #(2,3,[2,3]):'Error' # Кортеж можно использовать как ключь но не рекомендуется

# 3.
# Одна будьте здесь, есть два метода MRO в зависимости от версии Python, которую вы используете. Хотя разница между ними
# вряд ли порадует большинство из нас в повседневном использовании, я предполагаю, что если вы изучаете Python сегодня,
# вы используете версию 3.x, и по этой причине я поговорим с новым стилем классов в этой статье.
# Погорим о наследовании. Если один класс унаследован от другого, то он от него перенимает себе методы и атрибуты своего родителя. 
# Вы, конечно, можете переопределить некоторые из них или добавить свою новую функциональность – в этом и есть смысл наследования. 
# Но те методы, которые вы не переопределяли, так и останутся родительскими. Таким образом, когда вы вызываете метод экземпляра класса, 
# Python должен посмотреть, есть ли в нем этот метод. Если есть – он и будет вызван, а если его нет, то ему придется проверить 
# классы-родители данного класса.
# 4.Если мы хотим внести изменения то мы локально должны сохранить наши изменения в консоле надо написать:
#     1.git add .   -  добавление в локальном уровне
#     2. git commit -m “Adds our information”- комментарий
#     3.git push - добавление в гитхаб.
#     4.git status – проверка о добавлении 
# 5.
# Функция представляет собой фрагмент кода , который называется по имени. Это может быть передано данные для работы 
# и может дополнительно возвращать данные (возвращаемое значение). Все данные, которые передаются в функцию, передаются явно.
# Метод представляет собой фрагмент кода , который называется по имени, связанное с объектом. В большинстве случаев она идентична функции, за исключением двух ключевых отличий:
#     -Метод неявно передается объект, на котором он был вызван.
#     -Метод может работать с данными, содержащимися в классе (помня, что объект является экземпляром класса - 
#     класс является определением, объект является экземпляром этих данных).

# Теория + Задачи
# 1.Oператоры
#     1.	Арифметические
#     2.	Операторы сравнения
#     3.	Операторы присваивания
#     4.	Логические операторы
#     5.	Операторы принадлежности
#     6.	Операторы идентификации
#     7.	Операторы приоритета
#     8.	Операторы сравнения:
#     print(2==2,3==2)
#     print(2!=2,3!=2)
#     print(2>2,3>2)
#     print(2<2,3<2)
#     print(2>=2,3>=2)
#     print(2<=2,3<=2)
#     9.Логические операторы:
#     	and (логическое умножение)
#         Возвращает True, если оба выражения равны True
#         age = 22
#         weight = 58
#         isMarried = False
#         result = age > 21 and weight == 58 and isMarried
#         print(result)
#     	or (логическое сложение)
#         Возвращает True, если хотя бы одно из выражений равно True
#         age = 22
#         isMarried = False
#         result = age > 21 or isMarried
#         print(result) 
#     	not (логическое отрицание)
#         Возвращает True, если выражение равно False

# 2.Полиморфизм — очень важная идея в объектно-ориентированном программировании.
# Чтобы узнать больше об ООП в Python, посетите эту статью: Python Object-Oriented Programming.
# Мы можем использовать идею полиморфизма для методов класса, так как разные классы в Python могут иметь методы с одинаковым именем.
# Позже мы сможем обобщить вызов этих методов, игнорируя объект, с которым мы работаем. Давайте взглянем на пример:
class Car1:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def info(self):
        print(f"Name is {self.name}. it is type {self.type}")

    def make_country(self):
        print("USA")


class Car2:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def info(self):
        print(f"Name is {self.name}. it is type {self.type}")

    def make_country(self):
        print("Uzbekistan")


car1 = Car1("NExia", 'style')
car2 = Car2("Lada", 'elegant')

for cars in (car1,car2):
    cars.make_country()
    cars.info()
3.
def validate(username, password):
    if username=="Random" and password =='2321ewfsef':
        return "Вы успешно вошли в систему!"
    else:
        return f'Пароль или имя пользователя не правильны'
print(validate("Random",'2321ewfsef'))
4.
# Область видимости переменных
# Глобальный контекст
# Глобальный контекст подразумевает, что переменная является глобальной, она определена вне любой из функций и доступна любой функции в программе.
# Локальный контекст
# В отличие от глобальных переменных локальная переменная определяется внутри функции и доступна только из этой функции, то
# есть имеет локальную область видимости:
# Если же мы хотим изменить в локальной функции глобальную переменную, а не определить локальную, то необходимо использовать
#  ключевое слово global
# nonlocal
# Выражение nonlocal прикрепляет идентификатор к переменной из ближайщего окружающего контекста (за исключением глобального контекста). Обычно nonlocal применяется во вложенных функциях, когда надо прикрепить идентификатор за переменной или параметром окружающей внешней функции. 

def outer():
    # enclosed
    x='local'
    def inner():
        # local
        nonlocal x
        x='non local'
        print("inner", x)
    inner()
    print('outer:',x)
outer()   
name='Dave'
def spam():
    global name #Импортируем глобальную переменную
    name='Guido' #Change the global name above
 
spam()
print(name)

def parent():
    a=5
    return a
print("Не вложенные",parent())
5.
def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))
# Задачи:
# 1.
def get_data(code,salary,*args, **kwargs):
    other_info = []
    # other_info.append(code)
    # other_info.append(salary)
    print(other_info)
    for arg in args:
        print(arg)
    for key,val in kwargs.items():
        other_info.append({key:val})
        return other_info

print(get_data('Code','Salary',23,25,kola=200))
2.
class Gum:  
    def __init__(self,smell,price,company, name, special_features, count):
        self.smell=smell
        self.company=company
        self.name =name
        self.price=price
        self.special_features=special_features
        self.count=count
    def __str__(self):
        return f'smell={self.smell},price={self.price},company={self.company},name={self.name},special_features={self.special_features},count={self.count}'
class Orbit(Gum):
    def __init__(self, smell, price, company, name, special_features, count,country):
        self.country=country
        super().__init__(smell, price, company, name, special_features, count)
    def __str__(self):
        return f'smell={self.smell},price={self.price},company={self.company},name={self.name},special_features={self.special_features},count={self.count},country={self.country}'
class Trident(Gum):
    def __init__(self, smell, price, company, name, special_features, count,date_of_production):
        self.date_of_production=date_of_production
        super().__init__(smell, price, company, name, special_features, count)
    def __str__(self):
        return f'smell={self.smell},price={self.price},company={self.company},name={self.name},special_features={self.special_features},count={self.count},date_of_production={self.date_of_production}'
a=Gum('Good',1000,'Niga','Pub','watermale',20)
b=Orbit('Good',1000,'Niga','Fight','apple',3000,'US')
c=Trident('Good',1000,'Niga','GM','pear',400,20.01)
print(a)
print(b)
print(c)
3.
class Fighter:
    def __init__(self, name, health, damage_per_attack):
        self.name = name
        self.health = health
        self.damage_per_attack = damage_per_attack

    def attack(self,enemy):
        return enemy-self.damage_per_attack

player1=Fighter('Lew',10,2)
player2=Fighter('Harry',5,4)
player2.health=player1.attack(player2.health)
player1.health=player2.attack(player1.health)
player2.health=player1.attack(player2.health)
player1.health=player2.attack(player1.health)
player2.health=player1.attack(player2.health)
player1.health=player2.attack(player1.health)
print(f'Harry now has {player2.health}  health and is dead. Lew wins    ')

class BaseCharacter:
    def __init__(self,health,mana,damage,type,skills):
        self.health=health
        self.mana=mana
        self.damage=damage
        self.type=type
        self.skills=skills
    
    def attack(self,enemy_health):
    
        c=[a-b for a, b in zip(enemy_health,self.damage)]
        pos_nos = [num  for num in c if num >= 0]
        print(sum(x<5 for x in pos_nos))
        pos_nos2 = [num  for num in c if num <= 0]
        print(sum(x<5 for x in pos_nos2))

player1=BaseCharacter(10,50,[1, 3, 5, 7] ,'base',['heal'])
player2=BaseCharacter([2, 4,0,0],50, 0,'base',['heal'])
player2.health=player1.attack(player2.health)
print(player2.health)

player1=BaseCharacter(10,50,[1, 3, 5, 7] ,'base',['heal'])
player2=BaseCharacter([2, 4,6,8],50, 0,'base',['heal'])
player2.health=player1.attack(player2.health)
print(player2.health)

player1=BaseCharacter(10,50,[1, 3, 5, 7] ,'base',['heal'])
player2=BaseCharacter([2, 4,0,8],50, 0,'base',['heal'])
player2.health=player1.attack(player2.health)
print(player2.health)


