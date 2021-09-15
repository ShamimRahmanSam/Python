import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",passwd="44094")

mycursor = mydb.cursor()

mycursor.execute("create database ShuvSR")                                   #database er name capital dileo seta small letter e er e hoye show hobe. show database e gele dekha jay

print(mydb)                                                             #eta na dile emn ouytput dekha jeto na. but database obviously create hoye jeto .show krleoi pawa jeto