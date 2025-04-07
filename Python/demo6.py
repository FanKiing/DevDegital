from tkinter import *
from tkinter import messagebox
import sqlite3
import ast
window=Tk()
window.title('SignUp')
window.geometry('926x500')
window.config(bg='#fff')
window.resizable(False,False)
img=PhotoImage(file='login.png')
Label(window,image=img,border=0,bg='white').place(x=50,y=90)
frame=Frame(window,width=350,height=390,bg='white')
frame.place(x=480,y=50)
heading=Label(frame,text='Sign up',fg='#57aAf8',bg='white',font=('tahoma',23,'bold'))
heading.place(x=100,y=5)
#####-------------------------------------
def signup():
    l=user.get()
    c=code.get()
    cc=confirm_code.get()
    if l=='Username' or c=='Password' or cc=='':
        messagebox.showerror('Error', 'Tous les champs sont obligatoires  !!!')
    elif c!=cc:
        messagebox.showwarning('warning', 'valeur password incorrect  !!!')
    else:
        conn = sqlite3.connect('mydatabase.db')
        cur = conn.cursor()
        req1 = "create table if not exists user(id integer primary key autoincrement,login Text, pwd Text)"
        cur.execute(req1)
        req2 = "insert into user(login,pwd) values (?,?)"
        cur.execute(req2, (l, c))
        messagebox.showinfo('info','inserted successfully !!!')
        user.delete(0,'end')
        code.delete(0,'end')
        conn.commit()
        conn.close()

####-----------------------------------
def on_enter(e):
    confirm_code.delete(0,'end')
def on_leave(e):
    if confirm_code.get()=='':
        confirm_code.insert(0,'confirm password')
confirm_code=Entry(frame,width=25,fg='black',border=0,bg='white',font=('cursive',11))
confirm_code.place(x=30,y=220)
confirm_code.insert(0,'confirm password')
confirm_code.bind("<FocusIn>",on_enter)
confirm_code.bind("<FocusOut>",on_leave)
Frame(frame,width=295,height=2,bg='black').place(x=25,y=247)

###------------------------------
def on_enter(e):
    code.delete(0,'end')
def on_leave(e):
    if code.get()=='':
        code.insert(0,'Password')
code=Entry(frame,width=25,fg='black',border=0,bg='white',font=('cursive',11))
code.place(x=30,y=150)
code.insert(0,'Password')
code.bind("<FocusIn>",on_enter)
code.bind("<FocusOut>",on_leave)
Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)


####--------------------------------------
def on_enter(e):
    user.delete(0,'end')
def on_leave(e):
    if user.get()=='':
        user.insert(0,'UserName')
user=Entry(frame,width=25,fg='black',border=0,bg='white',font=('cursive',11))
user.place(x=30,y=80)
user.insert(0,'Username')
user.bind("<FocusIn>",on_enter)
user.bind("<FocusOut>",on_leave)
Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)
###-----------------------------------------------
Button(frame,width=39,pady=7,text="Sign up",bg="#57a1f8",fg="white",border=0,command=signup).place(x=35,y=280)
label=Label(frame,text="I have an account",fg='black',bg='white',font=('cursive',9))
label.place(x=90,y=340)
signin=Button(frame,width=6,text="Sign in",border=0, bg='white',cursor='hand2',fg='#57a1f8')
signin.place(x=200,y=340)
window.mainloop()