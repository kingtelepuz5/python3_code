a = complex(7, 3) #a = 7 + 3i  float

print("real",a.real)
print("вещ",a.imag)

b  =  [1, 'word ', 2, complex(3,7)] #list
print(len(b))
print(b[0])
print(b[3]) 

c = list(range(10))
print(c)

d = list('cat')
print(d)    

p1 = ["Earth","Lun"]
p2 = ["Earth","Lun"]
p1.extend(p2)
print(p1)
del p1[2]
print(p1)
message = 'Quid est veritas?'
print(message[3])
print(message[3:8])

g = '2 12 85 06'
L = g.split(' ')
print(L)

f = [1,2,3,4,5]
f1 = list(f)

f[0]  = 0
print(f)
print("print",f1)

r = tuple(range(10))
print(r)

s1 = {'d', 'abc', 2, 3, 4, 5}

s2 = set('windom')
print(s2)

s3 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
s4 = {1, 2, 3, 11, 12, 14, 15}
print("it's A|B, объеденение: ",s3.union(s4))
print("it's A-B, разносноть : ",s3.difference(s4)) 
print("it's A ^ B, принадлежность : ",s3.symmetric_difference(s4))
print("it's A<=B, подмножество : ",s3.issubset(s4)) 
print("it's A>=B, подмножество : ",s3.issuperset(s4)) 

data = [[7235, 'brabery'],[4321, 'robery']]
vesees = dict(data)
print(vesees)

vesees[4444] = 'Procodief'
print(vesees)
del vesees[4444]
print(vesees)
print(vesees.keys())
print(vesees.values())
t = vesees.copy()
print(t.items())
t.clear()
for i in [3,2,1,'start']:
    print(i)
for i in 'hello world':
    if i=='o':
        continue
    print(i, end='')
for i in 'hello world':
    if i=='o':
        break
    print(i, end='')
e = 0
g = 1
while e < 50:
    print(e)
    g = g + e
    e = g - e
u,y = 0, 1
while u < 50:
    print(u)
    u, y = y,u + y
else:
    print('Следующие число фибонначи больше 50 и равно', u)


r3 = list(range(1, 10, 2))
print(r3)

week = ['Пн','Вт','Ср','Чт','Пя','Сб','Вскр']
n = len(week)

for i in range(n):
    print('''{}' день недели - {}'''.format(i+1, week[i]))


def spring_force (f0, fk, h, x):
    if 0 < x < h:
        res = 0
    else:
        res = f0 - (f0-fk)*x/h
    return res
y1 = spring_force(10, 2, 0.1, 0.005)
print(y1)

def height_max (v0, g = 9.81):
    '''
     Максимальная высота подъема груза, брошенного вверх 
     с начальной скоростью v0(м/с)
     при ускорении свободного падения g(м/с**2)
     '''
    return 0.5*v0**2/g

man_PAF = 80
man_up_down = height_max(man_PAF)
print(man_up_down)
print(height_max(man_PAF, 1.62))
def add_elements_to_p (o, p = []):
    p.append(o)
    return p
print(add_elements_to_p(5))
print(add_elements_to_p(6))

def add_element_to_p1(o1, p1 = []):
    if p1 == None:
        p1 = []
    p1.append(o1)
    return p1 
def zeros(*args):
    print('Аргументы: ', args)
    if len(args) == 1:
        return [0]*args[0]
    if len(args) == 2:
        return [[0]*args[0]]*args[1]

print(zeros(3, 3))

def zeros1(**kwargs):
    if kwargs.get('dim1'):
        res = [0]*kwargs['dim1']
    if kwargs.get('dim2'):
        res = [res]*kwargs['dim2']
    return res
print(zeros1(dim1=3))
print('\n')
print(zeros1(dim1 = 2, dim2= 2))