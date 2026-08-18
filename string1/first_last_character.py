text = input("Enter a string: ")

if len(text) == 0:
    print("String is empty")
else:
    print("First character:", text[0])
    print("Last character:", text[len(text) - 1])
