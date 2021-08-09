from tkinter import *
from PIL import Image, ImageTk
import tkinter.messagebox as tmsg
import tkinter.font


def confirm():
    import time
    value_1=root_log_entry1.get()
    print(value_1)
    value_2=root_log_entry2.get()
    print(value_2)

    if (str(value_1) == "Dev_115639") and (str(value_2) == '********'):
        def main_window():
            root_main = Toplevel();
            root_main.wm_iconbitmap("new_bg.ico")
            root_main.title("KEEP ORGANIZATION PROTOCOL")
            width_root_main= root_main.winfo_screenwidth()
            height_root_main=root_main.winfo_screenheight()
            root_main.geometry("%dx%d+0+0" % (width_root_main,height_root_main))
            root_main.maxsize(1366,768)
            root_main.config(background="black")

            def entr_val():

                top1=Toplevel()
                top1.wm_iconbitmap("new_bg.ico")
                top1.title("Directory Folder")
                top1.geometry("600x200")
                top1.maxsize(1366,768)
                top1.config(background="black")
                uservalue=StringVar()
                user_entry=Entry(top1,text = uservalue)
                user_entry.grid(row=0,column=0,columnspan=2)
                search_top1=Button(top1,text="Search")
                search_top1.grid(row=1,column=0)
                exit_top1=Button(top1,text="Exit",command=top1.destroy)
                exit_top1.grid(row=1,column=1)
                if uservalue.get()=="raja":
                    print("vah")
                else:
                    pass
            
            def record_fun():

                def search_fun(uservalue):
                    val = uservalue.get()
                    if  str(val) =="Praney Kumar":
                        top2=Toplevel()
                        top2.wm_iconbitmap("new_bg.ico")
                        top2.title(">RECORD :- Praney Kumar")
                        top2.geometry("600x500+415+180")
                        top2.maxsize(1366,768)
                        top2.config(background="black")
                        
                        photo_pr = PhotoImage(file="images/PRANEY KUMAR (Book Store).png");
                        b1_img_lbl=Label(top2,image = photo_pr,bg="black");
                        b1_img_lbl.grid(row=0,column=0);
                        top2.mainloop()

                    elif str(val) =="Ajay Yadav":
                        top3=Toplevel()
                        top3.wm_iconbitmap("new_bg.ico")
                        top3.title(">RECORD :- Ajay Yadav")
                        top3.geometry("600x500+415+180")
                        top3.maxsize(1366,768)
                        top3.config(background="black")
                        
                        photo_pr = PhotoImage(file="images/AJAY YADAV( Car Blast).png");
                        b1_img_lbl=Label(top3,image = photo_pr,bg="black");
                        b1_img_lbl.grid(row=0,column=0);
                        top2.mainloop()

                    elif str(val) =="Aditya Singh":
                        top3=Toplevel()
                        top3.wm_iconbitmap("new_bg.ico")
                        top3.title(">RECORD :- Aditya Singh")
                        top3.geometry("600x500+415+180")
                        top3.maxsize(1366,768)
                        top3.config(background="black")
                        
                        photo_pr = PhotoImage(file="images/Aditya_Singh.png");
                        b1_img_lbl=Label(top3,image = photo_pr,bg="black");
                        b1_img_lbl.grid(row=0,column=0);
                        top2.mainloop()

                    elif str(val) =="Anshika Singhal":
                        top3=Toplevel()
                        top3.wm_iconbitmap("new_bg.ico")
                        top3.title(">RECORD :- Anshika Singhal")
                        top3.geometry("600x500+415+180")
                        top3.maxsize(1366,768)
                        top3.config(background="black")
                        
                        photo_pr = PhotoImage(file="images/AKANSHA medical (MAll Blast).png");
                        b1_img_lbl=Label(top3,image = photo_pr,bg="black");
                        b1_img_lbl.grid(row=0,column=0);
                        top2.mainloop()

                    else:
                        print("else executed")
                        root_srch = Toplevel();
                        root_srch.wm_iconbitmap("new_bg.ico")
                        root_srch.title(">>RECORD STATUS")
                        root_srch.geometry("300x100+560+280")
                        root_srch.maxsize(1366,768)
                        root_srch.config(background="black")
                        root_srch_lbl = Label(root_srch,time.sleep(1),text="NO RECORD FOUND",fg="red",bg="black",font="oxygen 20 bold")
                        root_srch_lbl.pack(pady=10)
                
                        root_srch.mainloop()
                        


                top1=Toplevel()
                top1.wm_iconbitmap("new_bg.ico")
                top1.title(">RECORD FOLDER")
                top1.geometry("600x100+380+220")
                top1.maxsize(1366,768)
                top1.config(background="black")
                f_top1 =Frame(top1,bg="black",borderwidth=2,relief=SUNKEN)
                f_top1.grid(padx=130)

                #photo1 = PhotoImage(file="images/Toko.png");
                #b1_img_lbl=Label(f_top1,image = photo1,bg="black");
                #b1_img_lbl.grid(row=0,column=0,rowspan=2);

                uservalue=StringVar()
                user_entry=Entry(f_top1,text = uservalue,fg="lime",bg="black",font="Monaco 20 bold")
                user_entry.grid(row=0,column=2,columnspan=2)

                search_top1=Button(f_top1,text="Search",fg="lime",bg="black",font="Monaco 10 bold",command=lambda: search_fun(uservalue))
                search_top1.grid(row=1,column=2)
                exit_top1=Button(f_top1,text="Exit",fg="lime",bg="black",font="Monaco 10 bold",command=top1.destroy)
                exit_top1.grid(row=1,column=3)

            def alert_box():
                top_alert=Toplevel()
                top_alert.wm_iconbitmap("new_bg.ico")
                top_alert.title(">ALERTS")
                top_alert.geometry("400x300+420+220")
                top_alert.maxsize(1366,768)
                top_alert.config(background="black")

                def open7():
                    top_open1=Toplevel()
                    top_open1.wm_iconbitmap("new_bg.ico")
                    top_open1.title(">2020-09-30 IST  09:30")
                    top_open1.geometry("470x200+520+200")
                    top_open1.maxsize(1366,768)
                    top_open1.config(background="black")

                    def address():
                        top_open2=Toplevel()
                        top_open2.wm_iconbitmap("new_bg.ico")
                        top_open2.title(">Use upload IST  time")
                        top_open2.geometry("900x390+100+150")
                        top_open2.maxsize(1366,768)
                        top_open2.config(background="black")

                        frm_21 = Frame(top_open2,borderwidth=2,relief=SUNKEN,bg="black")
                        frm_21.grid(row=0,column=0,rowspan=2,columnspan=3)
                        #btnmm=Button(top_open2,text="kala",fg="lime",bg="black",font="Monaco 12 bold")
                        #btnmm.grid(row=0,column=0)

                        #1st frame in Mainframe
                        frm_21a=Frame(frm_21,borderwidth=2,relief=SUNKEN,bg="black")
                        frm_21a.grid(row=0,column=0)

                        lbl5 = Label(frm_21a,text="Map",fg="lime",bg="black",font="Monaco 12 bold")
                        lbl5.grid(row=0,column=0)
                        photo = PhotoImage(file="images/world map.png");
                        b_img_lbl=Label(frm_21a,image = photo,bg="black");
                        b_img_lbl.grid(row=1,column=0);

                        #2nd frame in Mainframe
                        frm_21b=Frame(frm_21,borderwidth=2,relief=SUNKEN,bg="black")
                        frm_21b.grid(row=0,column=1,columnspan=2)

                        frm_3 = Frame(frm_21b,borderwidth=2,relief=SUNKEN,bg="black")
                        frm_3.grid(row=0,column=0,padx=5)
                        lbl6=Label(frm_3,text="Addresses ",fg="lime",bg="black",font="Monaco 12 bold")
                        lbl6.grid(row=0,column=0)
                        lbl7 = Label(frm_3,text="  Location",fg="lime",bg="black",font="Monaco 12 bold")
                        lbl7.grid(row=0,column=1)

                        frm_31 = Frame(frm_21b,borderwidth=2,relief=SUNKEN,bg="black")
                        frm_31.grid(row=1,column=0)

                        btn_1=Button(frm_31,text="128.35.658",fg="lime",bg="black",font="Monaco 12 bold")
                        btn_1.grid(row=0,column=0)
                        btn_1a=Button(frm_31,text="India",fg="lime",bg="black",font="Monaco 12 bold")
                        btn_1a.grid(row=0,column=1,ipadx=20)
                        btn_1=Button(frm_31,text="128.56.582",fg="lime",bg="black",font="Monaco 12 bold")
                        btn_1.grid(row=1,column=0)
                        btn_1a=Button(frm_31,text="Japan",fg="lime",bg="black",font="Monaco 12 bold")
                        btn_1a.grid(row=1,column=1,ipadx=18)
                        btn_1=Button(frm_31,text="125.69.487",fg="lime",bg="black",font="Monaco 12 bold")
                        btn_1.grid(row=2,column=0)
                        btn_1a=Button(frm_31,text="Brazil",fg="lime",bg="black",font="Monaco 12 bold")
                        btn_1a.grid(row=2,column=1,ipadx=18)
                        btn_1=Button(frm_31,text="128.48.587",fg="lime",bg="black",font="Monaco 12 bold")
                        btn_1.grid(row=3,column=0)
                        btn_1a=Button(frm_31,text="Australia",fg="lime",bg="black",font="Monaco 12 bold")
                        btn_1a.grid(row=3,column=1,ipadx=4)
                        btn_1=Button(frm_31,text="131.56.874",fg="lime",bg="black",font="Monaco 12 bold")
                        btn_1.grid(row=4,column=0)
                        btn_1a=Button(frm_31,text="Masagascar",fg="lime",bg="black",font="Monaco 12 bold")
                        btn_1a.grid(row=4,column=1)
                        btn_1=Button(frm_31,text="144.58.669",fg="lime",bg="black",font="Monaco 12 bold")
                        btn_1.grid(row=5,column=0)
                        btn_1a=Button(frm_31,text="Mexico",fg="lime",bg="black",font="Monaco 12 bold")
                        btn_1a.grid(row=5,column=1,ipadx=17)
                        btn_1=Button(frm_31,text="151.55.336",fg="lime",bg="black",font="Monaco 12 bold")
                        btn_1.grid(row=6,column=0)
                        btn_1a=Button(frm_31,text="Greenland",fg="lime",bg="black",font="Monaco 12 bold")
                        btn_1a.grid(row=6,column=1,ipadx=0)
                        btn_1=Button(frm_31,text="784.59.787",fg="lime",bg="black",font="Monaco 12 bold")
                        btn_1.grid(row=7,column=0)
                        btn_1a=Button(frm_31,text="Peru",fg="lime",bg="black",font="Monaco 12 bold")
                        btn_1a.grid(row=7,column=1,ipadx=23)
                        btn_1=Button(frm_31,text="101.65.574",fg="lime",bg="black",font="Monaco 12 bold")
                        btn_1.grid(row=8,column=0)
                        btn_1a=Button(frm_31,text="Morocco",fg="lime",bg="black",font="Monaco 12 bold")
                        btn_1a.grid(row=8,column=1,ipadx=15)
                        btn_1=Button(frm_31,text="747.84.556",fg="lime",bg="black",font="Monaco 12 bold")
                        btn_1.grid(row=9,column=0)
                        btn_1a=Button(frm_31,text="Italy",fg="lime",bg="black",font="Monaco 12 bold")
                        btn_1a.grid(row=9,column=1,ipadx=20)
                        btn_1=Button(frm_31,text="112.56.112",fg="lime",bg="black",font="Monaco 12 bold")
                        btn_1.grid(row=10,column=0)
                        btn_1a=Button(frm_31,text="China",fg="lime",bg="black",font="Monaco 12 bold")
                        btn_1a.grid(row=10,column=1,ipadx=20)



                        

                        top_open2.mainloop()



                    frm1 = LabelFrame(top_open1,text="Details",borderwidth=2,fg="lime",bg="black",font="Monaco 12 bold")
                    frm1.grid(row=0,column=0,ipadx=35,padx=10)
                    lbl3=Label(frm1,text="  Message:              From:          More:",fg="lime",bg="black",font="Monaco 12 bold")
                    lbl3.grid(row=1,column=0,columnspan=3)
                    lbl2 = Label(frm1,text="Ek Awaj or Jaldi he Garmi \n me Ugta suraj dikhai dega",fg="lime",bg="black",font="Monaco 12 bold")
                    lbl2.grid(row=2,column=0)
                    lbl2_1 = Label(frm1,text=" No. 989758",fg="Red",bg="black",font="Monaco 12 bold")
                    lbl2_1.grid(row=2,column=1)
                    btn11=Button(frm1,text="...",fg="lime",bg="black",font="Monaco 12 bold",command=address)
                    btn11.grid(row=2,column=2)


                    top_open1.mainloop()
                    

                f_top_alert =Frame(top_alert,bg="black",borderwidth=2,relief=SUNKEN)
                f_top_alert.grid(row=0,column=0,columnspan=2)
                msg_labl = Label(f_top_alert,text="Messages >",fg="lime",bg="black",font="Monaco 15 bold")
                msg_labl.grid(ipadx=140)
                
                #mainFrame for below frames
                man_frame = Frame(top_alert,bg="black",borderwidth=2,relief=SUNKEN)
                man_frame.grid(row=1,column=0)
            
                #Frame F1
                f1_top_alert =Frame(man_frame,bg="black",borderwidth=2,relief=SUNKEN)
                f1_top_alert.grid(row=0,column=0)
                
                msg_labl = Label(f1_top_alert,text="2020-01-15 IST  19:18",fg="lime",bg="black",font="Monaco 15 bold")
                msg_labl.grid(row=0,column=0,padx=20)
                f1_btn = Button(f1_top_alert,text="OPEN",fg="lime",bg="black",font="Monaco 12 bold")
                f1_btn.grid(row=0,column=1,padx=0)

                #Frame F2
                f2_top_alert =Frame(man_frame,bg="black",borderwidth=2,relief=SUNKEN)
                f2_top_alert.grid(row=1,column=0)

                msg_labl = Label(f2_top_alert,text="2020-02-18 IST  01:03",fg="lime",bg="black",font="Monaco 15 bold")
                msg_labl.grid(row=0,column=0,padx=20)
                f2_btn = Button(f2_top_alert,text="OPEN",fg="lime",bg="black",font="Monaco 12 bold")
                f2_btn.grid(row=0,column=1)

                #Frame F3
                f3_top_alert =Frame(man_frame,bg="black",borderwidth=2,relief=SUNKEN)
                f3_top_alert.grid(row=2,column=0)

                msg_labl = Label(f3_top_alert,text="2020-02-20 IST  03:03",fg="lime",bg="black",font="Monaco 15 bold")
                msg_labl.grid(row=0,column=0,padx=20)
                f1_btn = Button(f3_top_alert,text="OPEN",fg="lime",bg="black",font="Monaco 12 bold")
                f1_btn.grid(row=0,column=1)

                #Frame F4
                f4_top_alert =Frame(man_frame,bg="black",borderwidth=2,relief=SUNKEN)
                f4_top_alert.grid(row=3,column=0)

                msg_labl = Label(f4_top_alert,text="2020-03-30 IST  12:03",fg="lime",bg="black",font="Monaco 15 bold")
                msg_labl.grid(row=0,column=0,padx=20)
                f1_btn = Button(f4_top_alert,text="OPEN",fg="lime",bg="black",font="Monaco 12 bold")
                f1_btn.grid(row=0,column=1)

                #Frame F5
                f5_top_alert =Frame(man_frame,bg="black",borderwidth=2,relief=SUNKEN)
                f5_top_alert.grid(row=4,column=0)

                msg_labl = Label(f5_top_alert,text="2020-05-30 IST  22:03",fg="lime",bg="black",font="Monaco 15 bold")
                msg_labl.grid(row=0,column=0,padx=20)
                f1_btn = Button(f5_top_alert,text="OPEN",fg="lime",bg="black",font="Monaco 12 bold")
                f1_btn.grid(row=0,column=1)

                #Frame F6
                f6_top_alert =Frame(man_frame,bg="black",borderwidth=2,relief=SUNKEN)
                f6_top_alert.grid(row=5,column=0)

                msg_labl = Label(f6_top_alert,text="2020-07-30 IST  16:25",fg="lime",bg="black",font="Monaco 15 bold")
                msg_labl.grid(row=0,column=0,padx=20)
                f1_btn = Button(f6_top_alert,text="OPEN",fg="lime",bg="black",font="Monaco 12 bold")
                f1_btn.grid(row=0,column=1)
                #scrl.config(command=man_frame.yview)

                #Frame F7
                f7_top_alert =Frame(man_frame,bg="black",borderwidth=2,relief=SUNKEN)
                f7_top_alert.grid(row=6,column=0)

                msg_labl = Label(f7_top_alert,text="2020-09-30 IST  09:30",fg="Blue",bg="black",font="Monaco 15 bold")
                msg_labl.grid(row=0,column=0,padx=20)
                f1_btn = Button(f7_top_alert,text="OPEN",fg="Red",bg="black",font="Monaco 12 bold",command=open7)
                f1_btn.grid(row=0,column=1)
                #scrl.config(command=man_frame.yview)

                top_alert.mainloop()


            #Top Frame
            f1=Frame(root_main,borderwidth=5,relief=RAISED,bg="black")
            f1.grid(row=0,column=0,columnspan=3);
            #Left Frame
            f2=Frame(root_main,borderwidth=5,relief=RAISED,bg="black")
            f2.grid(row=1,column=0,ipadx=20);
            photo1 = PhotoImage(file="images/left.png");
            b_img_lbl=Label(f2,image = photo1,bg="black");
            b_img_lbl.grid(row=0,column=0);
            #Middle Frame
            f3=Frame(root_main,borderwidth=1,relief=RAISED,bg="black")
            f3.grid(row=1,column=1,ipadx=20);
            txtarea = Text(f3,fg="lime",bg="black",font="Monaco 11 bold")
            txtarea.grid(row=0,column=0)
            file=None
            #Right Frame
            #f4=Frame(root_main,borderwidth=5,relief=RAISED,bg="black")
            #f4.grid(row=1,column=2);
            #photo2 = PhotoImage(file="images/left.png");
            #b_img_lbl=Label(f4,image = photo2,bg="black");
            #b_img_lbl.grid(row=0,column=0);
            #bottom Frame
            f6=Frame(root_main,borderwidth=5,relief=RAISED,bg="black")
            f6.grid(row=2,column=1);
            photo3 = PhotoImage(file="images/bottom.png");
            b_img_lbl=Label(f6,image = photo3,bg="black",height=200,width=750);
            b_img_lbl.grid(row=0,column=0);

            photo4 = PhotoImage(file="images/bottom_left.png");
            b_img_lbl=Label(root_main,image = photo4,bg="black");
            b_img_lbl.grid(row=2,column=0);

            photo5 = PhotoImage(file="images/bottom_right.png");
            b_img_lbl=Label(root_main,image = photo5,bg="black");
            b_img_lbl.grid(row=2,column=2);

            #f7=Frame(root_main,borderwidth=5,relief=RAISED,bg="black")
            #f7.grid(row=1,column=5);
            #bt2=Button(f7,text="DIRECTORY >",fg="lime",bg="black",font="oxygen 15 bold")
            #bt2.grid(row=0,column=0)

            photo = PhotoImage(file="icons/ten.png");
            b_img_lbl=Label(f1,image = photo,bg="black");
            b_img_lbl.grid(row=0,column=0,padx=50);

            bt1=Button(f1,text="DIRECTORY >",fg="lime",bg="black",font="oxygen 15 bold")
            bt1.grid(row=0,column=1,padx=0)

            bt2=Button(f1,text="RECORD LIST >",fg="lime",bg="black",font="oxygen 15 bold",command=record_fun)
            bt2.grid(row=0,column=2,padx=0);

            bt3=Button(f1,text="TRACK >",fg="lime",bg="black",font="oxygen 15 bold")
            bt3.grid(row=0,column=3,padx=0);

            bt4=Button(f1,text="SETTINGS >",fg="lime",bg="black",font="oxygen 15 bold")
            bt4.grid(row=0,column=4,padx=0);

            bt5=Button(f1,text="ALERTS >",fg="lime",bg="black",font="oxygen 15 bold",command=alert_box)
            bt5.grid(row=0,column=5,padx=0);

            bt6=Button(f1,text="HELP >",fg="lime",bg="black",font="oxygen 15 bold")
            bt6.grid(row=0,column=6,padx=0);

            bt7=Button(f1,text="WINDOW >",fg="lime",bg="black",font="oxygen 15 bold")
            bt7.grid(row=0,column=7,padx=0);

            bt7=Button(f1,text="SETTINGS >",fg="lime",bg="black",font="oxygen 15 bold")
            bt7.grid(row=0,column=8,padx=0);

            bt7=Button(f1,text="EXIT >",fg="lime",bg="black",font="oxygen 15 bold",command=quit)
            bt7.grid(row=0,column=9,padx=0);

            root_main.mainloop()
            

        root_enter =Toplevel()
        root_enter.wm_iconbitmap("new_bg.ico")
        root_enter.title("Status")
        root_enter.geometry("280x200+550+250")
        root_enter.maxsize(800,400)
        root_enter.config(background="black")
        root_enter_l1 = Label(root_enter,text="IDENTITY CONFIRMED",font="Corbel 15 bold ",bg="black",fg="lime")
        root_enter_l1.grid(row=0,column=0,pady=(40,0),padx=(35,0))
        root_enter_l1 = Label(root_enter,text=value_1,font="Corbel 20 bold ",bg="black",fg="lime")
        root_enter_l1.grid(row=1,column=0,pady=(10,0),padx=(20,0))
        time.sleep(0.5)
        root_enter_b1 = Button(root_enter,text="ENTER",font="Monaco 10 bold",bg="black",fg="lime",command=main_window)
        root_enter_b1.grid(row=2,column=0,ipadx=20,pady=10,ipady=7,padx=(8,0))

    else:
        root_enter =Toplevel()
        root_enter.wm_iconbitmap("new_bg.ico")
        root_enter.title("Status")
        root_enter.geometry("250x150+550+250")
        root_enter.maxsize(800,400)
        root_enter.config(background="black")
        root_enter_l2 = Label(root_enter,text="INCORRECT USER \n 3 Trail Left",font="Corbel 15 bold ",bg="black",fg="lime")
        root_enter_l2.grid(row=0,column=0,pady=(40,0),padx=(35,0))
 
root_log=Tk()
root_log.wm_iconbitmap("new_bg.ico")
root_log.title("KOP-LOGIN")
root_log.geometry("550x300+400+200")
root_log.maxsize(800,400)
root_log.config(background="black")
def e1_hover(e):
    root_log_entry1["bg"] ="dimgrey"
def e1_leave(e):
    root_log_entry1["bg"] = "black"
def e2_hover(e):
    root_log_entry2["bg"] ="dimgrey"
def e2_leave(e):
    root_log_entry2["bg"] = "black"

root_log_label1 = Label(root_log,text="Username",font="Corbel 15 bold ",bg="black",fg="lime")
root_log_label1.grid(row=0,column=0,pady=(20,0),padx=(25,0))
root_log_entry1=Entry(root_log,font="Monaco 20 bold",bg="black",fg="lime")
root_log_entry1.grid(row=0,column=1,columnspan=3,pady=(20,0),padx=10)
root_log_entry1.bind("<Enter>",e1_hover)
root_log_entry1.bind("<Leave>",e1_leave)

root_log_label2 = Label(root_log,text="Password",font="Corbel 15 bold ",bg="black",fg="lime")
root_log_label2.grid(row=1,column=0,pady=10,padx=(25,0))
root_log_entry2=Entry(root_log,font="Monaco 20 bold",bg="black",fg="lime")
root_log_entry2.grid(row=1,column=1,columnspan=3,pady=10,padx=10)
root_log_entry2.bind("<Enter>",e2_hover)
root_log_entry2.bind("<Leave>",e2_leave)


root_log_b1 = Button(root_log,text="Log-In",font="Monaco 10 bold",bg="black",fg="lime",command=confirm)
root_log_b1.grid(row=2,column=1,ipadx=20,pady=10,ipady=7)
root_log_b2 = Button(root_log,text="Cancel",font="Monaco 10 bold",bg="black",fg="lime",command=quit)
root_log_b2.grid(row=2,column=3,ipadx=20,pady=10,ipady=7)

root_log_label = Label(root_log,text="OR",font="Monaco 12 bold underline",bg="black",fg="lime")
root_log_label.grid(row=3,column=2,pady=10)

root_log_b2 = Button(root_log,text="Scan Eye To\nConfirm ID",font="Monaco 11 bold",bg="black",fg="lime",command=confirm)
root_log_b2.grid(row=4,column=2,pady=10)


root_log.mainloop()