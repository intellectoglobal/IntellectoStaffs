#1)prime number



# num=int(input("enter the number"))
# flag=False
# if num > 1:
#     # check for factors
#     for i in range(2, num):
#         if (num % i) == 0:
#             # if factor is found, set flag to True
#             flag = True
#             # break out of loop
#             break

# # check if flag is True
# if flag:
#     print(num, "is not a prime number")
# else:
#     print(num, "is a prime number")
#  #output::
#  enter the number4
# 4 is not a prime number
# enter the number5
# 5 is a prime number



# from typing import Reversible


# from typing import Reversible


# str=("nju")
# print(str)
# if Reversible :
#     print("PALINDROME")
# else:
#     print("NOT A PALINDROME")
x = "malayala"
 
w = ""
for i in x:
    w = i + w
 
if (x == w):
     print("Yes")
else:
     print("No")


# def fib(n):
#     a, b = 0, 1
#     while a < n:
#          print(a, end=' ')
#          a, b = b, a+b
#     print()
# fib(1000)

#output:
#0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987

#print sum of given digit

# a=int(input('enter the number'))
# b=int(input('enter 2nd number'))
# c=int(input('enter 3rd number'))
# x=a+b+c
# print(x)

# output:
# enter the number3
# enter 2nd number5
# enter 3rd number7
# 15