# to open mysql from cmd 
# cd c:\xampp\mysql\bin
# mysql.exe -u root --password

from tkinter import *
from tkinter.ttk import *

from tkinter import messagebox

import mysql.connector
try:
    con = mysql.connector.connect(
        host="localhost",
        database="project",
        user="root",
        password="",
    )
    cursor = con.cursor()
except Exception as e:
    print("\nDatabase connection : false\n\n",e)
    quit()
else:
    print("Database connected")
    

a = Tk()

a.title("app")
a.geometry("500x500")

name = ""

def login():
    name = text.get()
    pas = pwd.get()
    cursor.execute("select * from user")
    result = cursor.fetchall()
    for i in range(len(result)):
        if name == result[i][0] and pas == result[i][1]:
            address=result[i][2]
            age_=result[i][3]
            phone=result[i][4]
            # a.destroy()
            b = Tk()
            b.geometry("500x500")
            #details
            Label(b,text="welcome").pack() 
            Label(b,text="User details").pack()
            Label(b,text=name).pack()
            Label(b,text=address).pack()
            Label(b,text=age_).pack()
            Label(b,text=phone).pack()
            #book train
            Label(b,text="Enter destination").pack()
            list = Entry(b)
            list.pack()
            def check():
                cursor.execute("select tr_id from trains where tr_destination = '{}'".format(list.get()))
                destinations = cursor.fetchall()
                print(destinations)
                box = Listbox(b)
                for i,a in enumerate(destinations):
                    print(i)
                    box.insert(i,a)
                box.pack()
                def book():
                    trainid=box.get(ANCHOR)
                    cursor.execute("insert into bookings(tr_id,username) values('{}','{}')".format(name,trainid[0]))
                    con.commit()
                    cursor.execute("SELECT transaction_id,tr_id FROM bookings ORDER BY bookings.order_time DESC");
                    res = cursor.fetchone()
                    return messagebox.showinfo("booking was successful","booking id {}\nbooked train {}".format(res[0],res[1]))
                Button(b,text='book',command=book).pack()
            Button(b,text='submit',command=check).pack()

            #logout
            Button(b,text='logout',command=b.destroy).pack()
            b.mainloop()
            break
    else:
        return messagebox.showerror("error","invalid credentials")


def register():
    c = Tk()
    c.title("register")
    c.geometry("500x500")

    def square():
        name = text.get()
        if name=="":
            return messagebox.showerror("cannot be empty","please try again")
        pas = pwd.get()
        address = add.get()
        age_ = age.get()
        phone = phno.get()
        cursor.execute("select * from user")
        result = cursor.fetchall()
        for i in range(len(result)):
            if name == result[i][0]:
                return messagebox.showerror("error","User already exist")
        querry = "insert into user (username,password,address,age,ph_no) values (%s,%s,%s,%s,%s)"
        values = [(name,pas,address,age_,phone)]
        cursor.executemany(querry,values)
        con.commit()
        text.delete(0,END)
        pwd.delete(0,END)
        add.delete(0,END)
        age.delete(0,END)
        phno.delete(0,END)
        c.destroy()
        return messagebox.showinfo("Registered","successfully")
    Label(c,text="Enter user Name").place(x=100,y=100)
    text = Entry(c)
    text.place(x=200,y=100)
    Label(c,text="Enter password").place(x=100,y=150)
    pwd = Entry(c,show="*")
    pwd.place(x=200,y=150)
    Label(c,text="Enter your address").place(x=100,y=250)
    add = Entry(c);
    add.place(x=200,y=250)
    Label(c,text="Enter your age").place(x=100,y=300)
    age = Entry(c);
    age.place(x=200,y=300)
    Label(c,text="Enter your ph no").place(x=100,y=350)
    phno = Entry(c);
    phno.place(x=200,y=350)
    Button(c,text="register",command=square).place(x=150,y=400)
    c.mainloop()


Label(a,text="Enter user Name").place(x=100,y=100)
text = Entry(a)
text.place(x=200,y=100)
Label(a,text="Enter password").place(x=100,y=150)
pwd = Entry(a,show="*")
pwd.place(x=200,y=150)
Button(a,text="login",command=login).place(x=250,y=400)
Button(a,text="register",command=register).place(x=150,y=400)
a.mainloop()