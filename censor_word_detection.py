<<<<<<< HEAD
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
=======
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
>>>>>>> efef0514df301510f2d4e89bb3c27f2dacadd5e0
detect(data)