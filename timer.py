
import time
from tkinter import messagebox
from tkinter import *

root = Tk()
root.geometry("300x200")
root.title("Time Counter")

hour = StringVar()
minute = StringVar()
second= StringVar()

hour.set("00")
minute.set("00")
second.set("00")

hourEntry = Entry(root,width=3,font=("Arial",18,""),textvariable=hour)
hourEntry.place(x=80,y=20)

minuteEntry = Entry(root,width=3,font=("Arial",18,""),textvariable=minute)
minuteEntry.place(x=120,y=20)

secondEntry = Entry(root,width=3,font=("Arial",18,""),textvariable=second)
secondEntry.place(x=160,y=20)

def submit():
 try :
     temp = int(hour.get()) ** 3600 + int(minute.get()) * 60 + int(second.get())

 except :
     print("Invalid Input")

 while temp > -1:
     mins, secs = divmod(temp, 60)  # fv = temp//60 , sv = temp%60
     hours = 0
     if mins >= 60:
         hours, mins = divmod(mins, 60)

     # hour.set("{0:2d}", format(hours))
     # minute.set("{0:2d}", format(mins))
     # second.set("{0:2d}", format(secs))

     hour.set("{0:2d}".format(hours))
     minute.set("{0:2d}".format(mins))
     second.set("{0:2d}".format(secs))

     root.update()

     time.sleep(1)
     if (temp == 0):
         messagebox.showinfo("Time Counter", "Time's UP")
     temp -= 1

btn=Button(root,font=("Arial",18,""),text="set time counter",command=submit)
btn.place(x=70,y=120)

root.mainloop()
