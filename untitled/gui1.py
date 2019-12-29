from tkinter import *
a_root =Tk()
#width*height
a_root.geometry("900x900")
#width.height
a_root.minsize(300,300)
a_root.maxsize(1200,1200)
name=Label(text="First GUI application")
name.pack()

a_root.mainloop()
