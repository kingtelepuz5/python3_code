import sys
sys.setrecursionlimit(3000) #слишком болое число убьет идеа
#num = int(input('Введите целое число: '))
def delim(num):
    ''' если число больше 0, выводит первое число, остатка от деления на 10 '''
    while num >0:
        print(num %10)
        num //=10
def post(num):
    '''проверка находится ли число в диапазоне от 0 до 100 '''
    while True:
        num = float(input('Введите число от 0 до 100: '))
        if num >= 0 and num <= 100:
            print('Вы ввели', num)
            break
        else:
            print("Попробуйте еще раз")

#print("Это вывод вне тела цикла")
def out(num):
    '''Выводит 10 раз num '''
    i = 0
    while i <= 100:
        print(i)
        i +=1
def out1(num):
    '''Выводит 10 раз num '''
    for i in range(11):
        print(1)
def recurs_1(a, b):
    if a == b:
        return str(a)

    if a > b:
        return a, recurs_1(a -1, b)
    if a < b:
        return a, recurs_1(a + 1, b)
def akk(m, n):
    '''
алгоритм аккермана
    '''
    if m ==0:
        return n + 1
    elif m > 0 and n == 0:
        return akk(m - 1, 1)
    return akk(m - 1, akk(m, n-1))
#print(akk(3, 8))
def gcd(m, n):
    '''
    Алгоритм Евклида
    нахождение общего большего делителя с помощью вычитания
    '''
    while m!= n:
        if m > n:
            m -=n
        else:
            n -=m
    return m
#print(gcd(540, 24454329294))
def gcd1(m, n):
    if n==0:
        return m
    return gcd1(n, m % n)

#print(gcd1(540, 24454329294))
def gcd3(n, m):
    while n!=0:
        m, n = n, m % n
    return m
#print(gcd1(540, 24454329294))
#начало
n = int(input('До какого числа получить простые числа: '))
sieve = [i for i in range(n)]
sieve[1] = 0
'''решето Эратосфена '''
for i in range(2, n):
    if sieve[i] != 0:
        j = i*2
        while j < n:
            sieve[j] = 0
            j += i
result = [i for i in sieve if i != 0]
#конец
def binary(num):
    s = 0
    while num > 0:
        s = num % 2
        s += s
        num //= 2
    return s
#============дом задание ================
while True:
    print("Ноль в качевстве знака операции завершит задание")
    s = input("Введите знак (+,-,*,/,0): ")
    if s == '0':
        break
    if s in {'+', '-', '*', '/'}:
        x = float(input("x = "))
        y = float(input("y= "))
        if s == '+':
            z = x + y
            print("Сумма = ", z)
        elif s == '-':
            z = x -y
            print("Разница = ", z)
        elif  s == '*':
            z = x * y
            print("Умножение = ",z)
        elif s == '/':
            if y != 0:
                z = x / y
                print("Деление = ",z)
            else:
                print("Деление на ноль!")
    else:
        print("Неверный знак операции")

        
