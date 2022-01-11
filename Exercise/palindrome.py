# def isPalindrome(s):
# 	return s == s[::-1]
# s = "malayalam"
# ans = isPalindrome(s)
# if ans:
# 	print("Yes")
# else:
# 	print("No")



str = input("Enter the input: ")  
# str = 'MAM'
rev = reversed(str)
if list(str) == list(rev):
   print("PALINDROME !")
else:
   print("NOT PALINDROME !")