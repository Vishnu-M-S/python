class rect:
	def __init__(self,length,breadth):
		self.length=length
		self.breadth=breadth
	def area(self):
		return self.length*self.breadth
	def per(self):
		return 2*(self.length+self.breadth)
a=int(input("Enter the length of rectangle: "))
b=int(input("Enter the breadth of rectangle: "))
obj=rect(a,b)
print("Area of the rectangle: ",obj.area())
print("Perimeter of the rectangle: ",obj.per())
