s=input("Enter the string: ")
count=0
for i in range (len(s)):
	if s[i]!=' ':
		count+=1
print("number of characters: ",count)
