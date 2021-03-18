class cat:
    def __init__ (self, color, legs):
        self.color = color
        self.legs = legs

Felix = cat("ginger", 4)
Rover = cat("dog-colored", 4)
stumpy = cat("brown", 3)

print("it's color Felix: ",Felix.color)
print("it's legs fo Felix: ",Felix.legs)

class student:
    def __init__(self, name):
        self.name = name


test = student("Artur")

class Dog:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def bark(self):
        print("Woof!")

fido = Dog("Fido", "Brown")
print(fido.color)
fido.bark()

class Std:
    def __init__(self, name):
        self.name = name
    
    def sayHi(self):
        print("Hi from : " + self.name)

s1 = Std("Ame")
s1.sayHi()