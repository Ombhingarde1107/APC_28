# 1. Extract all digits from a string
# import re
# text = "Room 204 has 18 chairs and 3 tables."
# print(re.findall(r"\d", text))
# 2. Words beginning with A or a
# import re
# sentence = "An apple and a banana are around a large area."
# print(re.findall(r"\b[Aa]\w*\b", sentence))
# 3. Count occurrences of vowels
# import re
# text = input("Enter a string: ")
# vowels = re.findall(r"[aeiou]", text, re.IGNORECASE)
# print("Vowels:", vowels)
# print("Count:", len(vowels))
# 4. Extract uppercase letters
# import re
# text = "Hello PYTHON World 2026!"
# print(re.findall(r"[A-Z]", text))
# 5. Identify spaces, tabs, and newline characters
# import re
# text = "Hello world\tPython\nRegular expressions"
# chars = re.findall(r"[ \t\n]", text)
# print([repr(ch) for ch in chars])
# print("Count:", len(chars))
# 6. Replace multiple consecutive spaces with one space
# import re
# text = "Python is easy to learn."
# print(re.sub(r" {2,}", " ", text))
# 7. Words containing exactly five characters
# import re
# sentence = "Apple mango grape peach banana."
# print(re.findall(r"\b[A-Za-z]{5}\b", sentence))
# 8. Words ending with the letter s
# import re
# sentence = "Roses are flowers and trees are plants."
# print(re.findall(r"\b\w+s\b", sentence, re.IGNORECASE))
# 9. Remove special characters but retain letters, digits, and spaces
# import re
# text = "Hello @Python! Version #3.12 costs $0."
# print(re.sub(r"[^A-Za-z0-9 ]", "", text))
# 10. Count words in a sentence
# import re
# sentence = "Python regular expressions are very useful."
# words = re.findall(r"\b\w+\b", sentence)
# print("Word count:", len(words))

# 11. Validate a 10-digit Indian mobile number
# import re
# mobile = input("Enter mobile number: ")
# if re.fullmatch(r"[6-9]\d{9}", mobile):
#  print("Valid mobile number")
# else:
#  print("Invalid mobile number")
# 12. Validate a reasonable email format

# 13. Extract dates in DD-MM-YYYY format
# import re
# text = "Events are on 05-12-2025 and 21-10-2026."
# print(re.findall(r"\b\d{2}-\d{2}-\d{4}\b", text))
# 14. Identify URLs beginning with http:// or https://
# import re
# text = "Visit https://example.com and http://test.org/page."
# print(re.findall(r"https?://[^\s]+", text))
# 15. Extract hashtags from a social media post
# import re
# post = "Learning #Python and #RegularExpressions is fun! #coding2026"
# print(re.findall(r"(?<!\w)#[A-Za-z0-9_]+", post))
# 16. Check password requirements
# import re
# password = input("Enter password: ")
# pattern = r"(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[^A-Za-z0-9]).{8,}"
# if re.fullmatch(pattern, password):
#  print("Password meets the requirements")
# else:
#  print("Use 8+ characters with uppercase, lowercase, digit, and special character")
# 17. Find consecutive repeated words, ignoring case
# import re
# sentence = "This is is a test TEST sentence."
# print(re.findall(r"\b(\w+)\s+\1\b", sentence, re.IGNORECASE))
# 18. Extract six-digit Indian PIN codes
# import re
# text = "PIN codes: 416001, 110001 and 560034."
# print(re.findall(r"(?<!\d)[1-9]\d{5}(?!\d)", text))
# 19. Check a common Indian vehicle registration format
# import re
# number = input("Enter vehicle number (e.g. MH12AB1234): ").upper()
# pattern = r"[A-Z]{2}\d{2}[A-Z]{1,2}\d{4}"
# print("Format looks valid" if re.fullmatch(pattern, number) else "Invalid vehicle number format")
# 20. Extract file extensions from filenames
# import re
# text = "Files: report.pdf, photo.jpeg, script.py and data.csv"
# print(re.findall(r"\b[\w-]+\.([A-Za-z0-9]+)\b", text))
# 21. Remove HTML tags, extra whitespace, and unwanted punctuation
# import re
# from html import unescape
# text = "<p>Hello, world!!!</p>\n<p>Python &amp; regex are useful.</p>"
# text = re.sub(r"<[^>]*>", " ", text)
# text = unescape(text)
# text = re.sub(r"[^\w\s.,!?'-]", "", text)
# text = re.sub(r"\s+", " ", text).strip()
# print(text)
# # Regex is not a complete HTML parser.
# Python Regular Expressions — 26 Programs Page 3
# 22. Extract invoice numbers, dates, and monetary amounts
# import re
# text = """Invoice No: INV-2026-104
# Date: 14-10-2026
# Total: Rs. 12,450.50"""
# invoice = re.search(r"Invoice\s*No\s*:\s*([A-Z0-9-]+)", text, re.I)
# date = re.search(r"Date\s*:\s*(\d{2}-\d{2}-\d{4})", text, re.I)
# amount = re.search(r"(?:Rs\.?|INR|■)\s*([\d,]+(?:\.\d{2})?)", text, re.I)
# print("Invoice:", invoice.group(1) if invoice else "Not found")
# print("Date:", date.group(1) if date else "Not found")
# print("Amount:", amount.group(1) if amount else "Not found")
# 23. Identify single-line comments in Python source code
# import re
# source = """x = 10 # set starting value
# # print the result
# text = "# this is inside a string"
# print(text) # display text"""
# comments = re.findall(r"(?m)^\s*#.*|#.*$", source)
# print("Possible comments:")
# for comment in comments:
#  print(comment)
# # Limitation: this simple regex may mistake # inside strings for comments.
# # Use Python's tokenize module for reliable source-code comment detection.
# 24. Validate product code ABC-1234-XY
# import re
# code = input("Enter product code: ")
# pattern = r"[A-Za-z]{3}-\d{4}-[A-Za-z]{2}"
# print("Valid product code" if re.fullmatch(pattern, code) else "Invalid product code")
# 25. Extract student names, roll numbers, and marks
# import re
# text = """Name: Asha, Roll: 101, Marks: 87
# Name: Rahul, Roll: 102, Marks: 91"""
# pattern = r"Name:\s*([A-Za-z ]+),\s*Roll:\s*(\d+),\s*Marks:\s*(\d+)"
# for name, roll, marks in re.findall(pattern, text):
#  print("Name:", name.strip(), "| Roll:", roll, "| Marks:", marks)
# 26. Extract DOI identifiers, years, emails, and URLs
# import re
# references = """Sharma, A. (2023). Data systems. doi:10.1234/example.567
# Contact: author@example.com
# Available at https://example.org/paper
# Another paper (2021), DOI 10.5555/abc.def.12"""
# dois = re.findall(r"\b10\.\d{4,9}/[-._;()/:A-Z0-9]+", references, re.I)
# years = re.findall(r"\b(?:19|20)\d{2}\b", references)
# emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", references)
# urls = re.findall(r"https?://[^\s]+", references)
# print("DOIs:", dois)
# print("Years:", years)
# print("Emails:", emails)
# print("URLs:", urls)