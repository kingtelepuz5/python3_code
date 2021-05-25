
#x = int(input('Введите X, функция один \n'))
def func1(*args):
    '''
    при х > 0 = 2*x -10, x == 0 = 0, x < 0 = 2 *abs(x) - 1
    '''
    y1 = 2*x - 10
    y2 = 0
    y3 = 2 * abs(x) -1 # abs it's |x|, mod s
    if x > 0:
        return y1
    elif x==0:
        return y2
    else:
        return y3

def func2(*args):
    '''здесь проверка на max  '''
    m = int(input('Введите несколько чисел, функия два \n'))
    b = int(input('Введите несколько чисел, функия два \n'))
    c = int(input('Введите несколько чисел, функия два \n'))
    if m < b:
        m = b
    if m < c:
        m = c
    print("it's max :", m)


def func3(*args):
    '''здесь проверка на max  '''
    a = int(input('Введите несколько чисел, функия два \n'))
    b = int(input('Введите несколько чисел, функия два \n'))
    c = int(input('Введите несколько чисел, функия два \n'))
    if a > b:
        if a > c:
            print('Максимум = ', a)
        else:
            print('Максимум = ', c)
    else:
        if b > c:
            print('Максимум = ', b)
        else:
            print('Максимум = ', c)

def bit(*args):
    '''
b-байты в к-килобайты из ans
    '''
    num = int(input("Введите байты\n"))
    ans = input("Перевести в байты - 'b', в килобайты - 'k'\n")
    ans = ans.lower()#делаем все входные заниженными
    if ans == 'b':
        print("{} Килобайт = {} байт".format(num, num*1024))
    elif ans == 'k':
        print("{} байт = {} килобайт".format(num, num/1024))
    else:
        print('Невернный код ')



bit()
