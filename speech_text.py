import pyttsx3
import speech_recognition as sr 
import time

x=pyttsx3.init()
def talk():
    x.say('Welcome sir, Please say some thing')
    x.runAndWait()
    time.sleep(0.05)
    
def get():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        talk()
        y='Say something'
        for i in y:
            print(i,end="", flush=True)
            time.sleep(0.05)
        print()
        print('Say something')
        audio = r.listen(source)
        print('Done')
        
        try:
            text = r.recognize_google(audio)
            print("You said, " + text)
        except Exception as e:
            print(e)

if __name__ == '__main__':
    get()