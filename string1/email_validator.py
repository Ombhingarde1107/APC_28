email = input("Enter email address: ")

is_valid = True

if email.count("@") != 1:
    is_valid = False
else:
    username, domain = email.split("@")

    if len(username) == 0 or len(domain) == 0:
        is_valid = False
    elif "." not in domain:
        is_valid = False
    elif domain.startswith(".") or domain.endswith("."):
        is_valid = False
    elif " " in email:
        is_valid = False

if is_valid:
    print("Valid email address")
else:
    print("Invalid email address")
