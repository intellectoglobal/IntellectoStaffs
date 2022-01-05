#for loop using if 
# i=1
# for i in range(1,11):
#     if i%2!=0:
#         print(i)
# #output        
1
2
3
6
9
#print all the perfect square numbers between 1 to 500

'''
for i in range(1,500):
    x = i ** 2
 #   if x >= 500:
        break
    else:
        print(x) 
# output:1
# 4 
# 9 
# 16
# 25
# 36
# 49
# 64
# 81
# 100
# 121
# 169
# 1964
# 225
# 256
# 289
# 324
# 361
# 400
# 441
# 484

'''
6

 #break statement : With the break statement we can stop the loop before it has looped through all the items
# i=1
# x=int(input("how many candies you needed?"))
# av=5
# while i<=5:
#     if i>av:
#         break
#     print("candy")
#     i=i+1
#output:
# how many candies you needed?7
# candy
# candy
# candy
# candy
# candy
#
# 
#  #continue statement:With the continue statement we can stop the current iteration of the loop, and continue with the next
# #i=1
# for i in range(0,20):
#     if i%8!=0 and i%9!=0:
#         print(i) 
#         continue
# output:
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 10
# 11
# 12
# 13
# 14
# 15
# 16
# 17
# 18
# 19

#loop statementfor loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.
for i in range(1,11):
    if(i%2!=0):
        pass
    else:
        print(i)




