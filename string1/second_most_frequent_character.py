text = input("Enter a string: ")

if len(text) == 0:
    print("String is empty")
else:
    checked = ""
    most_char = ""
    second_char = ""
    most_count = 0
    second_count = 0

    for ch in text:
        if ch not in checked:
            count = 0
            for item in text:
                if item == ch:
                    count += 1

            if count > most_count:
                second_count = most_count
                second_char = most_char
                most_count = count
                most_char = ch
            elif count > second_count and count < most_count:
                second_count = count
                second_char = ch

            checked += ch

    if second_char == "":
        print("Second most frequent character not found")
    else:
        print("Second most frequent character:", second_char)
        print("Frequency:", second_count)
