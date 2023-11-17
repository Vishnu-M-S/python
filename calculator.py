def add(a,b):
	return a+b
def sub(a,b):
	return a-b
def mul(a,b):
	return a*b
def div(a,b):
	return a/b
def po(a,b):
	return a**b
def calculator(a,operation,b):
	if operation=="+":
		return add(a,b)
	elif operation=="-":
		return sub(a,b)
	elif operation=="*":
		return mul(a,b)
	elif operation=="/":
		return div(a,b)
	elif operation=="^":
		return po(a,b)
a=int(input("enter the first number: "))
b=int(input("enter the second number: "))
operation=input("Choose an arithmetic operation(+,-,*,/,^): ")
result=calculator(a,operation,b)
print(a,operation,b,"=",result)
