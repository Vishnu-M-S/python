student = {}
num = int(input("Enter the number of students: "))

for i in range(num):
    name = input("Enter the name of student: ")
    grade = input("Enter the grade of student: ")
    student[name] = grade

sorted_student = sorted(student.items())

print("The list printed in ascending order by key: ")
for name, grade in sorted_student:
    print(f"{name}: {grade}")

