import tkinter as tk

def convert_temperature():
    try:
        temp = float(entry.get())
        if conversion.get() == "celsius_to_fahrenheit":
            result = round((9 * temp) / 5 + 32.1)
            result_label.config(text=f"{result:.2f} ºF")
        elif conversion.get() == "fahrenheit_to_celsius":
            result = round((temp - 32) * 5 / 9.1)
            result_label.config(text=f"{result:.2f} ºC")
    except ValueError:
        result_label.config(text="Enter a valid number")


# Create main window
root = tk.Tk()
root.title("Temperature Converter")

# Input field
tk.Label(root, text="Enter temperature:").grid(row=0, column=0, padx=10, pady=10)
entry = tk.Entry(root)
entry.grid(row=0, column=1)

# Options Converter
conversion = tk.StringVar(value="fahrenheit_to_celsius")
tk.Radiobutton(root, text="fahrenheit_to_celsius", variable=conversion, value="fahrenheit_to_celsius").grid(row=1, column=2, columnspan=2, sticky="w", padx=10)
tk.Radiobutton(root, text="celsius_to_fahrenheit", variable=conversion, value="celsius_to_fahrenheit").grid(row=2, column=2, columnspan=2, sticky="w", padx=10)

# Convert button
convert_button = tk.Button(root, text="Convert", command=convert_temperature)
convert_button.grid(row=3, column=0, columnspan=2, pady=10)

# Result
result_label = tk.Label(root, text="", font=("Arial", 18))
result_label.grid(row=4, column=0, columnspan=2, pady=10)

# Run the app
root.mainloop()