#vec1 = [1, 3, 4, 5]
#vec2 = [8, 5, 3, 1]
#prod = map(lambda x,y: x*y, vec1, vec2)
#scalar_product = sum(list(prod))


#data = [10, 11, 12 ,13, 14]

#list(map(lambda x: x**2, data))

# res = [x**2 for x in data]


#[x**2 for x in range(10) if x %2 ==0]

#list(map(lambda x: x**2, filter(lambda x:x%2 ==0, range(10))))
#[x+'-'+y for x in ('A', 'B') for y in ('1', '2')] # берем х из а и б, у из 1 и 2, и спаиваем

def pregression(a1, d, n):
    ''' прегрессия генерирует числа по формуле а + д * н,
    на вход подаются три числа, где первое это а, второе это д,
    третье это н, н равно колличевству чисел в листе на выходе, а степень зависит от и
    пример list(pregression(1, 15, 15))
    [1, 16, 31, 46, 61, 76, 91, 106, 121, 136, 151, 166, 181, 196, 211]
    '''
    # an = a1 + d(n-1)
    for i in range(n):
        yield  a1 + d * i
#list(pregression(1, 15, 15))

def fib(count):
    '''
    генерирует числа Фибоначи
    list(fib(10))

    '''
    n0, n1 = 0, 1
    for i in range(count):
        n0, n1 = n1, n0 + n1
        yield n0
#list(fib(10))
