from pdf2image import convert_from_path
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

root4=tk.Toplevel()
root4.geometry("800x900")
root4.title("PDF Viewer")
root4.configure(bg="#202020")
root4.minsize(300, 200)
root4.maxsize(900, 800)

pdf_frame = tk.Frame(root4)
pdf_frame.pack(fill=tk.BOTH,expand=1)

scrol_y = tk.Scrollbar(pdf_frame,orient=tk.VERTICAL)
pdf = tk.Text(pdf_frame,yscrollcommand=scrol_y.set,bg="grey")

scrol_y.pack(side=tk.RIGHT,fill=tk.Y)
scrol_y.config(command=pdf.yview)
pdf.pack(fill=tk.BOTH,expand=1)


pages = convert_from_path(filedialog.askopenfilename(initialdir = "/home",title = "Select file",filetypes = (("pdf files","*.pdf"),("all files","*.*"))),size=(800,900))

photos = []

for i in range(len(pages)):
  photos.append(ImageTk.PhotoImage(pages[i]))

for photo in photos:
  pdf.image_create(tk.END,image=photo)
  pdf.insert(tk.END,'\n\n')

root4.update()
root4.mainloop()