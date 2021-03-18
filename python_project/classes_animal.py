class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color

class Cat(Animal):
    def purr(self):
        print("purr....")

class Dog(Animal):
    def bark(self):
        print("Woof")

fido = Dog("Fido", "brown")
print(fido.color)
fido.bark()

class Wolf:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    def bark1(self):
        print("Grrrr....")

class Dog1(Wolf):
    def bark1(self):
        print("Woof")

husky = Dog("Max", "grey")
husky.bark()

class A:
    def spam(self):
        print(1)
class B(A):
    def spam(self):
        print(2)
        super().spam()# ищет в родителе функцию спами вовзращает

B().spam()


class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

first = Vector2D(5, 7)
second = Vector2D(3, 9)
result = first + second
print(result.x)
print(result.y)

'''
__sub__ for -
__mul__ for *
__truediv__ for /
__floordiv__ for //
__mod__ for %
__pow__ for **
__and__ for &
__xor__ for ^
__or__ for |
''' 

class SpecialString:
    def __init__(self, cont):
        self.cont = cont

    def __mul__(self, other):
        line = "=" * len(other.cont)
        return "\n".join([self.cont, line, other.cont])

spam = SpecialString("spam")
hello = SpecialString("hello world!")
print(spam*hello)


''' 
__lt__ for <
__le__ for <=
__eq__ for ==
__ne__ for !=
__gt__ for >
__ge__ for >=

If __ne__ is not implemented, it returns the opposite of __eq__.
''' 

class SpecialString1:
    def __init__(self, cont):
        self.cont = cont
    
    def __gt__(self, other):
        for index in range(len(other.cont)+1):
            result = other.cont[:index] + ">" + self.cont
            result += ">" + other.cont[index:]
            print(result)
spam = SpecialString1("spam")
eggs = SpecialString1("eggs")
spam > eggs

'''
__len__ for len()
__getitem__ for indexing
__setitem__ for assigning to indexed values
__delitem__ for deleting indexed values
__iter__ for iteration over objects (e.g., in for loops)
__contains__ for in

There are many other magic methods that we won't cover here, such as __call__ for calling objects as functions, and __int__, __str__, and the like, for converting objects to built-in types.
'''

import random 

class VagueList:
    def __init__(self, cont):
        self.cont = cont
    def __getitem__(self, index):
        return self.cont[index + random.randint(-1, 1)]
    def __len__(self):
        return random.randint(0, len(self.cont)*2)

vague_list = VagueList(["A", "B", "C", "D", "e"])
print(len(vague_list))
print(len(vague_list))
print(vague_list[2])
print(vague_list[2]
)

def zeros(*args, **kwargs):
    if kwargs.get('dim1'):
        res = [0]*kwargs['dim1']
    if kwargs.get('dim2'):
        res = [0]*kwargs['dim2']
    return res
print(zeros(dim1 = 2, dim2 = 2))
dims = {'dim1': 2, 'dim2': 2 }
print(zeros(**dims))

import numpy as np

def orbital_velocity(height):
    ''' 
    скорость движения по круговой орбите вокруг земли км/ч 
    height - высота орбиты в км 
    '''
    Rz = 6371
    mu = 398600.4418
    return np.sqrt(mu/(Rz+height))

def step_function(x0, y0, y1):
    def step(x):
        if x<x0:
            return y0
        else:
            return y1
    return step

unit_step = step_function(0.0, 0.0, 0.1)
print(unit_step(-2))
print(unit_step(1))