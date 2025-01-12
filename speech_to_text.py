import pyttsx3 
import speech_recognition as sr   

engine = pyttsx3.init()
def talk():
    engine.say("Please.... say something..")
    engine.runAndWait()

def get():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        talk()
        print("Say something....!")
        audio = r.listen(source)
        print("Done!")
    
    try:
        text = r.recognize_google(audio)
        print("You Said, " + text)
    except Exception as e:
        print(e)

get()
