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
    
    import mysql.connector as m
    con=m.connect(host='localhost',user='root',passwd='pp1801',database='student_mgmt')
    mycur=con.cursor()
    mycur.execute('Select UserName,ins_name from credentials;')
    data=mycur.fetchall()
    ID=data[0][0]
    IN=data[0][1]
    
    label_1=Label(hm,bg='cyan',bd=5,text=IN,font=('Cambria bold',30),relief=SOLID)
    label_1.place(x=250,y=14)
    
    def clock():
        IST=timezone('Asia/Kolkata')
        global hm
        dt_label = Label(hm,bg='lime',text="Current Date", font = 'Verdana 12 bold')
        dt_label.place(x=50, y=30)

        tm_label = Label(hm,bg='lime',text="Current Time",font = 'Verdana 12')
        tm_label.place(x=50, y=50)

        raw_TS = datetime.now(IST)
        cur_date = raw_TS.strftime("%d %b %Y")
        cur_time = raw_TS.strftime("%H:%M:%S %p")
        formatted_now = raw_TS.strftime("%d-%m-%Y")
        dt_label.config(text = cur_date)
        tm_label.config(text = cur_time)
        tm_label.after(1000, clock)
        return formatted_now
    clock()
    
    t=Balloon(hm)    
    hm_icn=PhotoImage(file='home_icon.png')
    hmicn_btn=Button(hm, image=hm_icn,command=body,height=25,width=25,relief=SOLID,cursor='hand2')
    hmicn_btn.place(x=1055,y=30)
    t.bind_widget(hmicn_btn,balloonmsg='Home')

    icf=PhotoImage(file='min1.png')
    icf_btn=Button(hm, image=icf, command=hm.iconify,height=26,width=26,relief=SOLID,cursor='hand2')
    icf_btn.place(x=1190,y=30)
    t.bind_widget(icf_btn,balloonmsg='Minimize')
    
    def acc_rec():
        def usr_acc():
            def update_acc():
                global ac,e1,e3,e4,e5,e6,e7,e8,e9,e10,ID
                UN=e1.get()
                ANo=e3.get()
                IN=e4.get()
                IT=e5.get()
                AD=e6.get()
                ST=e7.get()
                PC=e8.get()
                EM=e9.get()
                CNo=e10.get()
                
                import mysql.connector as c1
                conn=c1.connect(host='localhost',user='root',passwd='pp1801',database='student_mgmt')
                mycur=conn.cursor()
                q="""UPDATE credentials SET UserName=%s,Aff_No=%s, Ins_name=%s, Ins_type=%s, Ins_Ad=%s,
                    State=%s, PinCode=%s, Email=%s, Contact=%s  where UserName=%s;"""
                v=(UN,ANo,IN,IT,AD,ST,PC,EM,CNo,ID)
                mycur.execute(q,v)
                ID=UN
                conn.commit()

            global ac
            ac=Frame(hm,bg='chocolate1',width=430,height=490)
            ac.place(x=520,y=200)

            def pw_b1_fn():
                ac.destroy()
                acc_rec()
                
            pw_b1=Button(ac, text=' X ', command=pw_b1_fn,relief=SOLID,bg='tomato',cursor='hand2')
            pw_b1.place(x=390,y=10)

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
            
            global e1,e3,e4,e5,e6,e7,e8,e9,e10

            epf=Label(ac,text='Edit  Profile',bg='chocolate1',font=('Calibri bold',20))
            epf.place(x=120,y=10)
            
            usr = Label(ac, text="Username * ",font=('Calibri',12),bg='chocolate1')
            usr.place(x=20,y=65)
            e1 = Entry(ac,font=('Calibri',12),textvariable=usrvalue)
            e1.place(x=220,y=65)

            afn = Label(ac, text="Affilation Number * ",font=('Calibri',12),bg='chocolate1')
            afn.place(x=20,y=100)
            e3 = Entry(ac,font=('Calibri',12),textvariable=afnvalue)
            e3.place(x=220,y=100)

            ins = Label(ac, text="Institution Name * ",font=('Calibri',12),bg='chocolate1')
            ins.place(x=20,y=135)
            e4 = Entry(ac,font=('Calibri',12),textvariable=insvalue)
            e4.place(x=220,y=135)

            ins_type = Label(ac, text="Institution Type * ",font=('Calibri',12),bg='chocolate1')
            ins_type.place(x=20,y=170)
            e5 = ttk.Combobox(ac,font=('Calibri',12),width=15,textvariable=ins_type)
            e5['values']=('Government','Government Aided','Cooperative','Private')
            e5.place(x=220,y=170)

            ad = Label(ac, text="Institution Address * ",font=('Calibri',12),bg='chocolate1')
            ad.place(x=20,y=205)
            e6 = Entry(ac,font=('Calibri',12),textvariable=adtype)
            e6.place(x=220,y=205)

            state = Label(ac, text="State * ",font=('Calibri',12),bg='chocolate1')
            state.place(x=20,y=240)
            e7 = ttk.Combobox(ac,font=('Calibri',12),width=15,textvariable=statetype)
            e7['values']=('Andhra Pradesh','Arunachal Pradesh','Assam','Bihar','Chhattisgarh','Goa','''
Gujarat''','Haryana','Himachal Pradesh','Jharkhand','Karnataka','Kerala','''Madhya
 Pradesh''','Maharashtra','Manipur','Meghalaya','Mizoram','Nagaland','Odisha','''Pun
jab''','Rajasthan','Sikkim','Tamil Nadu','Telangana','Tripura','Uttarakhand','''Uttar
 Pradesh''','West Bengal',' ',' ','Andaman and Nicobar Islands','Chandigarh','''Dadra and
 Nagar Haweli & Daman and Diu''','Delhi / NCR','Jammu and Kashmir','Ladakh','''Laksha
dweep''','Puducherry')
            e7.place(x=220,y=240)

            pin = Label(ac, text="Pincode * ",font=('Calibri',12),bg='chocolate1')
            pin.place(x=20,y=275)
            e8 = Entry(ac,font=('Calibri',12),textvariable=pintype)
            e8.place(x=220,y=275)

            mail = Label(ac, text="Email ID * ",font=('Calibri',12),bg='chocolate1')
            mail.place(x=20,y=310)
            e9 = Entry(ac,font=('Calibri',12),textvariable=mailtype)
            e9.place(x=220,y=310)

            cno = Label(ac, text="Contact No.* ",font=('Calibri',12),bg='chocolate1')
            cno.place(x=20,y=345)
            e10 = Entry(ac,font=('Calibri',12),textvariable=cnotype)
            e10.place(x=220,y=345)

            import mysql.connector as c
            conn=c.connect(host='localhost',user='root',
                           passwd='pp1801',database='student_mgmt')
            mycur=conn.cursor()
            mycur.execute("Select * from credentials where UserName='{}' ;".format(ID))
            get_val=mycur.fetchall()
            
            e1.insert(0,get_val[0][0])
            e3.insert(0,get_val[0][2])
            e4.insert(0,get_val[0][3])
            e5.insert(0,get_val[0][4])
            e6.insert(0,get_val[0][5])
            e7.insert(0,get_val[0][6])
            e8.insert(0,get_val[0][7])
            e9.insert(0,get_val[0][8])
            e10.insert(0,get_val[0][9])

            conn.commit()

            def CFB6():
                update_acc()
                messagebox.showinfo('Info',' Profile Updated Successfully ! ',parent=ac)
                ac.destroy()
                acc_rec()
                
            b6=Button(ac,text="Save", height="2", width="20",font=('Calibri',12,'bold'),
                      bg='cyan',cursor='hand2',relief=SOLID,command=CFB6)
            b6.place(x=110,y=410)
        
        global acw
        acw=Frame(hm,bg='gold',width=550,height=690)
        acw.place(x=460,y=90)
        
        def change_paswd():
            def update_pas():
                global ID
                p1=e1.get()
                p2=e2.get()
                p3=e3.get()
                
                import mysql.connector as c
                conn=c.connect(host='localhost',user='root',
                           passwd='pp1801',database='student_mgmt')
                mycur=conn.cursor()
                mycur.execute("Select Password from credentials where username='{}';".format(ID))
                data=mycur.fetchone()
                op=data[0]

                if op==p1:
                    if p2==p3:
                        mycur.execute("UPDATE CREDENTIALS SET Password='{}' where UserName='{}';".format(p2,ID))
                        conn.commit()
                        messagebox.showinfo('Success','Password Changed Successfully !',parent=frame_6)
                        frame_6.destroy()
                    else:
                        messagebox.showinfo('Error','New passwords did not match !',parent=frame_6)
                        e2.delete(0,END)
                        e3.delete(0,END)
                else:
                    messagebox.showinfo('Error','Incorrect Current Password !',parent=frame_6)
                    e1.delete(0,END)
                    e2.delete(0,END)
                    e3.delete(0,END)
                
            cpvalue=StringVar
            npvalue=StringVar
            cnpvalue=StringVar
            
            frame_6=Frame(acw,bg='purple1',width=400,height=300)
            frame_6.place(x=60,y=195)

            hd=Label(frame_6,text='Change Password',bg='purple1',font=('Calibri bold',19))
            hd.place(x=110,y=12)

            usr = Label(frame_6, text="Current Password * ",font=('Calibri',12),bg='purple1')
            usr.place(x=20,y=65)
            e1 = Entry(frame_6,font=('Calibri',12),textvariable=cpvalue,show='*')
            e1.place(x=220,y=65)

            def show_pas(event):
                e1.configure(show='')
            def hide_pas(event):
                e1.configure(show='*')
        
            show1=Button(frame_6,text='👀',cursor='hand2',bg='purple1',font=10,
                         relief=FLAT,activebackground='purple1',fg='black')
            show1.place(x=360,y=63)

            show1.bind('<ButtonPress-1>',show_pas)
            show1.bind('<ButtonRelease-1>',hide_pas)

            usr = Label(frame_6, text="New Password * ",font=('Calibri',12),bg='purple1')
            usr.place(x=20,y=115)
            e2 = Entry(frame_6,font=('Calibri',12),textvariable=npvalue,show='*')
            e2.place(x=220,y=115)

            def show_pas(event):
                e2.configure(show='')
            def hide_pas(event):
                e2.configure(show='*')
        
            show2=Button(frame_6,text='👀',cursor='hand2',bg='purple1',font=10,
                         relief=FLAT,activebackground='purple1',fg='black')
            show2.place(x=360,y=113)

            show2.bind('<ButtonPress-1>',show_pas)
            show2.bind('<ButtonRelease-1>',hide_pas)

            usr = Label(frame_6, text="Confirm New Password * ",font=('Calibri',12),bg='purple1')
            usr.place(x=20,y=165)
            e3 = Entry(frame_6,font=('Calibri',12),textvariable=cnpvalue,show='*')
            e3.place(x=220,y=165)

            def show_pas(event):
                e3.configure(show='')
            def hide_pas(event):
                e3.configure(show='*')
        
            show3=Button(frame_6,text='👀',cursor='hand2',bg='purple1',font=10,
                         relief=FLAT,activebackground='purple1',fg='black') 
            show3.place(x=360,y=163)

            show3.bind('<ButtonPress-1>',show_pas)
            show3.bind('<ButtonRelease-1>',hide_pas)

            b6=Button(frame_6,text="Save", width="16",font=('Calibri',12,'bold'),
                      bg='cyan',cursor='hand2',relief=SOLID,command=update_pas)
            b6.place(x=220,y=215)

            b6=Button(frame_6,text="Cancel", width="17",font=('Calibri',12,'bold'),
                      bg='cyan',cursor='hand2',relief=SOLID,command=frame_6.destroy)
            b6.place(x=40,y=215)
        
        c_pas=Button(acw, text=' Change Password ', command=change_paswd,
                     relief=SOLID,bg='cyan',cursor='hand2')
        c_pas.place(x=400,y=10)

        pw_b1=Button(acw, text=' X ', command=acw.destroy,relief=SOLID,bg='tomato',cursor='hand2')
        pw_b1.place(x=515,y=10)

        import mysql.connector as c
        conn=c.connect(host='localhost',user='root',
                           passwd='pp1801',database='student_mgmt')
        mycur=conn.cursor()
        mycur.execute("Select * from credentials where UserName='{}';".format(ID))
        get_val=mycur.fetchall()

        ac_img = PhotoImage(file='acc_image.png')
        ac_img_label=Label(acw,image=ac_img,height='75',width='75')
        ac_img_label.place(x=180,y=20)
        
        pf=Label(acw,text='User  Profile',bg='gold',font=('Calibri bold',20))
        pf.place(x=160,y=110)

        lb=Label(acw,text='',bg='gold')
        
        usr = Label(acw, text="Username                       : ",font=('Calibri',12),bg='gold')
        usr.place(x=50,y=175)
        r1 = Label(acw, text=get_val[0][0],font=('Calibri',12),bg='cyan')
        r1.place(x=245,y=175)

        afn = Label(acw, text="Affilation Number        : ",font=('Calibri',12),bg='gold')
        afn.place(x=50,y=225)
        r2 = Label(acw, text=get_val[0][2],font=('Calibri',12),bg='cyan')
        r2.place(x=245,y=225)

        ins = Label(acw, text="Institution Name           : ",font=('Calibri',12),bg='gold')
        ins.place(x=50,y=275)
        r3 = Label(acw, text=get_val[0][3],font=('Calibri',12),bg='cyan')
        r3.place(x=245,y=275)

        ins_type = Label(acw, text="Institution Type             : ",font=('Calibri',12),bg='gold')
        ins_type.place(x=50,y=325)
        r4 = Label(acw, text=get_val[0][4],font=('Calibri',12),bg='cyan')
        r4.place(x=245,y=325)

        ad = Label(acw, text="Institution Address        : ",font=('Calibri',12),bg='gold')
        ad.place(x=50,y=375)
        r5 = Label(acw, text=get_val[0][5],font=('Calibri',12),bg='cyan')
        r5.place(x=245,y=375)

        state = Label(acw, text="State                                :",font=('Calibri',12),bg='gold')
        state.place(x=50,y=425)
        r6 = Label(acw, text=get_val[0][6],font=('Calibri',12),bg='cyan')
        r6.place(x=245,y=425)

        pin = Label(acw, text="Pincode                          : ",font=('Calibri',12),bg='gold')
        pin.place(x=50,y=475)
        r7 = Label(acw, text=get_val[0][7],font=('Calibri',12),bg='cyan')
        r7.place(x=245,y=475)

        mail = Label(acw, text="Email ID                          : ",font=('Calibri',12),bg='gold')
        mail.place(x=50,y=525)
        r8 = Label(acw, text=get_val[0][8],font=('Calibri',12),bg='cyan')
        r8.place(x=245,y=525)

        cno = Label(acw, text="Contact No.                   : ",font=('Calibri',12),bg='gold')
        cno.place(x=50,y=575)
        r9 = Label(acw, text=get_val[0][9],font=('Calibri',12),bg='cyan')
        r9.place(x=245,y=575)

        def edit_pf():
            usr_acc()
            acw.destroy()
            
        b15=Button(acw,text="Edit Profile", height="2", width="20",font=('Calibri',12,'bold'),
                   bg='cyan',cursor='hand2',command=edit_pf)
        b15.place(x=150,y=630)

        acw.mainloop()
        
        
        
        acc=PhotoImage(file='download - Copy.png')
        acc_b=Button(hm, image=acc, command=acc_rec,height=25,width=25,relief=SOLID,cursor='hand2')
        acc_b.place(x=1145,y=30)
        t.bind_widget(acc_b,balloonmsg='User Account')

        cal_logo=PhotoImage(file='cal_logo.png')

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
