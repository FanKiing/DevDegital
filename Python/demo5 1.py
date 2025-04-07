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


user=Entry(frame,width=25,fg='black',border=0,bg='white',font=('tahoma',11))
user.place(x=30,y=80)
user.insert(0,'Username')


########------------------------------------------------------------
code=Entry(frame,width=25,fg='black',border=0,bg='white',font=('tahoma',11))
code.place(x=30,y=150)
code.insert(0,'Password')

#######----------------------------------------------------------------
Button(frame,width=40,pady=7,text='Sign in',bg='#57a1f8',fg='white',border=0).place(x=30,y=204)
########---------------------------------
label=Label(frame,text="Don't have an account?",fg='black',bg='white',font=('tahoma',9))
label.place(x=75,y=270)
sign_up=Button(frame,width=6,text='Sign up',border=0,bg='white',cursor='hand2',fg='#57a1f8')
sign_up.place(x=215,y=270)
root.mainloop()
