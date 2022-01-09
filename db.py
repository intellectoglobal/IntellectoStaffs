# import xml.etree.ElementTree as ET 
import mysql.connector 
from bs4 import BeautifulSoup


conn = mysql.connector.connect(
    user='root',
    password='1234', 
    host='localhost',  
    database='xmldb',
    autocommit=True
) 

with open("park.xml") as f:
    soup = BeautifulSoup(f, 'xml')
    titles = soup.find_all("student")
    for i in (titles): 
        name = (i.find('name').text) 
        id = (i.find('id').text) 
        department = (i.find('department').text) 


        # data = "INSERT INTO students(name,id,department) VALUES(%s,%s,%s)"
        
        # c = conn.cursor() 



        # c.execute(data, (name, id, department)) 


        # print("student No-", name, " stored successfully") 