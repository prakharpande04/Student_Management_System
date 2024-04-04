from tkinter import *
from datetime import *
from pytz import *
from tkinter import ttk
from tkinter.ttk import Style
from tkinter import messagebox
from tkcalendar import Calendar
from tix import *

def login():
    def log():
        global lgn
        usrid=us_name_entry.get()
        pasw=pas_entry.get()
        f=0
        import mysql.connector as c
        conn=c.connect(host='localhost',user='root',passwd='pp1801',database='student_mgmt')
        csr=conn.cursor()
        csr.execute('SELECT UserName,Password FROM credentials;')
        cred=csr.fetchall()
        for i in cred:
            if i[0]==usrid:
                if i[0]==usrid and i[1]==pasw:
                    l_message_1()
                elif i[0]==usrid and i[1]!=pasw:
                    l_message_2()
            elif i[0]!=usrid:
                    l_message_3()
                    
    global w
    global lgn
    global pas_entry,us_name_entry
    lgn=Frame(w,bg='cyan',bd=10,height=600,width=750,relief=FLAT)
    lgn.place(x=800,y=370)
    
    l1_1=Label(lgn,bg='cyan')
    l1_1.pack()

    l1=Label(lgn, text="LOGIN",bg='cyan',font=('Calibri',28,'bold','italic','underline'))
    l1.pack()

    l9=Label(lgn, text=" Please enter details below to login ",bg='cyan')
    l9.pack()
    
    l10=Label(lgn, text="",bg='cyan')
    l10.pack()

    us_name = StringVar()
    pwd = StringVar()

    us_name=Label(lgn, text="Username * ",bg='cyan')
    us_name.pack()
    us_name_entry = Entry(lgn, textvariable=us_name)
    us_name_entry.pack()

    l10=Label(lgn,bg='cyan')
    l10.pack()
    
    pas=Label(lgn, text="Password * ",bg='cyan')
    pas.pack()
    pas_entry = Entry(lgn, textvariable=pwd, show= '*')
    pas_entry.pack()

    def show_pas(event):
        global pas_entry
        pas_entry.configure(show='')
    def hide_pas(event):
        global pas_entry
        pas_entry.configure(show='*')
        
    show=Button(lgn,text='👀',cursor='hand2',bg='cyan',font=10,relief=FLAT,activebackground='cyan')
    show.place(x=170,y=190)

    show.bind('<ButtonPress-1>',show_pas)
    show.bind('<ButtonRelease-1>',hide_pas)

    l11=Label(lgn,bg='cyan')
    l11.pack()

    b6=Button(lgn,text='<',bg='cyan',cursor='hand2',command=lgn.destroy)
    b6.place(x=0,y=0)      
    
    b2=Button(lgn,text="Login", height="2", width="30",bg='cyan',cursor='hand2',command=log)
    b2.pack()

def account():
    global w
    global w1
    global lgn
    b4=Button(w,text='Register',height='1',width='15',bg='darkorange',font=('Calibri bold',20),
              cursor='hand2',command=signup)
    b4.place(x=380,y=520)
    
    b5=Button(w,text='Login',height='1',width='15',bg='lime',font=('Calibri bold',20),
              cursor='hand2',command=login)
    b5.place(x=690,y=520)
account()
