import requests
import os 

url = "http://checkip.dyndns.org"
req=requests.get(url)
result = req.text.split(':')[1]
your_ip = result.split('<body></html>',1)[0]
print(your_ip.replace('</body></html>',' '))