def pal(s):
	return(s==s[::-1])
a=str(input("Enter a string to check: "))
if(pal(a)):
	print("It is a palindrome")
else:
	print("It is not a palindrome")
