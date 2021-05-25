print([x ** 2 for x in range(10) if x %2 > 0]) # выводит числа больше нуля и четные 2
print([x.lower() for x in ['I', 'AM', 'NOT', 'SHOUTING']])# делает числа низкими
empoy = {'Alice':100000,
        'Bob': 99817,
        'Frank': 88123,
        'Eve': 93121
}
top_era = [(k, v) for k, v in empoy.items() if v >= 10000] # не понял пока что как это работает
print(top_era)
text = "Call me Ishmael. Some years ago - never mind how long precisely - having little or no money in my purse, and nothing particular to interest me on shore, I thought I would sail about a little and see the watery part of the world. It is a way I have of driving off the spleen, and regulating the circulation. - Moby Dick"
w = [[x for x in line.split() if len(x)>3]for line in text.split('\n')] #мы помещаем х в цикл в лине сплит, и если длина больше 3, помещаем  цикл сплит
print(w)
#filename = "algoritm_with_python/algoritm_less2.py"
#f = open(filename)
#lines = []
#for line in f:
#    lines.append(line.strip())

#print(lines) # bad out
#f.close()
#print([line.strip() for line in open("algoritm_with_python/algoritm_less2.py")])
txt = ['lambda functions are anonymous functions.',
'anonymous functions dont have a name.',
'functions are objects in Python.']
mark = map(lambda s:(True, s) if 'anonymous' in s else (False, s), txt) # search string name 'anonymous'
print(list(mark))
letters_amazon = '''
We spent several years building our own database engine,
Amazon Aurora, a fully-managed MySQL and PostgreSQL-compatible
service with the same or better durability and availability as
the commercial engines, but at one-tenth of the cost. We were
not surprised when this worked.
'''
find = lambda x, q: x[x.find(q)-18:x.find(q)+18] if q in x else -1 # ищет диапазон 18 букв лево право, если q есть в икс, иначе -1
print(find(letters_amazon, 'SQL'))

price = [[9.9, 9.8, 9.8, 9.4, 9.5, 9.7],
[9.5, 9.4, 9.4, 9.3, 9.2, 9.1],
[8.4, 7.9, 7.9, 8.1, 8.0, 8.0],
[7.1, 5.9, 4.8, 4.8, 4.7, 3.9]]
sample = [line[::2] for line in price]
print(sample)

visitors = ['Firefox', 'corrupted', 'Chrome', 'corrupted',
'Safari', 'corrupted', 'Safari', 'corrupted',
'Chrome', 'corrupted', 'Firefox', 'corrupted']

visitors[1::2] = visitors[::2] # func заменяет все корруптед
print(visitors)
import matplotlib.pyplot as plt

cardiac_cycle = [62, 60, 62, 64, 68, 77, 80, 76, 71, 66, 61, 60, 62]

expected_cycle = cardiac_cycle[1:-2] * 10

#plt.plot(expected_cycle)
#plt.show()

companies = {'CoolCompany' : {'Alice' : 33, 'Bob' : 28, 'Frank' : 29},
'CheapCompany' : {'Ann' : 4, 'Lee' : 9, 'Chrisi' : 7},
'SosoCompany' : {'Esther' : 38, 'Cole' : 8, 'Paris' : 18}}
ilegal = [x for x in companies if any(y<9 for y in companies[x].values())]
print(ilegal)

lst_1 = [1, 2, 3]
lst_2 = [4, 5, 6]
zipped = list(zip(lst_1, lst_2))
print(zipped)
lst_1_new, lst_2_new = zip(*zipped)
print(list(lst_1_new))
print(list(lst_2_new))
colum_namex = ['name', 'salary', 'job']
db_rows = [('Alice', 180000, 'data scientist'),
('Bob', 99000, 'mid-level manager'),
('Frank', 87000, 'CEO')]
db = [dict(zip(colum_namex, row))for row in db_rows]
print(db)
