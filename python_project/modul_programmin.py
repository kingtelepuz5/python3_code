import numpy as np
import scipy.linalg as ls
import math as m
import sys
from scipy.optimize import root #

a = m.sin(m.pi/4.0)
print("sin pi/4", a)
A = np.matrix([[1,2,3],[4,5,6],[3, 4, 1]])
B = np.matrix([[1],[2],[3]])
x = ls.solve(A, B) # нахождение неизвестного х в формул Ax=B
print(x)
c = np.dot([2j, 3j], [2j, 3j]) # точечное произведение двух массивов
print(c)
sys.path # смотрим где все импорты лежат, каждый охтник желает знать, где
'''from cmath import *
    from math import *
 a = sqrt(-0,5)
 out: math domain Error

 or if use
 import math
 import cmath
 b = cmath.sqrt(x)
 out: ok
'''
b = m.isclose(59990.6678,60000.5678, rel_tol=0.001,abs_tol=0.0 ) # проверяет равенство чисел с заданной точностью
print(b)
c = m.log(10, 3)
print("log 10, по основанию 3: ",c)

m.hypot(10,30) # гипотинуза
m.radians(10) # в радианы
m.degrees(10) #в градусы
m.inf * m.e * m.pi  # бесконечность умножить на е и умножить на пи так же есть m.nan

m1 = np.matrix([[1,2,3],[5,5,6]])
m2 = np.matrix([[3,2],[4,2],[1,1]])
m1 * m2
import matplotlib.pyplot as plt

x = np.arange(0.0, np.pi*2.0, 0.1) # генерируем числа на интервале от нуля до 2пи с шагом 0.1
y1 = np.sin(x) #строим синус
y2 = np.cos(x) #строим косинус

plt.plot(x, y1, x, y2) # строим график синуса и косинуса
plt.axis([0, 2*np.pi, -1.1, 1.1 ]) # строим оси, (ось х начало,ось х конец, ось у начало, ось у конец )
plt.xlabel('$\\alpha, rad')
plt.ylabel('f(x)')
plt.legend(["sin","cos"])
plt.show()


def func(x):
    ''' x + 2cos(x) = 0 '''
    return x + 2 * np.cos(x)

sol = root(func, 0.3)
print(sol.x)
