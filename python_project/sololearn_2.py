    #икапсуляция
class Queue:
    def __init__(self, contents):
        self._hiddenlist = list(contents)

    def push(self, value):
        self._hiddenlist.insert(0, value)

    def pop(self):
        return self._hiddenlist.pop(-1)

    def __repr__(self):
        return "Queue({})".format(self._hiddenlist)

queue = Queue([1, 2, 3])
print(queue)
queue.push(0)
print(queue)
print(queue._hiddenlist)

class Spam:
    __egg = 7
    def print_egg(self):
        print(self.__egg)

s  = Spam()
s.print_egg()
print(s._Spam__egg)

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def calculate_area(self):
        return self.width * self.height

    @classmethod
    def new_square(cls, side_length):
        return cls(side_length, side_length)
square = Rectangle.new_square(5)
print(square.calculate_area())

class Person:
    def __init__(self, name):
        self.name = name
    @classmethod
    def sayHi(cls):
        print("hi")

Person.sayHi()


class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings

    @staticmethod
    def validate_topping(topping):
        if topping == "pineapple":
            raise ValueError("No pineapples!")
        else:
            return True
ingredients = ["cheese", "onions", "spam"]
if all(Pizza.validate_topping(i) for i in ingredients):
    pizza = Pizza(ingredients)
