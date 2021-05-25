import urllib.request
search_pharse = 'crypto'
with urllib.request.urlopen('https://www.wired.com/') as response:
    html = response.read().decode('utf-8') # convert to string
    first_pos = html.find(search_pharse)
    print(html[first_pos-10:first_pos+10])
