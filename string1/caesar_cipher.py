message = input("Enter message: ")
shift = int(input("Enter shift value: "))
choice = input("Enter E for encryption or D for decryption: ")

if choice == "D" or choice == "d":
    shift = -shift

result = ""

for ch in message:
    if "A" <= ch <= "Z":
        result += chr((ord(ch) - ord("A") + shift) % 26 + ord("A"))
    elif "a" <= ch <= "z":
        result += chr((ord(ch) - ord("a") + shift) % 26 + ord("a"))
    else:
        result += ch

print("Result:", result)
