

from tkinter import *
import datetime
from tkinter.messagebox import *
from tkinter.ttk import *
import winsound
obj=Tk()
obj.geometry("400x200")
def alarm():
    if c1.get()=="AM":
       x=int(e1.get())
       y=int(e2.get())
       z=int(e3.get())
    if c1.get()=="PM":
        x=int(e1.get())+12
        y=int(e2.get())
        z=int(e3.get())
    showinfo("NOTIFICATION:","ALARM HAS BEEN SET ,OKK")
    while True: 
      if x==datetime.datetime.now().hour and y==datetime.datetime.now().minute and z==datetime.datetime.now().second:
         for i in range(0,200):
           winsound.Beep(20000,200)
         break
l1=Label(obj,text="HOURS:")
l2=Label(obj,text="MINUTES:")
l3=Label(obj,text="SECONDS:")
l1.grid(row=0,column=0)
l2.grid(row=2,column=0)
l3.grid(row=4,column=0)
e1=Entry(obj)
e2=Entry(obj)
e3=Entry(obj)
e1.grid(row=0,column=1)
e2.grid(row=2,column=1)
e3.grid(row=4,column=1)
b1=Button(obj,text="SET ALARM",command=alarm)
b1.grid(row=6,column=1)
c1=Combobox(obj,values=["AM","PM"])
c1.grid(row=0,column=2)
l4=Label(obj,text="AM or PM")
l4.grid(row=0,column=3)
obj.mainloop()

