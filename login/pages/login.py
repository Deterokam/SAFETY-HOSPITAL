import customtkinter as ctk
from PIL import Image
from tkinter import PhotoImage
from tkinter import messagebox
from subprocess import call



root = ctk.CTk()
root.title("SAFETY HOSPITAL")
width = root.winfo_screenwidth()
heigth = root.winfo_screenheight()
root.geometry("{w}x{h}+0+0".format(w=width,h=heigth))
root.iconbitmap("images/logo.ico")

def connection():
    adm = admin_name.get()
    pwd = password.get()

    if adm == "" and  pwd == "":
        messagebox.showerror("SAFETY HOSPTAL","the fields is empty")
    elif adm == "admin" and pwd == "admin":
        messagebox.showinfo("SAFETY HOSPITAL","Welcom to SAFETY HOSPITAL")
        admin_name.delete("0","end")
        password.delete("0","end")
        root.destroy()
        call(["python","pages/welcom.py"])
    else:
        messagebox.showwarning("SAFETY HOSPITAL","The request is incorect try again")
        admin_name.delete("0","end")
        password.delete("0","end")

maintitle = ctk.CTkFrame(root,width=width,height=50,border_width=2,border_color="#333",corner_radius=10)
maintitle.pack(side="top",fill="x")

titlelbl = ctk.CTkLabel(maintitle,text="SAFETY HOSPITAL SYSTEM MANAGEMENT",font=("monaco",25),text_color="white")
titlelbl.pack(side="top",pady=5)


mainframe = ctk.CTkFrame(root,width=450,height=370,border_width=2,border_color="#333",corner_radius=10)
mainframe.place(x=480,y=200)

login_picture = ctk.CTkImage(Image.open("images/login.png"),size=(150,150))

login_picture_btn = ctk.CTkLabel(mainframe,text="",image=login_picture)
login_picture_btn.place(x=150,y=0)

admin_name = ctk.CTkEntry(mainframe,font=("monaco",18),width=300,placeholder_text="ADMIN NAME",border_width=2,border_color="gray",corner_radius=10)
admin_name.place(x=80,y=200)

password = ctk.CTkEntry(mainframe,font=("monaco",18),width=300,placeholder_text="PASSWORD",show=".",border_width=2,border_color="gray",corner_radius=10)
password.place(x=80,y=250)

btn_submit = ctk.CTkButton(mainframe,text="CONNECTION",fg_color="#0078d7",text_color="white",font=("monaco",18),width=300,command=connection)
btn_submit.place(x=80,y=300)





BottomFrameDetails = ctk.CTkFrame(root,height=200)
BottomFrameDetails.pack(side="bottom",fill="x")

copyr_ = ctk.CTkButton(BottomFrameDetails,text="copyright(©) 2024",fg_color="#333")
copyr_.grid(row=0,column=0)

UnetCorporation = ctk.CTkButton(BottomFrameDetails,text="®UNET CORPORATION",fg_color="#333")
UnetCorporation.place(x=620,y=0)

deter_okam = ctk.CTkButton(BottomFrameDetails,text="deterokam@gmail.com",fg_color="#333")
deter_okam.place(x=1210,y=0)
root.mainloop()