import requests as rq
import pandas as pd 
from bs4 import BeautifulSoup 

url =input("Enter Link :: - ")

if not url.startswith("https"):
    url = rq.get("https://"+url)
    
data = rq.get(url)    
soup = BeautifulSoup(data.text, "html.parser")

links = []

for link in soup.find_all('a'):
    href =link.get("href")
    if href:
        links.append(href)
    
df=pd.DataFrame(links)
df.columns = ['Links']
file = 'Links.xlsx'
df.to_excel(file, index=False)
print("JSON data successfully written")
