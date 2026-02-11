import customtkinter as ctk
from PIL import Image
from tkinter import PhotoImage
from tkinter import messagebox
from subprocess import call



root = ctk.CTk()
root.title("SAFETY HOSPITAL")
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry("{w}x{h}+0+0".format(w=width,h=height))
root.iconbitmap("images/logo.ico")

#===========================all pages
def patient_page():
    root.destroy()
    call(["python","pages/patient_reg.py"])
    
def patient_hist_page():
    root.destroy()
    call(["python","pages/patient_hist.py"])

btnEtat = False

def switch():
    global btnEtat
    if btnEtat is True:
        for x in range(220):
            frameLateral.place(x=-x,y=0)
            maintitle.update()
            btnEtat = False
    else:
        for x in range(-220,0):
            frameLateral.place(x=x, y=0)
            maintitle.update()
            btnEtat =  True



maintitle = ctk.CTkFrame(root,width=width,height=50,border_width=2,border_color="#333",corner_radius=10)
maintitle.pack(side="top",fill="x")

titlelbl = ctk.CTkLabel(maintitle,text="WELCOM TO SAFETY HOSPITAL SYSTEM MANAGEMENT",font=("monaco",25),text_color="white",bg_color="transparent",corner_radius=10)
titlelbl.pack(side="top",pady=5)






menuIcon = ctk.CTkImage(Image.open("images/menu.png"),size=(32,32))

maintitleMenu = ctk.CTkButton(root,text="",image=menuIcon,width=1,fg_color="#333",command=switch)
maintitleMenu.place(x=0,y=0)

frameLateral = ctk.CTkFrame(root,bg_color="#333",width=220,height=height)
frameLateral.place(x=-220,y=0)

#All historics
#title historic
title_historic = ctk.CTkLabel(frameLateral,text="MENU",text_color="white",fg_color="#333",font=("roboto",25))
title_historic.place(x=40,y=0) 


h_patient = ctk.CTkButton(frameLateral,text="HISTORIC PATIENT",fg_color="transparent",text_color="white",font=("monaco",18),command=patient_hist_page)
h_patient.place(x=0,y=80)

h_medecin = ctk.CTkButton(frameLateral,text="HISTORIC MEDECIN",fg_color="transparent",text_color="white",font=("monaco",18))
h_medecin.place(x=0,y=140)

h_consultant = ctk.CTkButton(frameLateral,text="HISTORIC CONSULTANT",fg_color="transparent",text_color="white",font=("monaco",18))
h_consultant.place(x=0,y=200)

h_resultat = ctk.CTkButton(frameLateral,text="HISTORIC RESULTAT",fg_color="transparent",text_color="white",font=("monaco",18))
h_resultat.place(x=0,y=260)

# h_traitement = ctk.CTkButton(frameLateral,text="HISTORIC TRAITEMENT",fg_color="#333",text_color="white",font=("monaco",18))
# h_traitement.place(x=0,y=320)



#all entity registraction
#frame 
frame_entity = ctk.CTkFrame(root,bg_color="#333",width=800,height=700)
frame_entity.place(x=360,y=100)

patientImg = ctk.CTkImage(Image.open("images/patient.png"),size=(150,150))
medecinImg = ctk.CTkImage(Image.open("images/medecin.png"),size=(150,150))
consultImg = ctk.CTkImage(Image.open("images/consult.png"),size=(150,150))
resultImg = ctk.CTkImage(Image.open("images/result.png"),size=(150,150))
traitementImg = ctk.CTkImage(Image.open("images/traitement.png"),size=(150,150))
laboImg = ctk.CTkImage(Image.open("images/labo.png"),size=(150,150))


patient_frame = ctk.CTkFrame(frame_entity)
patient_frame.grid(row=0,column=0,pady=30,padx=30)

medecin_frame = ctk.CTkFrame(frame_entity)
medecin_frame.grid(row=0,column=1,pady=30,padx=30)

consult_frame = ctk.CTkFrame(frame_entity)
consult_frame.grid(row=0,column=2,pady=30,padx=30)

result_frame = ctk.CTkFrame(frame_entity)
result_frame.grid(row=1,column=0,pady=30,padx=30)

traitement_frame = ctk.CTkFrame(frame_entity)
traitement_frame.grid(row=1,column=1,pady=30,padx=30)

labo_frame = ctk.CTkFrame(frame_entity)
labo_frame.grid(row=1,column=2,pady=30,padx=30)


#entity icons and text
patient_lbl = ctk.CTkLabel(patient_frame,text="",image=patientImg)
patient_lbl.pack()

patient_btn = ctk.CTkButton(patient_frame,text="PATIENT",font=("monaco",15),fg_color="transparent",text_color="white",command=patient_page)
patient_btn.pack()

medecin_lbl = ctk.CTkLabel(medecin_frame,text="",image=medecinImg)
medecin_lbl.pack()

medecin_btn = ctk.CTkButton(medecin_frame,text="MEDECIN",font=("monaco",15),fg_color="transparent",text_color="white",command=None)
medecin_btn.pack()

consult_lbl = ctk.CTkLabel(consult_frame,text="",image=consultImg)
consult_lbl.pack()

consult_btn = ctk.CTkButton(consult_frame,text="CONSULTATION",font=("monaco",15),fg_color="transparent",text_color="white",command=None)
consult_btn.pack()

result_lbl = ctk.CTkLabel(result_frame,text="",image=resultImg)
result_lbl.pack()

result_btn = ctk.CTkButton(result_frame,text="RESULT",font=("monaco",15),fg_color="transparent",text_color="white",command=None)
result_btn.pack()

traetement_lbl = ctk.CTkLabel(traitement_frame,text="",image=traitementImg)
traetement_lbl.pack()

traetement_btn = ctk.CTkButton(traitement_frame,text="TRAETEMENT",font=("monaco",15),fg_color="transparent",text_color="white",command=None)
traetement_btn.pack()

laboratory_lbl = ctk.CTkLabel(labo_frame,text="",image=laboImg)
laboratory_lbl.pack()

laboratory_btn = ctk.CTkButton(labo_frame,text="LABORATORY",font=("monaco",15),fg_color="transparent",text_color="white",command=None)
laboratory_btn.pack()



#btn back menu

backIcon = ctk.CTkImage(Image.open("images/back.png"),size=(32,32))

mainBack = ctk.CTkButton(frameLateral,text="",image=backIcon,width=1,fg_color="#333",command=switch)
mainBack.place(x=170,y=0)











BottomFrameDetails = ctk.CTkFrame(root,height=200)
BottomFrameDetails.pack(side="bottom",fill="x")

copyr_ = ctk.CTkButton(BottomFrameDetails,text="copyright(©) 2024",fg_color="#333")
copyr_.grid(row=0,column=0)

UnetCorporation = ctk.CTkButton(BottomFrameDetails,text="®UNET CORPORATION",fg_color="#333")
UnetCorporation.place(x=620,y=0)

deter_okam = ctk.CTkButton(BottomFrameDetails,text="deterokam@gmail.com",fg_color="#333")
deter_okam.place(x=1210,y=0)

root.mainloop()