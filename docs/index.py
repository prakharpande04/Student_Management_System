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
    con=m.connect(host='sql6.freemysqlhosting.net',user='sql6706105',passwd='lsregtItpA',database='sql6706105')
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
    hm_icn=PhotoImage(file="C://Git_Projects//Student_Management_System//Code//Images//home_icon.png")
    hmicn_btn=Button(hm, image=hm_icn,command=body,height=25,width=25,relief=SOLID,cursor='hand2')
    hmicn_btn.place(x=1055,y=30)
    t.bind_widget(hmicn_btn,balloonmsg='Home')

    icf=PhotoImage(file="C://Git_Projects//Student_Management_System//Code//Images//min1.png")
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
                conn=c1.connect(host='sql6.freemysqlhosting.net',user='sql6706105',passwd='lsregtItpA',database='sql6706105')
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
            conn=c.connect(host='sql6.freemysqlhosting.net',user='sql6706105',
                           passwd='lsregtItpA',database='sql6706105')
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
                conn=c.connect(host='sql6.freemysqlhosting.net',user='sql6706105',
                           passwd='lsregtItpA',database='sql6706105')
                print(conn.is_connected())
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
        conn=c.connect(host='sql6.freemysqlhosting.net',user='sql6706105',
                           passwd='lsregtItpA',database='sql6706105')
        mycur=conn.cursor()
        mycur.execute("Select * from credentials where UserName='{}';".format(ID))
        get_val=mycur.fetchall()

        ac_img = PhotoImage(file="C://Git_Projects//Student_Management_System//Code//Images//acc_image.png")
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
        
    acc=PhotoImage(file="C://Git_Projects//Student_Management_System//Code//Images//download - Copy.png")
    acc_b=Button(hm, image=acc, command=acc_rec,height=25,width=25,relief=SOLID,cursor='hand2')
    acc_b.place(x=1145,y=30)
    t.bind_widget(acc_b,balloonmsg='User Account')

    cal_logo=PhotoImage(file="C://Git_Projects//Student_Management_System//Code//Images//cal_logo.png")
    
    def std_data():
        frame_1=Frame(hm,bg='cyan',height=550,width=450,relief=GROOVE)
        frame_1.place(x=27,y=200)

        label_2=Label(frame_1,bg='white',font=('Calibri',12),text='Student Data : ',relief=SOLID)
        label_2.place(x=15,y=10)

        label_3=Label(frame_1,bg='white',font=('Calibri',12),text=' Unique Student ID ',relief=SOLID)
        label_3.place(x=15,y=50)

        label_4=Label(frame_1,bg='white',font=('Calibri',12),text=' Student Name ',relief=SOLID)
        label_4.place(x=15,y=80)

        label_5=Label(frame_1,bg='white',font=('Calibri',12),text=' Admission No. ',relief=SOLID)
        label_5.place(x=15,y=110)

        label_6=Label(frame_1,bg='white',font=('Calibri',12),text=' Admission Date ',relief=SOLID)
        label_6.place(x=15,y=140)

        label_7=Label(frame_1,bg='white',font=('Calibri',12),text=' Date of Birth ',relief=SOLID)
        label_7.place(x=15,y=170)

        label_8=Label(frame_1,bg='white',font=('Calibri',12),text=' Gender ',relief=SOLID)
        label_8.place(x=15,y=200)

        label_9=Label(frame_1,bg='white',font=('Calibri',12),text=' Class ',relief=SOLID)
        label_9.place(x=15,y=230)

        label_10=Label(frame_1,bg='white',font=('Calibri',12),text=" Father's Name ",relief=SOLID)
        label_10.place(x=15,y=260)

        label_11=Label(frame_1,bg='white',font=('Calibri',12),text=" Mother's Name ",relief=SOLID)
        label_11.place(x=15,y=290)

        label_12=Label(frame_1,bg='white',font=('Calibri',12),text=' Aadhar No. ',relief=SOLID)
        label_12.place(x=15,y=320)

        label_13=Label(frame_1,bg='white',font=('Calibri',12),text=' Address ',relief=SOLID)
        label_13.place(x=15,y=357)

        label_14=Label(frame_1,bg='white',font=('Calibri',12),text=' Contact No. ',relief=SOLID)
        label_14.place(x=15,y=397)

        label_15=Label(frame_1,bg='white',font=('Calibri',12),text=' Email ID ',relief=SOLID)
        label_15.place(x=15,y=427)

        label_16=Label(frame_1,bg='white',font=('Calibri',12),text=' Mother Tongue ',relief=SOLID)
        label_16.place(x=15,y=457)

        def add_recs():
            global frame_2
            e1=ent1.get()
            e2=ent2.get()
            e3=ent3.get()
            e4=ent4.get()
            e5=ent5.get()
            e6=ent6.get()
            e7=ent7.get()
            e8=ent8.get()
            e9=ent9.get()
            e10=ent10.get()
            e11=ent11.get('1.0',END)
            e12=ent12.get()
            e13=ent13.get()
            e14=ent14.get()

            import mysql.connector as c2
            conn2=c2.connect(host='sql6.freemysqlhosting.net',user='sql6706105',
                        passwd='lsregtItpA',database='sql6706105')
            mycur2=conn2.cursor()
            mycur2.execute("""INSERT INTO std_details VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}',
                                            '{}','{}','{}','{}')""".format(e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14))
            conn2.commit()

            messagebox.showinfo('Success','Record Added Successfully !',parent=frame_2)

            ent1.delete(0,END)
            ent2.delete(0,END)
            ent3.delete(0,END)
            ent4.delete(0,END)
            ent5.delete(0,END)
            ent6.delete(0,END)
            ent7.delete(0,END)
            ent8.delete(0,END)
            ent9.delete(0,END)
            ent10.delete(0,END)
            ent11.delete('1.0',END)
            ent12.delete(0,END)
            ent13.delete(0,END)
            ent14.delete(0,END)

            global trvw
            trvw.delete(*trvw.get_children())
            import mysql.connector as c3
            conn3=c3.connect(host='sql6.freemysqlhosting.net',user='sql6706105',
                        passwd='lsregtItpA',database='sql6706105')
            mycur3=conn3.cursor()
            mycur3.execute('SELECT * FROM std_details;')
            data=mycur3.fetchall()
            
            for i in data:
                trvw.insert('',1,text='',values=(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11],i[12],i[13]))

        usidvalue=StringVar()
        usnamevalue=StringVar()
        admnovalue=StringVar()
        admdtvalue=StringVar()
        dobvalue=StringVar()
        gndvalue=StringVar()
        clsvalue=StringVar()
        uidvalue=StringVar()
        fnamevalue=StringVar()
        mnamevalue=StringVar()
        cnovalue=StringVar()
        mailvalue=StringVar()
        mtngvalue=StringVar()

        global ent1,ent2,ent3,ent4,ent5,ent6,ent7,ent8,ent9,ent10,ent11,ent12,ent13,ent14
        ent1 = Entry(frame_1,font=('Calibri',12),textvariable=usidvalue,width=27)
        ent1.place(x=175,y=50)

        ent2 = Entry(frame_1,font=('Calibri',12),textvariable=usnamevalue,width=27)
        ent2.place(x=175,y=80)

        ent3 = Entry(frame_1,font=('Calibri',12),textvariable=admnovalue,width=27)
        ent3.place(x=175,y=110)

        ent4 = Entry(frame_1,font=('Calibri',12),textvariable=admdtvalue,width=27)
        ent4.place(x=175,y=140)

        def calender1():
            cdr1 = Toplevel()
            cdr1.geometry("255x220+450+250")
            cdr1.overrideredirect(1)
     
            cal1 = Calendar(cdr1, selectmode = 'day',date_pattern='dd-mm-y')
            cal1.place(x=2,y=2)

            def get_date():
                global ent4
                ent4.delete(0,END)
                ent4.insert(0,cal1.get_date())
                cdr1.destroy()
                
            Button(cdr1, text = "Get Date",
                        command = get_date,cursor='hand2').place(x=100,y=190)
            cdr1.mainloop()
            
        global win1,win2
        win1=Toplevel()
        win1.geometry('21x21+425+342')
        win1.overrideredirect(1)
        win1.attributes('-topmost',True)
        
        admcal=Button(win1,image=cal_logo,command=calender1,cursor='hand2')
        admcal.pack()
        
        ent5 = Entry(frame_1,font=('Calibri',12),textvariable=dobvalue,width=27)
        ent5.place(x=175,y=170)

        def calender2():
            cdr2 = Toplevel()
            cdr2.geometry("255x220+450+283")
            cdr2.overrideredirect(1)

            cal2 = Calendar(cdr2, selectmode = 'day',date_pattern='dd-mm-y')
            cal2.place(x=2,y=2)
            
            def get_date():
                global ent5
                ent5.delete(0,END)
                ent5.insert(0,cal2.get_date())
                cdr2.destroy()

            Button(cdr2, text = "Get Date",
                        command = get_date,cursor='hand2').place(x=100,y=190)
            cdr2.mainloop()

        win2=Toplevel()
        win2.geometry('21x21+425+372')
        win2.overrideredirect(1)
        win2.attributes('-topmost',True)
        
        dobcal=Button(win2,image=cal_logo,command=calender2,cursor='hand2')
        dobcal.pack()

        ent6=ttk.Combobox(frame_1,width=24,font=('Calibri',12),textvariable=gndvalue)
        ent6['values']=('Male','Female','Others')
        ent6.place(x=175,y=200)
            
        ent7 = Entry(frame_1,font=('Calibri',12),textvariable=clsvalue,width=27)
        ent7.place(x=175,y=230)

        ent8 = Entry(frame_1,font=('Calibri',12),textvariable=fnamevalue,width=27)
        ent8.place(x=175,y=260)

        ent9 = Entry(frame_1,font=('Calibri',12),textvariable=mnamevalue,width=27)
        ent9.place(x=175,y=290)

        ent10 = Entry(frame_1,font=('Calibri',12),textvariable=uidvalue,width=27)
        ent10.place(x=175,y=320)

        ent11 = Text(frame_1,width=27,height=2,font=('Calibri',12))
        ent11.place(x=175,y=350)

        ent12 = Entry(frame_1,font=('Calibri',12),textvariable=cnovalue,width=27)
        ent12.place(x=175,y=397)

        ent13 = Entry(frame_1,font=('Calibri',12),textvariable=mailvalue,width=27)
        ent13.place(x=175,y=427)

        ent14 = Entry(frame_1,font=('Calibri',12),textvariable=mtngvalue,width=27)
        ent14.place(x=175,y=457)

        def clr_entry():
            ent1.delete(0,END)
            ent2.delete(0,END)
            ent3.delete(0,END)
            ent4.delete(0,END)
            ent5.delete(0,END)
            ent6.delete(0,END)
            ent7.delete(0,END)
            ent8.delete(0,END)
            ent9.delete(0,END)
            ent10.delete(0,END)
            ent11.delete('1.0',END)
            ent12.delete(0,END)
            ent13.delete(0,END)
            ent14.delete(0,END)

        def del_rec():
            global frame_2
            ans2=messagebox.askokcancel('Warning','Are you sure you want to delete ?',parent=frame_2)
            if ans2:
                del_id=ent1.get()

                import mysql.connector as c4
                conn4=c4.connect(host='sql6.freemysqlhosting.net',user='sql6706105',
                                passwd='lsregtItpA',database='sql6706105')
                mycur4=conn4.cursor()
                mycur4.execute("DELETE FROM std_details WHERE UNIQUE_STUDENT_ID='{}';".format(del_id))
                conn4.commit()

                messagebox.showinfo('Success !','Record Deleted Successfully !',parent=frame_2)
                clr_entry()

                global trvw
                trvw.delete(*trvw.get_children())
                
                conn5=c4.connect(host='sql6.freemysqlhosting.net',user='sql6706105',
                            passwd='lsregtItpA',database='sql6706105')
                mycur5=conn5.cursor()
                mycur5.execute('SELECT * FROM std_details;')
                data=mycur5.fetchall()

                for i in data:
                    trvw.insert('',1,text='',values=(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11],i[12],i[13]))

        def update_recs():
            e1=ent1.get()
            e2=ent2.get()
            e3=ent3.get()
            e4=ent4.get()
            e5=ent5.get()
            e6=ent6.get()
            e7=ent7.get()
            e8=ent8.get()
            e9=ent9.get()
            e10=ent10.get()
            e11=ent11.get('1.0',END)
            e12=ent12.get()
            e13=ent13.get()
            e14=ent14.get()
            
            import mysql.connector as c6
            conn6=c6.connect(host='sql6.freemysqlhosting.net',user='sql6706105',
                            passwd='lsregtItpA',database='sql6706105')
            mycur6=conn6.cursor()
            mycur6.execute("""UPDATE std_details SET UNIQUE_STUDENT_ID='{}', STUDENT_NAME='{}',
                                            ADMISSION_NO='{}', ADMISSION_DATE='{}', DATE_OF_BIRTH='{}', GENDER='{}',
                                            CLASS='{}', FATHER_NAME='{}', MOTHER_NAME='{}', Aadhar_no='{}', Address='{}',
                                            CONTACT_NO='{}', EMAIL='{}', Mother_Tongue='{}' WHERE UNIQUE_STUDENT_ID=
                                            '{}';""".format(e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,index))
            conn6.commit()

            global trvw
            trvw.delete(*trvw.get_children())
            import mysql.connector as c7
            conn7=c7.connect(host='sql6.freemysqlhosting.net',user='sql6706105',
                        passwd='lsregtItpA',database='sql6706105')
            mycur7=conn7.cursor()
            mycur7.execute('SELECT * FROM std_details;')
            data=mycur7.fetchall()

            ent1.delete(0,END)
            ent2.delete(0,END)
            ent3.delete(0,END)
            ent4.delete(0,END)
            ent5.delete(0,END)
            ent6.delete(0,END)
            ent7.delete(0,END)
            ent8.delete(0,END)
            ent9.delete(0,END)
            ent10.delete(0,END)
            ent11.delete('1.0',END)
            ent12.delete(0,END)
            ent13.delete(0,END)
            ent14.delete(0,END)

            for i in data:
                trvw.insert('',1,text='',values=(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11],i[12],i[13]))
            
                

        global frame_3
        frame_3=Frame(frame_1,bd=3,bg='crimson',width=390,height=40)
        frame_3.place(x=30,y=497)

        add_btn=Button(frame_3,text='ADD',width=10,command=add_recs,cursor='hand2')
        add_btn.place(x=10,y=5)

        del_btn=Button(frame_3,text='DELETE',width=10,command=del_rec,cursor='hand2')
        del_btn.place(x=105,y=5)

        updt_btn=Button(frame_3,text='UPDATE',width=10,command=update_recs,cursor='hand2')
        updt_btn.place(x=200,y=5)

        def clr_entry():
            ent1.delete(0,END)
            ent2.delete(0,END)
            ent3.delete(0,END)
            ent4.delete(0,END)
            ent5.delete(0,END)
            ent6.delete(0,END)
            ent7.delete(0,END)
            ent8.delete(0,END)
            ent9.delete(0,END)
            ent10.delete(0,END)
            ent11.delete('1.0',END)
            ent12.delete(0,END)
            ent13.delete(0,END)
            ent14.delete(0,END)
        
        clr_btn=Button(frame_3,text='CLEAR',width=10,command=clr_entry,cursor='hand2')
        clr_btn.place(x=295,y=5)

    def utilities():
        frame_5=Frame(hm,bd=3,bg='dark turquoise',width=655,height=45)
        frame_5.place(x=310,y=105)

        def age_calculator():
            def clear_entry() :
                    bd_e.delete(0, END)
                    bm_e.delete(0, END)
                    by_e.delete(0, END)
                    gd_e.delete(0, END)
                    gm_e.delete(0, END)
                    gy_e.delete(0, END)
                    cd_cal.configure(text='')

            # function for checking error
            def checkError():
                if (bd_e.get() == "" or bm_e.get() == ""
                    or by_e.get() == "" or gd_e.get() == ""
                    or gm_e.get() == "" or gy_e.get() == ""):
                    messagebox.showerror("Input Error",parent=ac_w)
                    clear_entry()
                    return -1

            def Age_cal():
                value = checkError()
                if value ==  -1:
                    return
                
                else :
                    b_d = int(bd_e.get())
                    b_m = int(bm_e.get())
                    b_y = int(by_e.get())

                    g_d= int(gd_e.get())
                    g_m = int(gm_e.get())
                    g_y = int(gy_e.get())
                            
                    m =[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
                    
                    if (b_d > g_d):
                        g_m = g_m-1
                        g_d = g_d + m[b_m-1]

                    if (b_m > g_m):
                        g_y = g_y-1
                        g_m = g_m+12
                                
                    # calculate 
                    cal_d = g_d - b_d;
                    cal_m = g_m - b_m;
                    cal_y = g_y - b_y;
                    
                    op='Age is '+str(cal_d)+' days , '+str(cal_m)+' months , '+str(cal_y)+' years. '
                    cd_cal.configure(text=op)
                    
            ac_w = Tk()
            ac_w.configure(background = "slateblue1")
            ac_w.geometry("250x520+450+150")
            ac_w.overrideredirect(1)

            pw_b1=Button(ac_w, text=' X ', command=ac_w.destroy,relief=SOLID,bg='tomato',cursor='hand2')
            pw_b1.place(x=225,y=5)
            
            lbl = Label(ac_w, text = "  Age  Calculator  ",font = 'Verdana 12', bg = "slateblue1")
            
            dob = Label(ac_w, text = "Date Of Birth", bg = "green yellow")

            gDate = Label(ac_w, text = "To Date", bg = "green yellow")

            bd = Label(ac_w, text = "Birth Date", bg = "slateblue1")
            bm = Label(ac_w, text = "Birth Month", bg = "slateblue1")
            by = Label(ac_w, text = "Birth Year", bg = "slateblue1")

            gd = Label(ac_w, text = "To Date", bg = "slateblue1")
            gm = Label(ac_w, text = "To Month", bg = "slateblue1")
            gy = Label(ac_w, text = "To Year", bg = "slateblue1")

            bd_e = Entry(ac_w)
            bm_e = Entry(ac_w)
            by_e = Entry(ac_w)
            
            gd_e = Entry(ac_w)
            gm_e = Entry(ac_w)
            gy_e = Entry(ac_w)
            
            cd_cal = Label(ac_w,bg = "slateblue1",)

            lh_9=Label(ac_w,bg='slateblue1')
            lh_9.pack()

            lbl.pack()
            
            lh_9=Label(ac_w,bg='slateblue1')
            lh_9.pack()
        
            dob.pack()
            
            bd.pack()
            bd_e.pack()
            
            bm.pack()
            bm_e.pack()
            
            by.pack()
            by_e.pack()

            lh_9=Label(ac_w,bg='slateblue1')
            lh_9.pack()
            
            gDate.pack()
            
            gd.pack()
            gd_e.pack()
            
            gm.pack()
            gm_e.pack()
            
            gy.pack()
            gy_e.pack()

            lh_9=Label(ac_w,bg='slateblue1')
            lh_9.pack()

            calc_age = Button(ac_w, text = "Calculate", font=('Calibri',12),fg = "Black",
                              bg = "Green yellow", command = Age_cal,cursor='hand2')
            calc_age.pack()

            Label(ac_w, bg = "slateblue1").pack()
            
            cd_cal.pack()

            Label(ac_w, bg = "slateblue1").pack()
            
            clr_e = Button(ac_w, text = "Clear Entry",font=('Calibri',12),
                           fg = "Black", bg = "Red", command = clear_entry,cursor='hand2')
            clr_e.pack()
            
            ac_w.mainloop()

        def calender():
            cdr = Toplevel()
            cdr.geometry("262x260+530+150")
            cdr.configure(bg='lemon chiffon')
            cdr.overrideredirect(1)

            cadr_label=Label(cdr,text=' CALENDAR ',font=('Bahnschrift SemiCondensed',19,'bold'),
                             bg='lemon chiffon',foreground='red')
            cadr_label.pack()
            
            cal = Calendar(cdr, selectmode = 'day',date_pattern='dd-mm-y')
            cal.place(x=5,y=35)

            def c_ch(ev):
                cl['background']='tomato'
            def c_ch_back(ev):
                cl['background']='SystemButtonFace'
                
            cl=Button(cdr, text = "Close",command = cdr.destroy,activebackground='tomato',cursor='hand2')
            cl.place(x=110,y=225)
            cl.bind('<Enter>',c_ch)
            cl.bind('<Leave>',c_ch_back)

        def calculator():
            calc=Toplevel()
            calc.geometry('320x350+500+150')
            calc.configure(bg='dark orange')
            calc.overrideredirect(1)

            def btn_click(item):
                global expression
                expression+=item
                input_field.delete(0,END)
                input_field.insert(END,expression)

            def bt_clear(expression):
                input_field.delete(0,END)
                expression=''

            def bt_equal(expression):
                result=str(eval(input_field.get()))
                input_field.delete(0,END)
                input_field.insert(END,result)
                expression=''

            global expression
            expression=''

            input_text=StringVar()
            
            cal_label=Label(calc,text=' CALCULATOR ',font=('Bahnschrift SemiCondensed',24,'bold'),
                            bg='dark orange',foreground='purple')
            cal_label.pack()

            pw_b4=Button(calc, text=' X ', command=calc.destroy, relief=SOLID, bg='tomato', cursor='hand2')
            pw_b4.place(x=290,y=7)

            global input_field
            input_field=Entry(calc,text='',font=('Calibri',18,'bold'),bd=2,relief=GROOVE,
                              textvariable=input_text,width=24,justify=RIGHT)
            input_field.place(x=12,y=45)

            clr=Button(calc,text='Clear',cursor='hand2',width=27,height=2,relief=GROOVE,
                       font=('Calibri',12,'bold'),command=lambda:bt_clear(expression))
            clr.place(x=11,y=80)
            
            div=Button(calc,text='/',cursor='hand2',width=8,height=2,relief=GROOVE,
                       font=('Calibri',12,'bold'),command=lambda:btn_click('/'))
            div.place(x=233,y=80)

            seven=Button(calc,text='7',cursor='hand2',width=8,height=2,relief=GROOVE,
                         font=('Calibri',12,'bold'),command=lambda:btn_click('7'))
            seven.place(x=11,y=132)

            eight=Button(calc,text='8',cursor='hand2',width=8,height=2,relief=GROOVE,
                         font=('Calibri',12,'bold'),command=lambda:btn_click('8'))
            eight.place(x=85,y=132)

            nine=Button(calc,text='9',cursor='hand2',width=8,height=2,relief=GROOVE,
                        font=('Calibri',12,'bold'),command=lambda:btn_click('9'))
            nine.place(x=159,y=132)

            mtpy=Button(calc,text='*',cursor='hand2',width=8,height=2,relief=GROOVE,
                        font=('Calibri',12,'bold'),command=lambda:btn_click('*'))
            mtpy.place(x=233,y=132)

            four=Button(calc,text='4',cursor='hand2',width=8,height=2,relief=GROOVE,
                        font=('Calibri',12,'bold'),command=lambda:btn_click('4'))
            four.place(x=11,y=184)

            five=Button(calc,text='5',cursor='hand2',width=8,height=2,relief=GROOVE,
                        font=('Calibri',12,'bold'),command=lambda:btn_click('5'))
            five.place(x=85,y=184)

            six=Button(calc,text='6',cursor='hand2',width=8,height=2,relief=GROOVE,
                       font=('Calibri',12,'bold'),command=lambda:btn_click('6'))
            six.place(x=159,y=184)

            sub=Button(calc,text='-',cursor='hand2',width=8,height=2,relief=GROOVE,
                       font=('Calibri',12,'bold'),command=lambda:btn_click('-'))
            sub.place(x=233,y=184)

            one=Button(calc,text='1',cursor='hand2',width=8,height=2,relief=GROOVE,
                       font=('Calibri',12,'bold'),command=lambda:btn_click('1'))
            one.place(x=11,y=236)

            two=Button(calc,text='2',cursor='hand2',width=8,height=2,relief=GROOVE,
                       font=('Calibri',12,'bold'),command=lambda:btn_click('2'))
            two.place(x=85,y=236)

            three=Button(calc,text='3',cursor='hand2',width=8,height=2,relief=GROOVE,
                         font=('Calibri',12,'bold'),command=lambda:btn_click('3'))
            three.place(x=159,y=236)

            plus=Button(calc,text='+',cursor='hand2',width=8,height=2,relief=GROOVE,
                        font=('Calibri',12,'bold'),command=lambda:btn_click('+'))
            plus.place(x=233,y=236)

            zero_2x=Button(calc,text='00',cursor='hand2',width=8,height=2,relief=GROOVE,
                           font=('Calibri',12,'bold'),command=lambda:btn_click('00'))
            zero_2x.place(x=11,y=288)

            zero=Button(calc,text='0',cursor='hand2',width=8,height=2,relief=GROOVE,
                        font=('Calibri',12,'bold'),command=lambda:btn_click('0'))
            zero.place(x=85,y=288)

            dot=Button(calc,text='.',cursor='hand2',width=8,height=2,relief=GROOVE,
                       font=('Calibri',12,'bold'),command=lambda:btn_click('.'))
            dot.place(x=159,y=288)

            equal=Button(calc,text=' = ',cursor='hand2',width=8,height=2,relief=GROOVE,
                         font=('Calibri',12,'bold'),command=lambda:bt_equal(expression))
            equal.place(x=233,y=288)

            calc.mainloop()

        def support():
            sp=Frame(hm,width=30,height=20,bg='lightseagreen')
            sp.place(x=850,y=150)

            ctc=Label(sp,text=' Contact ',font=10,bg='lightseagreen')
            ctc.pack()

            ct=Label(sp,text=''' Call us : 8275711340  
             9096195735''',bg='lightseagreen')
            ct.pack()

            em=Label(sp,text=' Mail us : softwares@.com',bg='lightseagreen')
            em.pack()

            pw_b4=Button(sp, text=' X ', command=sp.destroy, relief=SOLID, bg='white',fg='red', cursor='hand2')
            pw_b4.place(x=137,y=2)

        label_utl=Label(frame_5,text=' Utilities          :         ',bg='dark turquoise',font=('Calibri',14,'bold'))
        label_utl.place(x=8,y=6)

        calculator=Button(frame_5,text=' Calculator ',command=calculator,relief=SOLID,cursor='hand2')
        calculator.place(x=440,y=6)

        ag_cal=Button(frame_5,text=' Age Calculator ',command=age_calculator,relief=SOLID,cursor='hand2')
        ag_cal.place(x=170,y=6)

        cal_r=Button(frame_5,text=' Calendar ',command=calender,relief=SOLID,cursor='hand2')
        cal_r.place(x=320,y=6)

        spt=Button(frame_5,text=' Support ',command=support,relief=SOLID,cursor='hand2')
        spt.place(x=570,y=6)

    def std_recs():
        global frame_2
        srcvalue=StringVar()
        srcval=StringVar()

        def search():
            sb=label_18.get()
            sf=src_e.get()

            trvw.delete(*trvw.get_children())
            
            import mysql.connector as c9
            conn9=c9.connect(host='sql6.freemysqlhosting.net',user='sql6706105',
                        passwd='lsregtItpA',database='sql6706105')
            mycur9=conn9.cursor()
            mycur9.execute("SELECT * FROM std_details WHERE "+sb+" LIKE '%"+sf+"%';")
            data=mycur9.fetchall()

            for i in data:
                trvw.insert('',1,text='',values=(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11],i[12],i[13]))
                
        
        frame_2=Frame(hm,bg='cyan',height=580,width=850,relief=GROOVE)
        frame_2.place(x=500,y=180)

        dv_l=Label(frame_2,bg='cyan',text='Developed By : PD Software Developers',font=18)
        dv_l.place(x=450,y=568)

        label_17=Label(frame_2,text='Search By : ',bg='cyan',font=('Calibri',13,'bold'))
        label_17.place(x=10,y=10)

        label_18=ttk.Combobox(frame_2,font=('Calibri',10),state='readonly',width=20,
                              textvariable=srcvalue,cursor='hand2')
        label_18['values']=('Unique_Student_ID','Student_Name','Admission_No','Aadhar_No')
        label_18.place(x=100,y=12)

        src_e=Entry(frame_2,font=('Calibri',10,'bold'),textvariable=srcval,bd=2)
        src_e.place(x=280,y=12)

        src_btn=Button(frame_2,text='Search',width=9,command=search,cursor='hand2')
        src_btn.place(x=445,y=10)

        def show_all():
            trvw.delete(*trvw.get_children())
            import mysql.connector as c8
            conn8=c8.connect(host='sql6.freemysqlhosting.net',user='sql6706105',
                        passwd='lsregtItpA',database='sql6706105')
            mycur8=conn8.cursor()
            mycur8.execute('SELECT * FROM std_details;')
            data=mycur8.fetchall()

            for i in data:
                trvw.insert('',1,text='',values=(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11],i[12],i[13]))
            
        shw_all=Button(frame_2,text='Show All',width=9,command=show_all,cursor='hand2')
        shw_all.place(x=535,y=10)

        def select_rec(ev):
            global index
            fc=trvw.focus()
            get_val=trvw.item(fc,'values')

            ent1.delete(0,END)
            ent2.delete(0,END)
            ent3.delete(0,END)
            ent4.delete(0,END)
            ent5.delete(0,END)
            ent6.delete(0,END)
            ent7.delete(0,END)
            ent8.delete(0,END)
            ent9.delete(0,END)
            ent10.delete(0,END)
            ent11.delete('1.0',END)
            ent12.delete(0,END)
            ent13.delete(0,END)
            ent14.delete(0,END)

            ent1.insert(END,get_val[0])
            ent2.insert(END,get_val[1])
            ent3.insert(END,get_val[2])
            ent4.insert(END,get_val[3])
            ent5.insert(END,get_val[4])
            ent6.insert(END,get_val[5])
            ent7.insert(END,get_val[6])
            ent8.insert(END,get_val[7])
            ent9.insert(END,get_val[8])
            ent10.insert(END,get_val[9])
            ent11.insert(END,get_val[10])
            ent12.insert(END,get_val[11])
            ent13.insert(END,get_val[12])
            ent14.insert(END,get_val[13])

            index=ent1.get()

        frame_4=Frame(frame_2,bd=2,bg='navajo white',width=730,height=500)
        frame_4.pack(padx=10,pady=50)
        frame_4.pack_propagate(False)

        st=Style()
        st.configure('Treeview.Heading',font=('Bahnschrift SemiCondensed',14),foreground='red')
        st.configure('Treeview',font=('Calibri',12))

        hsb = Scrollbar(frame_4,orient='horizontal')
        vsb = Scrollbar(frame_4,orient='vertical')

        global trvw
        trvw=ttk.Treeview(frame_4,show='headings',height=23,
                          columns=('USI','SN','ANO','ADT','DOB','GD','CL','FN','MN','AN','AD','CN','ML','MT'))
        
        hsb.pack(side ='bottom',fill='both')
        
        vsb.pack(side='right',fill='both')

        hsb.config(command=trvw.xview)
        vsb.config(command=trvw.yview)

        trvw.heading('USI',text=' Unique Student ID ')
        trvw.heading('SN',text=' Student  Name ')
        trvw.heading('ANO',text=' Admission No. ')
        trvw.heading('ADT',text=' Admission Date ')
        trvw.heading('DOB',text=' Date of Birth ')
        trvw.heading('GD',text=' Gender ')
        trvw.heading('CL',text=' Class ')
        trvw.heading('FN',text=" Father's Name ")
        trvw.heading('MN',text=" Mother's Name ")
        trvw.heading('AN',text=' Aadhar No. ')
        trvw.heading('AD',text=' Address ')
        trvw.heading('CN',text=' Contact Number ')
        trvw.heading('ML',text=' Email ID ')
        trvw.heading('MT',text=' Mother Tongue ')

        trvw.column('USI',width=150,minwidth=150,anchor=CENTER)
        trvw.column('SN',width=260,minwidth=260,anchor=CENTER)
        trvw.column('ANO',width=120,minwidth=120,anchor=CENTER)
        trvw.column('ADT',width=130,minwidth=130,anchor=CENTER)
        trvw.column('DOB',width=110,minwidth=110,anchor=CENTER)
        trvw.column('GD',width=80,minwidth=80,anchor=CENTER)
        trvw.column('CL',width=70,minwidth=70,anchor=CENTER)
        trvw.column('FN',width=200,minwidth=200,anchor=CENTER)
        trvw.column('MN',width=200,minwidth=200,anchor=CENTER)
        trvw.column('AN',width=150,minwidth=150,anchor=CENTER)
        trvw.column('AD',width=320,minwidth=320,anchor=CENTER)
        trvw.column('CN',width=240,minwidth=240,anchor=CENTER)
        trvw.column('ML',width=240,minwidth=240,anchor=CENTER)
        trvw.column('MT',width=170,minwidth=170,anchor=CENTER)

        trvw.bind('<ButtonRelease-1>',select_rec)

        trvw.pack()

        import mysql.connector as c1
        conn=c1.connect(host='sql6.freemysqlhosting.net',user='sql6706105',
                        passwd='lsregtItpA',database='sql6706105')
        mycur=conn.cursor()
        mycur.execute('SELECT * FROM std_details;')
        
        a=0
        for i in mycur:
            trvw.insert('',1,text='',values=(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11],i[12],i[13]))
            a+=1
            
        trvw.configure(xscrollcommand = hsb.set)
        trvw.configure(yscrollcommand=vsb.set)

        def refresh():
            trvw.delete(*trvw.get_children())
            import mysql.connector as c3
            conn=c3.connect(host='sql6.freemysqlhosting.net',user='sql6706105',
                        passwd='lsregtItpA',database='sql6706105')
            mycur=conn.cursor()
            mycur.execute("SELECT * FROM std_details ORDER BY  UNIQUE_STUDENT_ID ASC;")
            data=mycur.fetchall()

            for i in data:
                trvw.insert('',1,text='',values=(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11],i[12],i[13]))
            
        refsh=Button(frame_2,text='Refresh',width=9,command=refresh,cursor='hand2')
        refsh.place(x=630,y=10)
        
    def exit_program():
        global win1,win2,hm,w
        ans1=messagebox.askokcancel('Warning','Are you sure you want to exit ?',parent=hm)
        if ans1:
            hm.destroy()
            win1.destroy()
            win2.destroy()
            w.destroy()
    pwr=PhotoImage(file="C://Git_Projects//Student_Management_System//Code//Images//c1.png")
    pwr_b=Button(hm, image=pwr, command=exit_program,height=26,width=26,relief=SOLID,cursor='hand2')
    pwr_b.place(x=1235,y=30)
    t.bind_widget(pwr_b,balloonmsg='Close')
    
    def logout():
        global win1,win2,hm
        ans1=messagebox.askokcancel('Warning','Are you sure you want to logout ?',parent=hm)
        if ans1:
            hm.destroy()
            win1.destroy()
            win2.destroy()
    lg_out=PhotoImage(file="C://Git_Projects//Student_Management_System//Code//Images//pwrbtn.png")
    lgout_btn=Button(hm, image=lg_out,command=logout,height=25,width=25,relief=SOLID,cursor='hand2')
    lgout_btn.place(x=1100,y=30)
    t.bind_widget(lgout_btn,balloonmsg='LogOut')
    
    std_data()
    std_recs()
    utilities()
    hm.mainloop()

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
        conn=c.connect(host='sql6.freemysqlhosting.net',user='sql6706105',
                       passwd='lsregtItpA',database='sql6706105')
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

image1=PhotoImage(file="C://Git_Projects//Student_Management_System//Code//Images//IMG-20220219-WA0002.png")
label = Label(w, image=image1,width=1280,height=800).place(x=0,y=0)

text = "  STUDENT  MANAGEMENT  SYSTEM   "
label = Label(w, text=text,bg='orangered2',height='1',border='3',font=('Cambria bold italic',58),fg='cyan').place(x=10,y=5)

close=PhotoImage(file="C://Git_Projects//Student_Management_System//Code//Images//c1.png")
b3=Button(w, image=close, command=w.destroy,height=26,width=26,relief=SOLID,cursor='hand2')
b3.place(x=1235,y=20)

icf1=PhotoImage(file="C://Git_Projects//Student_Management_System//Code//Images//min1.png")
icf1b=Button(w, image=icf1, command=w.iconify,height=26,width=26,relief=SOLID,cursor='hand2')
icf1b.place(x=1235,y=60)

img=PhotoImage(file="C://Git_Projects//Student_Management_System//Code//Images//Presentation1.png")
l8=Label(w,image=img,height=200,width=200,bg='black')
l8.place(x=540,y=280)

dv_l=Label(w,bg='cyan',text='Developed By : PD Software Developers',font=18)
dv_l.place(x=970,y=770)

def login():
    def log():
        global lgn
        usrid=us_name_entry.get()
        pasw=pas_entry.get()
        f=0
        import mysql.connector as c
        conn=c.connect(host='sql6.freemysqlhosting.net',user='sql6706105',passwd='lsregtItpA',database='sql6706105')
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
w.mainloop()

# created by Prakhar Pande
