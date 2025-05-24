# 🌡️ Temperature Converter App with Python + Tkinter

This project is a simple desktop application built using Python and Tkinter, designed to convert temperature values between Celsius, Fahrenheit, and Kelvin. Users can input a numeric temperature, select the input and output units, and get instant results in a user-friendly interface.

---

## 🚀 Features

🌡️ Converts temperatures between Celsius, Fahrenheit, and Kelvin (bidirectional) <br>
📥 Input field for entering any temperature value <br>
🔘 Dropdown menus to select “From” and “To” units <br>
🎯 "Convert" button to execute the calculation <br>
🧹 "Clear" button to reset the input and output fields <br>
📢 Displays formatted output with units (e.g., "72.60 Fahrenheit") <br>
❌ Error handling for invalid (non-numeric) input <br>
🪟 Clean and simple layout using Tkinter widgets <br>
🛠️ Easy to extend with more unit types or conversion logic <br>

---

## 🖥️ Technologies Used

- Python 3.x
- Tkinter (for GUI interface)
- PyCharm (recommended IDE)

---

## 📂 Project Structure

- **main.py**: Main application script. Handles both UI layout and logic. Key responsibilities:

🖼️ Builds GUI layout using labels, entries, buttons, and dropdown menus <br>
🔁 Uses .config() to dynamically update result text <br>
🧠 Performs conversion logic between Celsius, Fahrenheit, and Kelvin <br>
🧹 Includes a Clear button to reset both input and output <br>
❌ Handles ValueError when user input is not a number <br>
📏 Uses precise float conversion and formatting for output display <br>


---

## 🛠️ Setup

### Step 1: Clone the Repository

To get started, clone this repository to your local machine using the following command:

`git clone https://github.com/your-username/TemperatureConverter.git`

### Step 2: Dependencies

Make sure you have Python 3.x installed. You can check your version with:

`python3 --version`

### Step 3: Run the project

Once you've installed the dependencies, you can run the main Python script to generate and interact with the calculator app.

`python3 main.py`

---

## 🤝 Contributing

Contributions are welcome! If you'd like to improve the project, feel free to:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Make your changes and commit them (`git commit -m 'Add new feature'`).
4. Push to your branch (`git push origin feature-name`).
5. Submit a pull request.

If you find bugs or have feature requests, please [open an issue](https://github.com/ximenes13/Calculator/issues).
