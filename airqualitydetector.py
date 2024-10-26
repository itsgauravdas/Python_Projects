from tkinter import *
from PIL import ImageTk,Image
import requests
import json

root=Tk() #--Screen

root.title('Air quality index!')
root.geometry("1200x400") #--Screen size
root.configure(background='green')#--Screen color

try:
    
    api_request=requests.get('http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=10&API_KEY=1415D85E-FB89-40EF-B8F0-63F99A595BC8')
    api=json.loads(api_request.content)
    city=api[0]['ReportingArea']
    quality=api[0]['AQI']
    category=api[0]['Category']['Name']
except Exception as e:
    api="Error..."

myLabel=Label(root,text= city + "Air Quality" + str(quality) + "" + category , font=("Helvetica",20),background="green")
myLabel.pack()
root.mainloop() #--To hold the screen