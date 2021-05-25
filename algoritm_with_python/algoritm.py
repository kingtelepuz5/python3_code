# list_1 = [1, 2, 3, 4]
# list_2 = [1, 2, 3, 4]
# list_3 = [1, 2, 3, 4]
# list_4 = [1, 2, 3, 4]
# for i, item in enumerate(list_1):
#     del item
#
# print(list_1)
# seasons = ['Spring', 'Summer', 'Fall', 'Winter']
# print(list(enumerate(seasons)))
# for i, item in enumerate(list_2):
#     list_2.remove(item)
#
# print(list_2)
#
# for i, item in enumerate(list_3):
#     list_3.pop(i)
#
# print(list_3)
# for i, item in enumerate(list_4[:]):
#     list_4.remove(item)
# print(list_4)
# row = [''] * 3
# board = [row]* 3
# print(board)
# board[0][0] = 'X'
# print(board)
# board = [[''] * 3 for _ in range(3)]
# board[0][0] = 'X'
# print(board)
# t = ('one', 'two')
# for i in t:
#     print(i)
# t = ('one')
# for i in t:
#     print(i)
# lst = [1 , 5, 6, 1, 6, 2, 4, 5, 1 ,6 ,5]
# lst = list(set(lst))
# print(lst)
import random
# def bin_search(array, value):
#     left = 0
#     right = len(array) - 1
#     pos = len(array) // 2
#
#     while array[pos] != value and left <= right:
#         if value > array[pos]:
#             left = pos + 1
#         else:
#             right = pos - 1
#         pos = (left + right) //2
#     return -1 if left > right else pos
# a = [random.randint(0, 1000) for _ in range(100)]
# a.sort()
# print(a)
# #n = int(input('Какой элементы вы ищите: '))
# #print(bin_search(a, n))
# array = [random.randint(-100, 100) for _ in range(100)]
# print(array)
# arr_below = []
# arr_lager = []
# for item in array:
#     if item > 0:
#         arr_lager.append(item)
#     elif item < 0:
#         arr_below.append(item)
# print(arr_below)
# print(arr_lager)
#
# num = int(input('Введите целое число для вставки:\n'))
# pos = int(input('На какую позицию вставить число:\n'))

# array.append(None)
#
# i = len(array) - 1
# while i > pos:
#     array[i], array[i - 1] = array[i -1], array[i]
#     i -= 1
# array[pos] = num
# print(array)

# array.insert(pos, num)
# array[pos] = num
# print(array)
# matrix = [[random.randint(1 ,10) for _ in range(10)] for _ in range(7)]
# for line in matrix:
#     for item in line:
#         print(f'{item:>4}', end='')
#     print()
#
# sum_column = [0] * len(matrix)
# for line in matrix:
#     sum_line = 0
#     for i, item in enumerate(line):
#         sum_line += item
#         sum_column[i] += item
#
#         print(f'{item:>5}', end='')
#     print(f'   | {sum_line}')
#
k = int(input('Введите колличевство предприятий:'))
enterprises = {}

for i in range(1, k + 1):
    name = input('Введите название предпреятия:')
    enterprises[name] = [float(input('План:')), float(input('Факт:'))]

    enterprises[name].append(enterprises[name][1] / enterprises[name][0])

print('Фактическая прибыль больше 10, но план не выполнен (меньше 100%)')
for key, value in enterprises.items():
    if value[1] > 10 and value[2] < 1:
        print(f'предприятие {key} заработало {value[1]}, что составило {value[2] * 100:.2f}%')
# a = [0] * 8
#
# for i in range(2 ,100):
#     for j in range(2, 100):
#         if i % j == 0:
#             a[j - 2] += 1
# for i, item in enumerate(a, start=2):
#     print(f'Числу {i} кратно {item} чисел')
M = 5
N = 4
matrix = []

for i in range(N):
    row = []
    summ = 0
    for j in range(M-1):
        num = int(input(f'Строка {i}, элемент {j}: '))
        summ += num
        row.append(num)
    row.append(summ)
    matrix.append(row)
for line in matrix:
    for item in line:
        print(f'{item:>5}', end='')
    print() 
