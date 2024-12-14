import pyttsx3 #--text to speech 
import datetime
import speech_recognition as sr  #--audio to text
import pyaudio 
import wikipedia 
import webbrowser 
import smtplib
"""
defines an SMTP client session 
object that can be used to send mail to any 
internet machine with an SMTP or ESMTP listener daemon
"""
import pywhatkit as kit 
"""

pywhatkit is a Python library that simplifies WhatsApp automation
"""
import pyjokes 
import time 
import sys 

print("Your assistant is starting............")
engine = pyttsx3.init('sapi5')
"""
The argument 'sapi5' explicitly
specifies the speech synthesis driver to use, 
in this case, SAPI5, which is built into Windows operating systems.
"""
voices=engine.getProperty('voice') # Get available voices
engine.setProperty('voice',voices[1][0]) # Select a voice
engine.setProperty('rate', 190) # Speed

# when you start using the assistant enter your name here
Master = input("Enter your name :: - ")

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish_user():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour < 12 :
        speak(f"Good Mornig {Master}")
    elif hour >=10 and hour < 16:
        speak(f"Good Afternoon {Master}")
    else:
        speak(f'Good Evening {Master}')

def user_command():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("I am listning....")
        r.pause_threshold = 1
        audio = r.listen(source)
        
        try:
            print("Recognising.....")
            query = r.recognize_google(audio, language = 'en-in')
            print(f"User said : {query}")
        except Exception as e:
            print("I am sorry i don't understand, say that again please....")
            return "None"
        return query

# def mailSent(to, content):
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.ehlo()
#     server.starttls()
#     # when you start working with the assistant, save this on your device
#     server.login('your email', 'your app password')
#     # check READme.md for creating an app password
#     server.sendmail('Your email', to, content)

#     server.close()
    
if __name__ == '__main__':
     wish_user()
     while True:
        query = user_command().lower()
         
        if 'wikipedia' in query:
             speak('Give me somethime i am looking into wikipedia...')
             query = query.replace("wikipedia","")
             results = wikipedia.summary(query, sentences = 5)
             speak("This is what i found")
             speak(results)
             
        elif 'open Youtube' in query:
             webbrowser.open("youtube.com")
        elif 'search google' in query:
             webbrowser.open('google.com')
        elif 'play music' in query:
            webbrowser.open("spotify.com")
            # you can use API as well, with the help of spotipy module
        elif 'time' in query:
            time=datetime.datetime.now().strftime("%H:%M")
            speak(f"Its {time} now")
        elif 'date today' in query:
            date=datetime.datetime.today()
            speak(f"Today is {date}")
        elif 'send whatsapp message' in query: # you should be logged in into whatsapp web for this
            speak('to whom i need to send this')
            number = int(input())
            speak('Please tell me the message')
            message = user_command()
            speak("At what time should I send?")
            speak("At what time? (24 hours system)")
            hr=int(input("Hours: "))
            mins=int(input("Minutes : "))
            try:
                kit.sendwhatmsg(number, message, hr, mins)
                print("Message scheduled successfully!")
            except Exception as e:
                 print(f"An error occurred: {e}")
            # this should be in the format ("+91xxxxxxxxxx","This is message", 15, 20)
            
        elif 'open facebook' in query:
            webbrowser.open('facebook.com')
        elif 'make me laugh' in query:
            joke = pyjokes.get_joke()
            speak(joke)
        elif 'no thanks' in query:
            speak('thanks for using me ! Have a good day')
            exit()
        
        time.sleep(5)
        speak('Do you have any other work?')
            
        