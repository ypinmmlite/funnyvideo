import requests 
import requests_html
from bs4 import BeautifulSoup
from requests_html import HTMLSession


url= "https://t5c2.bdhub.link"

session=HTMLSession()
response=session.get(url)
response.html.render()

print(response.html)
print(response.html.html)

#soup=BeautifulSoup(response.content, 'html.parser')

#print(soup.find_all('article',class_='book'))