##1. Write a Python program to create a file named student.txt and write the student's name,
###roll number, branch, and semester into the file.

name = input("Enter student name: ")
roll = input("Enter roll number: ")
branch = input("Enter branch: ")
semester = input("Enter semester: ")

file = open("student.txt", "w")

file.write("Name: " + name + "\n")
file.write("Roll Number: " + roll + "\n")
file.write("Branch: " + branch + "\n")
file.write("Semester: " + semester + "\n")

file.close()
print("Student information written successfully.")


##2. Write a program to open a text file and display its complete contents.

file=open("student.txt")
print(file.read())
file.close()

##3. Write a program to append additional student information to an existing file without
##deleting its previous contents.

file = open("student.txt", "a")

file.write("College: DYPcet\n")
file.write("City: Kolhapur\n")

file.close()
print("Information appended successfully.")

##4. Write a program to read a text file line by line and display each line separately.
file = open("student.txt", "r")

for line in file:
    print(line, end="")

file.close()

##5. Write a program to count and display the total number of lines present in a text file.
file = open("student.txt", "r")

lines = file.readlines()

print("Total number of lines:", len(lines))

file.close()

##6. Write a program to count the total number of words present in a text file.
file = open("student.txt", "r")

data = file.read()

words = data.split()

print("Total number of words:", len(words))
file.close()


##7. Write a program to count the total number of characters in a text file, including spaces.
file = open("student.txt", "r")

data = file.read()

print("Total number of characters:", len(data))

file.close()

##8. Write a program to read a text file and display its lines in reverse order.
file = open("student.txt", "r")

lines = file.readlines()

for line in reversed(lines):
    print(line, end="")

file.close()

##9. Read a text file and count the number of vowels and consonants present in the file.
file = open("student.txt", "r")
data = file.read()
vowels = 0
consonants = 0

for ch in data:
    if ch.isalpha():
        if ch.lower() in "aeiou":
            vowels = vowels + 1
        else:
            consonants = consonants + 1

print("Total vowels:", vowels)
print("Total consonants:", consonants)

file.close()

##10. Read a text file and calculate the number of alphabets, digits, spaces, and special
##characters.
file = open("student.txt", "r")

data = file.read()

alphabets = 0
digits = 0
spaces = 0
special = 0

for ch in data:
    if ch.isalpha():
        alphabets = alphabets + 1
    elif ch.isdigit():
        digits = digits + 1
    elif ch == " ":
        spaces = spaces + 1
    else:
        special = special + 1

print("Alphabets:", alphabets)
print("Digits:", digits)
print("Spaces:", spaces)
print("Special characters:", special)

file.close()
