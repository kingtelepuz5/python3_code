'''
message = 'Live long and prosper'
f = open('data_file.txt', 'wt')
print('a', 'b', 'c', file=f)
f.close()
f = open('data_file.txt', 'rt')
data = f.read()
f.close()

f = open('data_file', 'rt')
data = ' ыфвф фыв фы вфы фыв фыв фыв фыв ввфы'
block_size = 100
while True:
    block = f.read(block_size)
    if not block:
        break
    data += block
f.close()
f = open('results.txt', 'rt')
data = ''
while True:
    line = f.readline()
    if not line:
        break
    data += line
f.close()

# файл как итератор

f = open('results.txt', 'rt')
for line in f:
    data +=line
f.close()
# чтение бинарных файлов
f = open('data.xlsb', 'rb') # b = binar
bdata = f.read()
print(type(bdata))
f.close()

# запись бинарных данных

bdata = bytes(x for x in range(0, 256))
f = open('data.obj', 'wb') # создаем и записываем в файл
f.write(bdata)
f.close()
message = '0123'
with open('data.txt','wt') as f:
    f.write(message)

f = open('data.obj', 'rt')

f.tell()
'''
#проверка на наличие ключа
def p_d_E(d, my_key): # print_dict_val_EAFP проверяем ключ
    try:
        print(d[my_key])
    except  KeyError:
        print('Ключ не найден:', my_key)
def p_d_L(d, my_key): #print_dict_val_LBLYL
    if my_key in d:
        print(d[my_key])
    else:
        print('Ключ не найден', my_key)

try:
    f = open("data_file.txt", "r")
    a = f.readline()
    a1 = int(a)
except  IOError as error:
    printa("Невозможно открыть или прочитать файл")
    print("имя файла: ", err.filename)
except (FileNotFoundError, ValueError) as err:
    print("Ошибка загрузки данных")
except:
    print("Неизвестная ошибка")
else:
    a = f.readline()
finally:
    f.close() #finally в любом случае выполнит код
#help(func)

#s = float(input('Введите основание треугольника'))
#р = float(input('Введите высоту треугольника'))
def input_as(text, type_of_value):
    is_bad_input = True
    while is_bad_input:
        try:
            val = input(text)
            val = type_of_value(val)
            is_bad_input = False
        except  ValueError as err:
            print("это не " + type_of_value.__name__+" попробуйте еще раз ")
    return val

val = input_as("Введите целое число ", int)
print("Введено значение", val)

try:
    a = float(input('a='))
    b = float(input('b='))
    divide(a, b)
except:
    print('Неверные исходные данные')
def divide(a, b):
    try:
        res = a / b
    except:
        print('divide: b = 0!')
        raise
    return res
try:
    msg = 'Введите число в диапазоне от {} до {} : '
    a, b = 1, 100
    x = int(input(msg.format(a,b)))
    if x<a or x>b:
        msg = 'Значение вне диапазона {}, {} :'
        raise Exception(msg.format(x, a, b))
    print(x)
except Exception as err:
    print(err.args[0])

'''
class Point:
    def __init__(self, coordinates): #конструктор
        self.x = coordinates[0]
        self.y = coordinates[1]
    def move(self, delta): #переместить точку
        self.x = self.x + delta[0]
        self.y = self.y + delta[1]


p1 = Point([1, 3])
print(p1.x, p1.y)
p1.move([2, 3])
print(p1.x, p1.y)

class Tree(object):
    def __init__(self, kind, age, height):
            self.kind = kind
            self.age = 0
            self.height = height

    def info(self):
            """ метод выводи информацию о дереве"""
            print("name -> {}, years old -> {}, meters high -> {} ".format(self.kind, self.age,self.height ))
    def grow(self):
            self.age +=1
            self.height += 0.5

kind = "rovv"
height = 5
age = 0
print("{} years old {}. {} meters high".format(kind, age, height))

tree1 = Tree("tran", 1, 3)
print("tree1 kind :->" ,tree1.kind)
print("tree1 age:-> ",  tree1.age)
print("tree1 height:-> ", tree1.height )
tree1.grow()
print("tree1 one year ago, kind :->" ,tree1.kind)
print("tree1 one year ago, age:-> ",  tree1.age)
print("tree1 one year ago, height:-> ", tree1.height )
tree1.info()

class FruitTree(Tree):
    def __init__(self, kind , age, height):
        #наследование происходит с помощью super(), без self
        super().__init__(kind ,age, height)

    def give_fruits(self):
        print("Collected 20kg of {}s".format(self.kind))

tree_1 = Tree("oak", 0.5, 1)
tree_2 = FruitTree("apple", 0.7, 1)

tree_2.info()
tree_2.grow()

tree_1.info()
tree_1.grow()

tree_2.give_fruits()
#tree_1.give_fruits()
tree_1.info()
tree_2.info()


class i_am_pregoremmer:
    def __init__(self,i_am , can, create, boobs):
        self.i_am = i_am
        self.can = can
        self.create = create
        self.boobs = boobs
import math

class Circle:
    def __init__(self, radius):
        self.__radius = radius

    @property
    def area(self):
        return math.pi*self.__radius**2

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, radius):
        self.__radius = radius



c = Circle(10.0)
print(c.area)
c.radius = 5
print(c.area)

class Circle1:
    def __init__(self,x ,y, r):
        self.x = x
        self.y = y
        self.r = r
    def __eq__(self, other):
        return self.r == other.r
o1 = Circle(0, 0, 2)
o2 = Circle(1, 0, 2)

print(o1 == o2)
'''
