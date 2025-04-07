from tkinter import *
fen=Tk()
cS=IntVar(master=fen,value=0)

a=IntVar(master=fen,value=0)
b=IntVar(master=fen,value=0)
res=IntVar(master=fen,value=0)
def action():
    if cS.get()==1:
        res.set(a.get()+b.get())
    elif cS.get()==2:
        res.set(a.get() * b.get())
    elif cS.get()==3:
        res.set(a.get() - b.get())




mystyle="{arial} 18 bold"
fen.geometry("700x600")
l=Label(fen,font=mystyle,width="700",height="600",bg="#370028").place(x=0,y=0)
l1=Label(fen,padx="40",pady="80",font=mystyle,text="Give the value of A",fg="white",bg="#370028").grid(row=0,column=0)
t1=Entry(fen,font=mystyle,textvariable=a).grid(row=0,column=1)
l2=Label(fen,padx="40",pady="80",font=mystyle,text="Give the value of B",fg="white",bg="#370028").grid(row=1,column=0)
t2=Entry(fen,font=mystyle,textvariable=b).grid(row=1,column=1)
rb1=Radiobutton(fen,font=mystyle,text="Somme",fg="white",bg="#370028",variable=cS,value=1).grid(row=2,column=0)
rb2=Radiobutton(fen,font=mystyle,text="Produit",fg="white",bg="#370028",variable=cS,value=2).grid(row=3,column=0)
rb3=Radiobutton(fen,font=mystyle,text="Soustraction",fg="white",bg="#370028",variable=cS,value=3).grid(row=4,column=0)
b1=Button(fen,text="Calculer",font=mystyle,fg="white",bg="#370028",command=action).grid(row=5,column=0)
l4=Label(fen,padx="40",pady="80",font=mystyle,text="Resultat",fg="white",bg="#370028").grid(row=6,column=0)
t4=Entry(fen,font=mystyle,textvariable=res).grid(row=6,column=1)
fen.mainloop()