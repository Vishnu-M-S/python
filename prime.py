lower=int(input("enter the lower limit : "))
upper=int(input("enter the upper limit : "))
print("the prime numbers in between",lower,"&",upper,"are :")
for i in range(lower,upper+1):
	if i == 0 or i == 1:
		continue
	j=2
	flag=0
	while j<=i/2:
		if i%j==0:
			flag=1
			break
		j=j+1
	if flag==0:
		print(i)
