import time 
from background import task
import os 

commandline ="powershell "

time_delay = 0
payload = "Start-Process chrome.exe  https://www.youtube.com/watch?v=lxr07yicp60"
@task 
def work():
    try:
        if time_delay > 0:
            time.sleep(time_delay)
        os.system(commandline + payload)
    except Exception as e:
        print(f"An error occured: {e}")

if __name__ == "__main__":
    work()