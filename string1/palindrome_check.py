text = input("Enter a string: ")

clean_text = text.lower().replace(" ", "")

reversed_text = ""
for ch in clean_text:
    reversed_text = ch + reversed_text

if clean_text == reversed_text:
    print("Palindrome")
else:
    print("Not a palindrome")
