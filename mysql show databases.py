import mysql.connector

mydb = mysql.connector.connect(host='localhost', user='root', passwd='44094')              #srs namer ekta create kora hoisilo mysql workbench e

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")                    #create or show databases emn capital or small ekta dilei hoy

for x in mycursor:                                 #ei loop er dui ta line na dile output e show hbena database gulo. especially print(x) na dile toh hbeina show
  print(x)


print(mydb)