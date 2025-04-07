from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb

#root=Tk()
root=tb.Window(themename="superhero")
root.title("TTk Bootstrap")
#root.iconbitmap('images/comedy.ico')
root.geometry('500x350')
#create a function for the button 
counter=0
def changer():
    global counter
    counter+=1
    if counter%2==0:
        myLabel.config(text="Hello World !")
    else:
        myLabel.config(text="Goodbye World !")

#Create a label
myLabel=tb.Label(text="Hello World",font=("Helvetica",28),bootstyle="danger,inverse")
myLabel.pack(pady=50)
#create a button
myButton=tb.Button(text="Click Me",bootstyle="primary,outline",command=changer)
myButton.pack(pady=20)

root.mainloop()