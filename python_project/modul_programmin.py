import numpy as np
import scipy.linalg as ls
import math as m
import sys

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
