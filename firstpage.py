#import module from tkinter for UI
from tkinter import *
#from playsound import playsound
import os
from datetime import datetime;
import mysql.connector;
#creating instance of TK
root=Tk()

mydb = mysql.connector.connect(host="localhost",user="root",passwd="billgates",database="student_database")
mycursor = mydb.cursor()

sql="UPDATE Attendance SET status='Absent' WHERE status='Present';"
mycursor.execute(sql);
mydb.commit();
print(mycursor.rowcount, "record inserted.")
s = "update Attendance SET date=current_date();"
mycursor.execute(s);
mydb.commit()
print(mycursor.rowcount, "record inserted.")
print("Database updated")
root.configure(background="white")

#root.geometry("300x300")

def function1():
    os.system("python3 dataset_capture.py")
    
def function2():
    os.system("python3 02_training_dataset.py")

def function3():

    os.system("python3 03_face_recognition.py")
    #playsound('sound.mp3')

def function5():
    root.destroy()

def attend():
    os.system("python3 database.py")

#stting title for the window
root.title("FACIAL RECOGNITION BASED ATTENDANCE SYSTEM AND MANAGEMENT")

#creating a text label
Label(root, text="FACIAL RECOGNITION BASED ATTENDANCE SYSTEM AND MANAGEMENT",font=("times new roman",20),fg="white",bg="maroon",height=3).grid(row=0,rowspan=2,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating first button
Button(root,text="Create Face Dataset",font=("times new roman",20),bg="red",fg='white',command=function1).grid(row=3,columnspan=2,sticky=W+E+N+S,padx=5,pady=5)

#creating second button
Button(root,text="Train Face Dataset",font=("times new roman",20),bg="brown",fg='white',command=function2).grid(row=4,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating third button
Button(root,text="Recognize Face and Set Attendance",font=('times new roman',20),bg="red",fg="white",command=function3).grid(row=5,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating attendance button
Button(root,text="Generate Attendance Sheet",font=('times new roman',20),bg="brown",fg="white",command=attend).grid(row=6,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

Button(root,text="Exit",font=('times new roman',20),bg="black",fg="white",command=function5).grid(row=9,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)


root.mainloop()
