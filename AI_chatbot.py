import requests
import pyfiglet 
import itertools
import threading 
import time
import sys 

url = "https://simple-chatgpt-api.p.rapidapi.com/ask"

headers = {
    "Content-type": "application/json",
    "X-RapidAPI-Key" : "OUR API KEY",
    "X-RapidAPI-Host": "simple-chatgpt-api.p.rapidapi.com"
    
}

def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\r' + c) #\r updated the same line itaratively
        sys.stdout.flush()
        time.sleep(0.1)
        
def ask(question):
    payload={'question' : question}
    response = requests.post(url,headers=headers,json=payload)
    return response.json().get("answer")

if __name__ == "__main__":
    print(pyfiglet.figlet_format("AI Chat BOT"))
    print("Enter the question to ask")
    print("Enter q to quit")
    print()
    while True:
        question=str(input(">>"))
        if question == 'q':
            print(">> Bye! Thanks for using..")
            break
        done=False
        # Create and start the thread
        t=threading.Thread(target=animate)
        t.start()
        answer = ask(question)
        time.sleep(5)
        done=True
        # Wait for the animation thread to finish before continuing
        t.join()
        print(">> ",answer)
        print()
        
        
        