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
height = root.winfo_screenheight()
root.geometry("{w}x{h}+0+0".format(w=width,h=height))
root.iconbitmap("images/logo.ico")



#refresh button
def restart_page():
    root.destroy()
    call(["python","pages/patient_reg.py"])
#backpage button
def backpage():
    root.destroy()
    call(["python","pages/entity.py"])
#connection search
db = database.connect(host="localhost",user="root",password="",database="safety_hospital")
connection = db.cursor()

#=====================================ADD===================

def add():
    rollno = rollnoENTRY.get().upper()
    name = nameENTRY.get().upper()
    lastname = lastnameENTRY.get().upper()
    sex = sexENTRY.get().upper()
    age = ageENTRY.get().upper()
    date_arrived = date_arrivedENTRY.get().upper()
    hour_arrived = hour_arrivedENTRY.get().upper()
    blood_group = blood_groupENTRY.get().upper()
    symptom = symptomsENTRY.get().upper()
    malady = maladyENTRY.get().upper()
    cure = cureENTRY.get().upper()
    address = addressENTRY.get().upper()

    mysqlDB = database.connect(host="localhost",user="root",database="safety_hospital")
    meconnect = mysqlDB.cursor()

    try:
        sql = "INSERT into patient (rollno,name,lastname,sex,age,date_arrived,hour_arrived,blood_group,symptoms,sickness,cure,address)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        if(len(rollno)==0 or len(name)==0 or len(lastname)==0 or len(sex)==0 or len(age)==0 or len(date_arrived)==0 or len(hour_arrived)==0 or len(blood_group)==0 or len(symptom)==0 or len(malady)==0 or len(cure)==0 or len(address)==0):
            Messagebox.show_error("ALL FIELDS SHOULD BE REQUIRED !","SAFETY HOSPITAL")
        else:
            val=(rollno,name,lastname,sex,age,date_arrived,hour_arrived,blood_group,symptom,malady,cure,address)
            meconnect.execute(sql,val)
            mysqlDB.commit()
            Messagebox.show_info("ADD SUCESSFULY","SAFETY HOSPITAL")
            root.destroy()
            call(["python","pages/patient_reg.py"])
    except Exception as e:
        print(e)
        mysqlDB.rollback()
        mysqlDB.close()

#=====================================update===================
def update():
    rollno = rollnoENTRY.get().upper()
    name = nameENTRY.get().upper()
    lastname = lastnameENTRY.get().upper()
    sex = sexENTRY.get().upper()
    age = ageENTRY.get().upper()
    date_arrived = date_arrivedENTRY.get().upper()
    hour_arrived = hour_arrivedENTRY.get().upper()
    blood_group = blood_groupENTRY.get().upper()
    symptom = symptomsENTRY.get().upper()
    malady = maladyENTRY.get().upper()
    cure = cureENTRY.get().upper()
    address = addressENTRY.get().upper()

    mysqlDB = database.connect(host="localhost",user="root",password="",database="safety_hospital")
    meconnect = mysqlDB.cursor()

    try:
        sql = "update patient set name=%s,lastname=%s,sex=%s,age=%s,date_arrived=%s,hour_arrived=%s,blood_group=%s,symptoms=%s,sickness=%s,cure=%s,address=%s where rollno=%s"
        if(len(rollno)==0 or len(name)==0 or len(lastname)==0 or len(sex)==0 or len(age)==0 or len(date_arrived)==0 or len(hour_arrived)==0 or len(blood_group)==0 or len(symptom)==0 or len(malady)==0 or len(cure)==0 or len(address)==0):
            Messagebox.show_error("ALL FIELDS SHOULD BE REQUIRED !","SAFETY HOSPITAL")
        else:
            val=(rollno,name,lastname,sex,age,date_arrived,hour_arrived,blood_group,symptom,malady,cure,address)
            meconnect.execute(sql,val)
            mysqlDB.commit()
            Messagebox.show_info("ADD SUCESSFULY","SAFETY HOSPITAL")
            root.destroy()
            call(["python","pages/patient_reg.py"])
        
    except Exception as e:
        print(e)
        mysqlDB.rollback()
        mysqlDB.close()
#=====================================delete===================
def supp():
    rollno = rollnoENTRY.get()
    mysqlDB = database.connect(host="localhost",user="root",password="",database="safety_hospital")
    meconnect = mysqlDB.cursor()


    try:
        sql = "delete from patient where rollno = %s"
        val  = (rollno,)
        meconnect.execute(sql,val)
        mysqlDB.commit()
        Messagebox.show_warning("DELETE DATA SUCCESSFULY","SAFETY HOSPITAL")
        root.destroy()
        call(["python","pages/patient_reg.py"])
    except Exception as e:
        print(e)
        mysqlDB.rollback()
        mysqlDB.close()







#=========================icons =======================


reg = PhotoImage(file="icons/reg.png")
edit = PhotoImage(file="icons/edit.png")
delete = PhotoImage(file="icons/delete.png")
clean = PhotoImage(file="icons/clean.png")
arrowback = PhotoImage(file="icons/arrowback.png")
print__ = PhotoImage(file="icons/print.png")
search = PhotoImage(file="icons/search.png")
refresh = PhotoImage(file="icons/refresh.png")


title_frame = Frame(root,bd=1,relief=GROOVE,height=30,background="#333")
title_frame.pack(side=TOP,fill=X)

titlelbl = tb.Label(title_frame,text=("SAFETY HOSPITAL SYSTEM MANAGEMENT/ PATIENT REGISTRACTION"),font=("monaco",25))
titlelbl.pack(side=TOP)

frame_left = tb.Frame(root,bootstyle="#333")
frame_left.place(x=0,y=47,width=405,height=667)



frame_rigth = tb.Frame(root,bootstyle="dark")
frame_rigth.place(x=410,y=47,width=950,height=667)

frame_rigth_UP = tb.Frame(frame_rigth,bootstyle="secondary",height=38)
frame_rigth_UP.pack(side=TOP,fill=X)

frame_rigth_table = tb.Frame(frame_rigth,bootstyle="secondary")
frame_rigth_table.place(x=0,y=45,width=950,height=622)

#=======================field place=========================
rollnoTXT = tb.Label(frame_left,text=("ROLLNO"),font=("monaco",15),bootstyle="#333")
rollnoTXT.grid(row=0,column=0,padx=0,pady=10)

rollno_ = StringVar()
rollnoENTRY = tb.Entry(frame_left,font=("monaco",15),bootstyle="secondary",textvariable=rollno_)
rollnoENTRY.grid(row=0,column=1,padx=0,pady=10)


nameTXT = tb.Label(frame_left,text=("NAME"),font=("monaco",15),bootstyle="#333")
nameTXT.grid(row=1,column=0,padx=0,pady=10)

name_ = StringVar()
nameENTRY = tb.Entry(frame_left,font=("monaco",15),bootstyle="secondary",textvariable=name_)
nameENTRY.grid(row=1,column=1,padx=0,pady=10)

lastnameTXT = tb.Label(frame_left,text=("LASTNAME"),font=("monaco",15),bootstyle="#333",)
lastnameTXT.grid(row=2,column=0,padx=0,pady=10)

lastname_ = StringVar()
lastnameENTRY = tb.Entry(frame_left,font=("monaco",15),bootstyle="secondary",textvariable=lastname_)
lastnameENTRY.grid(row=2,column=1,padx=0,pady=10)

sexTXT = tb.Label(frame_left,text=("SEX"),font=("monaco",15),bootstyle="#333")
sexTXT.grid(row=3,column=0,padx=0,pady=10)

sex_ = StringVar()
data = ["M","F"]
sexENTRY = tb.Combobox(frame_left,font=("monaco",15),bootstyle="secondary",values=data,width=19,textvariable=sex_)
sexENTRY.grid(row=3,column=1,padx=0,pady=10)

ageTXT = tb.Label(frame_left,text=("AGE"),font=("monaco",15),bootstyle="#333")
ageTXT.grid(row=4,column=0,padx=0,pady=10)

age_ = StringVar()
ageENTRY = tb.Entry(frame_left,font=("monaco",15),bootstyle="secondary",textvariable=age_)
ageENTRY.grid(row=4,column=1,padx=0,pady=10)

date_arrived_TXT = tb.Label(frame_left,text=("DATE ARRIVED"),font=("monaco",15),bootstyle="#333")
date_arrived_TXT.grid(row=5,column=0,padx=1,pady=10)

date_arrived_ = StringVar()
date_arrivedENTRY = tb.Entry(frame_left,font=("monaco",15),bootstyle="secondary",textvariable=date_arrived_)
date_arrivedENTRY.grid(row=5,column=1,padx=0,pady=10)

hour_arrived_TXT = tb.Label(frame_left,text=("HOUR ARRIVED"),font=("monaco",15),bootstyle="#333")
hour_arrived_TXT.grid(row=6,column=0,padx=0,pady=10)

hour_arrived_ = StringVar()
hour_arrivedENTRY = tb.Entry(frame_left,font=("monaco",15),bootstyle="secondary",textvariable=hour_arrived_)
hour_arrivedENTRY.grid(row=6,column=1,padx=0,pady=10)

blood_groupTXT = tb.Label(frame_left,text=("BLOOD GROUP"),font=("monaco",15),bootstyle="#333")
blood_groupTXT.grid(row=7,column=0,padx=0,pady=10)

blood_group_ = StringVar()
data = ["A","A-","B","B+"]
blood_groupENTRY = tb.Combobox(frame_left,font=("monaco",15),values=data,width=19,bootstyle="secondary",textvariable=blood_group_)
blood_groupENTRY.grid(row=7,column=1,padx=0,pady=10)

symptomsTXT = tb.Label(frame_left,text=("SYMPTOMS"),font=("monaco",15),bootstyle="#333")
symptomsTXT.grid(row=8,column=0,padx=0,pady=10)

symptoms_ = StringVar()
symptomsENTRY = tb.Entry(frame_left,font=("monaco",15),bootstyle="secondary",textvariable=symptoms_)
symptomsENTRY.grid(row=8,column=1,padx=0,pady=10)

maladyTXT = tb.Label(frame_left,text=("SICKNESS"),font=("monaco",15),bootstyle="#333")
maladyTXT.grid(row=9,column=0,padx=0,pady=10)

malady_ = StringVar()
maladyENTRY = tb.Entry(frame_left,font=("monaco",15),bootstyle="secondary",textvariable=malady_)
maladyENTRY.grid(row=9,column=1,padx=0,pady=10)

cureTXT = tb.Label(frame_left,text=("CURE"),font=("monaco",15),bootstyle="#333")
cureTXT.grid(row=10,column=0,padx=0,pady=10)

cure_ = StringVar()
cureENTRY = tb.Entry(frame_left,font=("monaco",15),bootstyle="secondary",textvariable=cure_)
cureENTRY.grid(row=10,column=1,padx=0,pady=10)

addressTXT = tb.Label(frame_left,text=("ADDRESS"),font=("monaco",15),bootstyle="#333")
addressTXT.grid(row=11,column=0,padx=0,pady=10)

address_ = StringVar()
addressENTRY = tb.Entry(frame_left,font=("monaco",15),bootstyle="secondary",textvariable=address_)
addressENTRY.grid(row=11,column=1,padx=0,pady=10)
#====================================icons table frame up bar===========================
reg_ = tb.Button(frame_rigth_UP,image=reg,bootstyle="secondary",command=add,width=0)
reg_.grid(row=0,column=0,padx=5,pady=0)

edit_ = tb.Button(frame_rigth_UP,image=edit,bootstyle="secondary",command=update)
edit_.grid(row=0,column=2,padx=5,pady=0)

delete_ = tb.Button(frame_rigth_UP,image=delete,bootstyle="secondary",command=supp)
delete_.grid(row=0,column=4,padx=5,pady=0)


print_ = tb.Button(frame_rigth_UP,image=print__,bootstyle="secondary",command=None)
print_.grid(row=0,column=6,padx=5,pady=0)

refresh_ = tb.Button(frame_rigth_UP,image=refresh,bootstyle="secondary",command=restart_page)
refresh_.place(x=430,y=0)

arrowback_ = tb.Button(frame_rigth_UP,image=arrowback,bootstyle="secondary",command=backpage)
arrowback_.place(x=500,y=0)

def clean_fields():
    rollno_.set("")
    name_.set("")
    lastname_.set("")
    sex_.set("")
    age_.set("")
    date_arrived_.set("")
    hour_arrived_.set("")
    blood_group_.set("")
    symptoms_.set("")
    malady_.set("")
    cure_.set("")
    address_.set("")

clean_ = tb.Button(frame_rigth_UP,image=clean,bootstyle="secondary",command=clean_fields)
clean_.grid(row=0,column=5,padx=5,pady=0)


#=========================================table party==================================
table_frame = tb.Frame(frame_rigth_table,bootstyle="secondary")
table_frame.pack(fill=BOTH,expand=True)

y_scroll = tb.Scrollbar(table_frame,orient=VERTICAL,bootstyle="#333 round")
x_scroll = tb.Scrollbar(table_frame,orient=HORIZONTAL,bootstyle="#333 round")

table = tb.Treeview(table_frame,columns=(1,2,3,4,5,6,7,8,9,10,11,12),show="headings",yscrollcommand=y_scroll.set,xscrollcommand=x_scroll.set)

y_scroll.config(command=table.yview)
x_scroll.config(command=table.xview)

y_scroll.pack(side="right",fill=Y)
x_scroll.pack(side="bottom",fill=X)


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


searchENTRY = tb.Entry(frame_rigth_UP,font=("monaco",14),bootstyle="info")
searchENTRY.place(x=710,y=5)
searchbtn = tb.Button(frame_rigth_UP,image=search,bootstyle="secondary",command=search_button,width=0)
searchbtn.place(x=660,y=0)

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
    symptoms_.set(row[8])
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