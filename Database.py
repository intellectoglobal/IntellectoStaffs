
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost", 
    user = 'root', 
    passwd = "1234", 
    database = 'var'
)

mycursor = mydb.cursor()

mycursor.execute("select * from expanse")
for i in mycursor:
    print(i)