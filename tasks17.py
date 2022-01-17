#1) REVERSE OF STRING

# x="bharanidharan8143"[::-1]
# print(x)

# OUTPUT:
# 3418narahdinarahb

#2) REVERSE OF LIST

# x=["hey","google","this","is","bharani"] [::-1]
# print(x)

# OUTPUT:
# ['bharani', 'is', 'this', 'google', 'hey']

#3) PRINT KEYS ALONE FROM DICTIONARIES


# dict = {'Name': 'Bharani', 'Age': 23, 'Class': 'First'}
# print ("dict['Name']:"),dict['Name']
# print ("dict['Age']:"),dict['Age']

# #OUTPUT:
# dict['Name']:
# dict['Age']:

#4) PRINT VALUES ALONE FROM DICTIONARIES


# dict = {'Name': 'Bharani', 'Age': 7, 'Class': 'First'}
# print ("dict['Bharani']:"),dict['Name']
# print ("dict['7']:"),dict['Age']


#OUTPUT:
# dict['Zara']:
# dict['7']:

#5) ADD ELEMENT TO A LIST AND DICTIONARIES

# x=["where", "is", "your", "bike"]
# x.insert(4,"man")
# print(x)

#OUTPUT:
# ['where', 'is', 'your', 'bike', 'man']

#6) ADD LIST TO ANOTHER LIST

# x=["it","will","be","on"]
# x.insert(4,"chennai")
# x.insert(5,"by")
# x.insert(6,"nextweek")
# x.insert(7,"monday")
# print(x)

# OUTPUT:
# ['it', 'will', 'be', 'on', 'chennai', 'by', 'nextweek', 'monday']

#7) CAPITALIZE A STRING

# x="hey siri i want a call after 10 minutes with gopal set the remainder and connect the call after the time"
# x=x.capitalize()
# print(x)

# OUTPUT:
# Hey siri i want a call after 10 minutes with gopal set the remainder and connect the call after the time

#8) UPPER OR LOWER A STRING

# x="take a cup of coffee"
# x=x.upper()
# print(x)

# OUTPUT:
# TAKE A CUP OF COFFEE

#8)b) LOWER  STRING

# X="WE WERE BORN ON THE EDGES OF THE BEAUTIFULL"
# X=X.lower()
# print(X)

# OUTPUT:
# we were born on the edges of the beautifull

#9) VERIFY THE GIVEN OUTPUT IS NUMBER OR CHARACTER

# x=(input("enter the number or character"))
# if x.isdigit():
#     print("NUMBER")
# else:
#     print("CHARACTER")    

# OUTPUT:
# enter the number or character888
# NUMBER
# PS C:\Users\admin\Documents> & C:/Users/admin/AppData/Local/Microsoft/WindowsApps/python3.7.exe "c:/Users/admin/Documents/Python Scripts/tasks17.py"
# enter the number or characterb hara
# CHARACTER


#10) ROUND OF DECIMAL VALUE TO 2 DIGIT?

# print(round(6.995, 2))
# print(round(9.446, 2))


# OUTPUT:
# 7.0
# 9.45

#11) VERIFY THE GIVEN INPUT IS NUMBER OR A PHONE NUMBER
x=int(input("enter the given number"))
if x==10:
    print("MOBILE NUMBER")
else:
    print("NUMBER")     

