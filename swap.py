print("using temperory variable")
a=5
b=10
print("a before swapping:",a)
print("b before swapping:",b)
temp=a
a=b
b=temp
print("a after swapping:",a)
print("b after swapping:",b)
print("without using temperory variable")
a=5
b=10
print("a before swapping:",a)
print("b before swapping:",b)
a=a+b
b=a-b
a=a-b
print("a after swapping:",a)
print("b after swapping:",b)
