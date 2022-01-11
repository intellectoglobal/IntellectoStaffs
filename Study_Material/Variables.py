
#VARIABLES
#The equal sign is called the assignment operator and is used to assign a value to a Variable
x = 42
y = "Hello"
z = 3.42

#Variable Names
#You can use letters,numbers and underscores in variable names.But you can't use special symbols or start the name with a number
#e.g A_variable_name

#Working with variables:
#The variable stores it's value throughout the program
x = 7
print(x)
print(x+3)
print(x)
#output : 
7
10
7

spam = "eggs"
print(spam*3)
#output : eggseggseggs

#Variables can be reassigned as you want

x = 123.456
print(x)
x = "this is a string"
print(x+"!")
#output: 123.456
#output: this is a string!

age = 42
age = 24-6
print(age)
#output : 18

#A program can include multiple variables,which can be used together to produce a result.

a = 8
name = "Bob"
print(a * name)
#output: BobBobBobBobBobBobBobBob

#deleted variables can be reassigned 
x = 2
del x 
x = 8 
print(x)
#output : 8

#INPUT
#some programs need to take input from the user. the input() function prompts the user for input,and returns what they enter as a string
x = input ()
print(x)

name = input()
print("welcome,"+name)

#you can provide a string to input() between the parentheses ,producing a prompt message.
name = input("Enter your name: ")
print("Hello,"+name)

#we can use int function to make the input in numbers "int()"
age = int(input())
print(age)

#This will turn it from a string to an integer

#similarly we can also turn string to a float by adding float()

Height = float(input())
print(Height)

#Sometimes there is a need to use a number in a string concatenation.This can be done using the str() function,which converts a number to a string

age = 42
print("His age is " + str (age))

#You can use input() multiple times to take multiple user inputs
name = input()
age = input()
print(name +" is "+ age + " years old ")

#In-place operators:
#in-place operator let you write code like 'x=x+3' more concisely as 'x+=3'

x = 2
print(x)
x += 3
print(x)

#it can be used in any numerical operation(+,-,*,/,%,**,//)
x = 8
x -= 2
print(x)
x /= 3
print(x)
x **= 5
print(x) 

#you can also use string in in-place operations
x = "spam"
print(x)
x += "eggs"
print(x)

#we can use all 3 topics like variables,input and operators to make more complex program
miles = int(input())
km = miles*1.60934
print(km)

x = 35e3
print(x)