import time 

def print_floating_text(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.05)
    print()
    
print_floating_text(
    "I have added this python script which creates floating text effects.")
time.sleep(1)