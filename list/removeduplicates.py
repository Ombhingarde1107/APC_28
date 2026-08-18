numbers = [1,2,2,3,4,3,5]
result = []
for i in numbers:
    if i not in result:
        result.append(i)
print(result)