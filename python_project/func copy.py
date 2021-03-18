#nums = [1, 2, 3, 4]
#nums.append(4)
#print(nums)

#words = ["Python", "fun"]
#index = 1
#words.insert(index, "is")
#print(words)

#letters = ['a', 'd', 'r', 'a', 'x', 'e', 't', 'a', 'y','u', 'i', 'l']
#print(letters.index('r'))
#print(letters.index('a'))
#print(letters.index('x'))
#print(max(letters))
#print(min(letters))
#print(list.count(a))
#print(list.reverse(a))
#print(list.remove(a[2]))

#msg = "Numbers {0} {1} {2} ".format(nums[1],nums[3],nums[3])
#print(msg)

#x_y = "{x} {y} ".format(x = 5, y = 10)
#print(x_y)

#print(", ".join(['spam', 'robert', 'loh']))

#print("hello me".replace("me", "WORLD"))

#print("Start chocho kiko".startswith('Start'))
#print("starn advase rob".endswith('rob')) 
#print("this is low to UP!".upper())
#print("ALL STRING NOW DOWN".lower())
#print("spam, egg, ochko, lesha".split(' , '))


#def h_w():
#    print('Hello World')

#h_w()

#def print_egg(word):
#    print(word + " " + "egg!")

#print_egg('Ar')
#print_egg('OPA')

#def print_double(x):
#   print(2 * x)

#print_double(3)

#def print_sum(a , b):
#    print(a + b)
    


#print_sum(5,10)
#def max(x, y):
#    if x >= y:
  #      return x
 #   else:
 #       return y

#print(max(4, 7))
##z = max(8, 144)
#print(z)


#def add_numbers(x, y):
 #   total = x + y
 ##   return total
 #   print("This won't be printed")

#print(add_numbers(5, 10))


#def sum(x):
 #   res = 0
 #   for i in range(x):
 #       res += i
 #   return res

#print(sum(4))


#def print_nums(x):
#  for i in range(x):
#    print(i)
#    return
#print_nums(10)


text = input()
word = input()

def search(text, word):
    if text.count(word):
        return "Word found"
    else:
        return "Word not found"
print(search(text, word))

def concatenate(*args):
    return '-'.join(args)
    

print(concatenate("I", "love", "Python", "!"))