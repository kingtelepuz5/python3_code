import re

text = '''A blockchain, originally block chain,
is a growing list of records, called blocks,
which are linked using cryptography.
'''
print(re.findall('b...k', text))
print(re.findall('y.*y', text))
print(re.findall('blocks?', text))
txt = '<div>Hello World<div>'
print(re.findall('<.*>', txt))
print(re.findall('<.*?>', txt))
d
text = 'peter piper picked a peck of pickled peppers'

result = re.findall('p.*?e.*?r', text)
print(result)
result = re.findall('p.*e.*r', text)
print(result)

#---------------------web_pars-------------

#запустить с интернетом
import urllib.request
search_pharse = 'crypto'
with urllib.request.urlopen('https://www.wired.com/') as response:
    html = response.read().decode('utf-8') # convert to string
    first_pos = html.find(search_pharse)
    print(html[first_pos-10:first_pos+10])


#-------------------------------------------
text_1 = "crypto-bot that is trading Bitcoin and other currencies"
text_2 = "cryptographic encryption methods that can be cracked easily with quantum computers"

pattern = re.compile("crypto(.{1,30})coin")
print(pattern.match(text_1))
print(pattern.match(text_2))

#=======================================
text = '''
"One can never have enough socks", said Dumbledore.
"Another Christmas has come and gone and I didn't
get a single pair. People will insist on giving me books."
Christmas Quote
'''
regex = 'Christ.*'
print("Re mathc :\n",re.match(regex, text))
print("Re search :\n",re.search(regex, text))
print("Re findal :\n",re.findall(regex, text))
#===============================
page = '''
 <!DOCTYPE html>
<html>
<body>
<h1>My Programming Links</h1>
<a href="https://app.finxter.com/">test your Python skills</a>
<a href="https://blog.finxter.com/recursion/">Learn recursion</a>
<a href="https://nostarch.com/">Great books from NoStarchPress</a>
<a href="http://finxter.com/">Solve more Python puzzles</a>
</body>
</html>
'''
practice_test = re.findall("(<a.*?finxter.*?(test|puzzle).*?>)", page)
print("Preactice test: \n",practice_test)
#================================
string = 'helloworld'

regex_1 = 'hello(world)'
regex_2 = '(hello(world))'

res_1 = re.findall(regex_1, string)
res_2 = re.findall(regex_2, string)

print("Res_1:\n",res_1)
print("Res_2:\n",res_2)
#=======================
report = '''
If you invested $1 in the year 1801, you would have $18087791.41 today.
This is a 7.967% return on investment.
But if you invested only $0.25 in 1801, you would end up with $4521947.8525.
'''

dollars = [x[0] for x in re.findall('(\$[0-9]+(\.[0-9]*)?)', report)]
print(dollars)

#===================================================
article = '''The algorithm has important practical applications
http://blog.finxter.com/applications/
in many basic data structures such as sets, trees,
dictionaries, bags, bag trees, bag dictionaries,
hash sets, https://blog.finxter.com/sets-in-python/
hash tables, maps, and arrays. http://blog.finxter.com/
http://not-a-valid-url
http:/bla.ba.com
http://bo.bo.bo.bo.bo.bo/
http://bo.bo.bo.bo.bo.bo/333483--33343-/
'''

stale_links = re.findall('http://[a-z0-9_\-.]+\.[a-z0-9_\-/]+',article)
print("result state links:\n",stale_links)

#================================
print(re.findall('x{3,5}y', 'xy'))
print(re.findall('x{3,5}y', 'xxxxxy')) #очень чувствительный к регистру
print("this is are, \n sheet who don't did work ",re.findall('x{3,5}y', 'xxxxxxy'))
#==================================

inputs = ['18:29','23:55','123','ab:de','18:299','99:999' ]
inputs_ok = lambda x:re.fullmatch('[0-9]{2}:[0-9]{2}', x) != None #регулярка чисел диапазона, два знака
for x in inputs:
    print(inputs_ok(x))

#-==================-============FALIDE TIME=================
inputs = ['18:29', '23:55', '123', '18:299', '99:99']
inputs_ok = lambda x: re.fullmatch('[01][0-9]|2[0-3]:[0-5][0-9]', x) != None
for x in inputs:
    print(inputs,inputs_ok(x))
#============================================
pattern = '(?P<quote>[\''']).*(?P=quote)'
text = 'She said "hi"'
print("ITS REZULT : ==\n",re.search(pattern, text))

text ='''
It was a bright cold day in April, and the clocks were
striking thirteen. Winston Smith, his chin nuzzled into
his breast in an effort to escape the vile wind, slipped
quickly through the glass doors of Victory Mansions,
though not quickly enough to prevent a swirl of gritty
dust from entering along with him.
-- George Orwell, 1984
'''
duplicates = re.findall('([^\s]*(?P<x>[^\s])(?P=x)[^\s]*)', text)
print("dublicates \n",duplicates)
#================================================

text = 'if you use words too often words become used'

style_problems = re.search('\s(?P<x>[a-z]+)\s+([a-z]+\s+){0,10}(?P=x)\s','' + text + '')
print("STYLE PROBLEM: == \n",style_problems)
#==========================
text = '''
Alice Wonderland married John Doe.
The new name of former 'Alice Wonderland' is Alice Doe.
Alice Wonderland replaces her old name 'Wonderland' with her new name 'Doe'.
Alice's sister Jane Wonderland still keeps her old name.
'''
update_text = re.sub("Alice Wonderland(?!')", 'Alice Doe', text)
print(update_text)
