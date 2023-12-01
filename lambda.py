print("Rectangle\n----------")
l=int(input("Enter length of rectangle: "))
b=int(input("Enter breadth of rectangle: "))
area=lambda x,y:x*y
per=lambda x,y:2*(x+y)
print("Area= ",area(l,b))
print("Perimeter= ",per(l,b))
print("\nSquare\n-------")
a=int(input("Enter side of square: "))
area=lambda z:z*z
per=lambda z:4*z
print("Area= ",area(a))
print("Perimeter= ",per(a))
