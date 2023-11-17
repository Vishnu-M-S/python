a=input("Enter the string: ")
count=0
for i in range(len(a)):
	if a[i]=='a':
		count+=1
print("Occurance of 'a' in the string: ",count)
