import tkinter as tk
from tkinter import StringVar, Frame, Label, Entry, Button, RIDGE, RIGHT
import math

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.resizable(0, 0)
        self.var_txt = StringVar()
        self.var_operator = ''

        self.create_calculator_interface()

    def btn_click(self, num): 
        self.var_operator += str(num)
        self.var_txt.set(self.var_operator)

    def result(self):
        try:
            if self.var_operator[-1] in '+-*/':
                self.var_operator = self.var_operator[:-1]
            
            res = str(eval(self.var_operator))
            self.var_txt.set(res)
            self.var_operator = res
        except ZeroDivisionError:
            self.var_txt.set("Error")
            self.var_operator = ''
        except Exception:
            self.var_txt.set("Error")
            self.var_operator = ''

    def clear(self):
        self.var_txt.set('')
        self.var_operator = ''

    def backspace(self):
        self.var_operator = self.var_operator[:-1]
        self.var_txt.set(self.var_operator)

    def percentage(self):
        try:
            res = str(eval(self.var_operator) / 100)
            self.var_txt.set(res)
            self.var_operator = res
        except Exception:
            self.var_txt.set("Error")
            self.var_operator = ''

    def sqrt(self):
        try:
            res = str(math.sqrt(eval(self.var_operator)))
            self.var_txt.set(res)
            self.var_operator = res
        except Exception:
            self.var_txt.set("Error")
            self.var_operator = ''

    def create_calculator_interface(self):
        CalculatorFrame = Frame(self.root, bd=7, relief=RIDGE, bg="white")
        CalculatorFrame.place(x=2, y=2, width=260, height=400)

        lbl_calculator = Label(CalculatorFrame, text="Calculator", font="arial 20 bold", bg="Red")
        lbl_calculator.place(x=0, y=0, relwidth=1, height=50)

        txt_cal = Entry(CalculatorFrame, textvariable=self.var_txt, font="arial 30 bold", bg="lightgrey", fg="black", justify=RIGHT, state='readonly')
        txt_cal.place(x=0, y=50, relwidth=1)

        buttons = [
            ('7', 0, 100), ('8', 63, 100), ('9', 126, 100), ('/', 189, 100),
            ('4', 0, 160), ('5', 63, 160), ('6', 126, 160), ('*', 189, 160),
            ('1', 0, 217), ('2', 63, 217), ('3', 126, 217), ('-', 189, 217),
            ('0', 0, 277), ('.', 63, 277), ('+', 126, 277), ('=', 189, 277),
            ('C', 0, 337), ('←', 63, 337), ('%', 126, 337), ('√', 189, 337)
        ]

        for (text, x, y) in buttons:
            if text.isdigit() or text in ['+', '-', '*', '/', '.']:
                btn = Button(CalculatorFrame, text=text, font="arial 20 bold", bg="tan", fg="black", cursor="hand2", command=lambda t=text: self.btn_click(t))
            elif text == 'C':
                btn = Button(CalculatorFrame, text=text, font="arial 20 bold", bg="tan", fg="black", cursor="hand2", command=self.clear)
            elif text == '←':
                btn = Button(CalculatorFrame, text=text, font="arial 20 bold", bg="tan", fg="black", cursor="hand2", command=self.backspace)
            elif text == '=':
                btn = Button(CalculatorFrame, text=text, font="arial 20 bold", bg="tan", fg="black", cursor="hand2", command=self.result)
            elif text == '%':
                btn = Button(CalculatorFrame, text=text, font="arial 20 bold", bg="tan", fg="black", cursor="hand2", command=self.percentage)
            elif text == '√':
                btn = Button(CalculatorFrame, text=text, font="arial 20 bold", bg="tan", fg="black", cursor="hand2", command=self.sqrt)

            btn.place(x=x, y=y, width=63 if text != '=' else 61, height=60 if y != 337 else 50)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.geometry("265x410")
    root.mainloop()
