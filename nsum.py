def sum(n):
	s=0
	for i in range(1,n+1):
		s=s+i
	return s
a=int(input("enter a number : "))
result=sum(a)
print("sum of first ",a," numbers : ",result) 
