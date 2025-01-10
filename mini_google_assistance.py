# pip install SpeechRecognition
import speech_recognition as sr  
import pyttsx3  #text_speech converter
import pywhatkit
import datetime
import pyjokes
"""
pip install opencv-python
"""
import cv2

listner = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
# engine.say("Hello Bro ")
# engine.runAndWait()

def talk(text):
    engine.say(text)
    engine.runAndWait()
    
def take_command():
    command=""
    try:
        with sr.Microphone() as  source:
            print("Listening...(Speak Now)")
            voice = listner.listen(source)
            command = listner.recognize_google(voice)
            command= command.lower()
            if "google" in command:
                command = command.replace("google", '')
                print(f"Command received: {command}")
                
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that.")
    except sr.RequestError:
        print("Request error. Check your internet connection.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return command

def run_mini_google_assistance():
    command = take_command()
    print(command)
    if "play" in command:
        song = command.replace("play","").strip()
        talk("play the song"+ song)
        print(song)
        pywhatkit.playonyt(song)
    elif "time" in command:
        time = datetime.datetime.now().strftime("%I:%M%p")
        print(time)
        talk("Current time is" + time)
    elif "joke" in command:
        talk("Here is the joke")
        talk(pyjokes.get_joke())
        talk("Heeehee quite ")
    elif "date" in command:
        date = datetime.date.today()
        print(date)
        talk("Today is")
        talk(date)
    elif "How are you" in command:
        talk('I am good. Nice to see you here!')
    elif "capture" in command or "camera" in command:
        talk("Ok I'll do it for you!")
        talk("Remenber, You can use s button to quit")
        vid = cv2.VideoCapture(0)
        
        while True:
            ret, frame = vid.read()
            cv2.imshow('frame', frame)
            if cv2.waitKey(0) & 0xFF == ord('s'):
                break
            vid.release()
            cv2.destroyAllWindows()
    elif "exit" in command or "quit" in command:
        talk("Goodbye! Have a great day!")
        exit()  # Exit the program
    else:
        talk("Sorry, I didn't understand. Could you repeat that?")  

 
talk("Hello my friend, i am your personal mini google assistant.")
talk("And i can help you to play song, tell time, tell date, tell joke and i can also capture photo and video for you")
talk("Now please tell me how can i help you!")       
while True:
    run_mini_google_assistance()
    # talk("Nice to see you here, I belive that you enjoyed!")





