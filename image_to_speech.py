import pytesseract # For Optical Character Recognition (OCR) to extract text from the image.
from PIL import image # Image handling 
from gtts import gTTS # (Google Text-to-Speech): To convert text into a speech audio file.
import os

pytesseract.pytesseract.tesseract_cmd = input(r'Enter the path for pytesseract: ')
"""
prompts the user to input the file path for the 
Tesseract OCR executable. This is necessary because 
pytesseract needs to know the 
location of the Tesseract binary to perform OCR.
"""
