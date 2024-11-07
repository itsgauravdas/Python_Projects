# import cx_Oracle 
import oracledb
import requests 
import bs4
import os 
import json
#Connection
connection=oracledb.connect(
    user="hr",
    password="hr",
    dsn="localhost/ORCLPDB"
)

#Create cursor
cursor=connection.cursor()

data=requests.get('https://www.google.co.in/')
links=bs4.BeautifulSoup(data.text, 'html.parser')
x=links.find_all('a',{'class':''})
k=[]
for i in x:
    t=i.get('href')
    k.append(t)
    
for j in k:
    cursor.execute("INSERT INTO python (links) values (:1)",(j,))
connection.commit()
cursor.close()
connection.close()





