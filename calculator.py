import tkinter as tk
from tkinter import *

window = tk.Tk()
window.title("Calculator")
window.geometry("500x600+100+200")
window.resizable(False, False)
window.configure(bg="#17161b")

equation = ""

def show(value):
    global equation
    equation+=value
    label_result.config(text=equation)
    
def clear():
    global equation
    equation = ""
    label_result.config(text=equation)
    
def calculate():
    global equation
    result = ""
    if equation !="":
        try:
            result = eval(equation)
        except:
            result = "error"
            equation = ""
    label_result.config(text=result)
    

label_result = tk.Label(window, width=35, height=2, text="", font=("Arial", 30))
label_result.pack()

Button(window, text="AC", width=5, height=2, font=("Arial", 30, "bold"), bd=1, command=lambda: clear()).place(x=10, y=100)
Button(window, text="*", width=5, height=2, font=("Arial", 30, "bold"), bd=1, command=lambda: show("*")).place(x=130, y=100)
Button(window, text="%", width=5, height=2, font=("Arial", 30, "bold"), bd=1, command=lambda: show("%")).place(x=250, y=100)
Button(window, text="/", width=5, height=2, font=("Arial", 30, "bold"), bd=1, command=lambda: show("/")).place(x=370, y=100)

Button(window, text="7", width=5, height=2, font=("Arial", 30, "bold"), bd=1, command=lambda: show("7")).place(x=10, y=200)
Button(window, text="8", width=5, height=2, font=("Arial", 30, "bold"), bd=1, command=lambda: show("8")).place(x=130, y=200)
Button(window, text="9", width=5, height=2, font=("Arial", 30, "bold"), bd=1, command=lambda: show("9")).place(x=250, y=200)
Button(window, text="", width=5, height=2, font=("Arial", 30, "bold"), bd=1, command=lambda: show("")).place(x=370, y=200)

Button(window, text="4", width=5, height=2, font=("Arial", 30, "bold"), bd=1, command=lambda: show("4")).place(x=10, y=300)
Button(window, text="5", width=5, height=2, font=("Arial", 30, "bold"), bd=1, command=lambda: show("5")).place(x=130, y=300)
Button(window, text="6", width=5, height=2, font=("Arial", 30, "bold"), bd=1, command=lambda: show("6")).place(x=250, y=300)
Button(window, text="-", width=5, height=2, font=("Arial", 30, "bold"), bd=1, command=lambda: show("-")).place(x=370, y=300)

Button(window, text="1", width=5, height=2, font=("Arial", 30, "bold"), bd=1, command=lambda: show("1")).place(x=10, y=400)
Button(window, text="2", width=5, height=2, font=("Arial", 30, "bold"), bd=1, command=lambda: show("2")).place(x=130, y=400)
Button(window, text="3", width=5, height=2, font=("Arial", 30, "bold"), bd=1, command=lambda: show("3")).place(x=250, y=400)
Button(window, text="+", width=5, height=2, font=("Arial", 30, "bold"), bd=1, command=lambda: show("+")).place(x=370, y=400)

Button(window, text="00", width=5, height=2, font=("Arial", 30, "bold"), bd=1, command=lambda: show("00")).place(x=10, y=500)
Button(window, text="0", width=5, height=2, font=("Arial", 30, "bold"), bd=1, command=lambda: show("0")).place(x=130, y=500)
Button(window, text=".", width=5, height=2, font=("Arial", 30, "bold"), bd=1, command=lambda: show(".")).place(x=250, y=500)
Button(window, text="=", width=5, height=2, font=("Arial", 30, "bold"), bd=1, command=lambda: calculate()).place(x=370, y=500)




window.mainloop()