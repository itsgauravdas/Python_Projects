from better_profanity import profanity 
from better_profanity import profanity
"""
pip install better-profanity
"""

def detect(data):
    try :
        output = profanity.censor(data, '#')
        print(output)
    except Exception as e :
        print(e)
        

data=input("Enter msg: ")
detect(data)