# list = [3,6,4,1,2,7]

# # for i in list:
# #     if i == 7:
# #         print(i)
# list.sort()

# print("The second largest number is" + list[-2])


# Python program to find largest
# number in a list
 
# list of numbers
list1 = [3,6,4,1,2,7,7]
 
mx=max(list1[0], 
    
    list1[1])
secondmax=min(list1[0],list1[1])
n =len(list1)
for i in range(2,n):
    if list1[i]>mx:
        secondmax=mx
        mx=list1[i]
    elif list1[i]>secondmax and \
        mx != list1[i]:
        secondmax=list1[i]
 
print("Second highest number is : ",\
      str(secondmax))

 
# # sorting the list
# list.sort()
 
# # printing the second last element
# print("Second largest element is:", list[-2])