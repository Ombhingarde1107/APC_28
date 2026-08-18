employees = (
    (201, "John Smith",   55000),
    (202, "Sarah Connor", 62000),
    (203, "Mike Ross",    48000),
    (204, "Rachel Zane",  71000),
)
print(f"{'EmpID':<8} {'Name':<16} {'Salary'}")
print("-" * 38)
for emp_id, emp_name, salary in employees:
    print(f"{emp_id:<8} {emp_name:<16} {salary:,}")
