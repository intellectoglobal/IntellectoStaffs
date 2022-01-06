#HOW TO PRINT PATTERNS 
#1)# # # #
  # # # #
  # # # #
  # # # #

# to solve this pattern   : i is row j is coloumn
# for i in range(4): 
#     for j in range(4):
#         print("# ",end="") 
#     print()
#output:
 # # # # 
 # # # # 
 # # # #
 # # # #

#2)
#
# #
# # #
# # # #

# to solve this pattern   : i is row j is coloumn
# for i in range(4):
#      for j in range(i+1):
#          print("# ",end="")


#      print()

 #output:
#     
#
# #
# # #
# # # #

#3)# # # #
   # # #
   # #
   #
  #to get this pattern       : i is row j is coloumn 
# for i in range(4):
#     for j in range(4-i)  :
#         print("# ",end="")
#     print()

# output   
# # # # 
# # # 
# #
# 
  
 #4)#for else in python
# nums = [1,3,4,7,9]
# for num in nums:
#     if num % 5 ==0:
#         print(num)
#         break
# else:
#     print("not found")   
        
 #output:
# not found

#5)# to find prime number or not
num=23
for i in range(2,num):
    if num % i == 0:
        print("not prime")
        break
else:
    print("prime")    



        
        


