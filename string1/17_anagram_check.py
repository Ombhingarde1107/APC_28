first = input("Enter first string: ")
second = input("Enter second string: ")

first = first.lower().replace(" ", "")
second = second.lower().replace(" ", "")

if len(first) != len(second):
    print("Not anagrams")
else:
    is_anagram = True

    for ch in first:
        count_first = 0
        count_second = 0

        for item in first:
            if item == ch:
                count_first += 1

        for item in second:
            if item == ch:
                count_second += 1

        if count_first != count_second:
            is_anagram = False
            break

    if is_anagram:
        print("Anagrams")
    else:
        print("Not anagrams")
