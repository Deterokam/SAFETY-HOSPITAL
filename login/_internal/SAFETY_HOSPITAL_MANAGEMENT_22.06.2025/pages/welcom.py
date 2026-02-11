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

def entity():
    root.destroy()
    call(["python","pages/entity.py"])

maintitle = ctk.CTkFrame(root,width=width,height=50,border_width=2,border_color="#333",corner_radius=10)
maintitle.pack(side="top",fill="x")

titlelbl = ctk.CTkLabel(maintitle,text="WELCOM TO SAFETY HOSPITAL SYSTEM MANAGEMENT",font=("monaco",25),text_color="white",bg_color="transparent",corner_radius=10)
titlelbl.pack(side="top",pady=5)

#=====================same pictures==================
chirugi_img= ctk.CTkImage(Image.open("images/chirugie.png"),size=(200,200))

chirugi_lbl = ctk.CTkLabel(root,text="",image=chirugi_img)
chirugi_lbl.place(x=60,y=65)

medicament_img = ctk.CTkImage(Image.open("images/medicament.png"),size=(200,200))

medicament_lbl = ctk.CTkLabel(root,text="",image=medicament_img)
medicament_lbl.place(x=460,y=140)

psycholgie = ctk.CTkImage(Image.open("images/psychologie.png"),size=(200,200))

psycholgie_lbl = ctk.CTkLabel(root,text="",image=psycholgie)
psycholgie_lbl.place(x=760,y=65)

sang = ctk.CTkImage(Image.open("images/sang.png"),size=(200,200))

sang_lbl = ctk.CTkLabel(root,text="",image=sang)
sang_lbl.place(x=1080,y=65)

nutrition = ctk.CTkImage(Image.open("images/nutrition.png"),size=(200,200))

nutrition_lbl = ctk.CTkLabel(root,text="",image=nutrition)
nutrition_lbl.place(x=150,y=300)

radio = ctk.CTkImage(Image.open("images/radio.png"),size=(200,200))

radio_lbl = ctk.CTkLabel(root,text="",image=radio)
radio_lbl.place(x=450,y=370)

soin = ctk.CTkImage(Image.open("images/soin.png"),size=(200,200))

soin_lbl = ctk.CTkLabel(root,text="",image=soin)
soin_lbl.place(x=750,y=330)

hygiene = ctk.CTkImage(Image.open("images/hygiene.png"),size=(200,200))

hygiene_lbl = ctk.CTkLabel(root,text="",image=hygiene)
hygiene_lbl.place(x=1060,y=300)

dentiste = ctk.CTkImage(Image.open("images/dentiste.png"),size=(200,200))

dentiste_lbl = ctk.CTkLabel(root,text="",image=dentiste)
dentiste_lbl.place(x=255,y=510)

emergency_car = ctk.CTkImage(Image.open("images/emergency_car.png"),size=(200,200))

emergency_car_lbl = ctk.CTkLabel(root,text="",image=emergency_car)
emergency_car_lbl.place(x=900,y=530)



click = ctk.CTkButton(root,text="CLICK TO ENTER",fg_color="green",command=entity)
click.place(x=620,y=685)






BottomFrameDetails = ctk.CTkFrame(root,height=200)
BottomFrameDetails.pack(side="bottom",fill="x")

copyr_ = ctk.CTkButton(BottomFrameDetails,text="copyright(©) 2024",fg_color="#333")
copyr_.grid(row=0,column=0)

UnetCorporation = ctk.CTkButton(BottomFrameDetails,text="®UNET CORPORATION",fg_color="#333")
UnetCorporation.place(x=620,y=0)

deter_okam = ctk.CTkButton(BottomFrameDetails,text="deterokam@gmail.com",fg_color="#333")
deter_okam.place(x=1210,y=0)

root.mainloop()