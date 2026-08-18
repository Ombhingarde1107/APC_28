text = input("Enter a string: ")

uppercase_count = 0
lowercase_count = 0

for ch in text:
    if "A" <= ch <= "Z":
        uppercase_count += 1
    elif "a" <= ch <= "z":
        lowercase_count += 1

print("Uppercase letters:", uppercase_count)
print("Lowercase letters:", lowercase_count)
