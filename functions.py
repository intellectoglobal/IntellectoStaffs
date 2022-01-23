# def greet():
#     print("hello")
#     print("good morning")


# def add_sub(x,y):
#     c=x+y
#     d=x-y
#     return(c,d)

# # add(4,5)
# # greet()    

# # greet() 

# result1,result2=add_sub (4,5)
# print(result1,result2)

# def update(x):
#     x=8
#     print(id(x))
#     print("x",x)

# a=10
# print(id(a))
# update(a)
# print("a",a)     

def person(name,**data):
    print(name)
    print(data)

person('bharani",age=23,city='chennai',mob=0987654321)    