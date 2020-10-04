"""
Created by,
Suryanath.A
"""

import tkinter as tk # importing neccessary libraries
from PIL import Image, ImageTk

roots = tk.Tk() # Making and Configuring Tkinter main window
roots.geometry("580x600")
roots.configure(bg="#202020")
roots.title("Super PDF")

def merger(): # importing other python files to use in the main file
    roots.update()
    import merging

def splitters():
    import splitter

def password_pdf():
    import password

def pdf_view():
    import pdf_viewer

def jpgtopdf():
    import jpgPDF

image1 = Image.open("bd.jpg") # Opening the image
photo1 = ImageTk.PhotoImage(image1) # Using ImageTk so that we can use the JPG in tkinter.

background_image=photo1 # Setting it as the background image
background_label = tk.Label(roots, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1) # Placing the image

button2 = tk.Button(roots, text= 'Merge PDFs', command=merger, bg="#B8B8B8") # Making and placing buttons
button2.place(width=300, height=50, x=300, y=500)

button_jpg = tk.Button(roots, text='Convert JPG to PDF', command=jpgtopdf, bg="#B8B8B8")
button_jpg.place(width=300, height=50, x=0, y=500)

button_main = tk.Button(roots, text= 'Split PDFs', command=splitters, bg="#B8B8B8")
button_main.place(width=300, height=50, x=0, y=550)

button_pass = tk.Button(roots, text= 'Set Passwords to PDFs', command=password_pdf, bg="#B8B8B8")
button_pass.place(width=300, height=50, x=300, y=550)

button_viewer = tk.Button(roots, text= 'View PDFs', command=pdf_view, bg="#B8B8B8")
button_viewer.place(width=300, height=50, x=150, y=450)

roots.update() # Updating the main window
roots.mainloop()# mainloop foe tkinter

"""
Don't Just copy my code. Understand what's happening
"""