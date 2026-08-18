marks = [50,60,70,80,90,55,65,75,85,95,45,40,35,88,92,78,69,58,82,73]
highest = max(marks)
lowest = min(marks)
average = sum(marks)/len(marks)
above = 0
below = 0
for i in marks:
    if i > average:
        above += 1
    elif i < average:
        below += 1
print("Highest:", highest)
print("Lowest:", lowest)
print("Average:", average)
print("Above Average:", above)
print("Below Average:", below)