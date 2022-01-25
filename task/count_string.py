x = "HELLO"
res = {i : x.count(i) for i in set(x)}
print ("The count of all characters in HELLO is : " +  str(res))
