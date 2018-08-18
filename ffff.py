from tkinter import *

root = Tk()
root.title("Calculator")
root.resizable(width=False, height=False)
root.iconbitmap('calculator.ico')

# Main variables
equation = StringVar()
equation.set("0")

equa = ""


# Program functions
def ButtonPress(num):
    global equa
    equa = equa + str(num)
    equation.set(equa)

def Clear():
    global equation
    equation.set("0")

def Equation():
    try:
        global equa
        global equation
        total = str(eval(equa))
        equation.set(total)
        equa = ""
    except:
        equation.set("error :(")
        equa = ""

# Widgets
calculation = Entry(root, textvariable=equation, font=("Verdana", 15, ), bd=12,
                 insertwidth=4, width=14, justify = RIGHT)
calculation.grid(columnspan=4)
# Numbers
button1 = Button(root, text='1', command=lambda: ButtonPress(1), bg="gainsboro",
                 bd=3,  padx=12, pady=5, font=("Helvetica", 14, "bold"))
button1.grid(row=1, column=0, sticky=W)
button2 = Button(root, text='2', command=lambda: ButtonPress(2), bg="gainsboro",
                 bd=3,  padx=12, pady=5, font=("Helvetica", 14, "bold"))
button2.grid(row=1, column=1, sticky=W)
button3 = Button(root, text='3', command=lambda: ButtonPress(3), bg="gainsboro",
                 bd=3,  padx=12, pady=5, font=("Helvetica", 14, "bold"))
button3.grid(row=1, column=2, sticky=W)
button4 = Button(root, text='4', command=lambda: ButtonPress(4), bg="gainsboro",
                 bd=3,  padx=12, pady=5, font=("Helvetica", 14, "bold"))
button4.grid(row=2, column=0, sticky=W)
button5 = Button(root, text='5', command=lambda: ButtonPress(5), bg="gainsboro",
                 bd=3,  padx=12, pady=5, font=("Helvetica", 14, "bold"))
button5.grid(row=2, column=1, sticky=W)
button6 = Button(root, text='6', command=lambda: ButtonPress(6), bg="gainsboro",
                 bd=3,  padx=12, pady=5, font=("Helvetica", 14, "bold"))
button6.grid(row=2, column=2, sticky=W)
button7 = Button(root, text='7', command=lambda: ButtonPress(7), bg="gainsboro",
                 bd=3,  padx=12, pady=5, font=("Helvetica", 14, "bold"))
button7.grid(row=3, column=0, sticky=W)
button8 = Button(root, text='8', command=lambda: ButtonPress(8), bg="gainsboro",
                 bd=3,  padx=12, pady=5, font=("Helvetica", 14, "bold"))
button8.grid(row=3, column=1, sticky=W)
button9 = Button(root, text='9', command=lambda: ButtonPress(9), bg="gainsboro",
                 bd=3,  padx=12, pady=5, font=("Helvetica", 14, "bold"))
button9.grid(row=3, column=2, sticky=W)
button0 = Button(root, text='0', command=lambda: ButtonPress(0), bg="gainsboro",
                 bd=3,  padx=12, pady=5, font=("Helvetica", 14, "bold"))
button0.grid(row=4, column=1, sticky=W)


button_plus = Button(root, text='+', command=lambda: ButtonPress('+'), bg="gray70",
                 bd=3,  padx=11, pady=5, font=("Helvetica", 14, "bold"))
button_plus.grid(row=1, column=3, sticky=W)
button_minus = Button(root, text='-', command=lambda: ButtonPress('-'), bg="gray70",
                 bd=3,  padx=11, pady=5, font=("Verdana", 14, "bold"))
button_minus.grid(row=2, column=3, sticky=W)
button_multiply = Button(root, text='*', command=lambda: ButtonPress('*'), bg="gray70",
                 bd=3,  padx=13, pady=5, font=("Helvetica", 14, "bold"))
button_multiply.grid(row=3, column=3, )
button_division = Button(root, text='/', command=lambda: ButtonPress('/'), bg="gray70",
                 bd=3,  padx=14, pady=5, font=("Helvetica", 14, "bold"))
button_division.grid(row=4, column=3, )
button_equal = Button(root, text='=', command=Equation, bg='orange',
                 bd=3, padx=12, pady=5, font=("Helvetica", 14))
button_equal.grid(row=4, column=2)
button_clear = Button(root, text='C', command=Clear, bg='gray70',
                 bd=3, padx=11, pady=5, font=("Helvetica", 14))
button_clear.grid(row=4, column=0)

root.mainloop()