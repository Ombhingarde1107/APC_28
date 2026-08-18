patients = ["Ravi", "Amit"]
ages = [25, 40]
patients.append("Sneha")
ages.append(30)
name = input("Search patient: ")
if name in patients:
    index = patients.index(name)
    print("Age:", ages[index])
else:
    print("Patient not found")
patients.remove("Amit")
ages.pop(1)
print("Patients:", patients)
print("Ages:", ages)
print("Total Patients:", len(patients))