import lecture_one_lisa as ll
a = str(list(ll.fib(10)))
print("it's fib simbol :\n ", a)
b = str(list(ll.pregression(4, 10, 20)))
print("it's pregression simbol :\n ", b)
'''with open('test.txt', 'w') as f:
    f.write(a)
    f.write(b)'''
my_list = list(ll.pregression(4, 10, 20))
with  open('test.txt', 'w') as f:
    for item in my_list:
        f.write("%s," % item)

#with open('test.txt', 'a') as f:
#    f.write(''' r	открытие на чтение (является значением по умолчанию)
#'w'	открытие на запись, содержимое файла удаляется, если файла не существует, создается новый.
#'x'	открытие на запись, если файла не существует, иначе исключение.
#'a'	открытие на дозапись, информация добавляется в конец файла.
#'b'	открытие в двоичном режиме.
#'t'	открытие в текстовом режиме (является значением по умолчанию).
#'+'	открытие на чтение и запись ''')

with open('test.txt', 'a') as f:
    f.write('\n ЭТОТ ФАЙЛ ТЕСТОВЫЙ')

with open('test.txt', 'r') as f:
    print(f.read())
