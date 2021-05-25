is_anagram = lambda  x1, x2:sorted(x1) == sorted(x2) # анограма сравнивает на соотвествее колличевственного и качевственного смысла переменной
print("is anagram(elvis, lives)=\n",is_anagram("elvis", "lives"))
print("is anagram(elvise, livees)=\n",is_anagram("elvise", "livees"))
print("is anagram(elvis, dead)=\n",is_anagram("elvis", "dead"))
print("it's sorted(elvis)=\n",sorted("elvis"))
print("it's sorted=\n(lives)",sorted("lives"))
#=====================================
is_palindrome = lambda phrase: phrase == phrase[::-1] # проверка перевертыша
print("is palindrome(anna)=\n",is_palindrome("anna"))
print("is palindrome(kdljfasjf)=\n",is_palindrome("kdljfasjf"))
print("is palindrome(rats live on no evil star)=\n",is_palindrome("rats live on no evil star"))
#======================
n = 5

factorial = lambda n: n * factorial(n-1) if n > 1 else 1
print("factorial(n=5)=\n",factorial(n))

#===============================
a = "cat"
b = "chello"
c = "chess"
ls = lambda a, b: len(b) if not a else len(a) if not b else min(ls(a[1:],b[1:])+(a[0] != b[0]),ls(a[1:],b)+1,ls(a, b[1:])+1)
print("it's ls(a,b)",ls(a,b))
print("it's ls(a,c)",ls(a,c))
print("it's ls(b,c)",ls(b,c))
#=======================
from functools import reduce
print("============================================================")
s = {1, 2, 3, 4, 5} #комбинаторика с дополнением
ps = lambda s: reduce(lambda P, x: P + [subset | {x} for subset in P], s, [set()])
print("Subset ps= \n",ps(s))
#====================
#abc ="acdefghijklmnopqrstuvwxyz"
#s ="xthexrussiansxarexcoming"
#не работает
#rt13 = lambda x: "".join([abc[(abc.find(c) + 13)%26] for c in x])
#print(rt13(s))
#print(rt13(rt13(s)))
#================================prime==========

def prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
        return True

print("prime 10",prime(10))
print("prime 11",prime(11))
print("prime 11",prime(12))
print("prime 11",prime(13))
#find all prime numbers <= m
m = 20
primes = [n for n in range(2, m+1) if prime(n)]

print("primes=\n",primes)

#========================

n = 100
primes = reduce(lambda r, x: r - set(range(x**2, n, x)) if x in r else r, range(2, int(n**0.5)+1),set(range(2, n)))
print("primes to 100=\n",primes)

#==== FIBONACHI===============
n = 12
fibs = reduce(lambda x, _: x + [x[-2] + x[-1]], [0] * (n-2),[0,1])
print("fibs=\n",fibs)

# ============= binary search
#don't work
#l = [3, 6, 14, 16, 33, 55, 56, 89]
#x = 33
#bs = lambda l, x, lo, hi: -1 if lo>hi else \
#(lo+hi)//2 if l[(lo+hi)//2] == x else \
#bs(l, x, lo, (lo+hi)//2-1) if l[(lo+hi)//2] > x else \
#bs(l, x, (lo+hi)//2+1, hi)
#print(bs(l, x, 0, len(1)-1))
#======== quic sort ============
unsorted = [33, 2, 3, 45, 6, 54, 33]
q = lambda l: q([x for x in l[1:] if x <= l[0]])\
 + [l[0]] + q([x for x in l if x > l[0]])\
 if l else []
print("sorted=\n",q(unsorted))
