temp = [30,31,32,33,34,35,36,29,28,27,31,32,30,33,35,36,34,29,28,30,31,32,33,34,35,36,37,29,30,31]
print("Hottest:", max(temp))
print("Coldest:", min(temp))
avg = sum(temp)/len(temp)
print("Average:", avg)
above = 0
below = 0
for i in temp:
    if i > avg:
        above += 1
    elif i < avg:
        below += 1
print("Above Average:", above)
print("Below Average:", below)