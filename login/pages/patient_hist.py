from tkinter import *
from ttkbootstrap.constants import *
from tkinter import PhotoImage
from ttkbootstrap.dialogs import Messagebox
from subprocess import call
import ttkbootstrap as tb
import mysql.connector as database


root = tb.Window(themename="darkly")
root.title("SAFETY HOSPITAL")
width = root.winfo_screenwidth()
heigth = root.winfo_screenheight()
root.geometry("{w}x{h}+0+0".format(w=width,h=heigth))
root.iconbitmap("images/logo.ico")

def backpage():
    root.destroy()
    call(["python","pages/entity.py"])

def refreshpage():
    root.destroy()
    call(["python","pages/patient_hist.py"])

def addpatient():
    root.destroy()
    call(["python","pages/patient_reg.py"])



#connection search
db = database.connect(host="localhost",user="root",password="",database="safety_hospital")
connection = db.cursor()


search = PhotoImage(file="icons/search.png")
refresh = PhotoImage(file="icons/refresh.png")
add = PhotoImage(file="icons/add.png")
arrowback = PhotoImage(file="icons/arrowback.png")
clean = PhotoImage(file="icons/clean.png")
print_ = PhotoImage(file="icons/print.png")
person = PhotoImage(file="images/person.png")


title_frame = Frame(root,bd=1,relief=GROOVE,height=30,background="#333")
title_frame.pack(side=TOP,fill=X)


title_lbl = tb.Label(title_frame,text=("SAFETY HOSPITAL SYSTEM MANAGEMENT / PATIENT HISTORIC"),font=("monaco",25))
title_lbl.pack(side=TOP)

frame_left = Frame(root,bd=1,relief=GROOVE)
frame_left.place(x=0,y=47,width=745,height=667)

frame_right = Frame(root,bd=1,relief=GROOVE)
frame_right.place(x=748,y=47,width=610,height=667)

frame_right_down = Frame(frame_right,bd=0)
frame_right_down.place(x=0,y=170,width=500,height=500)


frame_leght_table = Frame(frame_left,bd=2,relief=GROOVE)
frame_leght_table.place(x=0,y=40,width=742,height=622)

frame_leght_UP = tb.Frame(frame_left,bootstyle="secondary",height=38)
frame_leght_UP.pack(side=TOP,fill=X)

#==================================buttons=============================
add_ = tb.Button(frame_leght_UP,image=add,bootstyle="secondary",command=addpatient)
add_.grid(row=0,column=0,padx=5,pady=0)



refresh_ = tb.Button(frame_leght_UP,image=refresh,bootstyle="secondary",command=refreshpage)
refresh_.grid(row=0,column=2,padx=5,pady=0)

print__ = tb.Button(frame_leght_UP,image=print_,bootstyle="secondary",command=None)
print__.grid(row=0,column=3,padx=5,pady=0)

back = tb.Button(frame_leght_UP,image=arrowback,bootstyle="secondary",command=backpage)
back.place(x=300,y=0)

def clean_fields():
    rollno_.set("")
    name_.set("")
    lastname_.set("")
    sex_.set("")
    age_.set("")
    date_arrived_.set("")
    hour_arrived_.set("")
    blood_group_.set("")
    symptom_.set("")
    malady_.set("")
    cure_.set("")
    address_.set("")

clean_ = tb.Button(frame_leght_UP,image=clean,bootstyle="secondary",command=clean_fields)
clean_.grid(row=0,column=1,padx=5,pady=0)


#=============================name and lastname frame=====================
frame_name_lastname = Frame(frame_right,bd=1,relief=GROOVE,width=600,height=150)
frame_name_lastname.pack(side=TOP,fill=X)

personn_ = Label(frame_name_lastname,image=person)
personn_.place(x=250,y=0)

name_ =StringVar()
nameENTRY = tb.Label(frame_name_lastname,font=("monaco",18),bootstyle="white",textvariable=name_)
nameENTRY.place(x=150,y=115)

lastname_ = StringVar()
lastnameENTRY = tb.Label(frame_name_lastname,font=("monaco",18),bootstyle="white",textvariable=lastname_)
lastnameENTRY.place(x=390,y=115)

#================================================================
rollnoTXT = tb.Label(frame_right_down,text=("ROLLNO     :"),font=("monaco",15),bootstyle="#333")
rollnoTXT.grid(row=0,column=0,padx=10,pady=10)

rollno_ = StringVar()
rollnoENTRY = tb.Label(frame_right_down,font=("monaco",15),bootstyle="primary",textvariable=rollno_)
rollnoENTRY.grid(row=0,column=1,padx=3,pady=3)

sexTXT = tb.Label(frame_right_down,text=("SEX        :"),font=("monaco",15),bootstyle="#333")
sexTXT.grid(row=1,column=0,padx=10,pady=10)

sex_ = StringVar()
sexENTRY = tb.Label(frame_right_down,font=("monaco",15),bootstyle="primary",textvariable=sex_)
sexENTRY.grid(row=1,column=1,padx=3,pady=3)

ageTXT = tb.Label(frame_right_down,text=("AGE        :"),font=("monaco",15),bootstyle="#333")
ageTXT.grid(row=2,column=0,padx=10,pady=10)

age_ = StringVar()
ageENTRY = tb.Label(frame_right_down,font=("monaco",15),bootstyle="primary",textvariable=age_)
ageENTRY.grid(row=2,column=1,padx=3,pady=3)

date_arrivedTXT = tb.Label(frame_right_down,text=("DATE       :"),font=("monaco",15),bootstyle="#333")
date_arrivedTXT.grid(row=3,column=0,padx=10,pady=10)

date_arrived_ = StringVar()
date_arrivedENTRY = tb.Label(frame_right_down,font=("monaco",15),bootstyle="primary",textvariable=date_arrived_)
date_arrivedENTRY.grid(row=3,column=1,padx=3,pady=3)

hour_arrivedTXT = tb.Label(frame_right_down,text=("HOUR       :"),font=("monaco",15),bootstyle="#333")
hour_arrivedTXT.grid(row=4,column=0,padx=10,pady=10)

hour_arrived_ = StringVar()
hour_arrivedENTRY = tb.Label(frame_right_down,font=("monaco",15),bootstyle="primary",textvariable=hour_arrived_)
hour_arrivedENTRY.grid(row=4,column=1,padx=3,pady=3)

blood_groupTXT = tb.Label(frame_right_down,text=("BLOOD GROUP:"),font=("monaco",15),bootstyle="#333")
blood_groupTXT.grid(row=5,column=0,padx=10,pady=10)

blood_group_ = StringVar()
blood_groupENTRY = tb.Label(frame_right_down,font=("monaco",15),bootstyle="primary",textvariable=blood_group_)
blood_groupENTRY.grid(row=5,column=1,padx=3,pady=3)

symptomTXT = tb.Label(frame_right_down,text=("SYMTOM     :"),font=("monaco",15),bootstyle="#333")
symptomTXT.grid(row=6,column=0,padx=10,pady=10)

symptom_ = StringVar()
symtomENTRY = tb.Label(frame_right_down,font=("monaco",15),bootstyle="primary",textvariable=symptom_)
symtomENTRY.grid(row=6,column=1,padx=3,pady=3)

maladyTXT = tb.Label(frame_right_down,text=("SICKNESS   :"),font=("monaco",15),bootstyle="#333")
maladyTXT.grid(row=7,column=0,padx=10,pady=10)

malady_ = StringVar()
maladyENTRY = tb.Label(frame_right_down,font=("monaco",15),bootstyle="primary",textvariable=malady_)
maladyENTRY.grid(row=7,column=1,padx=3,pady=3)

cureTXT = tb.Label(frame_right_down,text=("CURE       :"),font=("monaco",15),bootstyle="#333")
cureTXT.grid(row=8,column=0,padx=10,pady=10)

cure_ = StringVar()
cureENTRY = tb.Label(frame_right_down,font=("monaco",15),bootstyle="primary",textvariable=cure_)
cureENTRY.grid(row=8,column=1,padx=3,pady=3)

addressTXT = tb.Label(frame_right_down,text=("ADDRESS    :"),font=("monaco",15),bootstyle="#333")
addressTXT.grid(row=9,column=0,padx=10,pady=10)

address_ = StringVar()
addressENTRY = tb.Label(frame_right_down,font=("monaco",15),bootstyle="primary",textvariable=address_)
addressENTRY.grid(row=9,column=1,padx=3,pady=3)


#=============================table==============================

table_frame = tb.Frame(frame_leght_table,bootstyle="secondary")
table_frame.pack(fill=BOTH,expand=True)


y_scroll = tb.Scrollbar(table_frame,orient=VERTICAL,bootstyle="#333 round")

table = tb.Treeview(table_frame,columns=(1,2,3,4,5,6,7,8,9,10,11,12),show="headings",yscrollcommand=y_scroll.set,bootstyle="secondary")

y_scroll.config(command=table.yview)
y_scroll.pack(side="right",fill=Y)


table.heading(1,text=("ROLLNO."))
table.heading(2,text=("NAME"))
table.heading(3,text=("LASTNAME"))
table.heading(4,text=("SEX"))
table.heading(5,text=("AGE"))
table.heading(6,text=("DATE ARRIVED"))
table.heading(7,text=("HOUR ARRIVED"))
table.heading(8,text=("BLOOD GROUP"))
table.heading(9,text=("SYMPTOMS"))
table.heading(10,text=("SICKNESS"))
table.heading(11,text=("CURE"))
table.heading(12,text=("ADDRESS"))

table.column(1,width=65,anchor="center")
table.column(2,width=150,anchor="center")
table.column(3,width=150,anchor="center")
table.column(4,width=50,anchor="center")
table.column(5,width=150,anchor="center")
table.column(6,width=150,anchor="center")
table.column(7,width=150,anchor="center")
table.column(8,width=100,anchor="center")
table.column(9,width=250,anchor="center")
table.column(10,width=150,anchor="center")
table.column(11,width=200,anchor="center")
table.column(12,width=200,anchor="center")

def search_button():
    for item in table.get_children():
        table.delete(item)
    val = searchENTRY.get()
    connection.execute("SELECT * FROM `patient` WHERE `name` LIKE %s or `lastname` like %s ",("%"+val+"%","%"+val+"%"))
    get_finding = connection.fetchall()
    for row in get_finding:
        table.insert("",END,values=row)


searchENTRY = tb.Entry(frame_leght_UP,font=("monaco",14),bootstyle="info")
searchENTRY.place(x=500,y=5)
searchbtn = tb.Button(frame_leght_UP,image=search,bootstyle="secondary",command=search_button,width=0)
searchbtn.place(x=450,y=0)


def get_cursor(e):
    cursor_row = table.focus()
    content = table.item(cursor_row)
    row = content["values"]
    rollno_.set(row[0])
    name_.set(row[1])
    lastname_.set(row[2])
    sex_.set(row[3])
    age_.set(row[4])
    date_arrived_.set(row[5])
    hour_arrived_.set(row[6])
    blood_group_.set(row[7])
    symptom_.set(row[8])
    malady_.set(row[9])
    cure_.set(row[10])
    address_.set(row[11])

table.bind("<ButtonRelease-1>",get_cursor)
table.pack(fill=BOTH,expand=True)



mysqlDB = database.connect(host="localhost",user="root",password="",database="safety_hospital")
meconnect = mysqlDB.cursor()


meconnect.execute("select * from patient")

for row in meconnect:
    table.insert("",END,values=row)

mysqlDB.close()





BottomFrameDetails = tb.Frame(root,height=100,bootstyle="dark")
BottomFrameDetails.pack(side=BOTTOM,fill=X)

copyr_ = tb.Button(BottomFrameDetails,text=("copyright(©) 2024"),bootstyle="dark")
copyr_.grid(row=0,column=0)

UnetCorporation = tb.Button(BottomFrameDetails,text=("®UNET CORPORATION"),bootstyle="dark")
UnetCorporation.place(x=600,y=0)

deter_okam = tb.Button(BottomFrameDetails,text=("deterokam@gmail.com"),bootstyle="dark")
deter_okam.place(x=1200,y=0)


root.mainloop()

