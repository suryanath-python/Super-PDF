import tkinter as tk
from PyPDF2 import PdfFileReader, PdfFileWriter
from PIL import Image, ImageTk
from tkinter import filedialog
from tkinter import messagebox

root_pass = tk.Toplevel()
root_pass.geometry("600x600")
root_pass.title("PDF Protect")
root_pass.configure(bg="#202020")
user_input_pdf = ''

image_pass = Image.open("password.jpg")
new_img_pass = image_pass.resize((600,400))
photo_pass = ImageTk.PhotoImage(new_img_pass)
lbl_pass = tk.Label(root_pass,image=photo_pass)
lbl_pass.place(x=0, y=0)

password = tk.Entry(root_pass, fg='red')
password.place(x=250, y=450)

lbl1_pass = tk.Label(root_pass, text="Enter the Password", bg="#202020",fg='green')
lbl1_pass.place(x=100, y=451)

def pdf_open():
    global user_input_pdf
    user_input_pdf=filedialog.askopenfilename(initialdir = "/home",title = "Select file",filetypes = (("pdf files","*.pdf"),("all files","*.*")))

def set_pass():
    global password, user_input_pdf

    pdfFile = open(user_input_pdf, 'rb')
    pdfReader = PdfFileReader(pdfFile)
    pdfWriter = PdfFileWriter()

    for pageNum in range(pdfReader.numPages):
        pdfWriter.addPage(pdfReader.getPage(pageNum))
    
    pdfWriter.encrypt(password.get())
    resultPdf = open('protected.pdf', 'wb')
    pdfWriter.write(resultPdf)
    resultPdf.close()

    messagebox.showinfo("Password","PDF saved in desktop as protected.pdf")


button_pass = tk.Button(root_pass, text="Open PDF", command=pdf_open, bg="#B8B8B8")
button_pass.place(width=300, height=50, x=150, y=500)

button_pass1 = tk.Button(root_pass, text="Set Password", command=set_pass, bg="#B8B8B8")
button_pass1.place(width=300, height=50, x=150, y=550)


root_pass.update()
root_pass.mainloop()