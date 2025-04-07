from tkinter import *
from tkinter import messagebox
import sqlite3;


#---------------------end create table and database -----------------------------------
root=Tk()
root.title('Login')
root.geometry('950x500')
root.configure(bg='#FFF')
root.resizable(False,False),
img=PhotoImage(file='login.png')
Label(root,image=img,bg='white').place(x='60',y='50')
frame=Frame(root,width=460,height=400,bg='white')
frame.place(x=430,y=40)
heading=Label(frame,text='Sign in',fg='#57a1f8',bg='white',font=('tahoma',23,'bold'))
heading.place(x=165,y=5)
#########-----------------------------------------------------------
def signin():
    username=user.get()
    password=code.get()
    """if username=='admin' and password=='1234':
        screen=Toplevel(root)
        screen.title("App")
        screen.geometry('460x400')
        screen.config(bg='white')
        Label(screen,text='Hello !!!',bg='#fff',font=('tahoma',50,'bold')).pack()
        screen.mainloop()"""
    conn = sqlite3.connect('mydatabase.db')
    cur = conn.cursor()
    req3 = "select * from user"
    select = cur.execute(req3)
    conn.commit()
    messagebox.showinfo('info',select.rowcount)
    conn.close()



def on_enter(e):
    user.delete(0,'end')
def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'Username')
#--------------------------------------------

def on_enterC(e):
    code.delete(0,'end')
def on_leaveC(e):
    pwd=code.get()
    if pwd=='':
        code.insert(0,'Password')

#--------------------------------------------
user=Entry(frame,width=25,fg='black',border=0,bg='white',font=('tahoma',11))
user.place(x=30,y=80)
user.insert(0,'Username')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)
Frame(frame,width=295,height=2,bg='black').place(x=24,y=107)
########------------------------------------------------------------
code=Entry(frame,width=25,fg='black',border=0,bg='white',font=('tahoma',11))
code.place(x=30,y=150)
code.insert(0,'Password')
code.bind('<FocusIn>',on_enterC)
code.bind('<FocusOut>',on_leaveC)
Frame(frame,width=295,height=2,bg='black').place(x=24,y=177)
#######----------------------------------------------------------------
Button(frame,width=40,pady=7,text='Sign in',bg='#57a1f8',fg='white',border=0,command=signin).place(x=30,y=204)
########---------------------------------
label=Label(frame,text="Don't have an account?",fg='black',bg='white',font=('tahoma',9))
label.place(x=75,y=270)
sign_up=Button(frame,width=6,text='Sign up',border=0,bg='white',cursor='hand2',fg='#57a1f8')
sign_up.place(x=215,y=270)
root.mainloop()
