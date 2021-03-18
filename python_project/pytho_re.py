import re

pattern = r"pam"

if re.match(pattern, "eggspameggspameggspam"):
    print("Match")
else:
    print("No mutch")

if re.search(pattern, "eggspameggspameggspam"):
    print("Match")
else:
    print("No match ")

print(re.findall(pattern,"eggspameggspameggspam" ))
'''
import re
quote = "Always do your best. Your best is going to change from moment to moment; it will be different when you are healthy as opposed to sick. Under any circumstance, simply do your best, and you will avoid self-judgment, self-abuse and regret"

word = input()
print(re.findall(word, quote)) # слова в тексте 
# ДЛЯ ПОИСКА СОВПАДЕНИЙ В ТЕКСТЕ 
''' 
match = re.search(pattern, "eggspameggspameggspam")
if match:
    print(match.group())
    print(match.start())
    print(match.end())
    print(match.span())


str = "My name is David. Hi David"

pattern1 = r"David"
newstr = re.sub(pattern1, "Ame", str)
print(newstr)

'''
Программа которая проверяет название книги и присваевает ей сначала первую букву имени
после суммирует все числа и выдает их + первая буква 
Some book
Another book

Your program should output:
S9
A12


file = open("/usercode/files/books.txt", "r")

#your code goes here
for line in file:
    title=line.replace('\n', '')
    count=len(title)
    print(f'{title[0]}{count}')

file.close() 
'''

try:
    print("hello world")
    print(1 / 0)
except ZeroDivisionError:
    print("Divided by zero")
finally:
    print("This code will run no matter what")

try:
    print(1)
    print(10 / 0)
except ZeroDivisionError:
    print('unknown_var')
finally:
    print("This is executed last")


'''try:
    num = 5/ 0
except:
    print("An erro occurated")
    raise
'''
print(1)

assert 2+2 == 4

print(2)

temp = -10

assert (temp >= 0), "Colder than absolvet zero!"