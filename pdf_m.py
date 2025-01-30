import tkinter
from tkinter import Tk     #
from tkinter.filedialog import askopenfilename
import PyPDF2 
import os 

def merge_pdfs(output_filename, input_file):
    pdf_merge = PyPDF2.PdfMerger()
    
    for file in input_file:
        try:
            os.chdir(os.getcwd())
            if os.path.exists(file):
                # file = os.path.join(file,)
                with open(file, 'rb') as pdf_file:
                    pdf_merge.append(pdf_file)
                
        except FileNotFoundError:
            print(f'Warning: file {file} not found. skipping')
    
    with open(output_filename, 'wb') as output_file:
        pdf_merge.write(output_file)
    print(f'PDFs merged successfully! Output file: {output_filename}')
    
def main():
    print('PDF Merge tool')
    print("Please enter the names of the two PDF files to merge:")
    
    pdf1 = filename = askopenfilename()
    pdf2 = filename = askopenfilename()
    
    # root = Tk()
    # root.geometry("500x500")

    # b=tkinter.Button(root, text="Please select the file", command=choose)
    # b.pack()

    # root.mainloop()

    output_filename = input("Enter the name for the merged PDF: ")
    
    input_file = [pdf1, pdf2]
    
    merge_pdfs(output_filename, input_file)
    
if __name__ == '__main__':
    main()


# def choose():
# # Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
#     filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
#     print(filename)
#     exit()

# root = Tk()
# root.geometry("500x500")

# b=tkinter.Button(root, text="Please select the file", command=choose)
# b.pack()

# root.mainloop()