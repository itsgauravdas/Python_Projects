import speech_recognition as sr   

def convert_audio_to_text():
    r=sr.Recognizer()
    
    # Open the Mic and start recording
    with sr.Microphone() as source:
        print('Recording ..Speak something into the microphone')
        audio= r.listen(source, timeout=5, phrase_time_limit=10)
        
    try:
        # Use the recognizer to convert audio to text 
        # Covert audio to text using Goog;e speech Recognition service
        
        text = r .recognize_google(audio)
        return text
    except sr.UnknownValueError:
        print('Unable to recognize the script')
    except sr.RequestError as e:
        print("Error:{0}".format(e))

# Calling that function
audio_text=convert_audio_to_text()

if audio_text:
    print('You said:', audio_text)
    # Print the converted text

# Manipulate the text for further operations

    lower_case= audio_text.lower()
    print("Lowercase_text =" , lower_case)
    
    #Split the text into words
    words = lower_case.split()
    print("Words: ", words)
