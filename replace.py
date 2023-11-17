s=input("enter a string: ")
c=s[0]
s=c+s[1:].replace(c,'$')
print(s)
