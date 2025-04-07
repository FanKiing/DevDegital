from tkinter import *
fen=Tk()
fen.title('My First window with label and background')
fen.geometry('900x700')
fen.resizable(False,False)
#fen.iconbitmap('icon.ico')
l=Label(fen,text="First Label",font="48",fg="black")
#l.pack(side="")
l.place(x=0,y=0)
l.pack(padx=50,pady=60)
#autrement
#l=Label(fen,text="MyFirst Title",font="40",bg="black",fg="white").place(x=100,y=80)
#l=Label(fen,text="MySecond Title",font="40",bg="black",fg="white").place(x=100,y=180)

fen.mainloop()