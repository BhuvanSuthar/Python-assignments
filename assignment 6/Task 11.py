from tkinter import *

root = Tk()
root.title("Calculator")
root.geometry("300x400")

expression = ""

def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = total
    except:
        equation.set("Error")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

equation = StringVar()
entry = Entry(root, textvariable=equation, font=('Arial', 20), bd=10, relief=RIDGE)
entry.grid(columnspan=4, ipadx=10, ipady=15, pady=10)

buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('.',4,1), ('=',4,2), ('+',4,3)
]

for (text, r, c) in buttons:
    if text == '=':
        Button(root, text=text, width=5, height=2, command=equalpress).grid(row=r, column=c)
    else:
        Button(root, text=text, width=5, height=2, command=lambda t=text: press(t)).grid(row=r, column=c)

Button(root, text='Clear', width=22, height=2, command=clear).grid(row=5, column=0, columnspan=4, pady=10)

root.mainloop()
