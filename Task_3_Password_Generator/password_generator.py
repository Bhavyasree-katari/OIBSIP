import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

# pyperclip helps copy the password to clipboard
# string module has all the character sets we need


def generate_password():
    # first check if at least one character type is selected
    if not (upper_var.get() or lower_var.get() or num_var.get() or sym_var.get()):
        messagebox.showwarning("Oops!", "Please select at least one character type!")
        return

    # building the character pool based on what user selected
    chars = ""
    if upper_var.get():
        chars += string.ascii_uppercase   # A-Z
    if lower_var.get():
        chars += string.ascii_lowercase   # a-z
    if num_var.get():
        chars += string.digits            # 0-9
    if sym_var.get():
        chars += string.punctuation       # !@#$%^&*...

    # getting the length from the slider
    length = length_var.get()

    # generating the password by picking random characters
    password = "".join(random.choice(chars) for _ in range(length))

    # showing the password in the entry box
    password_var.set(password)

    # updating the strength indicator
    update_strength(password)


def update_strength(password):
    # checking how strong the password is based on length and variety
    score = 0

    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1
    if any(c in string.ascii_uppercase for c in password):
        score += 1
    if any(c in string.ascii_lowercase for c in password):
        score += 1
    if any(c in string.digits for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1

    # showing strength based on score
    if score <= 2:
        strength_label.config(text="Strength: Weak ❌", fg="#e74c3c")
    elif score <= 4:
        strength_label.config(text="Strength: Medium ⚠️", fg="#f39c12")
    else:
        strength_label.config(text="Strength: Strong 💪", fg="#2ecc71")


def copy_password():
    # copying the generated password to clipboard
    password = password_var.get()

    if not password:
        messagebox.showwarning("Nothing to copy!", "Please generate a password first!")
        return

    pyperclip.copy(password)
    messagebox.showinfo("Copied!", "Password copied to clipboard! ✅")


def update_length_label(val):
    # updating the length number shown next to slider
    length_label.config(text=f"Length: {int(float(val))}")


def generate_multiple():
    # generating 5 passwords at once and showing in a new window
    if not (upper_var.get() or lower_var.get() or num_var.get() or sym_var.get()):
        messagebox.showwarning("Oops!", "Please select at least one character type!")
        return

    chars = ""
    if upper_var.get():
        chars += string.ascii_uppercase
    if lower_var.get():
        chars += string.ascii_lowercase
    if num_var.get():
        chars += string.digits
    if sym_var.get():
        chars += string.punctuation

    length = length_var.get()

    # opening a new window to show multiple passwords
    multi_window = tk.Toplevel(root)
    multi_window.title("Multiple Passwords")
    multi_window.geometry("400x350")
    multi_window.config(bg="#1e1e2e")

    tk.Label(multi_window, text="🔑 Generated Passwords",
             font=("Arial", 14, "bold"),
             bg="#1e1e2e", fg="white").pack(pady=10)

    # generating and showing 5 passwords
    for i in range(5):
        pwd = "".join(random.choice(chars) for _ in range(length))

        frame = tk.Frame(multi_window, bg="#2d2d44")
        frame.pack(fill="x", padx=15, pady=4)

        tk.Label(frame, text=pwd,
                 font=("Courier", 11),
                 bg="#2d2d44", fg="#2ecc71",
                 padx=10, pady=6).pack(side="left")

        # copy button for each password
        tk.Button(frame, text="Copy",
                  font=("Arial", 9),
                  bg="#3498db", fg="white",
                  relief="flat", padx=8,
                  command=lambda p=pwd: pyperclip.copy(p)).pack(side="right", padx=5, pady=4)


# setting up the main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("450x520")
root.config(bg="#1e1e2e")
root.resizable(False, False)

# title
tk.Label(root, text="Password Generator 🔐",
         font=("Arial", 20, "bold"),
         bg="#1e1e2e", fg="white").pack(pady=20)

# length slider section
slider_frame = tk.Frame(root, bg="#1e1e2e")
slider_frame.pack(pady=5)

length_var = tk.IntVar(value=12)  # default length is 12
length_label = tk.Label(slider_frame, text="Length: 12",
                        font=("Arial", 12),
                        bg="#1e1e2e", fg="white")
length_label.pack()

slider = tk.Scale(slider_frame,
                  from_=4, to=32,
                  orient="horizontal",
                  variable=length_var,
                  command=update_length_label,
                  bg="#1e1e2e", fg="white",
                  highlightthickness=0,
                  troughcolor="#2d2d44",
                  activebackground="#3498db",
                  length=300)
slider.pack(pady=5)

# character type checkboxes
options_frame = tk.Frame(root, bg="#1e1e2e")
options_frame.pack(pady=10)

tk.Label(options_frame, text="Include:",
         font=("Arial", 12, "bold"),
         bg="#1e1e2e", fg="white").grid(row=0, column=0, columnspan=2, pady=5)

upper_var = tk.BooleanVar(value=True)
lower_var = tk.BooleanVar(value=True)
num_var = tk.BooleanVar(value=True)
sym_var = tk.BooleanVar(value=True)

# styling for checkboxes
check_style = {"font": ("Arial", 11), "bg": "#1e1e2e",
               "fg": "white", "activebackground": "#1e1e2e",
               "activeforeground": "white", "selectcolor": "#2d2d44"}

tk.Checkbutton(options_frame, text="Uppercase (A-Z)",
               variable=upper_var, **check_style).grid(row=1, column=0, sticky="w", padx=20, pady=3)

tk.Checkbutton(options_frame, text="Lowercase (a-z)",
               variable=lower_var, **check_style).grid(row=1, column=1, sticky="w", padx=20, pady=3)

tk.Checkbutton(options_frame, text="Numbers (0-9)",
               variable=num_var, **check_style).grid(row=2, column=0, sticky="w", padx=20, pady=3)

tk.Checkbutton(options_frame, text="Symbols (!@#$)",
               variable=sym_var, **check_style).grid(row=2, column=1, sticky="w", padx=20, pady=3)

# generate button
tk.Button(root, text="Generate Password 🔑",
          font=("Arial", 13, "bold"),
          bg="#3498db", fg="white",
          relief="flat", padx=20, pady=8,
          cursor="hand2",
          command=generate_password).pack(pady=15)

# password display box
password_var = tk.StringVar()
password_entry = tk.Entry(root,
                          textvariable=password_var,
                          font=("Courier", 13),
                          width=30,
                          bg="#2d2d44", fg="#2ecc71",
                          relief="flat",
                          justify="center",
                          insertbackground="white")
password_entry.pack(pady=5, ipady=8)

# strength indicator
strength_label = tk.Label(root, text="Strength: --",
                          font=("Arial", 12),
                          bg="#1e1e2e", fg="white")
strength_label.pack(pady=5)

# bottom buttons
button_frame = tk.Frame(root, bg="#1e1e2e")
button_frame.pack(pady=15)

tk.Button(button_frame, text="📋 Copy to Clipboard",
          font=("Arial", 11),
          bg="#2ecc71", fg="white",
          relief="flat", padx=15, pady=6,
          cursor="hand2",
          command=copy_password).grid(row=0, column=0, padx=10)

tk.Button(button_frame, text="🔑 Generate Multiple",
          font=("Arial", 11),
          bg="#9b59b6", fg="white",
          relief="flat", padx=15, pady=6,
          cursor="hand2",
          command=generate_multiple).grid(row=0, column=1, padx=10)

# starting the app
root.mainloop()
