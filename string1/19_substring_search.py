main_string = input("Enter main string: ")
substring = input("Enter substring to search: ")

found = False

for i in range(len(main_string) - len(substring) + 1):
    match = True
    for j in range(len(substring)):
        if main_string[i + j] != substring[j]:
            match = False
            break

    if match:
        found = True
        break

if found:
    print("Substring exists")
else:
    print("Substring does not exist")
