#Import GUI library
from tkinter import *
#Create GUI object variable
calc = Tk(className='Calculator')
#Define GUI size and lock it to that size
calc.geometry("320x421")
calc.resizable(0,0)
#Define variable for the display
resultext=""
#Define functions
def addnum(x):
    global resultext
    global result
    resultext = result.cget("text")+x
    result.configure({"text": resultext})
def clear():
    global result
    result.configure({"text": ""})
#def sum():

#Define GUI elements
result = Label(calc,text="", height=4,width=44)
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
sum = Button(calc, text="+", width=10, height=4)
subtract = Button(calc, text="-", width=10, height=4)
multiply = Button(calc, text="x", width=10, height=4)
divide = Button(calc, text="/", width=10, height=4)
equal = Button(calc, text="=",width=44, height=4)
#Place previus elements inside GUI grid
result.grid(row="0", column="0", columnspan="4")
nine.grid(row="1", column="0")
eight.grid(row="1", column="1")
seven.grid(row="1", column="2")
six.grid(row="2", column="0")
cinco.grid(row="2", column="1")
four.grid(row="2", column="2")
three.grid(row="3", column="0")
two.grid(row="3", column="1")
one.grid(row="3", column="2")
zero.grid(row="4", column="1")
decimal.grid(row="4", column="2")
delete.grid(row="4", column="0")
sum.grid(row="1", column="3")
subtract.grid(row="2", column="3")
multiply.grid(row="3", column="3")
divide.grid(row="4", column="3")
equal.grid(row="5", column="0", columnspan="4")
print(result.cget("text"))
#Start GUI
calc.mainloop()