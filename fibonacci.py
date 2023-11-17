def fib(n):
	c=0
	if n<2:
		return n
	else:
		c=fib(n-1)+fib(n-2)
		return c
a=int(input("enter the number of fibonacci numbers to print: "))
for i in range(0,a):
	print(fib(i),end=' ')
