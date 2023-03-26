import tkinter as tk
import tkinter.messagebox
from tkinter.constants import SUNKEN

calculator = tk.Tk()

calculator.title('Calculator@CodeClause')

frame = tk.Frame(master=calculator, bg="LightBlue", padx=13)

frame.pack()

entry = tk.Entry(master=frame, relief=SUNKEN, borderwidth=4, width=30)

entry.grid(row=0, column=0, columnspan=3, ipady=1, pady=1)


def user_click(user_input):
	entry.insert(tk.END, user_input)


def equal():
	try:
		y = str(eval(entry.get()))
		entry.delete(0, tk.END)
		entry.insert(0, y)

	except SyntaxError:
		tkinter.messagebox.showinfo("Syntax Error")


def clear():
	entry.delete(0, tk.END)

def erase():
	give_me = entry.get()
	last_input = len(give_me)-1
	entry.delete(last_input)

def decimal_binary():
	give_me= entry.get()
	change= int(give_me)
	binary= bin(change).replace("0b", "")
	entry.delete(0, tk.END)
	entry.insert(0, binary)

button_1 = tk.Button(master=frame, text='1', padx=15, pady=5, width=3, command=lambda: user_click(1))
button_1.grid(row=1, column=0, pady=2)

button_2 = tk.Button(master=frame, text='2', padx=15, pady=5, width=3, command=lambda: user_click(2))
button_2.grid(row=1, column=1, pady=2)

button_3 = tk.Button(master=frame, text='3', padx=15, pady=5, width=3, command=lambda: user_click(3))
button_3.grid(row=1, column=2, pady=2)

button_4 = tk.Button(master=frame, text='4', padx=15, pady=5, width=3, command=lambda: user_click(4))
button_4.grid(row=2, column=0, pady=2)

button_5 = tk.Button(master=frame, text='5', padx=15, pady=5, width=3, command=lambda: user_click(5))
button_5.grid(row=2, column=1, pady=2)

button_6 = tk.Button(master=frame, text='6', padx=15, pady=5, width=3, command=lambda: user_click(6))
button_6.grid(row=2, column=2, pady=2)

button_7 = tk.Button(master=frame, text='7', padx=15, pady=5, width=3, command=lambda: user_click(7))
button_7.grid(row=3, column=0, pady=2)

button_8 = tk.Button(master=frame, text='8', padx=15, pady=5, width=3, command=lambda: user_click(8))
button_8.grid(row=3, column=1, pady=2)

button_9 = tk.Button(master=frame, text='9', padx=15, pady=5, width=3, command=lambda: user_click(9))
button_9.grid(row=3, column=2, pady=2)

button_0 = tk.Button(master=frame, text='0', padx=15, pady=5, width=3, command=lambda: user_click(0))
button_0.grid(row=4, column=1, pady=2)

button_add = tk.Button(master=frame, text="+", padx=15, pady=5, width=3, command=lambda: user_click('+'))
button_add.grid(row=5, column=0, pady=2)

button_subtract = tk.Button(master=frame, text="-", padx=15, pady=5, width=3, command=lambda: user_click('-'))
button_subtract.grid(row=5, column=1, pady=2)

button_multiply = tk.Button(master=frame, text="*", padx=15, pady=5, width=3, command=lambda: user_click('*'))
button_multiply.grid(row=5, column=2, pady=2)

button_div = tk.Button(master=frame, text="/", padx=15, pady=5, width=3, command=lambda: user_click('/'))
button_div.grid(row=6, column=0, pady=2)

button_clear = tk.Button(master=frame, text="AC", fg='Red', bg='White', padx=15, pady=5, width=12, command=clear)
button_clear.grid(row=6, column=1, columnspan=2, pady=2)

button_equal = tk.Button(master=frame, text="=", padx=15, pady=5, width=3, command=equal)
button_equal.grid(row=7, column=0, columnspan=3, pady=2)

Decimal = tk.Button(master=frame, text='.', padx=8, pady=5, command=lambda: user_click('.'), height=1, width=5)
Decimal.grid(row=7, column=0)

button_erase = tk.Button(master=frame, text="X", fg='RED', bg='White', padx=15, pady=5, width=3, command=erase)
button_erase.grid(row=7, column=2, columnspan=2, pady=2)

button_modulo = tk.Button(master=frame, text='%', padx=8, pady=5, command=lambda: user_click('%'), height=1, width=5)
button_modulo.grid(row=4, column=0, pady=2)

button_empty = tk.Button(master=frame, text='pow', padx=8, pady=5, height=1, width=5, command=lambda: user_click('**'))
button_empty.grid(row=4, column=2, pady=2)

button_op = tk.Button(master=frame, text="(", padx=8, pady=5, command=lambda: user_click('('), height=1, width=5)
button_op.grid(row=8, column=0, pady=2)

button_cl = tk.Button(master=frame, text=")", padx=8, pady=5, command=lambda: user_click(')'), height=1, width=5)
button_cl.grid(row=8, column=1, pady=2)

button_binary = tk.Button(master=frame, text="bin", padx=8, pady=5, command=decimal_binary, height=1, width=5)
button_binary.grid(row=8, column=2, pady=2)


calculator.mainloop()
