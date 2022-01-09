import xml.sax
from xml.sax import handler
import mysql.connector


conn = mysql.connector.connect(
    user='root',
    password='1234', 
    host='localhost',  
    database='test',
    autocommit=True
) 



class XMLHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData = ""
        self.price = ""
        self.qty = ""
        self.company = ""

    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if(tag == "model"):
            print("*****Model*****")
            title = attributes["number"]
            print("Model number:", title)

    def endElement(self, tag):
        if(self.CurrentData == "price"):
            print("Price:", self.price)
        elif(self.CurrentData == "qty"):
            print("Quantity:", self.qty)
        elif(self.CurrentData == "company"):
            print("Company:", self.company)
        self.CurrentData = ""

    def characters(self, content):
        if(self.CurrentData == "price"):
            
            self.price = content
        elif(self.CurrentData == "qty"):
            self.qty = content
        elif(self.CurrentData == "company"):
            self.company = content

parser = xml.sax.make_parser()

parser.setFeature(xml.sax.handler.feature_namespaces,0)

handler = XMLHandler()

parser.setContentHandler( handler )

parser.parse("run.xml")


# with open("park.xml") as f:
#     soup = BeautifulSoup(f, 'xml')
#     titles = soup.find_all("student")

c = conn.cursor() 


# c.execute(data,(model, price, quantity, company_name)) 

# print("Data inserted") 

# for i in (parser): 
#         model = (i.find('model').text) 
#         price = (i.find('price').text) 
#         quantity = (i.find('quantity').text) 
#         company_name = (i.find('company_name').text)

# data = """INSERT INTO laptop_company(model, price, quantity,company_name) VALUES(%s,%s,%s,%s)"""



# model = "12345"

# price = "75000"

# quantity = "35"

# company_name = "LG"







# try:
#     connection = mysql.connector.connect(host='localhost',
#                                          database='test',
#                                          user='root',
#                                          password='1234')

#     mySql_insert_query = """INSERT INTO laptop_company (model, price, quantity, name) 
#                            VALUES 
#                            (SToo1, '35000', 12, 'Samsung') """

#     cursor = connection.cursor()
#     cursor.execute(mySql_insert_query)
#     connection.commit()
#     print(cursor.rowcount, "Record inserted successfully into Laptop table")
#     cursor.close()

# except mysql.connector.Error as error:
#     print("Failed to insert record into Laptop table {}".format(error))

# finally:
#     if connection.is_connected():
#         connection.close()
#         print("MySQL connection is closed")
