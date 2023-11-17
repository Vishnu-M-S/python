a=[]
l=int(input("Enter the limit "))
for i in range(0,l):
	e=input("enter the element: ")
	a.append(e)
max=len(a[0])
temp=a[0]
for i in range (1,l):
	if(len(a[i])>max):
		max=len(a[i])
		temp=a[i]
print("the longest word is: ",temp)
