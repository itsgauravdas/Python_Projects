from pdf2docx import Converter
import os
import sys 
import time
from tkinter.filedialog import askopenfilename

pdf=askopenfilename()
if pdf:
    print(pdf)
    time.sleep(5)
else:
    print('Please select the file')
    sys.exit()

#Ask for custom name for the word doc 
doc_name_choice = input('Do you want to give a custom name to your file ?(Y?N)::-')

if doc_name_choice.upper() == 'Y':
    doc_name = input('Enter the document name:- ') + ".docx"
else:
    pdf_name = os.path.basename(pdf)
    print(pdf_name)
    doc_name = os.path.splitext(pdf_name)[0] + ".docx"
    print(doc_name)

cv = Converter(pdf)

path=os.path.dirname(pdf)

cv.convert(os.path.join(path, "", doc_name), start=0, end=None)
print("Word doc created")
cv.close()


 
