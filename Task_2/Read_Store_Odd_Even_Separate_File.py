from numpy import spacing


fn = open("testfile.txt", "r")
fn1 = open('nfile.txt', 'w')
cont = fn.readlines()
type(cont)
for i in range(0, len(cont)):
	if(i % 2 ) == (0):
		fn1.write(cont[i]) 

for i in range(0, len(cont)):     
    	fn1.write("\n")   

for i in range(0, len(cont)):
	if(i % 2 ) == (1):
		fn1.write(cont[i])  
	else:
      
		pass
fn1.close()
fn1 = open('nfile.txt', 'r')
cont1 = fn1.read()
print(cont1)
fn.close()
fn1.close()
