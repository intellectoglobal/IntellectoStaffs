
# nterms = int(input("How many terms? "))
# n1, n2 = 0, 1
# count = 0
# if nterms <= 0:
#    print("Please enter a positive integer")
# elif nterms == 1:
#    print("Fibonacci sequence upto",nterms,":")
#    print(n1)
# else:
#    print("Fibonacci sequence:")
#    while count < nterms:
#        print(n1)
#        nth = n1 + n2
#        n1 = n2
#        n2 = nth
#        count += 1
# Python 3: Fibonacci series up to n
def fib(n):
     a, b = 0, 1
     while a < n:
         print(a, end=' ')
         a, b = b, a+b
     print()
fib(100)