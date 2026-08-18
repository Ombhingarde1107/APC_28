patients = (
    (1001, "Alice",   28, "A+"),
    (1002, "Bob",     45, "B-"),
    (1003, "Charlie", 33, "O+"),
    (1004, "Diana",   55, "A+"),
    (1005, "Edward",  40, "AB+"),
    (1006, "Fiona",   29, "B-"),
)
print("=" * 40)
print("(a) All Patient Records")
print("=" * 40)
print(f"{'ID':<6} {'Name':<12} {'Age':<5} {'Blood'}")
print("-" * 30)
for p in patients:
    print(f"{p[0]:<6} {p[1]:<12} {p[2]:<5} {p[3]}")
print("\n" + "=" * 40)
print("(b) Search Patient by ID")
print("=" * 40)
search_id = 1003
found = False
for p in patients:
    if p[0] == search_id:
        print(f"ID: {p[0]}, Name: {p[1]}, Age: {p[2]}, Blood: {p[3]}")
        found = True
        break
if not found:
    print(f"Patient ID {search_id} not found.")
print("\n" + "=" * 40)
print("(c) Total Number of Patients")
print("=" * 40)
print(f"Total patients: {len(patients)}")
print("\n" + "=" * 40)
print("(d) Patients with Blood Group 'A+'")
print("=" * 40)
target_bg = "A+"
print(f"{'ID':<6} {'Name':<12} {'Age':<5} {'Blood'}")
print("-" * 30)
for p in patients:
    if p[3] == target_bg:
        print(f"{p[0]:<6} {p[1]:<12} {p[2]:<5} {p[3]}")
