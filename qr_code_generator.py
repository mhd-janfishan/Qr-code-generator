from tkinter import *
import  pyqrcode
from PIL import ImageTk,Image
root=Tk()

def qr_code():
    link_name=name_entry.get()
    link=link_entry.get()
    file_name=link_name + ".png"
    url=pyqrcode.create(link)
    url.png(file_name,scale=10)
    image=ImageTk.PhotoImage(Image.open(file_name))
    image_label=Label(image=image)
    image_label.image=image
    canvas.create_window(200,500,window=image_label)

canvas=Canvas(root,width=400,height=400)
canvas.pack()
app_label=Label(root,text="qr code generator",fg="dark blue",font=('algerian',26))
canvas.create_window(150,50,window=app_label)

name_label=Label(root,text="link name")
link_label=Label(root,text="link")

canvas.create_window(200,100,window=name_label)
canvas.create_window(200,200,window=link_label)

name_entry=Entry(root)
link_entry=Entry(root)

canvas.create_window(200,120,window=name_entry)
canvas.create_window(200,220,window=link_entry)

button=Button(text="generate qr code",command=qr_code)
canvas.create_window(200,250,window=button)


root.mainloop()

