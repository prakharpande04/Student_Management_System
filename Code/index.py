from tkinter import *
from datetime import *
from pytz import *
from tkinter import ttk
from tkinter.ttk import Style
from tkinter import messagebox
from tkcalendar import Calendar
from tix import *

def r_message_1():
    global w1,register_screen
    global lgn
    messagebox.showinfo('Info',' Registered Successfully ! ',parent=w1)
    register_screen.destroy()
    login()
            
def l_message_1():
    global lgn
    messagebox.showinfo('Info',' Logged In Successfully ! ',parent=lgn)
    lgn.destroy()
    body()

def l_message_2():
    global lgn
    messagebox.showinfo('Info',' Password Incorrect ! ',parent=lgn)
    pas_entry.delete(0,END)

def l_message_3():
    global lgn
    messagebox.showinfo('Info',' Username does not exist ! ',parent=lgn)
    us_name_entry.delete(0,END)
    pas_entry.delete(0,END)
    
def body():
    global hm,ID,IN
    hm=Toplevel()
    hm.geometry('1280x800')
    hm.configure(bg='lime')
    hm.attributes('-fullscreen',True)

def signup():
    def register():
        global w1
        global UN
        
        UN=usr_entry.get()
        PW=pwd_entry.get()
        ANo=afn_entry.get()
        IN=ins_entry.get()
        IT=ins_type_entry.get()
        AD=ad_entry.get()
        ST=state_entry.get()
        PC=pin_entry.get()
        EM=mail_entry.get()
        CNo=cno_entry.get()


        
        import mysql.connector as c
        conn=c.connect(host='localhost',user='root',
                       passwd='pp1801',database='student_mgmt')
        mycur=conn.cursor()
        query1='INSERT INTO credentials VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        val=(UN,PW,ANo,IN,IT,AD,ST,PC,EM,CNo)
        mycur.execute(query1,val)
        conn.commit()
        if conn.is_connected:
            r_message_1()
            
    global w
    global w1
    global register_screen
    w1=Frame(w,bg='cyan',bd=10,height=600,width=750,relief=FLAT)
    w1.place(x=200,y=200)
    register_screen =w1
    
    usrvalue=StringVar()
    pwdvalue=StringVar()
    afnvalue=StringVar()
    insvalue=StringVar()
    ins_type=StringVar()
    adtype=StringVar()
    statetype=StringVar()
    pintype=StringVar()
    mailtype=StringVar()
    cnotype=StringVar()

    b6=Button(register_screen,text='<',bg='cyan',cursor='hand2',command=register_screen.destroy)
    b6.place(x=0,y=0)

    l1=Label(register_screen, text="Register",bg='cyan',font=('Calibri',28,'bold','italic','underline'))
    l1.pack()


    l9=Label(register_screen, text=" Please enter details below to register",bg='cyan')
    l9.pack()
    l10=Label(register_screen, text="",bg='cyan')
    l10.pack()

    usr = Label(register_screen, text="Username * ",bg='cyan')
    usr.pack()
    usr_entry = Entry(register_screen,textvariable=usrvalue)
    usr_entry.pack()

    pwd = Label(register_screen, text="Password * ",bg='cyan')
    pwd.pack()
    pwd_entry = Entry(register_screen,textvariable=pwdvalue,show='*')
    pwd_entry.pack()

    def show_pas(event):
        pwd_entry.configure(show='')
    def hide_pas(event):
        pwd_entry.configure(show='*')
        
    show=Button(register_screen,text='👀',cursor='hand2',bg='cyan',font=10,relief=FLAT,activebackground='cyan')
    show.place(x=170,y=150)

    show.bind('<ButtonPress-1>',show_pas)
    show.bind('<ButtonRelease-1>',hide_pas)

    afn = Label(register_screen, text="Affilation Number * ",bg='cyan')
    afn.pack()
    afn_entry = Entry(register_screen,textvariable=afnvalue)
    afn_entry.pack()

    ins = Label(register_screen, text="Institution Name * ",bg='cyan')
    ins.pack()
    ins_entry = Entry(register_screen,textvariable=insvalue)
    ins_entry.pack()

    ins_type = Label(register_screen, text="Institution Type * ",bg='cyan')
    ins_type.pack()
    ins_type_entry = ttk.Combobox(register_screen,font=('Calibri',10),width=15,
                                  textvariable=ins_type,state='readonly')
    ins_type_entry['values']=('Government','Government Aided','Cooperative','Private')
    ins_type_entry.pack()

    ad = Label(register_screen, text="Institution Address * ",bg='cyan')
    ad.pack()
    ad_entry = Entry(register_screen,textvariable=adtype)
    ad_entry.pack()

    state = Label(register_screen, text="State / Union Territory* ",bg='cyan')
    state.pack()
    state_entry = ttk.Combobox(register_screen,font=('Calibri',10),width=15,
                               textvariable=statetype,state='readonly')
    state_entry['values']=('Andhra Pradesh','Arunachal Pradesh','Assam','Bihar','Chhattisgarh','Goa','''
Gujarat''','Haryana','Himachal Pradesh','Jharkhand','Karnataka','Kerala','''Madhya
 Pradesh''','Maharashtra','Manipur','Meghalaya','Mizoram','Nagaland','Odisha','''Pun
jab''','Rajasthan','Sikkim','Tamil Nadu','Telangana','Tripura','Uttarakhand','''Uttar
 Pradesh''','West Bengal',' ',' ','Andaman and Nicobar Islands','Chandigarh','''Dadra and
 Nagar Haweli & Daman and Diu''','Delhi / NCR','Jammu and Kashmir','Ladakh','''Laksha
dweep''','Puducherry')
    state_entry.pack()

    pin = Label(register_screen, text="Pincode * ",bg='cyan')
    pin.pack()
    pin_entry = Entry(register_screen,textvariable=pintype)
    pin_entry.pack()

    mail = Label(register_screen, text="Email ID * ",bg='cyan')
    mail.pack()
    mail_entry = Entry(register_screen,textvariable=mailtype)
    mail_entry.pack()

    cno = Label(register_screen, text="Contact No.* ",bg='cyan')
    cno.pack()
    cno_entry = Entry(register_screen,textvariable=cnotype)
    cno_entry.pack()

    l11=Label(register_screen, text="",bg='cyan')
    l11.pack()
    b6=Button(register_screen,text="Register", height="2", width="30",bg='cyan',cursor='hand2',command=register)
    b6.pack()

global w
w=Tk()
w.title('Student Management System ')
w.attributes('-fullscreen',True)

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

# created by Prakhar Pande
