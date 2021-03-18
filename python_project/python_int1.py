n = [2, 4, 6, 8]
res = 1
for x in n[1:3]:
    res *=x
print(res)

ages = {
    "Dave" : 24,
    "Mary" : 42,
    "John" : 58,
}
print(ages["Dave"])
print(ages["Mary"])

a, b, *c, d = [1, 2, 3 ,4 ,5 ,6 , 7, 8, 9]
print(a)
print(b)
print(c)
print(d)

a, b, c, d, *e, f, g = range(20)
print(len(e))