# Calculator Application

A modern, functional calculator application built with Python's Tkinter library. This calculator features a sleek dark theme with a user-friendly interface and various mathematical operations.

## Features

- Basic arithmetic operations: addition, subtraction, multiplication, division
- Advanced operations: square and square root
- Clear and equals functions
- Responsive UI with a dark theme

## Installation

To run this calculator application, you need Python installed on your system. This project uses Tkinter, which is included with Python by default.

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/your-username/calculator-app.git
    ```

2. **Navigate to the Project Directory**:

    ```bash
    cd calculator-app
    ```

3. **Run the Application**:

    ```bash
    python calculator.py
    ```

## Usage

When you run the application, a window will appear with the calculator interface. You can:

- Enter numbers and operators using the on-screen buttons.
- Use the `=` button to evaluate the expression.
- Use the `C` button to clear the current input.
- Use the `x²` button to calculate the square of the current number.
- Use the `√x` button to calculate the square root of the current number.

## Code Structure

- **`calculator.py`**: The main Python file containing the calculator implementation.
- **`README.md`**: This file.

## Code Example

Here's a snippet of the code:

```python
import tkinter as tk

LARGE_FONT_STYLE = ("Arial", 40, "bold")
DEFAULT_FONT_STYLE = ("Arial", 20)

COLOR_BACKGROUND = "#000000"  # Black background color for the window
COLOR_DISPLAY_BACKGROUND = "#000000"  # Black background color for the display area
COLOR_TEXT = "#FFFFFF"       # White text color
COLOR_BUTTON = "#333333"     # Dark gray button color
COLOR_BUTTON_TEXT = "#000000" # Black button text color
COLOR_BUTTON_HOVER = "#444444"  # Darker gray button hover color

class Calculator:
    def __init__(self):
        # Initialization code here
        pass

    # Other methods here

if __name__ == "__main__":
    calculator = Calculator()
    calculator.run()
