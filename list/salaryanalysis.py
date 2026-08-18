salary = [25000,35000,50000,60000,75000]
print("Highest:", max(salary))
print("Lowest:", min(salary))
print("Average:", sum(salary)/len(salary))
above = 0
below = 0
for i in salary:
    if i > 50000:
        above += 1
    if i < 30000:
        below += 1
print("Above 50000:", above)
print("Below 30000:", below)