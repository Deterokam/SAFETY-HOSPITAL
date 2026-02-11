from tkinter import PhotoImage
from tkinter import Tk


app = Tk()
app.title("my application")
app.config(bg="gray30")
app.geometry("400x600")
app.iconbitmap("img/x.ico")


btnEtat = False

navIcon = PhotoImage(file="img/menu.png")
closeIcon = PhotoImage(file="img/close.png")

topfrape = Tk.frame(app, bg="purple")
topfrape.pack(side="top", fill=Tk.X)




app.mainloop()