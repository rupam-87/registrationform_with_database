from tkinter import *

import sqlite3 as sq

student=Tk()
student.geometry("600x600")
student.config(bg="red")
def database():
    name1=First-Name.get()
    email=E-mail.get()
    gender=Gender.get()
    country=Country.get()
    prog=var1.get()
    conn= sq.connect('register.db')
    with conn:
        cursor=conn.cursor()
        cursor.excute('CTREATE TABLE IF NOT EXISTS Student(First-Name TEXT,E-mail TEXT,Gender TEXT,Country TEXT,Programming TEXT)')
        cursor.excute('INSERT INTO STUDENT (First-Name,Email,Gender,Country,Programming) values[?,?,?,?,?]',(name,email,gender,country,prog,))
    













photo = PhotoImage(file = r"C:\Users\hp\Desktop\all\html\html\capture1.jpg")
label=Label(image=photo).pack(side=TOP)
student.title("STUDENT REGISTRATION FORM")

label1= Label(student,text="STUDENT REGISTRATION FORM",width=30,font=("Times New Roman",20),bg="red").pack()
label2= Label(student,text="First-Name",width=30,font=(" MS Sans Serif",10),bg="red")
label2.place(x=100,y=190)
label3= Label(student,text="Last-Name",width=30,font=(" MS Sans Serif",10),bg="red")
label3.place(x=100,y=240)
label4= Label(student,text="Phone-No",width=30,font=(" MS Sans Serif",10),bg="red")
label4.place(x=100,y=290)
label5= Label(student,text="E-mail",width=30,font=(" MS Sans Serif",10),bg="red")
label5.place(x=100,y=340)
label6= Label(student,text="Country",width=30,font=(" MS Sans Serif",10),bg="red")
label6.place(x=90,y=440)
label7= Label(student,text="Gender",width=30,font=(" MS Sans Serif",10),bg="red")
label7.place(x=90,y=390)
l1 = ["India","Africa","China","Nepal","Pakistan","Bangladesh"]
c = StringVar(student)
c.set("select country")
drplist = OptionMenu(student,c,*l1)
drplist.config(width=15,bg="black",fg="white")
drplist.place(x=300,y=440)
label7= Label(student,text="Programming",width=30,font=(" MS Sans Serif",10),bg="red")
label7.place(x=100,y=490)
var1=IntVar()
var2=IntVar()
Checkbutton(student,text="java",variable=var1).place(x=300,y=490)
Checkbutton(student,text="python",variable=var2).place(x=400,y=490)
var=IntVar()
Radiobutton(student,text="Male",variable=var,value=1).place(x=300,y=390)
Radiobutton(student,text="Female",variable=var,value=2).place(x=400,y=390)
entry=Entry(student,width=30,bg="black",fg="white").place(x=290,y=340)
entry=Entry(student,width=30,bg="black",fg="white").place(x=290,y=190)
entry=Entry(student,width=30,bg="black",fg="white").place(x=290,y=240)
entry=Entry(student,width=30,bg="black",fg="white").place(x=290,y=290)
btn=Button(student, text = 'Submit',bd = '5',width=20,fg="white",bg="black",font=('Times New Roman',10))
btn.place(x=250,y=540)
student.mainloop()
