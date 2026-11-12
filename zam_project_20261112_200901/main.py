import tkinter as tk
from tkinter import ttk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Zam Calculator")
        self.geometry("300x400")
        self.resizable(False, False)
        self.configure(bg="#2E2E2E")

        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure('TButton', font=('Helvetica', 14), foreground='white', background='#4B4B4B', padding=5)
        self.style.map('TButton', background=[('active', '#5A5A5A')])

        self.expression = ""

        self.create_widgets()

    def create_widgets(self):
        self.display = tk.Entry(self, font=('Helvetica', 18), bd=10, relief=tk.RIDGE, justify='right')
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=20, sticky="nsew")

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2,2), ('*', 2,3),
            ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
            ('0',4,0), ('C',4,1), ('=',4,2), ('+',4,3),
        ]

        for (text, row, col) in buttons:
            action = lambda x=text: self.on_button_click(x)
            btn = ttk.Button(self, text=text, command=action)
            btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

        # Make grid cells expand evenly
        for i in range(5):
            self.rowconfigure(i, weight=1)
        for i in range(4):
            self.columnconfigure(i, weight=1)

    def on_button_click(self, char):
        if char == 'C':
            self.expression = ""
            self.display.delete(0, tk.END)
        elif char == '=':
            try:
                result = str(eval(self.expression))
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, result)
                self.expression = result
            except Exception:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
                self.expression = ""
        else:
            self.expression += str(char)
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, self.expression)

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
