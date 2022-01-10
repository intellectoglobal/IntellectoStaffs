#FUNCTION


#1) 
# def greet():               ;def=syntax;greet=function name
#     print("hey bharani")
#     print("are you feeling better ")
# greet()                     ;this statement is CALLING the function

# #output:
# hey bharani
# are you feeling better 

#2)add two numbers in function

# def add(x,y):
#     c=x+y
#     print(c)
# add(9,9)    
#output:
18

#3)in function addition and subraction
# def add_sub(x,y):
#     c=x+y
#     d=x-y
#     return c,d
# result1,result2=add_sub(5,4)
# print(result1,result2)    
#output:
#9 1

#4)ID
def update(lst):
    lst(1)=25
    print(id(lst))
    print("lst",lst)
lst=[10,70,50]
update(lst) 
print(id(lst))
print("lst",lst)  

# #OUTPUT:

# 140729564101920
# x 8
# 140729564101984
# a 10