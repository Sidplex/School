from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

window = Tk()
window.geometry("1200x500")
window.title("Student Details")


def view():
    import mysql.connector
    conn = mysql.connector.connect(host='localhost',
                             database='student',
                             user='root',
                             password='bks12345')
    mycur = conn.cursor()
    mycur.execute("select * from studentdetails")
    print("Records shown are: ")
    for x in mycur:
        print(x)
                  
    mycur.close    
    conn.close

def submit():
    import mysql.connector
    conn = mysql.connector.connect(host='localhost',
                             database='student',
                             user='root',
                             password='bks12345')
    mycur = conn.cursor()
    
    mycur.execute("insert into studentdetails values ('"+ str(entry1.get())+"',"+entry2.get() +","+combo.get() +","+entry4.get() +","+entry5.get() +","+entry6.get() +","+entry7.get() +","+entry8.get() +","+entry9.get()+")")
    print("Record inserted.")
    mycur.close
    mycur.execute("select * from studentdetails ")
    print("View Total Record:")
    for x in mycur:
         print(x)
    mycur.close
    conn.commit()     
    conn.close

def close (): 

    window.destroy()
    
def delete():
    messagebox.showinfo('Message title', 'Message content')
    import mysql.connector
    conn = mysql.connector.connect(host='localhost',
                             database='student',
                             user='root',
                             password='bks12345')    
    mycur = conn.cursor()
    mycur.execute("delete from studentdetails where rollno="+entry10.get()+"")
    print("Record deleted")
    mycur.close
    mycur.execute("select * from studentdetails ")
    print("View Total Record:")
    for x in mycur:
         print(x)
    mycur.close
    conn.commit()     
    conn.close
    
def done():
    entryy= Entry(window)
    entryy.grid(row=33,column=5)
    entryy2= Entry(window)
    entryy2.grid(row=33,column=7)
    entryy3= Entry(window)
    entryy3.grid(row=33,column=9)
    entryy4= Entry(window)
    entryy4.grid(row=33,column=11)
    entryy5= Entry(window)
    entryy5.grid(row=33,column=13)
    
    
def edit():
    labell = Label(window,text="What do you want to edit?")
    labell.grid(row=31,column=10,command=done)
    btton = Button(text="ENG")
    btton.grid(row=32,column=5)
    btton2 = Button(text="MATH",command=done)
    btton2.grid(row=32,column=7)
    btton3 = Button(text="SCIENCE",command=done)
    btton3.grid(row=32,column=9)
    btton4 = Button(text="CS",command=done)
    btton4.grid(row=32,column=11)
    btton5 = Button(text="SSC",command=done)
    btton5.grid(row=32,column=13)
    
#        import mysql.connector
#        conn = mysql.connector.connect(host='localhost',
#                                 database='student',
#                                 user='root',
#                                 password='bks12345')
#        mycur = conn.cursor()
#        mycur.execute("alter table")
#        entryy=Entry(window)
#        entryy.grid(row=31,column=10)





    
label1 = Label(window,text="School Name- Amity International School",font="Arial 15")
label1.grid(row=3,column=10)
entry1 = Entry(window)
entry1.grid(row=4,column=1)

label2 = Label(window,text="Student name:")
label2.grid(row=4,column=0)
entry2 = Entry(window)
entry2.grid(row=5,column=1)

label3 = Label(window,text="Roll no:")
label3.grid(row=5,column=0)
combo = Combobox (window)
combo['values']= (8, 9, 10, 11, 12, "Select class:")
combo.current(5)
combo.grid(row=6, column=1)

label4 = Label(window,text="Class:")
label4.grid(row=6,column=0)


entry4 = Entry(window)
entry4.grid(row=14,column=20)

label5 = Label(window,text="Subject")
label5.grid(row=13,column=1)
entry5 = Entry(window)
entry5.grid(row=15,column=20)

label6 = Label(window,text="Marks")
label6.grid(row=13,column=20)
entry6 = Entry(window)
entry6.grid(row=16,column=20)

label7 = Label(window,text="English")
label7.grid(row=14,column=1)
entry7 = Entry(window)
entry7.grid(row=17,column=20)

label8 = Label(window,text="Math")
label8.grid(row=15,column=1)
entry8 = Entry(window)
entry8.grid(row=18,column=20)

label9 = Label(window,text="Science")
label9.grid(row=16,column=1)
entry9 = Entry(window)
entry9.grid(row=23,column=20)

label10 = Label(window,text="Computer Science")
label10.grid(row=17,column=1)
label11 = Label(window,text="Social Science")
label11.grid(row=18,column=1)

final = Label(window,text="Total")
final.grid(row=23,column=1)
bt3 = Button(text="Close",command=close)
bt3.grid(row=24,column=10)
bt4 = Button(text="View",command=view)
bt4.grid(row=25,column=10)
bt5 = Button(text="Submit",command=submit)
bt5.grid(row=28,column=10)

bt6 = Button(text="Delete",command=delete)
bt6.grid(row=29,column=2)
label12 = Label(window,text="Insert student roll number to be deleted--->")
label12.grid(row=29,column=10)
entry10 = Entry(window)
entry10.grid(row=29,column=15)

bt7 = Button(text="Edit",command=edit)
bt7.grid(row=30,column=2)
label13 = Label(window,text="Insert to edit table--->")
label13.grid(row=30,column=10)
entry11 = Entry(window)
entry11.grid(row=30,column=15)
window.mainloop()

