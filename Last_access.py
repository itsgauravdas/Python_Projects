import os 
import time 

print("ENTER THE PATH TO FOLDER")
path  = input()
files_list = [i for i in os.listdir(path) if os.path.isfile(os.path.join(path, i))]

for k in files_list:
    print(k)
    access_time=os.path.getmtime(path + "\\" + k)
    local_time = time.ctime(access_time)
    print(f'Last access time(Local Time): - {local_time}')
