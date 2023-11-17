student={}
num=int(input("enter the number of students: "))
for i in range(0,num):
	name=input("Enter the name of student: ")
	age=input("Enter the age of student: ")
	grade=input("Enter the grade of student: ")
	student[name]=age,grade
print(student)
