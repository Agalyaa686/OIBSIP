import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip 

def check_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1

    if any(c.isupper() for c in password):
        score += 1

    if any(c.islower() for c in password):
        score += 1

    if any(c.isdigit() for c in password):
        score += 1

    if any(c in string.punctuation for c in password):
        score += 1

    if score <= 2:
        strength_label.config(text="Strength: Weak", fg="red")
    elif score == 3 or score == 4:
        strength_label.config(text="Strength: Medium", fg="orange")
    else:
        strength_label.config(text="Strength: Strong", fg="green")


def generate_password():
    try:
        length = int(length_entry.get())

        characters = ""

        if uppercase_var.get():
            characters += string.ascii_uppercase

        if lowercase_var.get():
            characters += string.ascii_lowercase

        if numbers_var.get():
            characters += string.digits

        if symbols_var.get():
            characters += string.punctuation

        if characters == "":
            messagebox.showerror(
                "Error",
                "Please select at least one character type."
            )
            return

        if length <= 0:
            messagebox.showerror(
                "Error",
                "Please enter a valid password length."
            )
            return

        password = "".join(random.choice(characters) for _ in range(length))

        password_entry.config(state="normal")
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)

        if not show_password_var.get():
            password_entry.config(show="*")

        check_strength(password)

    except ValueError:
        messagebox.showerror(
            "Error",
            "Please enter numbers only."
        )

def copy_password():
    password = password_entry.get()

    if password == "":
        messagebox.showwarning(
            "Warning",
            "Generate a password first."
        )
        return

    pyperclip.copy(password)

    messagebox.showinfo(
        "Copied",
        "Password copied to clipboard."
    )

def toggle_password():
    if show_password_var.get():
        password_entry.config(show="")
    else:
        password_entry.config(show="*")

root = tk.Tk()

root.title("Random Password Generator")

root.geometry("500x600")

root.resizable(False, False)

title = tk.Label(
    root,
    text="Random Password Generator",
    font=("Arial", 18, "bold")
)

title.pack(pady=20)

length_label = tk.Label(
    root,
    text="Password Length",
    font=("Arial", 12)
)

length_label.pack()

length_entry = tk.Entry(
    root,
    width=10,
    font=("Arial", 12)
)

length_entry.pack(pady=10)


uppercase_var = tk.BooleanVar()

lowercase_var = tk.BooleanVar(value=True)

numbers_var = tk.BooleanVar()

symbols_var = tk.BooleanVar()


tk.Checkbutton(
    root,
    text="Uppercase Letters (A-Z)",
    variable=uppercase_var
).pack(anchor="w", padx=120)

tk.Checkbutton(
    root,
    text="Lowercase Letters (a-z)",
    variable=lowercase_var
).pack(anchor="w", padx=120)

tk.Checkbutton(
    root,
    text="Numbers (0-9)",
    variable=numbers_var
).pack(anchor="w", padx=120)

tk.Checkbutton(
    root,
    text="Symbols (!@#$%)",
    variable=symbols_var
).pack(anchor="w", padx=120)


generate_button = tk.Button(
    root,
    text="Generate Password",
    command=generate_password,
    bg="green",
    fg="white",
    font=("Arial", 12, "bold"),
    width=20
)

generate_button.pack(pady=20)


password_entry = tk.Entry(
    root,
    width=35,
    font=("Arial", 12),
    justify="center",
    show="*"
)

password_entry.pack()


strength_label = tk.Label(
    root,
    text="Strength:",
    font=("Arial", 11, "bold")
)

strength_label.pack(pady=10)


show_password_var = tk.BooleanVar()

show_checkbox = tk.Checkbutton(
    root,
    text="Show Password",
    variable=show_password_var,
    command=toggle_password
)

show_checkbox.pack()

copy_button = tk.Button(
    root,
    text="Copy Password",
    command=copy_password,
    bg="blue",
    fg="white",
    font=("Arial", 12, "bold"),
    width=20
)

copy_button.pack(pady=20)

root.mainloop()