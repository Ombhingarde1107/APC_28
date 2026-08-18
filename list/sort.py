numbers = []
for i in range(10):
    numbers.append(int(input("Enter number: ")))
numbers.sort()
print("Ascending:", numbers)
numbers.sort(reverse=True)
print("Descending:", numbers)