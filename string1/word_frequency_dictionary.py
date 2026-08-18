paragraph = input("Enter a paragraph: ")

words = paragraph.lower().split()
frequency = {}

for word in words:
    clean_word = ""
    for ch in word:
        if ("a" <= ch <= "z") or ("0" <= ch <= "9"):
            clean_word += ch

    if clean_word != "":
        if clean_word in frequency:
            frequency[clean_word] += 1
        else:
            frequency[clean_word] = 1

for word in frequency:
    print(word, ":", frequency[word])
