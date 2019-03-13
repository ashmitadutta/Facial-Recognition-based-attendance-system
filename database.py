import mysql.connector
import os
from openpyxl import Workbook
import csv
from datetime import datetime

p1=datetime.date(datetime.now())
p=str(datetime.date(datetime.now()))

s=p1.strftime("%B,%Y")
mydb = mysql.connector.connect(host="localhost",user="root",passwd="billgates",database="student_database")
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM Attendance")

rows = mycursor.fetchall()
with open('report_'+p+'.csv', 'w') as f:
    a = csv.writer(f, delimiter=',')
    a.writerow(["name","roll_no","class","status","date"])  ## etc
    a.writerows(rows)  ## closing paren added

wb = Workbook()
ws = wb.active
with open('report_'+p+'.csv', 'r') as f:
    for row in csv.reader(f):
        ws.append(row)



if os.path.exists('/home/ashmita/ProjectTE/attendance_report/'+s):
    wb.save('/home/ashmita/ProjectTE/attendance_report/'+s+'/Attendance_'+p+'.xlsx')
else:
    os.mkdir('/home/ashmita/ProjectTE/attendance_report/'+s)
    wb.save('/home/ashmita/ProjectTE/attendance_report/'+s+'/Attendance_'+p+'.xlsx')
       

       


os.remove("report_"+p+".csv")
print("done")
