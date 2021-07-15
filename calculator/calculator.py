#Import GUI library
from tkinter import *
#Create GUI object variable
calc = Tk(className='Calculator')
#Define GUI size and lock it to that size
calc.geometry("320x421")
calc.resizable(0,0)
#Define global variables
resultext=""
operation="" 
#Define GUI elements
display1 = Label(calc, text="", height=2, width=44)
display2 = Label(calc,text="", height=2,width=44)
nine = Button(calc,text="9", width=10, height=4,command=lambda: addnum("9"))
eight = Button(calc,text="8", width=10, height=4,command=lambda: addnum("8"))
seven = Button(calc,text="7", width=10, height=4,command=lambda: addnum("7"))
six = Button(calc,text="6", width=10, height=4,command=lambda: addnum("6"))
cinco = Button(calc,text="5", width=10, height=4,command=lambda: addnum("5"))
four = Button(calc,text="4", width=10, height=4,command=lambda: addnum("4"))
three = Button(calc,text="3", width=10, height=4,command=lambda: addnum("3"))
two = Button(calc,text="2", width=10, height=4,command=lambda: addnum("2"))
one = Button(calc,text="1", width=10, height=4,command=lambda: addnum("1"))
zero = Button(calc,text="0", width=10, height=4,command=lambda: addnum("0"))
decimal = Button(calc,text=".", width=10, height=4,command=lambda: addnum("."))
delete = Button(calc, text="C", width=10, height=4,command=lambda: clear())
sum = Button(calc, text="+", width=10, height=4,command=lambda: operator("+"))
subtract = Button(calc, text="-", width=10, height=4,command=lambda: operator("-"))
multiply = Button(calc, text="x", width=10, height=4,command=lambda: operator("*"))
divide = Button(calc, text="÷", width=10, height=4, command=lambda: operator("/"))
equal = Button(calc, text="=",width=44, height=4,command=lambda: calculate())

#Define functions


def addnum(x):
    global resultext
    global display1
    content = str(display1.cget("text")).count(".")
    if x == "." and content == 0:
        charnum=len(display1.cget("text"))
        if charnum == 0 :
            resultext = "0"+x
            display1
    elif x != ".":
        resultext = display1.cget("text")+x
        display1.configure({"text": resultext})


def clear():
    global display1
    display1.configure({"text": ""})

def operator(x):
    global display1
    global display2
    global operation

    display2.configure({"text": display1.cget("text")})
    display1.configure({"text": ""})
    operation=x


def calculate():
    global operation
    if operation == "+":
        result=int(display1.cget("text")) + int(display2.cget("text"))
        display1.configure({"text": result})
        display2.configure({"text": ""})
    if operation == "-":
        result = int(display1.cget("text")) - int(display2.cget("text"))
        display1.configure({"text": result})
        display2.configure({"text": ""})
    if operation == "x":
        result = int(display1.cget("text")) * int(display2.cget("text"))
        display1.configure({"text": result})
        display2.configure({"text": ""})
    if operation == "/":
        result = int(display2.cget("text")) / int(display1.cget("text"))
        display1.configure({"text": result})
        display2.configure({"text": ""})

#Place previus elements inside GUI grid
display1.grid(row="0", column="0", columnspan="4")
display2.grid(row="1", column="0", columnspan="4")
nine.grid(row="2", column="0")
eight.grid(row="2", column="1")
seven.grid(row="2", column="2")
six.grid(row="3", column="0")
cinco.grid(row="3", column="1")
four.grid(row="3", column="2")
three.grid(row="4", column="0")
two.grid(row="4", column="1")
one.grid(row="4", column="2")
zero.grid(row="5", column="1")
decimal.grid(row="5", column="2")
delete.grid(row="5", column="0")
sum.grid(row="2", column="3")
subtract.grid(row="3", column="3")
multiply.grid(row="4", column="3")
divide.grid(row="5", column="3")
equal.grid(row="6", column="0", columnspan="4")
print(display1.cget("text"))
print(display2.cget("text"))
#Start GUI
calc.mainloop()
