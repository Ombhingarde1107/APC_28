password = input("Enter password: ")

has_uppercase = False
has_lowercase = False
has_digit = False
has_special = False

for ch in password:
    if "A" <= ch <= "Z":
        has_uppercase = True
    elif "a" <= ch <= "z":
        has_lowercase = True
    elif "0" <= ch <= "9":
        has_digit = True
    else:
        has_special = True

if len(password) >= 8 and has_uppercase and has_lowercase and has_digit and has_special:
    print("Valid password")
else:
    print("Invalid password")
