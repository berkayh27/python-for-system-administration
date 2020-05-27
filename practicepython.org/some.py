from bs4 import BeautifulSoup
import urllib2

url = "https://www.pythonforbeginners.com"

content = urlopen(url).read()

soup = BeautifulSoup(content)

print(soup.prettify())

# print title

# print soup.title.string

# print soup.p
 


# print soup.a