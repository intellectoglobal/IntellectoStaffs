def Greatest_Three_Numbers(num1,num2,num3):
 if (num1 >= num2) and (num1 >= num3):
   largest = num1
 elif (num2 >= num1) and (num2 >= num3):
   largest = num2
 else:
   largest = num3

 print("The largest number is", largest)

Greatest_Three_Numbers(num1 = 10,num3 = 20,num2 = 30)