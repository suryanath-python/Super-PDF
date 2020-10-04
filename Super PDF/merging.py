import tkinter as tk
import PyPDF2
from PIL import Image, ImageTk
from tkinter import filedialog
from PyPDF2 import PdfFileMerger
from tkinter import messagebox

pdfs=[]
files = [("PDF Files", "*.pdf")]

root = tk.Toplevel()
root.geometry("600x600")
root.configure(bg="#202020")
root.title("PDF merger")

def add_files():
    pdfs.append(filedialog.askopenfilename(initialdir = "/home",title = "Select file",filetypes = (("pdf files","*.pdf"),("all files","*.*"))))
    
def merge():
    merger = PdfFileMerger()
    for pdf in pdfs:
        merger.append(pdf)
    merger.write("merged.pdf")
    merger.close()
    messagebox.showinfo("Merged","PDF Saved in Desktop as merged.pdf")  
    

image = Image.open("merge.jpg")
photo = ImageTk.PhotoImage(image)


button = tk.Button(root, text= 'Add PDF', command=add_files, bg="#B8B8B8")
button.place(width=300, height=50, x=150, y=450)

button1 = tk.Button(root, text= 'Merge to one PDF', command=merge, bg="#B8B8B8")
button1.place(width=300, height=50, x=150, y=500)

lbl = tk.Label(root,image=photo)
lbl.place(x=0, y=0)

root.update()
root.mainloop()