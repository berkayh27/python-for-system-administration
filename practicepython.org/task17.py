import requests
from bs4 import BeautifulSoup

url = 'http://github.com'
r = requests.get(url)
r_html = r.text
print(r_html)



# some requests code here for getting r_html 

soup = BeautifulSoup(r_html)
title = soup.find('span', 'articletitle').string