from tkinter import *
from datetime import *
from pytz import *
from tkinter import ttk
from tkinter.ttk import Style
from tkinter import messagebox
from tkcalendar import Calendar
from tix import *

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
