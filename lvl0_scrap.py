import requests
from bs4 import BeautifulSoup

def scrape():
    url ='https://www.example.com'
    response=requests.get(url)
    soup=BeautifulSoup(response.text,'html.parser')
    title=soup.select_one('h1').text
    texte=soup.select_one('p').text
    link=soup.select_one('a').get('href')
    print(title)
    print(texte)
    print(link)


scrape()
