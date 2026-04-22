import tkinter as tk
from tkinter import messagebox
import json
import os
import datetime
import matplotlib.pyplot as plt

# i'm storing all user data in this json file
# so it saves even after closing the app
DATA_FILE = "bmi_data.json"


def load_data():
    # loading existing data from file if it exists
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}


def save_data(data):
    # saving data back to the json file
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)


def calculate_bmi(weight, height):
    # simple bmi formula: weight divided by height squared
    return round(weight / (height ** 2), 2)


def get_category(bmi):
    # checking which category the bmi falls into
    if bmi < 18.5:
        return "Underweight", "#3498db"  # blue
    elif bmi < 25:
        return "Normal", "#2ecc71"       # green
    elif bmi < 30:
        return "Overweight", "#f39c12"   # yellow
    else:
        return "Obese", "#e74c3c"        # red


def on_calculate():
    # this runs when user clicks the calculate button
    name = name_entry.get().strip()
    weight_str = weight_entry.get().strip()
    height_str = height_entry.get().strip()

    # making sure all fields are filled
    if not name or not weight_str or not height_str:
        messagebox.showwarning("Missing Info", "Please fill in all fields!")
        return

    try:
        weight = float(weight_str)
        height = float(height_str)

        # basic validation so no weird numbers get in
        if weight <= 0 or height <= 0:
            messagebox.showerror("Invalid Input", "Weight and height must be positive numbers!")
            return

        if weight > 300 or height > 3:
            messagebox.showerror("Invalid Input", "Please enter realistic weight (kg) and height (m) values!")
            return

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers for weight and height!")
        return

    # calculating bmi and getting category
    bmi = calculate_bmi(weight, height)
    category, color = get_category(bmi)

    # showing result on screen with color
    result_label.config(
        text=f"Your BMI: {bmi}",
        fg=color
    )
    category_label.config(
        text=f"Category: {category}",
        fg=color
    )

    # saving this entry to the json file
    data = load_data()
    if name not in data:
        data[name] = []

    data[name].append({
        "bmi": bmi,
        "category": category,
        "weight": weight,
        "height": height,
        "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    })

    save_data(data)
    messagebox.showinfo("Saved!", f"BMI saved for {name} successfully!")


def show_history():
    # showing all past bmi entries for the entered name
    name = name_entry.get().strip()

    if not name:
        messagebox.showwarning("Missing Name", "Please enter your name first!")
        return

    data = load_data()

    if name not in data or len(data[name]) == 0:
        messagebox.showinfo("No History", f"No BMI history found for {name}!")
        return

    # building a nice history text to display
    history_text = f"BMI History for {name}:\n\n"
    for i, entry in enumerate(data[name], 1):
        history_text += f"{i}. Date: {entry['date']}\n"
        history_text += f"   BMI: {entry['bmi']} — {entry['category']}\n"
        history_text += f"   Weight: {entry['weight']} kg | Height: {entry['height']} m\n\n"

    # opening a new window to show history
    history_window = tk.Toplevel(root)
    history_window.title(f"History - {name}")
    history_window.geometry("400x400")
    history_window.config(bg="#1e1e2e")

    tk.Label(history_window, text=f"📋 History for {name}",
             font=("Arial", 14, "bold"), bg="#1e1e2e", fg="white").pack(pady=10)

    text_box = tk.Text(history_window, font=("Arial", 11),
                       bg="#2d2d44", fg="white", relief="flat", padx=10, pady=10)
    text_box.pack(fill="both", expand=True, padx=10, pady=10)
    text_box.insert("end", history_text)
    text_box.config(state="disabled")  # making it read only


def show_graph():
    # showing a line graph of bmi trend over time
    name = name_entry.get().strip()

    if not name:
        messagebox.showwarning("Missing Name", "Please enter your name first!")
        return

    data = load_data()

    if name not in data or len(data[name]) < 2:
        messagebox.showinfo("Not Enough Data", "Need at least 2 entries to show a graph!")
        return

    # getting dates and bmi values for the graph
    dates = [entry["date"] for entry in data[name]]
    bmis = [entry["bmi"] for entry in data[name]]

    # plotting the graph
    plt.figure(figsize=(8, 5))
    plt.plot(dates, bmis, marker="o", color="#3498db", linewidth=2, markersize=8)

    # adding color zones for bmi categories
    plt.axhspan(0, 18.5, alpha=0.1, color="blue", label="Underweight")
    plt.axhspan(18.5, 25, alpha=0.1, color="green", label="Normal")
    plt.axhspan(25, 30, alpha=0.1, color="yellow", label="Overweight")
    plt.axhspan(30, 50, alpha=0.1, color="red", label="Obese")

    plt.title(f"BMI Trend for {name}", fontsize=14)
    plt.xlabel("Date")
    plt.ylabel("BMI")
    plt.xticks(rotation=45, ha="right")
    plt.legend(loc="upper right")
    plt.tight_layout()
    plt.show()


# setting up the main window
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("420x500")
root.config(bg="#1e1e2e")
root.resizable(False, False)

# title at the top
tk.Label(root, text="BMI Calculator 🏋️",
         font=("Arial", 20, "bold"),
         bg="#1e1e2e", fg="white").pack(pady=20)

# input frame to hold all the fields
input_frame = tk.Frame(root, bg="#1e1e2e")
input_frame.pack(pady=10)

# name field
tk.Label(input_frame, text="Name :",
         font=("Arial", 12), bg="#1e1e2e", fg="white").grid(row=0, column=0, padx=10, pady=8, sticky="w")
name_entry = tk.Entry(input_frame, font=("Arial", 12), width=20,
                      bg="#2d2d44", fg="white", relief="flat", insertbackground="white")
name_entry.grid(row=0, column=1, padx=10, pady=8)

# weight field
tk.Label(input_frame, text="Weight (kg) :",
         font=("Arial", 12), bg="#1e1e2e", fg="white").grid(row=1, column=0, padx=10, pady=8, sticky="w")
weight_entry = tk.Entry(input_frame, font=("Arial", 12), width=20,
                        bg="#2d2d44", fg="white", relief="flat", insertbackground="white")
weight_entry.grid(row=1, column=1, padx=10, pady=8)

# height field
tk.Label(input_frame, text="Height (m) :",
         font=("Arial", 12), bg="#1e1e2e", fg="white").grid(row=2, column=0, padx=10, pady=8, sticky="w")
height_entry = tk.Entry(input_frame, font=("Arial", 12), width=20,
                        bg="#2d2d44", fg="white", relief="flat", insertbackground="white")
height_entry.grid(row=2, column=1, padx=10, pady=8)

# calculate button
tk.Button(root, text="Calculate BMI",
          font=("Arial", 13, "bold"),
          bg="#3498db", fg="white",
          relief="flat", padx=20, pady=8,
          cursor="hand2",
          command=on_calculate).pack(pady=20)

# result labels that change color based on bmi
result_label = tk.Label(root, text="Your BMI: --",
                        font=("Arial", 16, "bold"),
                        bg="#1e1e2e", fg="white")
result_label.pack()

category_label = tk.Label(root, text="Category: --",
                          font=("Arial", 13),
                          bg="#1e1e2e", fg="white")
category_label.pack(pady=5)

# bottom buttons for history and graph
button_frame = tk.Frame(root, bg="#1e1e2e")
button_frame.pack(pady=20)

tk.Button(button_frame, text="📋 View History",
          font=("Arial", 11),
          bg="#2ecc71", fg="white",
          relief="flat", padx=15, pady=6,
          cursor="hand2",
          command=show_history).grid(row=0, column=0, padx=10)

tk.Button(button_frame, text="📈 Show Graph",
          font=("Arial", 11),
          bg="#9b59b6", fg="white",
          relief="flat", padx=15, pady=6,
          cursor="hand2",
          command=show_graph).grid(row=0, column=1, padx=10)

# starting the app
root.mainloop()
