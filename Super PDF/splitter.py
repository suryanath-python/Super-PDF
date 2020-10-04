"""
Created by,
Suryanath.A
"""

import tkinter as tk # importing neccessary libraries
from PIL import Image, ImageTk
from PyPDF2 import PdfFileReader, PdfFileWriter
from tkinter import filedialog
from tkinter import messagebox
  
w = 0 # Setting variables with zero value so that we can use it later.
w1 = 0
root7 = tk.Toplevel() # Making and Configuring Tkinter main window
root7.geometry("600x600")
root7.title("PDF Splitter")
root7.configure(bg="#202020")
elements = [] # Making an empty list so that we can use it later

    
image7 = Image.open("split.jpg") # Opening the image
new_img7 = image7.resize((600,400)) # resizing the image
photo7 = ImageTk.PhotoImage(new_img7) # Using ImageTk so that we can use the JPG in tkinter.


def open1():
    global w, w1
    pdf = filedialog.askopenfilename(initialdir = "/home",title = "Select file",filetypes = (("pdf files","*.pdf"),("all files","*.*")))
    elements.append(pdf)

    w = tk.Spinbox(root7, from_=0, to=100, width=3)
    w.place(x=150, y=510)
    

    w1 = tk.Spinbox(root7, from_=0, to=100, width=3)
    w1.place(x=409, y=510)
    elements.append(int(w1.get()))
    
def split():
    global w, w1
    pdfs = PdfFileReader(elements[0], "rb")
    pdf_writer = PdfFileWriter()

    elements.append(int(w.get()))
    elements.append(int(w1.get()))

    w2 = int(w.get())
    w3 = int(w1.get())

    for page in range(45):
        pdf_writer.addPage(pdfs.getPage(w2-1))
        w2+=1
        if (w2-1)==(w3):
            break

    output_fname = "splitted.pdf"

    with open(output_fname, 'wb') as out:
        pdf_writer.write(out)

    messagebox.showinfo("Splitted","PDF Saved in Desktop as splitted.pdf")
    

lbl7 = tk.Label(root7,image=photo7)
lbl7.place(x=0, y=0)

button7 = tk.Button(root7, text= 'Open PDF', command=open1, bg="#B8B8B8")
button7.place(width=300, height=50, x=150, y=450)

button8 = tk.Button(root7, text= 'Split PDF', command=split, bg="#B8B8B8")
button8.place(width=300, height=50, x=150, y=540)


root7.update()
root7.mainloop()