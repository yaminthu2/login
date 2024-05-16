import tkinter
from tkinter import messagebox

window=tkinter.Tk()
window.title('login Form')
window.geometry('500x400')
window.configure(bg='#85c1e9')

def login():
    username="yamin"
    password="1234"
    if username_entry.get()==username and password_entry.get()==password:
        messagebox.showinfo(title= "Login successed",message="You Successfully logined in ")
    else:
        messagebox.showerror(title="Error",message="Invalid login")

frame=tkinter.Frame(bg='#85c1e9')


#creating widgets

login_label=tkinter.Label(frame,text="Login",bg='#85c1e9',font=("Aria",30))
username_label=tkinter.Label(frame,text="Username",bg='#85c1e9',font=("Aria",15))
username_entry=tkinter.Entry(frame,bg='#85c1e9')
password_label=tkinter.Label(frame,text="Password",bg='#85c1e9',font=("Aria",15))
password_entry=tkinter.Entry(frame,show='*',bg='#85c1e9')
login_button=tkinter.Button(frame,text="Login", bg='#85c1e9',command=login)


#creating widgets on the screen


login_label.grid(row=0,column=0,columnspan=2,sticky="news",pady=40)
username_label.grid(row=4,column=0)
username_entry.grid(row=4,column=1,pady=20)
password_label.grid(row=8,column=0)
password_entry.grid(row=8,column=1,pady=20)
login_button.grid(row=10,column=0,columnspan=2,pady=30)

frame.pack()

window.mainloop()



