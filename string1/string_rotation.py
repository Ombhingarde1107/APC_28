first = input("Enter first string: ")
second = input("Enter second string: ")

if len(first) != len(second):
    print("No")
else:
    combined = first + first
    found = False

    for i in range(len(combined) - len(second) + 1):
        match = True
        for j in range(len(second)):
            if combined[i + j] != second[j]:
                match = False
                break

        if match:
            found = True
            break

    if found:
        print("Yes")
    else:
        print("No")
