import os 
import requests 
from tqdm import tqdm 
import math 
import time 

url = input("Enter teh url of the file you want to download :: - ")
r=requests.get(url)

file_size = int(r.headers['Content-Length'])
file_size_mb = file_size // (1024 * 1024)
chunk_size = 1024*1024

"""Chunk size is the
number of bytes downloaded at a time
"""
print(f'{file_size_mb:.2f} MB')

r= requests.get(url, stream=True)

"""streams=True ensures that
will not get data at once, but will get data one by one

"""
extension = (os.path.splitext(url))[-1]
print(extension)
file = "file"+extension
print(file) 

iterations = math.ceil(file_size/chunk_size)

with open(file, "wb") as file:
    with tqdm(total=file_size, unit="B", unit_scale=True, desc="Downloading",colour="green") as pbar:
        for chunk in tqdm(r.iter_content(chunk_size=chunk_size)):
            if chunk:
                file.write(chunk)
                pbar.update(len(chunk))
    print(f'File has been downloaded successfully in {os.getcwd()}')
