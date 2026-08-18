sentence = input("Enter a sentence: ")

words = sentence.split()
result = ""

for i in range(len(words) - 1, -1, -1):
    result += words[i]
    if i != 0:
        result += " "

print("Reversed sentence:", result)
