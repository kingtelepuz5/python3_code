def apply_twice(func, arg):
    return func(func(arg))

def add_five(x):
    return x + 5

print(apply_twice(add_five, 10))

def mu_func(f, arg):
    return f(arg)

mu_func(lambda x: 2*x*x, 5)

#named func
def polynominal(x):
    return x**2 + 5*x + 4
print(polynominal(-4))

#labmda
print((lambda x: x**2 + 5*x + 4)(-4))
def add_five(x):
    return x + 5

nums = [11, 22, 33, 44, 55]
result = list(map(add_five, nums))
print(result)

result  =(list(map(lambda x: x+ 5, nums))) #  применяет к каждому элементу действие функции
print(result)

res = list(filter(lambda x: x%2 ==0, nums)) # только те, что сооветствуют условию
def countwodn():
    i = 5
    while i > 0:
        yield i
        i -= i
for i in countwodn():
    print(i)

#def infinty_sevens():
#    while True:
#        yield 7 # бесоконечная генерация семерки

#for i in infinty_sevens():
#    print(i)


#def get_primes():
#    num = 2
#    while True:
#        if is_prime(num):
#            yield num
#        num +=1

def numbers(x):
    for i in range(x):
        if i % 2 == 0:
            yield 1

print(list(numbers(1)))

def make_word():
  word = ""
  for ch in "spam":
    word +=ch
    yield word

print(list(make_word()))


def decor(func):
    def wrap():
        print("==============")
        func()
        print("==============")
    return wrap
@decor
def print_text():
    print("hello world")
print_text()

def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)

print("factorial 5 :",factorial( 5))

def is_even(x):
    if x == 0:
        return True
    else:
        return is_odd(x -1)
def is_odd(x):
    return not is_even(x)

print("is odd fo 17: ",is_odd(17))
print("is odd fo 23: ",is_odd(23))
print("is odd fo 0: ",is_odd(0))

def fib(x):
  if x == 0 or x == 1:
    return 1
  else:
    return fib(x-1) + fib(x-2)
print("fib fo 4",fib(4))

def function1(named_arg, *args):
    print(named_arg)
    print(args)

function1(1, 2 ,3 ,4, "syka blyat")

def func2(x, y =7, *args, **kwargs ):
    print(kwargs)
func2(2, 3, 4, c=5, d=6, a=7, b=8)

nums1 = {1, 2, 3, 4, 5}
nums1 = {0, 1, 2, 3} & nums1
nums1 = filter(lambda x: x> 1, nums1)
print(len(list(nums1)))

def power(x, y):
  if y == 0:
    return 1
  else:
    return x * power(x, y-1)

print("print power (2, 3): ",power(2, 3))

a = (lambda x: x * (x + 1))(6)
print("it's a lambda 6 x * x + 1: ",a)

nums2 = [1, 2, 3, 4, 5, 6, 7, 8]

res1 = list(filter(lambda x : x % 2== 0, nums2))
print(res1)

def func3(**kwargs):
    print(kwargs["zero"])
print("print func3 a = 0, zero = 8: ")
func3(a = 0, zero = 8)

def reverse(txt):
    n = len(txt)
    if n:
        print(txt[-1])
    if 1 < n:
        reverse(txt[:-1])

txt = input()
reverse(txt)
