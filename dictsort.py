student = {}
num = int(input("Enter the number of students: "))

for i in range(0, num):
    name = input("Enter the name of student: ")
    grade = input("Enter the grade of student: ")
    student[name] = grade
l = list(student.items())
print("The list printed in ascending order by key: ")
print(l.sort())
