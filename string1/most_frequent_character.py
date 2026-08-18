text = input("Enter a string: ")

if len(text) == 0:
    print("String is empty")
else:
    most_frequent = text[0]
    highest_count = 0

    for ch in text:
        count = 0
        for item in text:
            if item == ch:
                count += 1

        if count > highest_count:
            highest_count = count
            most_frequent = ch

    print("Most frequent character:", most_frequent)
    print("Frequency:", highest_count)
