
# import tkinter as tk
# from tkinter import messagebox

# def register():
#     name = entry_name.get()
#     roll = entry_roll.get()
#     course = entry_course.get()
#     email = entry_email.get()

#     if name == "" or roll == "" or course == "" or email == "":
#         messagebox.showwarning("Warning", "Please fill all fields!")
#     else:
#         messagebox.showinfo(
#             "Registration Successful",
#             f"Student Registered Successfully!\n\n"
#             f"Name: {name}\n"
#             f"Roll No: {roll}\n"
#             f"Course: {course}\n"
#             f"Email: {email}"
#         )

# root = tk.Tk()
# root.title("Student Registration Form")
# root.geometry("400x400")
# root.resizable(False, False)

# title = tk.Label(
#     root,
#     text="Student Registration Form",
#     font=("Arial", 16, "bold")
# )
# title.pack(pady=20)

# tk.Label(root, text="Student Name:").pack()
# entry_name = tk.Entry(root, width=30)
# entry_name.pack(pady=5)

# tk.Label(root, text="Roll Number:").pack()
# entry_roll = tk.Entry(root, width=30)
# entry_roll.pack(pady=5)

# tk.Label(root, text="Course:").pack()
# entry_course = tk.Entry(root, width=30)
# entry_course.pack(pady=5)

# tk.Label(root, text="Email:").pack()
# entry_email = tk.Entry(root, width=30)
# entry_email.pack(pady=5)

# tk.Button(
#     root,
#     text="Register",
#     command=register,
#     bg="green",
#     fg="white",
#     width=15
# ).pack(pady=15)

# tk.Button(
#     root,
#     text="Clear",
#     command=lambda: [
#         entry_name.delete(0, tk.END),
#         entry_roll.delete(0, tk.END),
#         entry_course.delete(0, tk.END),
#         entry_email.delete(0, tk.END)
#     ],
#     width=15
# ).pack()

# root.mainloop()



# import tkinter as tk
# from tkinter import messagebox

# root = tk.Tk()
# root.title("Registration Form")
# root.geometry("300x300")

# tk.Label(root, text="Student Registration",
#          font=("Arial", 14, "bold")).pack(pady=10)

# tk.Label(root, text="Name").pack()
# name = tk.Entry(root)
# name.pack()

# tk.Label(root, text="Age").pack()
# age = tk.Entry(root)
# age.pack()

# tk.Label(root, text="Email").pack()
# email = tk.Entry(root)
# email.pack()

# def register():
#     n = name.get().strip()
#     a = age.get().strip()
#     e = email.get().strip()

#     if n == "" or a == "" or e == "":
#         messagebox.showerror("Error", "Fill all fields")
#     elif not n.replace(" ", "").isalpha():
#         messagebox.showerror("Error", "Enter a valid name")
#     elif not a.isdigit() or int(a) < 1 or int(a) > 120:
#         messagebox.showerror("Error", "Enter a valid age")
#     elif "@" not in e or "." not in e:
#         messagebox.showerror("Error", "Enter a valid email")
#     else:
#         messagebox.showinfo("Success", "Registration Successful!")

# tk.Button(root, text="Register",
#           command=register).pack(pady=15)

# root.mainloop()