student = {}
num = int(input("Enter the number of students: "))

for i in range(0, num):
    name = input("Enter the name of student: ")
    grade = input("Enter the grade of student: ")
    student[name] = grade

print("The list printed in ascending order by key: ")
print(sorted(student.items()))
print("The list printed in descending order by key: ")
print(sorted(student.items(), key=lambda x: x[0], reverse=True))
print("The list printed in ascending order by value: ")
print(sorted(student.items(), key=lambda x: x[1]))
print("The list printed in descending order by value: ")
print(sorted(student.items(), key=lambda x: x[1], reverse=True))
