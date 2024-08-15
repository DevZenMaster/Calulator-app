import tkinter as tk

# Define theme colors
FONT_LARGE = ("Arial", 40, "bold")
FONT_SMALL = ("Arial", 16)
FONT_DIGITS = ("Arial", 24, "bold")
FONT_DEFAULT = ("Arial", 20)

COLOR_BACKGROUND = "#000000"  # Black background color for the window
COLOR_DISPLAY_BACKGROUND = "#000000"  # Black background color for the display area
COLOR_TEXT = "#FFFFFF"       # White text color
COLOR_BUTTON = "#333333"     # Dark gray button color
COLOR_BUTTON_TEXT = "#000000" # Black button text color
COLOR_BUTTON_HOVER = "#444444"  # Darker gray button hover color

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.resizable(0, 0)
        self.window.title("Calculator")
        self.window.configure(bg=COLOR_BACKGROUND)

        self.total_expr = ""
        self.current_expr = ""
        self.display_frame = self.create_display_frame()

        self.total_label, self.current_label = self.create_display_labels()

        self.digit_positions = {
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (3, 1), 2: (3, 2), 3: (3, 3),
            0: (4, 2), '.': (4, 1)
        }
        self.operators = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}
        self.buttons_frame = self.create_buttons_frame()

        self.buttons_frame.rowconfigure(0, weight=1)
        for x in range(1, 5):
            self.buttons_frame.rowconfigure(x, weight=1)
            self.buttons_frame.columnconfigure(x, weight=1)
        self.create_digit_buttons()
        self.create_operator_buttons()
        self.create_special_buttons()
        self.bind_keys()

    def bind_keys(self):
        self.window.bind("<Return>", lambda event: self.calculate_result())
        for key in self.digit_positions:
            self.window.bind(str(key), lambda event, digit=key: self.add_to_expression(digit))

        for key in self.operators:
            self.window.bind(key, lambda event, operator=key: self.add_operator(operator))

    def create_special_buttons(self):
        self.create_clear_button()
        self.create_equals_button()
        self.create_square_button()
        self.create_sqrt_button()

    def create_display_labels(self):
        total_label = tk.Label(self.display_frame, text=self.total_expr, anchor=tk.E, bg=COLOR_DISPLAY_BACKGROUND,
                               fg=COLOR_TEXT, padx=24, font=FONT_SMALL)
        total_label.pack(expand=True, fill='both')

        current_label = tk.Label(self.display_frame, text=self.current_expr, anchor=tk.E, bg=COLOR_DISPLAY_BACKGROUND,
                                 fg=COLOR_TEXT, padx=24, font=FONT_LARGE)
        current_label.pack(expand=True, fill='both')

        return total_label, current_label

    def create_display_frame(self):
        frame = tk.Frame(self.window, height=221, bg=COLOR_DISPLAY_BACKGROUND)
        frame.pack(expand=True, fill="both")
        return frame

    def add_to_expression(self, value):
        self.current_expr += str(value)
        self.update_current_label()

    def create_digit_buttons(self):
        for digit, pos in self.digit_positions.items():
            button = tk.Button(self.buttons_frame, text=str(digit), bg=COLOR_BUTTON, fg=COLOR_BUTTON_TEXT, font=FONT_DIGITS,
                               borderwidth=0, command=lambda x=digit: self.add_to_expression(x))
            button.grid(row=pos[0], column=pos[1], sticky=tk.NSEW)
            button.bind("<Enter>", lambda e, btn=button: btn.config(bg=COLOR_BUTTON_HOVER))
            button.bind("<Leave>", lambda e, btn=button: btn.config(bg=COLOR_BUTTON))

    def add_operator(self, operator):
        self.current_expr += operator
        self.total_expr += self.current_expr
        self.current_expr = ""
        self.update_total_label()
        self.update_current_label()

    def create_operator_buttons(self):
        i = 0
        for operator, symbol in self.operators.items():
            button = tk.Button(self.buttons_frame, text=symbol, bg=COLOR_BUTTON, fg=COLOR_BUTTON_TEXT, font=FONT_DEFAULT,
                               borderwidth=0, command=lambda x=operator: self.add_operator(x))
            button.grid(row=i, column=4, sticky=tk.NSEW)
            button.bind("<Enter>", lambda e, btn=button: btn.config(bg=COLOR_BUTTON_HOVER))
            button.bind("<Leave>", lambda e, btn=button: btn.config(bg=COLOR_BUTTON))
            i += 1

    def clear_all(self):
        self.current_expr = ""
        self.total_expr = ""
        self.update_current_label()
        self.update_total_label()

    def create_clear_button(self):
        button = tk.Button(self.buttons_frame, text="C", bg=COLOR_BUTTON, fg=COLOR_BUTTON_TEXT, font=FONT_DEFAULT,
                           borderwidth=0, command=self.clear_all)
        button.grid(row=0, column=1, sticky=tk.NSEW)
        button.bind("<Enter>", lambda e, btn=button: btn.config(bg=COLOR_BUTTON_HOVER))
        button.bind("<Leave>", lambda e, btn=button: btn.config(bg=COLOR_BUTTON))

    def calculate_square(self):
        self.current_expr = str(eval(f"{self.current_expr}**2"))
        self.update_current_label()

    def create_square_button(self):
        button = tk.Button(self.buttons_frame, text="x\u00b2", bg=COLOR_BUTTON, fg=COLOR_BUTTON_TEXT, font=FONT_DEFAULT,
                           borderwidth=0, command=self.calculate_square)
        button.grid(row=0, column=2, sticky=tk.NSEW)
        button.bind("<Enter>", lambda e, btn=button: btn.config(bg=COLOR_BUTTON_HOVER))
        button.bind("<Leave>", lambda e, btn=button: btn.config(bg=COLOR_BUTTON))

    def calculate_sqrt(self):
        self.current_expr = str(eval(f"{self.current_expr}**0.5"))
        self.update_current_label()

    def create_sqrt_button(self):
        button = tk.Button(self.buttons_frame, text="\u221ax", bg=COLOR_BUTTON, fg=COLOR_BUTTON_TEXT, font=FONT_DEFAULT,
                           borderwidth=0, command=self.calculate_sqrt)
        button.grid(row=0, column=3, sticky=tk.NSEW)
        button.bind("<Enter>", lambda e, btn=button: btn.config(bg=COLOR_BUTTON_HOVER))
        button.bind("<Leave>", lambda e, btn=button: btn.config(bg=COLOR_BUTTON))

    def calculate_result(self):
        self.total_expr += self.current_expr
        self.update_total_label()
        try:
            self.current_expr = str(eval(self.total_expr))
            self.total_expr = ""
        except Exception:
            self.current_expr = "Error"
        finally:
            self.update_current_label()

    def create_equals_button(self):
        button = tk.Button(self.buttons_frame, text="=", bg=COLOR_BUTTON, fg=COLOR_BUTTON_TEXT, font=FONT_DEFAULT,
                           borderwidth=0, command=self.calculate_result)
        button.grid(row=4, column=3, columnspan=2, sticky=tk.NSEW)
        button.bind("<Enter>", lambda e, btn=button: btn.config(bg=COLOR_BUTTON_HOVER))
        button.bind("<Leave>", lambda e, btn=button: btn.config(bg=COLOR_BUTTON))

    def create_buttons_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame

    def update_total_label(self):
        expr = self.total_expr
        for operator, symbol in self.operators.items():
            expr = expr.replace(operator, f' {symbol} ')
        self.total_label.config(text=expr)

    def update_current_label(self):
        self.current_label.config(text=self.current_expr[:11])

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    calculator = Calculator()
    calculator.run()
