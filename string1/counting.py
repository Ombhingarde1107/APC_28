s=input("Enter string :")
vowels="aeiouAEIOU"
num=0
vowel=0
cons=0
space=0
for i in s:
    if i.isalpha():
        if i in vowels:
            vowel+=1
        else:
            cons+=1
    if i.isdigit():
        num+=1
    if i.isspace():
        space+=1
print("vowels :",vowel)
print("consonant :",cons)
print("digits :",num)
print("spaces :",space)