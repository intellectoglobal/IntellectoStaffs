# try:
#   fh = open("testfile.txt", "w")
#   fh.write("This is my test file for exception handling!!")
# except IOError:
#   print ("Error: can\'t find file or read data")
# else:
#  print ("Written content in the file successfully")
# fh.close()



# file = open("testfile.txt")

# data = file.read()

# print('data')

# file.close()

with open("testfile.txt","w") as file: # Use file to refer to the file object
   file.write('Hi there!')
   
