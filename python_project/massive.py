squ = {1 : 1, 2:4, 3: "eror", 4 : 16,}
squ[8] = 64
squ[3] = 9
print(squ)

nums = {
    1 : "Two",
    2 : "Free",
    3 : "three",
}
print(1 in nums)
print("three" in nums)
print(4 not in nums )

pairs = {
    1 : "Apples",
    "orange" : [2, 3, 4],
    True : False,
    None : True,
}
print(1 in pairs)
print(pairs.get(None))
print(pairs.get(12345, "not in dectory"))

fib = {1: 1, 2: 1, 3: 2, 4: 3}
print(fib.get(7, 5))