students = ["Amit","Rahul","Priya"]
print("Total:", len(students))
name = input("Search student: ")
if name in students:
    print("Present")
else:
    print("Absent")
students.append("Sneha")
students.remove("Rahul")
print(students)