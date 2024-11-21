import requests 
from bs4 import BeautifulSoup
import time

def get_latest_crypto_price(coin):
    url=r"https://www.google.com/search?q="+(coin)+r"price"
    
    html=requests.get(url)
    soup=BeautifulSoup(html.text , 'html.parser')
    text1=soup.find('div', {'class':'BNeawe iBp4i AP7Wnd'}).find('div',{'class':'BNeawe iBp4i AP7Wnd'}).text
    return text1

price = get_latest_crypto_price('bitcoin')
print('BITCOIN Price: ' + price)