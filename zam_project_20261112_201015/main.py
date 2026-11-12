import tkinter as tk
from tkinter import ttk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.geometry("300x400")
        self.resizable(False, False)

        self.style = ttk.Style(self)
        self.style.theme_use('clam')
        # style configuration
        self.style.configure('TButton', font=('Arial', 18), padding=10)
        self.style.configure('Display.TEntry', font=('Arial', 24), foreground='black')

        self.display = ttk.Entry(self, justify='right', style='Display.TEntry')
        self.display.grid(row=0, column=0, columnspan=4, sticky='nsew', padx=5, pady=5)
        self.display.insert(0, "0")
        self.current = ''

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
            ('=', 5, 0, 4),
        ]

        for btn in buttons:
            text = btn[0]
            row = btn[1]
            column = btn[2]
            colspan = btn[3] if len(btn) > 3 else 1
            action = lambda x=text: self.on_click(x)
            ttk.Button(self, text=text, command=action).grid(row=row, column=column, columnspan=colspan, sticky='nsew', padx=2, pady=2)

        for i in range(6):
            self.rowconfigure(i, weight=1)
        for i in range(4):
            self.columnconfigure(i, weight=1)

    def on_click(self, char):
        if char == 'C':
            self.current = ''
            self.display.delete(0, tk.END)
            self.display.insert(0, '0')
        elif char == '=':
            try:
                result = str(eval(self.current))
                self.display.delete(0, tk.END)
                self.display.insert(0, result)
                self.current = result
            except Exception:
                self.display.delete(0, tk.END)
                self.display.insert(0, 'Error')
                self.current = ''
        else:
            if self.current == '0':
                self.current = ''
            self.current += char
            self.display.delete(0, tk.END)
            self.display.insert(0, self.current)

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
