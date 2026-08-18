text = input("Enter a string: ")

if len(text) == 0:
    print("Encoded string:")
else:
    encoded = ""
    current_char = text[0]
    count = 1

    for i in range(1, len(text)):
        if text[i] == current_char:
            count += 1
        else:
            encoded += current_char + str(count)
            current_char = text[i]
            count = 1

    encoded += current_char + str(count)
    print("Encoded string:", encoded)
