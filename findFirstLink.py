import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/Da_He_ding'
url = 'https://en.wikipedia.org/wiki/Protein'
response = requests.get(url)
# print(response.text)
soup = BeautifulSoup(response.text,"html.parser")
print(soup.prettify())
print(soup.find(id='mw-content-text').find(class_="mw-parser-output").p.a.get('href'))