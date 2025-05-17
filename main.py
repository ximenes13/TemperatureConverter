import tkinter as tk
from tkinter import ttk, messagebox

def convert_temperature():
    try:
        temp = float(entry.get())
        from_unit = from_unit_var.get()
        to_unit = to_unit_var.get()

        if from_unit == to_unit:
            result = temp
        elif from_unit == "Celsius":
            result = temp + 273.15 if to_unit == "Kelvin" else (temp * 9 / 5) + 32
        elif from_unit == "Fahrenheit":
            result = (temp - 32) * 5 / 9 if to_unit == "Celsius" else ((temp - 32) * 5 / 9) + 273.15
        elif from_unit == "Kelvin":
            result = temp - 273.15 if to_unit == "Celsius" else ((temp - 273.15) * 9 / 5) + 32

        result_label.config(text=f"{result:.2f} {to_unit}")
    except:
        messagebox.showerror("Error", "Please enter a valid temperature")

def clear_fields():
    entry.delete(0, tk.END)
    result_label.config(text="")

# Create main window
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("400x300")
root.resizable(False, False)

# Title
title = ttk.Label(root, text="Temperature Converter", font=("Arial", 20, "bold"))
title.grid(row=0, column=0, columnspan=3, pady=10)

# Input field
ttk.Label(root, text="Enter temperature:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
entry = ttk.Entry(root)
entry.grid(row=1, column=1, columnspan=2, sticky="w")

# Unit selectors
ttk.Label(root, text="From:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
from_unit_var = tk.StringVar(value="Celsius")
from_menu = ttk.OptionMenu(root, from_unit_var, "Celsius", "Celsius", "Fahrenheit", "Kelvin")
from_menu.grid(row=2, column=1, columnspan=2, sticky="w")

ttk.Label(root, text="To:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
to_unit_var = tk.StringVar(value="Fahrenheit")
to_menu = ttk.OptionMenu(root, to_unit_var, "Fahrenheit", "Celsius", "Fahrenheit", "Kelvin")
to_menu.grid(row=3, column=1, columnspan=2, sticky="w")

# Convert & Clean buttons
convert_button = ttk.Button(root, text="Convert", command=convert_temperature)
convert_button.grid(row=4, column=0, pady=15)

clear_button = ttk.Button(root, text="Clear", command=clear_fields)
clear_button.grid(row=4, column=1, pady=15)

# Result
result_label = ttk.Label(root, text="", font=("Arial", 18))
result_label.grid(row=5, column=0, columnspan=3, pady=10)

# Run the app
root.mainloop()