import tkinter as tk
from tkinter import messagebox
import math

class Calculator:
    def __init__(self):
        self.reset()

    def reset(self):
        self.current_result = 0
        self.last_operation = "="
        self.is_first_calculation = True

    def calculate(self, number):
        if self.last_operation == "+":
            self.current_result += number
        elif self.last_operation == "-":
            self.current_result -= number
        elif self.last_operation == "*":
            self.current_result *= number
        elif self.last_operation == "/":
            if number != 0:
                self.current_result /= number
            else:
                raise ArithmeticError("Error: Division by zero")
        elif self.last_operation == "sqrt":
            self.current_result = math.sqrt(self.current_result)
        elif self.last_operation == "log":
            self.current_result = math.log(self.current_result)
        elif self.last_operation == "sin":
            self.current_result = math.sin(math.radians(self.current_result))
        elif self.last_operation == "cos":
            self.current_result = math.cos(math.radians(self.current_result))
        elif self.last_operation == "tan":
            self.current_result = math.tan(math.radians(self.current_result))
        elif self.last_operation == "cbrt":
            self.current_result = math.cbrt(self.current_result)
        elif self.last_operation == "square":
            self.current_result = self.current_result ** 2
        elif self.last_operation == "cube":
            self.current_result = self.current_result ** 3
        elif self.last_operation == "=":
            self.current_result = number
        return self.current_result


class ScientificCalculatorGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.calculator = Calculator()

        self.title("Scientific Calculator")
        self.geometry("400x500")

        self.display = tk.Entry(self, font=("Arial", 24), borderwidth=2, relief="solid", justify="right")
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky="we")

        button_labels = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "=", "+",
            "sqrt", "log", "sin", "cos",
            "tan", "cbrt", "square", "cube",
            "Clear", "Ans", "Exit"
        ]

        row = 1
        col = 0
        for label in button_labels:
            button = tk.Button(self, text=label, font=("Arial", 18), command=lambda l=label: self.on_button_click(l))
            button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
            col += 1
            if col > 3:
                col = 0
                row += 1

        for i in range(4):
            self.grid_columnconfigure(i, weight=1)
            self.grid_rowconfigure(i + 1, weight=1)

    def on_button_click(self, label):
        if label == "Clear":
            self.display.delete(0, tk.END)
            self.calculator.reset()
        elif label == "Exit":
            self.quit()
        elif label == "Ans":
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, str(self.calculator.current_result))
        elif label in "0123456789.":
            self.display.insert(tk.END, label)
        else:
            try:
                if self.calculator.is_first_calculation:
                    self.calculator.current_result = float(self.display.get())
                    self.calculator.is_first_calculation = False
                else:
                    self.calculator.calculate(float(self.display.get()))
                self.calculator.last_operation = label
                self.display.delete(0, tk.END)
                if label == "=":
                    self.display.insert(tk.END, str(self.calculator.current_result))
                    self.calculator.is_first_calculation = True
            except (ValueError, ArithmeticError) as ex:
                messagebox.showerror("Error", str(ex))
                self.display.delete(0, tk.END)
                self.calculator.reset()


if __name__ == "__main__":
    app = ScientificCalculatorGUI()
    app.mainloop()
