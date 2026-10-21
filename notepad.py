
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog

root = tk.Tk()
root.title("My Notepad")
root.geometry("700x500")

# Text area
text = tk.Text(root, font=("Arial", 12), undo=True)
text.pack(expand=True, fill="both")

# New file
def new_file():
    text.delete("1.0", tk.END)
    root.title("My Notepad - New File")

# Open file
def open_file():
    file = filedialog.askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if file:
        with open(file, "r", encoding="utf-8") as f:
            text.delete("1.0", tk.END)
            text.insert("1.0", f.read())
        root.title(file)

# Save file
def save_file():
    file = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")]
    )
    if file:
        with open(file, "w", encoding="utf-8") as f:
            f.write(text.get("1.0", "end-1c"))
        messagebox.showinfo("Saved", "File saved successfully!")

# Cut, Copy, Paste
def cut():
    text.event_generate("<<Cut>>")

def copy():
    text.event_generate("<<Copy>>")

def paste():
    text.event_generate("<<Paste>>")

def select_all():
    text.tag_add("sel", "1.0", "end-1c")

# Find word
def find_word():
    word = simpledialog.askstring("Find", "Enter word:")
    if word:
        text.tag_remove("found", "1.0", tk.END)
        start = "1.0"
        while True:
            pos = text.search(word, start, tk.END, nocase=True)
            if not pos:
                break
            end = f"{pos}+{len(word)}c"
            text.tag_add("found", pos, end)
            start = end
        text.tag_config("found", background="yellow")

# Change font size
def change_size():
    size = simpledialog.askinteger(
        "Font Size", "Enter size (8 to 40):",
        minvalue=8, maxvalue=40
    )
    if size:
        text.config(font=("Arial", size))

# Word wrap
def word_wrap():
    if text.cget("wrap") == "none":
        text.config(wrap="word")
    else:
        text.config(wrap="none")

# Character count
def count_chars():
    count = len(text.get("1.0", "end-1c"))
    messagebox.showinfo("Character Count", f"Characters: {count}")

# Menu bar
menu = tk.Menu(root)
root.config(menu=menu)

# File menu
file_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.destroy)

# Edit menu
edit_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_command(label="Paste", command=paste)
edit_menu.add_command(label="Select All", command=select_all)
edit_menu.add_command(label="Find", command=find_word)
edit_menu.add_command(label="Clear All", command=new_file)

# Format menu
format_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Format", menu=format_menu)
format_menu.add_command(label="Change Font Size", command=change_size)
format_menu.add_command(label="Word Wrap", command=word_wrap)

# Tools menu
tools_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Tools", menu=tools_menu)
tools_menu.add_command(label="Character Count", command=count_chars)

# Keyboard shortcuts
root.bind("<Control-n>", lambda e: new_file())
root.bind("<Control-o>", lambda e: open_file())
root.bind("<Control-s>", lambda e: save_file())
root.bind("<Control-f>", lambda e: find_word())

root.mainloop()
