import mysql.connector

conn = mysql.connector.connect(
    user = "root",
    password = "1234",
    host = "localhost",
    database = "ginger"
)

mycursor = conn.cursor()

# sql = "INSERT INTO fruits (vitamin_A, vitamin_B) VALUES (%s, %s)"
# val = [
#     ("apple", "banana"),
#     ("amala", "kiwi"),
#     ("mango", "orange")
# ]

# mycursor.executemany(sql,val)

# conn.cursor()

# print(mycursor.rowcount, "record inserted")
# mycursor.execute("CREATE TABLE fruits (id INT AUTO_INCREMENT PRIMARY KEY, vitamin_A VARCHAR(20), vitamin_B VARCHAR(20))")

# mycursor.execute("ALTER TABLE fruits ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
# mycursor.execute("CREATE DATABASE ginger")

mycursor.execute("select * from fruits")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)