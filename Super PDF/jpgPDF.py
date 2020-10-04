"""
Created by,
Suryanath.A
"""

import tkinter as tk # importing neccessary libraries
from fpdf import FPDF
from PyPDF2 import PdfFileMerger
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image, ImageTk
import img2pdf as converter

root1 = tk.Toplevel () # Making and Configuring Tkinter main window
root1.geometry("600x600")
root1.configure(bg="#202020")
root1.title("JPG to PDF")
pdfs = [] 
pdf = FPDF() # Creating a class index for FPDF
i = 0

# Using tkinter messagebox for warn the user
messagebox.showinfo("Warning","While converting JPG to PDF always remember not to use very small images and also very large image, A4 size images are recommended")

def add_files1():
    # appending the file name to the empty pdf list
    pdfs.append(filedialog.askopenfilename(initialdir = "/home",title = "Select file",filetypes = (("jpg files","*.jpg"),("all files","*.*"))))

def merges():
    output = open("converted.pdf","wb") # Making a new pdf file so that we can write the output to it
    output.write(converter.convert(pdfs)) # Writing into the pdf
    messagebox.showinfo("Saved","PDF Saved in Desktop as jpg converted.pdf")

image_jpg = Image.open("jpgtopdf.jpg") # Opening the image
new_img_jpg = image_jpg.resize((600,400)) # resizing the image
photo_jpg = ImageTk.PhotoImage(new_img_jpg) # Using ImageTk so that we can use the JPG in tkinter.

lbl_jpg = tk.Label(root1,image=photo_jpg) # Adding the image
lbl_jpg.place(x=0, y=0)

button3 = tk.Button(root1, text= 'Add Images', command=add_files1, bg="#B8B8B8") # Creating the buttons
button3.place(width=300, height=50, x=150, y=450) # Placing the button

button4 = tk.Button(root1, text= 'Merge to one PDF', command=merges, bg="#B8B8B8")
button4.place(width=300, height=50, x=150, y=500)

root1.update() # Updating the main window
root1.mainloop() # mainloop foe tkinter

"""
Don't Just copy my code. Understand what's happening
"""