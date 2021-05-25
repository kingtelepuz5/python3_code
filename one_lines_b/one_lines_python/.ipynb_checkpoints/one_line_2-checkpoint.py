import numpy as np
a = np.array([1, 2, 3]) # 1d list
print(a)
b = np.array([[1,2],[3,4]]) # 2d list
print(b)
c = np.array([[[1,2],[3,4]]]) # 3d list
print(c)
a = np.array([[1, 0, 0], [1, 1,1], [2, 0, 0]])
b = np.array([[1,1,1], [1, 1, 2], [1, 1, 2]])
print(a+b)
print(a*b)
print(a/b)
print(np.max(a))
print(np.min(a))
print(np.average(a)) # среднее

alice = [99, 101, 103]
bob = [110, 108, 105]
tim = [90, 88, 85]
salaries = np.array([alice, bob, tim])
taxation = np.array([[0.2, 0.25,0.22], [0.4,0.5,0.5],[0.1,0.2,0.1]])
max_income = np.max(salaries - salaries * taxation)
print(max_income)
a = np.array([55, 56, 57, 58, 59, 60, 61])
print(a)
print(a[:])
print(a[2:])
print(a[1:4])
print(a[::2])
print(a[1::2])
print(a[:1:-2])
print(a[-1:1:-2])
a = np.array([[0, 1, 2, 3],
[4, 5, 6, 7],
[8, 9, 10, 11],
[12, 13, 14, 15]])
print(a)
print("it's [:,2]",a[:,2]) # столбцы
print(a[1,:]) # столбец

print(a[:-2,:])
a = np.array([1, 2, 3, 4])
print("who",a.ndim)
b = np.array([[2, 1, 2], [3, 2, 3], [4, 3, 4]]) # уровень глубины
print(b.ndim)
c = np.array([[[1, 2, 3], [2, 3, 4], [3, 4, 5]],
[[1, 2, 4], [2, 3, 5], [3, 4, 6]]])
print(a.shape)
print(b.shape)
print(c.shape)
a = np.array([1, 2, 3, 4], dtype=np.int16)
print(a.dtype)
b = np.array([1, 2, 3 ,4], dtype=np.float64)
print(b.dtype)
dataScientist = [130, 132, 137]
productManager = [127, 140, 145]
design = [118, 118, 127]
softwareEnginer = [129, 131, 137]

employees = np.array([dataScientist, productManager, design, softwareEnginer])
employees[0,::2]=employees[0,::2] * 1.1 # вторая строка каждый второй
print(employees)
X = np.array([[1, 0, 0], [0, 2, 2], [3, 0, 0]])
print(np.nonzero(X))
print(X==2)
X = np.array(
[[ 42, 40, 41, 43, 44, 43 ], # Hong Kong
[ 30, 31, 29, 29, 29, 30 ], # New York
[ 8, 13, 31, 11, 11, 9 ], # Berlin
[ 11, 11, 12, 13, 11, 12 ]]) # Montreal
cities = np.array(["Hong Kong", "New York", "Berlin", "Montreal"])

a = np.array([[1,2,3], [4,5,6], [7,8,9]])
indices = np.array([[False, False, True], [False, False, False], [True, True, False]])
print(a[indices])
inst = np.array([[232, "@instagram"],
[133, "@selenagomez"],
[59, "@victoriassecret"],
[120, "@cristiano"],
[111, "@beyonce"],
[76, "@nike"]])
superstars = inst[inst[:,0].astype(float) > 100, 1]
print(superstars)
a = np.array([4] * 16)
print(a)
a[1::] = [42] * 15
print(a)
a[1:8:2] = 16
print(a)
a = np.array([1, 2, 3, 4, 5, 6])
print(a.reshape(2, 3)) # создаем матрицу
a = np.array([1 , 2, 3, 4, 5, 6])
print(a.reshape(2, -1))
print(np.sort(a))
print(np.argsort(a))
#sequence = np.random.normal(10.0, 1.0, 500)
#print(sequence)
#import matplotlib.pyplot as plt
#plt.xkcd()
#plt.hist(sequence)
#plt.annotate(r"$\omega_1=9$", (9, 70))
#plt.annotate(r"$\omega_2=11$", (11, 70))
#plt.annotate(r"$\mu=10$", (10, 90))
#plt.savefig("plot.jpg")
#plt.show()

## Data: row is customer shopping basket
## row = [course 1, course 2, ebook 1, ebook 2]
## value 1 indicates that an item was bought.
basket = np.array([[0, 1, 1, 0],
[0, 0, 0, 1],
[1, 1, 0, 0],
[0, 1, 1, 1],
[1, 1, 1, 0],
[0, 1, 1, 0],
[1, 1, 0, 1],
[1, 1, 1, 1]])
## One-liner
copurchases = np.sum(np.all(basket[:,2:], axis = 1)) / basket.shape[0]
## Result
print(copurchases)
print(np.all(basket[:,2:], axis=1))
#чиним
copurchases = [(i, j, np.sum(basket[:,i] + basket[:,j] ==2)) for i in range(4) for j in range(i+1,4)]
print(copurchases)
print(max(copurchases, key = lambda x:x[2]))
