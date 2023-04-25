from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np

###For Microsoft SQL
#import pyodbc
window = Tk()
window.geometry("950x500")
window.title("Student Details")
window.configure(bg='light blue')


try:
    def view():
    
    ###For SQL 5.5.60'''    
        import mysql.connector
        conn = mysql.connector.connect(host='localhost',
                                 database='student',
                                 user='root',
                                 password='')
        mycur = conn.cursor()
        mycur.execute("select * from studentdetails")
        print("Records shown are: ")
        for x in mycur:
            print(x)
                      
        mycur.close    
        conn.close
    
    
    ###For Microsoft SQL'''
    #    conn = pyodbc.connect("Driver={SQL Server};"
    #                        "Server=LAPTOP-3QC3HN03\SQLEXPRESS;"
    #                        "database=student;"
    #                        "uid=knsa;pwd=knrai")
    #    mycur = conn.cursor()
    #    mycur.execute("select * from student.dbo.studentdetails")
    #    print("Records shown are: ")
    #    for x in mycur:
    #        print(x)
    #                  
    #    mycur.close    
    #    conn.close
    
    
    def submit():
    
    ###For SQL 5.5.60'''    
        import mysql.connector
        conn = mysql.connector.connect(host='localhost',
                                 database='student',
                                 user='root',
                                 password='')
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
        
    ###For Microsoft SQL'''
    #    conn = pyodbc.connect("Driver={SQL Server};"
    #                        "Server=LAPTOP-3QC3HN03\SQLEXPRESS;"
    #                        "database=student;"
    #                        "uid=knsa;pwd=knrai")
    #    mycur = conn.cursor()
    #    #mycur.execute("insert into studentdetails values(  str(entry1.get()),int(entry2.get()), int(entry3.get()), int(entry4.get()), int(entry5.get()), int(entry6.get()), int(entry7.get()), int(entry8.get()), int(entry9.get())    )")
    #    #mycur.execute("insert into studentdetails values('Sid',5814,67,77,97,85,68,300,777)")
    #    #print("insert into studentdetails values ('"+ str(entry1.get())+"',"+entry2.get() +","+entry3.get() +","+entry4.get() +","+entry5.get() +","+entry6.get() +","+entry7.get() +","+entry8.get() +","+entry9.get() +")")
    #    mycur.execute("insert into student.dbo.studentdetails values ('"+ str(entry1.get())+"',"+entry2.get() +","+combo.get() +","+entry4.get() +","+entry5.get() +","+entry6.get() +","+entry7.get() +","+entry8.get() +","+entry9.get()+")")
    #    print("Record inserted.")
    #    mycur.close
    #    mycur.execute("select * from student.dbo.studentdetails ")
    #    print("View Total Record:")
    #    for x in mycur:
    #         print(x)
    #    mycur.close
    #    conn.commit()     
    #    conn.close
    
    
    def close (): 
    
        window.destroy()
        
    def delete():
        messagebox.showinfo('Delete', 'Do you want to delete?')
    ##For SQL 5.5.60'''
        import mysql.connector
        conn = mysql.connector.connect(host='localhost',
                                 database='student',
                                 user='root',
                                 password='')    
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
    
    
    ###For Microsoft SQL   
    #    conn = pyodbc.connect("Driver={SQL Server};"
    #                        "Server=LAPTOP-3QC3HN03\SQLEXPRESS;"
    #                        "database=student;"
    #                        "uid=knsa;pwd=knrai")
    #    mycur = conn.cursor()
    #    mycur.execute("delete from student.dbo.studentdetails where rollno="+entry10.get()+"")
    #    print("Record deleted")
    #    mycur.close
    #    mycur.execute("select * from student.dbo.studentdetails ")
    #    print("View Total Record:")
    #    for x in mycur:
    #         print(x)
    #    mycur.close
    #    conn.commit()     
    #    conn.close
    

    def bargraph():
        graph = Toplevel()
        graph.geometry("500x500")
        graph.title("Bargraph")

        import mysql.connector
        conn = mysql.connector.connect(host='localhost',
                                 database='student',
                                 user='root',
                                 password='')    
        mycur = conn.cursor()
        mycur.execute("select engmarks, mathmarks, scimarks, csmarks, sscmarks from studentdetails")
        v=mycur.fetchall()
        l2=[]
        for x in v:
            y=x
            l=list(y)
            l2.append(l)
 
        eng=[]
        math=[]
        sci=[]
        cs=[]
        ssc=[]
        for lol in range(len(l2)):
            eng.append(l2[lol][0])
            math.append(l2[lol][1])
            sci.append(l2[lol][2])
            cs.append(l2[lol][3])
            ssc.append(l2[lol][4])

        
        mycur.close
        conn.commit()     
        conn.close  
        import mysql.connector
        conn = mysql.connector.connect(host='localhost',
                                 database='student',
                                 user='root',
                                 password='')    
        mycur = conn.cursor()
        mycur.execute("select studname from studentdetails")
        print("View Total Record:")
        l3=[]
        for name in mycur:
            l=name
            s=list(l)
            l3.append(s)

            
        mycur.close
        conn.commit()     
        conn.close

        
        n_groups=len(eng)
        fig, ax = plt.subplots()
        index=np.arange(n_groups)
        bar_width = 0.1
        opacity = 0.8
        plt.bar(index,eng,bar_width,alpha=opacity,color='b',label='English')
        plt.bar(index + bar_width, math, bar_width,alpha=opacity,color='g',label='math')
        plt.bar(index + (2*bar_width), sci, bar_width,alpha=opacity,color='r',label='science')
        plt.bar(index + (3*bar_width), cs, bar_width,alpha=opacity,color='m',label='CS')
        plt.bar(index + (4*bar_width), ssc, bar_width,alpha=opacity,color='y',label='SSC')
        plt.xlabel('Person')
        plt.ylabel('Scores')
        plt.title('Scores by person')
        plt.xticks(index + bar_width,l3)
        plt.legend()
        
        plt.tight_layout()
        plt.savefig("testbar.png")

        photo = PhotoImage(file= r"testbar.png")
        labbb = Label(graph,image = photo)
        labbb.pack(side = TOP)
        
        graph.mainloop()
                
    
    def edit():
        
        main = Tk()
        main.geometry("650x500")
        main.title("Edit menu")
        main.configure(bg="light blue")                

        labb = Label(main,text="Marks Updation",font="Arial 15")
        labb.grid(row=1,column=4)
        def eng():
            import mysql.connector
            conn = mysql.connector.connect(host='localhost',
                                     database='student',
                                     user='root',
                                     password='')    
            mycur = conn.cursor()
            mycur.execute("update studentdetails set engmarks="+entryy.get()+" where rollno="+roll1.get()+";")
            print("Record edited")
            mycur.close
            mycur.execute("select * from studentdetails ")
            print("View Total Record:")
            for x in mycur:
                 print(x)
            mycur.close
            conn.commit()     
            conn.close
        def math():
            import mysql.connector
            conn = mysql.connector.connect(host='localhost',
                                     database='student',
                                     user='root',
                                     password='')    
            mycur = conn.cursor()
            mycur.execute("update studentdetails set mathmarks="+entryy2.get()+" where rollno="+roll1.get()+";")
            print("Record edited")
            mycur.close
            mycur.execute("select * from studentdetails ")
            print("View Total Record:")
            for x in mycur:
                 print(x)
            mycur.close
            conn.commit()     
            conn.close
        def sci():
            import mysql.connector
            conn = mysql.connector.connect(host='localhost',
                                     database='student',
                                     user='root',
                                     password='')    
            mycur = conn.cursor()
            mycur.execute("update studentdetails set scimarks="+entryy3.get()+" where rollno="+roll1.get()+";")
            print("Record edited")
            mycur.close
            mycur.execute("select * from studentdetails ")
            print("View Total Record:")
            for x in mycur:
                 print(x)
            mycur.close
            conn.commit()     
            conn.close
        def csmarks():
            import mysql.connector
            conn = mysql.connector.connect(host='localhost',
                                     database='student',
                                     user='root',
                                     password='')    
            mycur = conn.cursor()
            mycur.execute("update studentdetails set csmarks="+entryy4.get()+" where rollno="+roll1.get()+";")
            print("Record edited")
            mycur.close
            mycur.execute("select * from studentdetails ")
            print("View Total Record:")
            for x in mycur:
                 print(x)
            mycur.close
            conn.commit()     
            conn.close
        def sscmarks():
            import mysql.connector
            conn = mysql.connector.connect(host='localhost',
                                     database='student',
                                     user='root',
                                     password='')    
            mycur = conn.cursor()
            mycur.execute("update studentdetails set sscmarks="+entryy5.get()+" where rollno="+roll1.get()+";")
            print("Record edited")
            mycur.close
            mycur.execute("select * from studentdetails ")
            print("View Total Record:")
            for x in mycur:
                 print(x)
            mycur.close
            conn.commit()     
            conn.close
            

        
        
        btton = Button(main,text="EDIT ENG",command=eng)
        btton.grid(row=3,column=4)
        
        entryy= Entry(main)
        entryy.grid(row=3,column=3)
        
        lab1 = Label(main,text="Enter new english marks ->")
        lab1.grid(row=3,column=2)
        
        roll1 = Entry(main)
        roll1.grid(row=2,column=4)
        
        lab= Label(main,text="Enter Roll no.->")
        lab.grid(row=2,column=3)
        
        but = Button(main,text = "ENTER")
        but.grid(row=2,column=5)
        
        btton2 = Button(main,text="EDIT MATH",command=math)
        btton2.grid(row=4,column=4)
        
        entryy2=Entry(main)
        entryy2.grid(row=4,column=3)
        
        lab2 = Label(main,text="Enter new math marks ->")
        lab2.grid(row=4,column=2)
        
        btton3 = Button(main,text="EDIT SCIENCE",command=sci)
        btton3.grid(row=5,column=4)
        
        entryy3=Entry(main)
        entryy3.grid(row=5,column=3)
        
        lab3 = Label(main,text="Enter new science marks ->")
        lab3.grid(row=5,column=2)
        
        btton4 = Button(main,text="EDIT CS",command=csmarks)
        btton4.grid(row=6,column=4)
        
        entryy4=Entry(main)
        entryy4.grid(row=6,column=3)
        
        lab4 = Label(main,text="Enter new CS marks ->")
        lab4.grid(row=6,column=2)
        
        btton5 = Button(main,text="EDIT SSC",command=sscmarks)
        btton5.grid(row=7,column=4)
        
        entryy5=Entry(main)
        entryy5.grid(row=7,column=3)
        
        lab5 = Label(main,text="Enter new SSC marks ->")
        lab5.grid(row=7,column=2)
        
        
        
        
        
        
        
        
        
        
        
        
        main.mainloop()
    
    ###For SQL 5.5.60    
        import mysql.connector
        conn = mysql.connector.connect(host='localhost',
                                 database='student',
                                 user='root',
                                 password='')
        mycur = conn.cursor()
        mycur.execute("alter table")
        entryy=Entry(window)
        entryy.grid(row=31,column=10)
    
    ###For Microsoft SQL
    #        conn1 = pyodbc.connect("Driver={SQL Server};"
    #                            "Server=LAPTOP-3QC3HN03\SQLEXPRESS;"
    #                            "database=student;"
    #                            "uid=knsa;pwd=knrai")
    #        mycur1 = conn1.cursor()
    #        mycur1.execute("alter table")
    #        entryy=Entry(window)
    #        entryy.grid(row=32,column=10)
except:
    print()
label1 = Label(window,text="Amity International School",font="Castellar 15")
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
combo['values']= (8, 9, 10, 11, 12, "Select")
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
bt7.grid(row=30,column=10)

btt10 = Button(text="Show Graph",command=bargraph)
btt10.grid(row=31,column=10)

window.mainloop()




