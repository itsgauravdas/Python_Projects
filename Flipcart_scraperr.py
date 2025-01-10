import pandas as pd 
import requests
from bs4 import BeautifulSoup 

product_name = []
prices = []
Description = []
reviews  = []

for i in range(2,45):
    url = "https://www.flipkart.com/search?q=MOBILE+PHONE+UNDER+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=" + \
        str(2)
    r=requests.get(url)
    with open('Flipcart.txt', mode = 'wb') as file:
        file.write(r.text.encode('utf-8'))
        
    # soup = BeautifulSoup(r.text, "html.parser")
    # # print(soup)
    
    # box = soup.find("div", {"class" :"_1YokD2 _3Mn1Gg"})
    # if box:
    #     names = box.find_all("div", {"class" :"_4rR01T"})
    #     print(names)