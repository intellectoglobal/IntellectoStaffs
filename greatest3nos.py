# find the greatest number among the three input numbers

# change the values of num1, num2 and num3
# for a different result
num1 = 56
num2 = 75
num3 = 34

# uncomment following lines to take three numbers from user

# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# num3 = float(input("Enter third number: "))

if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3

print("The largest number is", largest)