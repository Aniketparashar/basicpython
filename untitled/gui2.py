from tkinter import *
from PIL import Image, ImageTk
###tkinter only support png module so for the jpg and jpeg we have to used pillow module
a_root =Tk()
image=Image.open("index.jpeg")
photo=ImageTk.PhotoImage(image)

img=Label(image=photo)
img.pack()



a_root.mainloop()