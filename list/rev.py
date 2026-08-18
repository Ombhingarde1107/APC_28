numbers = [1,2,3,4,5]
rev = []
for i in range(len(numbers)-1, -1, -1):
    rev.append(numbers[i])
print(rev)