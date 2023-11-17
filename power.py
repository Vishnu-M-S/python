def power(base,expo):
	if expo==0:
		return 1
	elif expo==1:
		return base
	else:
		return base*power(base,expo-1)
b=int(input("Enter base number: "))
e=int(input("Enter exponent: "))
print(power(b,e))
