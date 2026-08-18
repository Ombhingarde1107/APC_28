sentence = input("Enter a sentence: ")
target_word = input("Enter word to count: ")

words = sentence.split()
count = 0

for word in words:
    if word == target_word:
        count += 1

print("Occurrences:", count)
