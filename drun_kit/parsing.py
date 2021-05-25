import urllib.request
import re

with urllib.request.urlopen('https://musical-artifacts.com/hydrogen_drumkits.xml') as response:
    html = response.read().decode('utf-8') # convert to string
    search_pharse = "\*.h2drumkit"
    print(re.findall(search_pharse,html))
