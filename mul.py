num=int(input("enter the number : "))
end=int(input("enter the limit : "))
print("multiplication table of ",num," upto ",end," is :")
for i in range (1,end+1):
	print(num,"*",i,"=",num*i)
