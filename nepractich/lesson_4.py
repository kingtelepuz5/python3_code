list_of_lists = [['16','12','8','4','0'],['1','5','9','13','17'],['18','14','10','6','2'],['3','7','11','15','19']]
for i in range(len(list_of_lists)):
    print(list_of_lists[i])
#загрузить цепочку
#конвертировать шифортекст в шифросписок, разбив его на отдельные слова
#получить входные данные с числом столбоц и строк
#получить входные данные с ключом
#конвертировать ключ в список, разбив на отдельные числа
#создать новый список для переводной матрицы
#для каждого числа в ключе:
#создать новый список и добавить n элементов(n = число строк) из шифросписка
#использовать знак числа ключа, для того что бы решить, как следует читать строку матриы:
#вперед или назад
#используя выбранное направление, добавить в матрицу новый список. Индекс каждого нового списка зависит от номера столба, используемого в ключе
#создать новую символьную цепочку для хранения результатов перевода
#для диапазона строк матрицы:
#для вложенного списка в переводной матрице :
#удалить последнее слово во вложенном списке
#добавить слово в цепочку с переводом
#напечатать символьную цепочку с переводом
ciphertext = "16 12 8 4 0 1 5 9 13 17 18 14 10 6 2 3 7 11 15 19"
#разбить элементы на слова, не на буквы
cipherlist = list(ciphertext.split())
#инициализировать переменные
COLS = 4
ROWS  = 5
key = '-1 2 -3 4' #отрицательное число означает чтение вверх столбца, а не вниз
translation_matrix = [None] * COLS
plaintext = ''
start = 0
stop = ROWS
#превратить key_int в список целых чисел
key_int = [int(i) for i in key.split()]
#превратить столбцы в элементы списков
for k in key_int:
    if k < 0: #читать столбец снизу вверх
        col_items = cipherlist[start:stop]
    elif k > 0: # читать в столбец сверх вниз
        col_items = list((reversed(cipherlist[start:stop])))
translation_matrix[abs(k) - 1] = col_items
start += ROWS
stop += ROWS

print('\n шифротекст = {}'.format(ciphertext))
print("\n переводная матрица =", *translation_matrix, sep="\n")
print("\n длина ключа = {}".format(len(key_int)))

#обойти в цикле вложенные списки, передавая последний элемент
#в новый список:
for i in range(ROWS):
    for col_items in translation_matrix:
        word = str(col_items.pop())
plaintext += word + ' '
print("\n открытый текст = {}".format(plaintext))
